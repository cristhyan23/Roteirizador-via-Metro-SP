# coding: utf-8
from dotenv import load_dotenv
import os
import requests
import json
load_dotenv() # Carregar variáveis de ambiente do arquivo .env
class CalcularRota:
    def __init__(self,endOrigin,endDestination):
        self.api_key = os.getenv('MAPS_API_KEY')
        self.api_url = f'https://maps.googleapis.com/maps/api/directions/json'
        self.endOrigin = endOrigin
        self.endDest = endDestination

    def gerar_lat_e_long_enderecos(self,data):
        json_final = []
        # Adicionar etapas ao mapa
        for leg in data[0]['legs']:
            for step in leg['steps']:
                start_coords = {"lat":step['start_location']['lat'],"lng":step['start_location']['lng']}
                json_final.append(start_coords)
                end_coords = {"lat":step['end_location']['lat'],"lng":step['end_location']['lng']}
                json_final.append(end_coords)
        # Escreve o JSON em um arquivo
        with open('files/pontos.json', 'w') as f:
            json.dump(json_final, f)
        return json_final
        
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
    endOrigin = "Av. Miguel Ignácio Curi, 111 - Artur Alvim, São Paulo - SP, 08295-005"
    endDest = "Praça Roberto Gomes Pedrosa, 1 - Morumbi, São Paulo - SP, 05653-070"

    analise = CalcularRota(endOrigin, endDest)
    rotas = analise.calcular_melhor_rota()
    print(analise.gerar_lat_e_long_enderecos(rotas))
 
   
