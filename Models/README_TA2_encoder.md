# Registro del Experimento: TA2_encoder

## Configuración Principal
- Neuronas:              [108, 64, 32, 8]
- Activaciones:          ['relu', 'tanh', 'tanh', 'relu']
- Dropouts:              [0.3, 0.2, 0.1, 0]
- Estandarizacion:       MinMax
- Nombre del Modelo:     TA2_encoder
- Loss:                  mse
- Semilla global:        42
- Data entrada:          cleanA_150k.csv
- Dimensión de Entrada:  66
- Split (train% - val%): (0.65-0.2)
- Epoch:                 250
- Bach_size:             96
- Optimizador:           adam 
- Learn_rate:            0.003
