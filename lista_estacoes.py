from bs4 import BeautifulSoup
import requests
import re

class EstacoesLista:
    def __init__(self):
        self.url = 'https://www.viamobilidade.com.br/voce/mapa'

    def corrigir_html_tags(self,html_content):
        # Corrigir o HTML malformado adicionando as tags de fechamento </li> onde faltam
        corrected_html_content = re.sub(r'(?<=</li>)(<li>)', r'\1', html_content)  # Corrige fechamento múltiplo </li>
        corrected_html_content = re.sub(r'<li>', r'</li><li>', corrected_html_content)  # Adiciona </li> antes de cada <li> novo
        #corrected_html_content = re.sub(r'^</li>', r'', corrected_html_content)  # Remove primeiro fechamento </li> incorreto
        return corrected_html_content
    
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
                    if colunas:
                        for coluna in colunas:
                            nome_linha_tag = coluna.find("h4")
                            if nome_linha_tag:  # Verifica se o nome da linha foi encontrado
                                nome_linha = nome_linha_tag.text.strip()
                                estacoes_tag = coluna.find("ul")
                                if estacoes_tag:
                                    estacoes_html = str(estacoes_tag)
                                    estacoes_corrigidas_html = self.corrigir_html_tags(estacoes_html)
                                    estacoes_soup = BeautifulSoup(estacoes_corrigidas_html, 'html.parser')
                                    estacoes_list = estacoes_soup.find_all('li')
                                    lista_estacoes = [estacao.get_text() for estacao in estacoes_list]
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
