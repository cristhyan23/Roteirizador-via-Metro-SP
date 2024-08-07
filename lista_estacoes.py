from bs4 import BeautifulSoup
import requests

class EstacoesLista:
    def __init__(self):
        self.url = 'https://www.viamobilidade.com.br/voce/mapa'

    def descricao_estacoes(self):
        response = requests.get(self.url)
        response.encoding = 'utf-8'  # Garantir que o encoding está correto
        try:
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                linhas = soup.find_all('div', class_='row line-list')
                data = {}
                for linha in linhas:
                    colunas = linha.find_all("div", class_="col-4")
                    for coluna in colunas:
                        nome_linha_tag = coluna.find("h4")
                        if nome_linha_tag:  # Verifica se o nome da linha foi encontrado
                            nome_linha = nome_linha_tag.text.strip()
                            estacoes = coluna.find_all("li")
                            lista_estacoes = [estacao.text.strip() for estacao in estacoes]
                            # Adiciona as estações à linha correspondente
                            if nome_linha in data:
                                data[nome_linha].extend(lista_estacoes)
                            else:
                                data[nome_linha] = lista_estacoes
                print(data)
            else:
                print('Não foi possível obter a lista de linhas')
        except Exception as e:
            print(f"Ocorreu um erro de exceção: {e}")

if __name__ == "__main__":
    a = EstacoesLista()
    a.descricao_estacoes()
