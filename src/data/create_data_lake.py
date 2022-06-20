def create_data_lake(parent_dir):
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```

    """
    #raise NotImplementedError("Implementar esta función")

    import os 

    os.mkdir(os.path.join(parent_dir, "data_lake"))
    os.mkdir(os.path.join(parent_dir, "data_lake/landing"))
    os.mkdir(os.path.join(parent_dir, "data_lake/raw"))
    os.mkdir(os.path.join(parent_dir, "data_lake/cleansed"))
    os.mkdir(os.path.join(parent_dir, "data_lake/business"))
    os.mkdir(os.path.join(parent_dir, "data_lake/business/reports"))
    os.mkdir(os.path.join(parent_dir, "data_lake/business/features"))
    os.mkdir(os.path.join(parent_dir, "data_lake/business/forecasts"))
    os.mkdir(os.path.join(parent_dir, "data_lake/business/reports/figures"))


if __name__ == "__main__":
    create_data_lake('/Users/valentinavasquezhernandez/Desktop/proyecto-vavasquezhe-1/src')
    import doctest
    doctest.testmod()
