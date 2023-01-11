# -*- coding: utf-8 -*-

#documentação
#https://portal.inmet.gov.br/manual

import requests
import pandas as pd

link = "https://apitempo.inmet.gov.br/condicao/capitais/2019-10-22"
type_data = "TMIN18"

class Create_csv_API_INMET:
    
    def __init__(self, link, type_data):
        self.link = link
        self.type_data = type_data
        self.dic_data = {"Capital":[],
                         "UF":[],
                         "Data": []
                         }
        self.dic_cities_UF = {
                "Rio branco":"AC",
                "Maceió":"AL",
                "Macapa":"AP",
                "Manaus":"AM",
                "Salvador":"BA",
                "Fortaleza":"CE",
                "Brasilia":"DF",
                "Vitoria":"ES",
                "Goiania":"GO",
                "Sao luis":"MA",
                "Cuiaba":"MT",
                "Campo grande":"MS",
                "Belo horizonte":"MG",
                "Belem":"PA",
                "Joao pessoa":"PB",
                "Curitiba":"PR",
                "Recife":"PE",
                "Teresina":"PI",
                "Rio de janeiro":"RJ",
                "Natal":"RN",
                "Porto alegre":"RS",
                "Porto velho":"RO",
                "Boa vista":"RR",
                "Florianopolis":"SC",
                "Sao paulo":"SP",
                "Aracaju":"SE",
                "Palmas":"TO",
            }
        
    def request_my_data(self):
        req = requests.get(self.link)
        status = req.status_code
        if status == 200:
            self.json_data_out = req.json()
            
    def convert_json_in_csv_filter(self, path):
        for i in self.json_data_out:
            city = i["CAPITAL"].capitalize()
            uf = self.dic_cities_UF[city]
            data = i[self.type_data] 
            if "*" in data:
                data = data.replace("*", "0")
                print(city)
            self.dic_data["Capital"].append(city)
            self.dic_data["UF"].append(uf)
            self.dic_data["Data"].append(data)
            
        df = pd.DataFrame(self.dic_data)
        df.to_csv(path)

path = "Pasta_de_destino" #Alterar para o nome da pasta do seu sistema        
date = "2019-10-22"
link = "https://apitempo.inmet.gov.br/condicao/capitais/"+date
type_data = "TMIN18"
api_inmet = Create_csv_API_INMET(link, type_data)
api_inmet.request_my_data()
api_inmet.convert_json_in_csv_filter(path)
