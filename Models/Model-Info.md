# Save this info every time u create a new model

- Archivos a escribir al entrenar un modelo:
	- Nombre y descripción breve (`md` o `txt`)
	- Datos de entrada al modelo (`csv` o `pkl`)
	- Summary:
		- Arquitectura, parámetros entrenables, etc
		- [TorchInfo](https://github.com/sksq96/pytorch-summary)
		- [Keras-Summary](https://keras.io/api/models/model/)
	- Modelo:
		- `h5` for Keras and `pth` for PyTorch
	- Resultados (`csv` or `pkl`)
		- Métricas: RMSE, MSE, MAE, R2
		- Gráfica de entrenamiento: Train-Loss & Val-Loss w.r.t. epochs.
	- Metadata: 
		- Caracterización de los datos de entrada (`pkl`): dataframe con los primeros 4 momentos de las variables de estrada 
	- Obs: Semilla 42 para todo
