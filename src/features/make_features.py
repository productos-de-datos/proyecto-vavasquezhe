"""This module calculates model features"""
import doctest
from pathlib import Path
import pandas as pd
def get_project_root():
    """This function gets project root path """
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
    parent_dir = str(get_project_root())
    df_inicial = pd.read_csv(parent_dir+'/data_lake/business/precios-diarios.csv')
    df_inicial['fecha'] =  df_inicial[['fecha']].apply(pd.to_datetime)
    df_inicial['weekday'] = df_inicial.fecha.dt.weekday
    df_inicial['weekday_bol'] = (df_inicial['weekday']>=5).astype(int)
    df_inicial.to_csv(parent_dir+'/data_lake/business/features/precios_diarios.csv',index=False)
    return True
if __name__ == "__main__":
    make_features()
    doctest.testmod()
