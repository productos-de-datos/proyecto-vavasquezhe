def get_project_root():
    from pathlib import Path
    return Path(__file__).parent.parent.parent

def test_train_datasets(data,perc):
    n = round(len(data)*perc)
    data_train = data[:-n]
    data_test  = data[-n:]
    return data_train, data_test

def save_estimator(estimator):
    import os
    import pickle
    with open("precios-diarios.pkl", "wb") as file:
        pickle.dump(estimator, file)

def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """

    import pandas as pd
    import pickle
    import statsmodels.api as sm
    #from sklearn.ensemble import RandomForestRegressor
    #from skforecast.ForecasterAutoreg import ForecasterAutoreg
    parent_dir = str(get_project_root())
   
    df = pd.read_csv(parent_dir + '/data_lake/business/features/precios_diarios.csv')
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')
    df['weekday'] = pd.to_numeric(df['weekday'])
    df = df.set_index('fecha')
    df = df.asfreq('D')
    df = df.sort_index()

    data_train, data_test = test_train_datasets(df,0.25)

    forecaster = sm.tsa.statespace.SARIMAX(
        endog=data_train[["precio"]],
        exog=data_train[["weekday"]],
        enforce_stationarity=False,
        enforce_invertibility=False,
        )

        #forecaster = ForecasterAutoreg(
        #            regressor = RandomForestRegressor(random_state=123),
        #            lags = 8
        #            )

    model = forecaster.fit(disp=0)
    pickle.dump(model, open(parent_dir + '/src/models/precios-diarios.pkl', "wb"))
    #save_estimator(forecaster)

if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()