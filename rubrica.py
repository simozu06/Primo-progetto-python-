import json 

class Rubrica: 
    pass
    def __init__(self):
        self.data = {}
    def APRI(self, nome_del_file):
        with open(nome_del_file) as file_in: 
            self.data = json.load(file_in)