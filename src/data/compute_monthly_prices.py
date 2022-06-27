def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    ##raise NotImplementedError("Implementar esta función")
    import pandas as pd 
    from create_data_lake import get_project_root 
    parent_dir = str(get_project_root())

    df = pd.read_csv(parent_dir + '/data_lake/cleansed/precios-horarios.csv') 
    #df = pd.DataFrame(df)
    df['fecha'] =  df[['fecha']].apply(pd.to_datetime)
    df['fecha'] = df['fecha'].dt.to_period('M').dt.to_timestamp()
    df_final = df.groupby(['fecha']).mean().reset_index()
    df_final.to_csv(parent_dir+'/data_lake/business/precios-mensuales.csv',index=False)


if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()
