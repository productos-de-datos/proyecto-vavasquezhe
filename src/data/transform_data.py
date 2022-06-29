def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    import pandas as pd
    import glob
    from create_data_lake import get_project_root 
    parent_dir = str(get_project_root())
    files = [i.split("/")[-1] for i in glob.glob(parent_dir+"/data_lake/landing/*.xls*")]

    for i in files:
        df-inicial = pd.read_excel(parent_dir+'/data_lake/landing/{}'.format(i),
         index_col=None, header=None)
        header_index = df-inicial.index[df-inicial.iloc[:, 0] == 'Fecha'].tolist()
        df_final = df-inicial.iloc[header_index[0]+1:,0:25]
        df_final.columns = ["Fecha","H00","H01","H02","H03",
        "H04","H05","H06","H07","H08","H09","H10","H11","H12","H13",
        "H14","H15","H16","H17","H18","H19","H20","H21","H22","H23"]
        df_final['Fecha'] =  df_final[['Fecha']].apply(pd.to_datetime)
        df_final['Fecha'] = df_final['Fecha'].dt.date
        df_final.to_csv(parent_dir+'/data_lake/raw/{}.csv'.format(i.split(".")[0]),index=False)

if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
