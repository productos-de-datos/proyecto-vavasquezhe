def get_project_root():
    from pathlib import Path
    return Path(__file__).parent.parent.parent

def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """

    import pandas as pd
    parent_dir = str(get_project_root())
    df = pd.read_csv(parent_dir+'/data_lake/business/precios-diarios.csv')
    df['fecha'] =  df[['fecha']].apply(pd.to_datetime)
    df['weekday'] = df.fecha.dt.weekday
    df['weekday_bol'] = (df['weekday']>=5).astype(int)
    df.to_csv(parent_dir+'/data_lake/business/features/precios-diarios.csv',index=False)
    ##raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()
