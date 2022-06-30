"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""
import os
from luigi import Task, LocalTarget
import luigi
from create_data_lake import create_data_lake,get_project_root 
from ingest_data import ingest_data
from transform_data import transform_data
from clean_data import clean_data
from compute_monthly_prices import compute_monthly_prices
from compute_daily_prices import compute_daily_prices
import pandas as pd

class ImportTransformData(Task):
    def output(self):
        from create_data_lake import get_project_root
        self.root_path = str(get_project_root())
        return LocalTarget(os.path.join(self.root_path, "data_lake/cleansed/precios-horarios.csv"))

    def run(self):
        #try:
            #create_data_lake()
        #except:
            #return "Create DataLake Error"

        try:
            ingest_data()
        except:
            return "Ingest Error"

        try:
            transform_data()
        except:
            return "Transform Error"
        
        try:
            import os
            import pandas as pd
            d = clean_data()
            os.remove(os.path.join(self.root_path, "data_lake/cleansed/precios-horarios.csv"))
            outfile = open(self.output().path, 'wb')
            d.to_csv(outfile,index=False)
            outfile.close()
        except: 
            "Save Error"    

class CleanDataMonth(Task):

    def requires(self):
        return ImportTransformData()

    def output(self):
        from create_data_lake import get_project_root
        self.root_path = str(get_project_root())
        return LocalTarget(os.path.join(self.root_path, "data_lake/business/precios-mensuales.csv"))

    def run(self):
        import pandas as pd
        import os
        #i = pd.read_csv(self.input().open('r'))
        #d = compute_monthly_prices(i)
        d = compute_monthly_prices()
        os.remove(os.path.join(self.root_path,  "data_lake/business/precios-mensuales.csv"))
        outfile = open(self.output().path, 'wb')
        d.to_csv(outfile,index=False)

class CleanDataDay(Task):

    def requires(self):
        return ImportTransformData()

    def output(self):
        from create_data_lake import get_project_root
        self.root_path = str(get_project_root())
        return LocalTarget(os.path.join(self.root_path, "data_lake/business/precios-diarios.csv"))

    def run(self):
        import pandas as pd
        import os
        #i = pd.read_csv(self.input().open('r'))
        #d = compute_daily_prices(i)
        
        d = compute_daily_prices()
        os.remove(os.path.join(self.root_path, "data_lake/business/precios-diarios.csv"))
        outfile = open(self.output().path, 'wb')
        d.to_csv(outfile,index=False)

class FinalRun(Task):

    def requires(self):
        return [
            CleanDataMonth(),
            CleanDataDay(),
        ]
        
if __name__ == "__main__":
    import doctest
    luigi.run(["FinalRun", "--local-scheduler"])
    doctest.testmod()
