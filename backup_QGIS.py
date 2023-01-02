
# -*- coding: utf-8 -*-

from datetime import date
from qgis.core import QgsProject, QgsVectorFileWriter
from qgis.core import QgsCoordinateReferenceSystem
import os


class BackupQGis():
    def __init__(self, path_folder):
        self.path = path_folder

    def create_folder(self):
        self.date_today = date.today()
        self.day = self.date_today.day
        self.month = self.date_today.month
        self.year = self.date_today.year
        self.date_temp = str(self.day)+'_'+str(self.month)+'_'+str(self.year)
        self.new_folder = self.path + self.date_temp
        if os.path.exists(self.new_folder):
            self.list_folder = os.listdir(self.new_folder)
            if self.list_folder == []:
                num = '01'
                self.new_folder = self.new_folder + '/' + num
                os.mkdir(self.new_folder)
            else:
                list_folder_2 = []
                for i in self.list_folder:
                    name_folder_exists = int(i)
                    list_folder_2.append(name_folder_exists)
                list_folder_2.sort()
                num = list_folder_2[-1] + 1
                nome_pasta = '0' + str(num)
                self.new_folder = self.new_folder + '/' + str(nome_pasta)
                os.mkdir(self.new_folder)
        else:
            num = '01'
            os.mkdir(self.new_folder)
            self.new_folder = self.new_folder + '/' + num
            os.mkdir(self.new_folder)
            
    def create_backup(self, tipo_save):
        names = []
        projet = QgsProject.instance().mapLayers().values()
        for layer in projet:
            names.append(layer.name())
        for nome in names:
            layer_save = QgsProject.instance().mapLayersByName(nome)[0]
            path_final = self.new_folder + '/' + nome + '.shp'
            cod = "utf-8"
            sr = QgsCoordinateReferenceSystem(nome)
            QgsVectorFileWriter.writeAsVectorFormat(layer_save, path_final,
                                                    cod, sr, tipo_save)


path = 'Caminho_da_pasta_saida_do_arquivo' #C://User//...
backup = BackupQGis(path)
backup.create_folder()
backup.create_backup("ESRI Shapefile")
