def load_estimator():

    import os
    import pickle

    with open("precios-diarios.pkl", "rb") as file:
        estimator = pickle.load(file)

    return estimator    
    
def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    ##raise NotImplementedError("Implementar esta función")
    import pandas as pd
    from train_daily_model import test_train_datasets, get_project_root 
    parent_dir = str(get_project_root())
    #raise NotImplementedError("Implementar esta función")

    df = pd.read_csv(parent_dir + '/data_lake/business/features/precios-diarios.csv')
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')
    df = df.set_index('fecha')
    df = df.asfreq('D')
    df = df.sort_index()

    data_train, data_test = test_train_datasets(df,0.25)
    price_estimator = load_estimator()
    steps = len(data_test)
    predictions = price_estimator.predict(steps=steps)
    
    result = pd.concat([data_test.loc[:, ['precio']], predictions], axis=1, join="inner")
    result = result.reset_index()
    result.columns = ["fecha", "precio", "precio_pred"]

    result.to_csv(parent_dir+'/data_lake/business/forecasts/precios-diarios.csv',index=False)

if __name__ == "__main__":
    import doctest
    make_forecasts()    
    doctest.testmod()