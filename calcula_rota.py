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
            'avoid':'indoor',
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
# Exemplo de uso:
if __name__ == "__main__":
    endOrigin = "Rua Santa Ana, 19 Residencial Sol Nascente - SP"
    endDest = "Av. Angélica, 2466 - 5º andar - Bela Vista, São Paulo - SP, 01228-200"

    analise = CalcularRota(endOrigin, endDest)
    rotas = analise.calcular_melhor_rota()
    #print(rotas)
    if rotas:
        
        for rota in rotas:
            print(f"Resumo da rota: {rota['summary']}")
            print(f"Ponto de Partida: {rota['legs'][0]['start_address']}")
            print(f"Ponto de Chegada: {rota['legs'][0]['end_address']}")
            print(f"Distância da rota: {rota['legs'][0]['distance']['text']}")
            print(f"Tempo da rota: {rota['legs'][0]['duration']['text']}")

            for leg in rota['legs']:
                for step in leg['steps']:
                    # Imprimindo as instruções e a distância
                    print(f"{step['html_instructions']} ({step['distance']['text']} - {step['duration']['text']})")
                    # Adicionalmente, verificando se é um passo de trânsito e imprimindo o local de desembarque
                    if 'transit_details' in step:
                        transit_details = step['transit_details']
                        print(f"Embarque em: {transit_details['departure_stop']['name']}")
                        print(f"Desembarque em: {transit_details['arrival_stop']['name']}")
                        print(f"Em direção a: {transit_details['headsign']}")
                        print(f"Linha: {transit_details['line']['name']}")
                        print(f"Número de estações até o destino: {transit_details['num_stops']}")
    else:
        print("Não foi possível calcular a rota.")
