#-- coding:utf-8 --
from dotenv import load_dotenv
import os
import requests
import json
load_dotenv() # Carregar variáveis de ambiente do arquivo .env
class CalcularRota:
    def __init__(self,endOrigin,endDestination):
        self.api_key = os.getenv('API_KEY')
        self.api_url = f'https://maps.googleapis.com/maps/api/directions/json'
        self.endOrigin = endOrigin
        self.endDest = endDestination

    def calcular_melhor_rota(self):
        params = {
            'origin': self.endOrigin,
            'destination': self.endDest,
            'mode': 'transit',  # Modo de transporte público
            'avoid': 'indoor', #evita caminhadas em grandes terminais
            'traffic_model':'pessimistic',
            'transit_mode':'train',
            'unit':'metric',
            'language':'pt-BR',
            'key': self.api_key

        }
        
        response = requests.get(self.api_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'OK':
                return data['routes']
            else:
                print(f"Erro na resposta da API: {data['status']}")
        else:
            print(f"Erro na requisição: {response.status_code}")
        
        return None

# Exemplo de uso:
if __name__ == "__main__":
    endOrigin = "Rua Santa Ana, 19 Residencial Sol Nascente - SP"
    endDest = "Av. Angélica, 2466 - 5º andar - Bela Vista, São Paulo - SP, 01228-200"

    analise = CalcularRota(endOrigin, endDest)
    rotas = analise.calcular_melhor_rota()
    #print(rotas)
   
