
def get_project_root():
    from pathlib import Path
    return Path(__file__).parent.parent.parent

def create_data_lake():
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
    import os 
    parent_dir = get_project_root()

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
    import doctest
    doctest.testmod()
