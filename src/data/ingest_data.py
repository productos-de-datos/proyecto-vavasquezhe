"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    #raise NotImplementedError("Implementar esta función")
    
    import wget
    from create_data_lake import get_project_root 
    import os
    os.system("pip install wget")
    url_xlsx = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xlsx?raw=true'
    url_xls = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xls?raw=true'
    xlsx =  list(range(1995, 2016)) + list(range(2018, 2022))
    parent_dir = get_project_root()

    for i in range(1995, 2022):
        if i == 2016 or i == 2017:
            wget.download(url_xls.format(str(i)),out = os.path.join(parent_dir, "data_lake/landing"))
        else: 
            wget.download(url_xlsx.format(str(i)),out = os.path.join(parent_dir, "data_lake/landing"))

if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()
