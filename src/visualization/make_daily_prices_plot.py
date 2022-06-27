
def get_project_root():
    from pathlib import Path
    return Path(__file__).parent.parent.parent

def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    #raise NotImplementedError("Implementar esta función")
    import pandas as pd 
    parent_dir = str(get_project_root())
    df = pd.read_csv(parent_dir + '/data_lake/business/precios-diarios.csv') 
    plot = df.plot.line()
    fig = plot.get_figure()
    fig.savefig(parent_dir + '/data_lake/business/reports/figures/daily_prices.png')

if __name__ == "__main__":
    import doctest
    make_daily_prices_plot()
    doctest.testmod()
