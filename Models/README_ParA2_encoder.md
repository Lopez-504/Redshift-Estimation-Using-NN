# Registro del Experimento: ParA2_encoder

## Configuración Principal
- Neuronas:              [32, 16, 8, 4]
- Activaciones:          ['relu', 'relu', 'relu', 'relu']
- Dropouts:              [0.35, 0.25, 0.2, 0.1]                      
- Estandarizacion:       Standar
- Nombre del Modelo:     ParA2_encoder
- Loss:                  mse
- Semilla global:        42
- Data entrada:          cleanA_150k.csv
- Dimensión de Entrada:  (97488, 66)
- Split (train% - val%): (0.65-0.2)
- Epoch:                 600
- Bach_size:             256
- Optimizador:           adam 
- Learn_rate:            0.0014
- Features:              ['dered_u', 'dered_g', 'dered_r', 'dered_i', 'dered_z', 'psfMag_u', 'psfMag_g', 'psfMag_r', 'psfMag_i', 'psfMag_z', 'fiberMag_u', 'fiberMag_g', 'fiberMag_r', 'fiberMag_i', 'fiberMag_z', 'modelMag_u', 'modelMag_g', 'modelMag_r', 'modelMag_i', 'modelMag_z', 'expRad_g', 'expRad_i', 'expRad_r', 'expRad_z', 'deVRad_g', 'deVRad_i', 'deVRad_r', 'deVRad_z', 'expPhi_u', 'expPhi_g', 'expPhi_r', 'expPhi_i', 'expPhi_z', 'petroRad_r', 'z']
