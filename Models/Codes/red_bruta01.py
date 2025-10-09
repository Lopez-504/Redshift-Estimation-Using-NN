import pandas as pd 
import numpy as np  

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader

path = r"C:\Users\danhm\OneDrive\Desktop\Electivo_NN\Proyecto_1\150k.csv" # obs: manualmente se quito la primera fila para poder trabajar con un formato mas simple 
df = pd.read_csv( path )
print(df.shape) 

torch.manual_seed(123)

# cuantos -9999 hay por columna (y el %), yo se que los nan son -9999
def resumen_sentinel(df, sentinel=-9999):
    counts = (df == sentinel).sum(numeric_only=False)
    perc = counts / len(df)
    rep = pd.DataFrame({"count": counts, "percent": perc}).sort_values("count", ascending=False)
    return rep

print(resumen_sentinel(df).head(10))

filas_sanas = (df != -9999).all(axis=1)
df = df.loc[filas_sanas].reset_index(drop=True)
print(f"filas tras filtrar -9999: {len(df)}")

print(df.columns[:68]) # Todas las columnas

error_cols = [col for col in df.columns if "err" in col.lower()] # separa las columnas que guardan los errores
print(len(error_cols))      # lista de columnas de errores

datos_sin_errores = df.drop(columns=error_cols)
datos_errores     = df[error_cols]

print('sin errores: ',len(datos_sin_errores.columns),' errores: ',len(datos_errores.columns))

# Solo columnas numéricas
#corr_matrix = datos_sin_errores.corr(method='pearson').abs()

corr_matrix = df.corr(method='pearson').abs()

umbral = 0.9

upper = corr_matrix.where( np.triu(np.ones(corr_matrix.shape), k=1).astype(bool) ) # se queda solo con la mitad superiror y la diagonal de la matriz, evitapares duplicados

cols_altamente_corr = [col for col in upper.columns if any(upper[col] > umbral)] # correlacion alta
print(len(cols_altamente_corr))

#datos_sin_corr = datos_sin_errores.drop(columns=cols_altamente_corr) # sin errores y correlacion baja

datos_sin_corr = df.drop(columns=cols_altamente_corr) # sin errores y correlacion baja

DF = datos_sin_corr # df final
print(DF.shape)
print(DF.columns)

X = DF.drop(columns=[DF.columns[0]])  # resto de variables
Y = DF[DF.columns[0]]                 # columna a predecir

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device) # por si se puede usar gpu

# ==== 6) Split train/test ====
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

scaler_X = StandardScaler() # se escalan los datos 
X_train_scaled = scaler_X.fit_transform(X_train)
X_test_scaled  = scaler_X.transform(X_test)

X_train_t = torch.tensor(X_train_scaled, dtype=torch.float32)
y_train_t = torch.tensor(y_train.values.reshape(-1, 1), dtype=torch.float32)

X_test_t  = torch.tensor(X_test_scaled, dtype=torch.float32)
y_test_t  = torch.tensor(y_test.values.reshape(-1, 1), dtype=torch.float32)

batch_size = 512
train_loader = DataLoader(TensorDataset(X_train_t, y_train_t), batch_size=batch_size, shuffle=True)
test_loader  = DataLoader(TensorDataset(X_test_t,  y_test_t),  batch_size=batch_size, shuffle=False)

# MLP 64-32-16-8 con Tanh 
class MLP(nn.Module):
    def __init__(self, in_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 64),
            nn.Tanh(),
            nn.Linear(64, 32),
            nn.Tanh(),
            nn.Linear(32, 16),
            nn.Tanh(),
            nn.Linear(16, 8),
            nn.Tanh(),
            nn.Linear(8, 1)   
        )
    def forward(self, x):
        return self.net(x)

model = MLP(in_dim=X_train_t.shape[1]).to(device)

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)


# Train
epochs = 200
model.train()
for epoch in range(1, epochs+1):
    running_loss = 0.0
    for xb, yb in train_loader:
        xb = xb.to(device)
        yb = yb.to(device)

        optimizer.zero_grad()
        pred = model(xb)
        loss = criterion(pred, yb)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * xb.size(0)

    epoch_loss = running_loss / len(train_loader.dataset)

    # evaluacion en validacion
    model.eval()
    with torch.no_grad():
        preds = []
        gts = []
        for xb, yb in test_loader:
            xb = xb.to(device)
            pred = model(xb)
            preds.append(pred.cpu().numpy())
            gts.append(yb.numpy())
        y_pred_val = np.vstack(preds).ravel()
        y_true_val = np.vstack(gts).ravel()
        val_mse = mean_squared_error(y_true_val, y_pred_val)
    model.train()

    if epoch % 50 == 0 or epoch == 1:
        print(f"Epoch {epoch:3d} | Train MSE: {epoch_loss:.6f} | Val MSE: {val_mse:.6f}")

# metricas
model.eval()
with torch.no_grad():
    y_pred_test = model(X_test_t.to(device)).cpu().numpy().ravel()

mse = mean_squared_error(y_test, y_pred_test)
mae = mean_absolute_error(y_test, y_pred_test)
r2  = r2_score(y_test, y_pred_test)

print(f"\nResultados en Test:")
print(f"  MSE: {mse:.6f}")
print(f"  MAE: {mae:.6f}")
print(f"  R2 : {r2:.6f}")

z_datos = y_test
z_pred = model(X_test_t.to(device)).cpu().detach().numpy().ravel()
print(len(z_datos),len(z_pred))

from torchinfo import summary

summary(model)


plt.figure(figsize=(5,5))

plt.scatter(z_datos,z_pred, alpha=0.02)
plt.plot(range(10),range(10),color='black')
plt.xlabel('Z true')
plt.ylabel('Z pred')
plt.savefig('modelo_vs_real.png',dpi=300)







