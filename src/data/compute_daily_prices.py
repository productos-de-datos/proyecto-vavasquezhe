def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional

    """
    ##raise NotImplementedError("Implementar esta función")
    import pandas as pd 
    from create_data_lake import get_project_root 
    parent_dir = str(get_project_root())
    df = pd.read_csv(parent_dir + '/data_lake/cleansed/precios-horarios.csv') 
    df_final = df.groupby(['fecha']).mean().reset_index()
    df_final.to_csv(parent_dir+'/data_lake/business/precios-diarios.csv',index=False)

if __name__ == "__main__":
    import doctest
    compute_daily_prices()
    doctest.testmod()
