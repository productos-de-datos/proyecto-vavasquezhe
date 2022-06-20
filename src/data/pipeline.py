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
import ingest_data
import transform_data
import clean_data


class ImportTransformData(Task):
    def output(self):
        return LocalTarget('/Users/valentinavasquezhernandez/Desktop/proyecto-vavasquezhe-1/src/data_lake/cleansed/precios-horarios.csv')

    def run(self):
        try:
            ingest_data.ingest_data('/Users/valentinavasquezhernandez/Desktop/proyecto-vavasquezhe-1/src/data_lake/landing')
        except:
            return "Ingest Error"

        try:
            transform_data.transform_data('/Users/valentinavasquezhernandez/Desktop/proyecto-vavasquezhe-1/src')
        except:
            return "Transform Error"
        
        try:
            d = clean_data.clean_data('/Users/valentinavasquezhernandez/Desktop/proyecto-vavasquezhe-1/src')
            outfile = open(self.output().path, 'wb')
            d.to_csv(outfile,index=False)
        except: 
            "Save Error"    
        
if __name__ == "__main__":
    import doctest
    luigi.run(["ImportTransformData", "--local-scheduler"])
    doctest.testmod()
