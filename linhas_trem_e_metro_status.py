# coding: utf-8
from bs4 import BeautifulSoup
import requests
import pandas as pd

class LinhasStatus:
    def __init__(self):
        self.url = 'https://www.viamobilidade.com.br/'

    def get_status_linha(self):
        response = requests.get(self.url)
        response.encoding = 'utf-8'  # Garantir que o encoding está correto
        try:
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                linhas = soup.find_all('div', class_='line-wrapper')
                data = []
                for itens in linhas:
                    line_items = itens.find_all('li')
                    for line_item in line_items:
                        linha_numero = line_item.find('span').text.strip() if line_item.find('span') else ''
                        linha_title = line_item.find('span')['title'] if line_item.find('span') and 'title' in line_item.find('span').attrs else ''
                        linha_situacao = line_item.find('div', class_='status').text.strip() if line_item.find('div', class_='status') else ''
                        wrapper = line_item.find('div', class_='wrapper')
                        if wrapper:
                            detalhe = wrapper.find('p').text.strip() if wrapper.find('p') else ''
                        else:
                            detalhe = ''
                        data.append([linha_numero, linha_title, linha_situacao, detalhe])
                
                return data 
            else:
                print(f'Erro ao acessar a página. Status code: {response.status_code}')
        except  Exception as e:
            print(f"Ocorreu um erro de excessão: {e}")

    def generate_data_frame(self,data):
        # Criar um DataFrame
        try:
           # nome_linhas_correta = ['Linha 1-Azul','Linha 2-Verde',
            #                    'Linha 3-Vermelha','Linha 4-Amarela','Linha 5-Lilás',
            #                    'Linha 7-Rubi','Linha 8-Diamante','Linha 9-Esmeralda',
            #                    'Linha 10-Turquesa','Linha 11-Coral','Linha 12-Safira',
            #                    'Linha 13-Jade','Linha 15-Prata']
            
            df = pd.DataFrame(data, columns=['Linha Número', 'Título', 'Situação', 'Detalhe'])  
            #de_para_nomes_ = {desejado: unificado for desejado, unificado in
             #                   zip(df['Título'], nome_linhas_correta)}
            #df['Título'] = df['Título'].map(de_para_nomes_)
            df.to_csv('files/status_linhas.csv',index=False,encoding='utf-8')
            return df
        except KeyError as e:
            print(f"Erro de mapeamento: {e}")    

if __name__ == "__main__":
    a = LinhasStatus()
    data = a.get_status_linha()
    a.save_csv(data)
