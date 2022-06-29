from numpy import column_stack


def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.
    """
    import pandas as pd
    import glob
    from create_data_lake import get_project_root 
    parent_dir = str(get_project_root())
    files = [i.split("/")[-1] for i in glob.glob(parent_dir+"/data_lake/raw/*.csv*")]
    df_final = pd.DataFrame(columns = ['Fecha','hora','precio'])

    for i in files:
        df_inicial = pd.read_csv(parent_dir + '/data_lake/raw/{}'.format(i)) 
        df_melt = pd.melt(df-inicial, id_vars=['Fecha'], value_vars=df_inicial.columns[1:], var_name='hora', value_name='precio')
        df_final = pd.concat([df_final,df_melt], axis=0)

    df_final.columns = ['fecha', 'hora', 'precio']
    df_final.to_csv(parent_dir+'/data_lake/cleansed/precios-horarios.csv',index=False)
    return df_final

if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()
