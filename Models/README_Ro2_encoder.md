# Registro del Experimento: Ro2_encoder

## Configuración Principal
- Neuronas:              [64, 32, 16, 8]
- Activaciones:          ['relu', 'relu', 'relu', 'softmax']
- Dropouts:              [0.3, 0.2, 0.1, 0.05]                      
- Estandarizacion:       Robust
- Nombre del Modelo:     Ro2_encoder
- Loss:                  mse
- Semilla global:        42
- Data entrada:          cleanA_150k.csv
- Dimensión de Entrada:  (97488, 66)
- Split (train% - val%): (0.65-0.2)
- Epoch:                 500
- Bach_size:             512
- Optimizador:           rmsprop 
- Learn_rate:            0.003
