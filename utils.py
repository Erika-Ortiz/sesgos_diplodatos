import pandas as pd
import numpy as np

def complete_group(dataset):
    """Completa los registros de resolución de los participantes y devuelve un nuevo dataset con los registros completos
    Arg: 
    dataset: pandas DataFrame
    returns:
    pandas DataFrame"""

    part = dataset['Participante'].unique() # participantes en nuestro dataset a completar

    df_all_groups = pd.DataFrame()

    for x in part: 
        if sum(dataset['Participante']==x)!=24: # identifica los participantes con registros incompletos

            y = np.array(dataset['Grupo'].loc[dataset['Participante']==x])[0] # obtiene el número de grupo del participante con registro incompleto
        
            df = pd.DataFrame() # crea dataframe vacío para cargar los registros grupales

            df['Participante'] = np.repeat(x, 8) # crea la columna "Participante" para los nuevos registros
            df['Modalidad'] = np.repeat('Resolución Grupal', 8) # Crea la columna "Modalidad" para los nuevos registros
            df['Grupo'] = np.repeat(y, 8) # crea la columna "Grupo" con el número de grupo que obtuvo previamente
        
            df_data_group = dataset[(dataset['Grupo']==y) & (dataset['Modalidad']=='Resolución Grupal')][['Validez', 'Creencia', 'ValidezxCreencia', 'Silogismo', 'Aceptación', 'Correctas']].copy().reset_index(drop=True) # Copia los registros que nos faltaban
            df = pd.concat([df, df_data_group], axis=1) # unimos las columnas de los nuevos registros
            df_all_groups = pd.concat([df_all_groups, df]) 

    complete_dataset = pd.concat([dataset, df_all_groups])
    return complete_dataset