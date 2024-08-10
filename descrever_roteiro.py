# coding: utf-8
from fuzzywuzzy import fuzz
from lista_estacoes import EstacoesLista
from linhas_trem_e_metro_status import LinhasStatus

class DescreveRoteiroRota:
    def __init__(self, rotas):
        self.rotas = rotas

#captura o dataframe da EstacoesLista e retona quais estacoes contem essa linha
    def conecta_estacao_com_linha(self,estacao_rota, limiar_similaridade=80):
        try:
            estacoes = EstacoesLista()
            lista_estacoes = estacoes.get_estacoes
            df_estacoes = estacoes.gera_dataframe_lista_estacoes(lista_estacoes)
            
            colunas_encontradas = []
            for coluna in df_estacoes.columns:
                for valor in df_estacoes[coluna]:
                    similaridade = fuzz.ratio(valor, estacao_rota)
                    if similaridade >= limiar_similaridade:
                        colunas_encontradas.append(coluna)
                        break        
            return colunas_encontradas
        except Exception as e:
            print(f"Error encontrado {e}")
            return None
#busca o status da linha no arquivo csv salvo pela classe LinhaStatus
    def captura_status_estacao(self,colunas_encontradas,limiar_similaridade=80):
        linhas_status = LinhasStatus()
        file = linhas_status.get_status_linha()
        df = linhas_status.generate_data_frame(file)
        status_linha = []
        #ler arquivo
        linhas_filtro =[]
        try:
            for valor in df['Título']:
                similaridade = fuzz.ratio(valor,colunas_encontradas)
                if similaridade >= limiar_similaridade:
                    linhas_filtro.append(valor)
                    break
                df_filtrado = df[df['Título'].isin(linhas_filtro)]
                df_filtrado = df_filtrado.drop("Linha Número",axis=1)
        except KeyError:
            print("Valores não encontrados na base")
            return []
        status_linha = df_filtrado.values.tolist()
        
        return status_linha
    
    def gerar_texto_referente_estacoes(self,colunas_encontradas,status):
        texto = ""
        linhas = ""
        if colunas_encontradas == None:
            return None
        if len(colunas_encontradas)>1:
            linhas = ",".join(colunas_encontradas)
            stat = ""
            for i in status:
                stat += f"\n {i[0]} - {i[1]} - {i[2]} " 
            texto = (f"Estação Baldeio das linhas :{linhas} \n" +
                        f"Status Estação: {stat}")
        else:
            linhas = " ".join(colunas_encontradas)
            texto = f"Estação:{linhas} \n Status Estação: {status}"
        return texto

#função de le o arquivo json retornado na classe CalculaRota para descrever os principais pontos
    def passo_a_passo_rota(self):
        if self.rotas:
            resumo_rota = ""
            descricao_rota = {}
            for rota in self.rotas:
                
                resumo_rota = (
                f"Ponto de Partida: {rota['legs'][0]['start_address']} \n"
                f"Ponto de Chegada:  {rota['legs'][0]['end_address']} \n"
                f"Distância Total: {rota['legs'][0]['distance']['text']} \n"
                f"Tempo Total: {rota['legs'][0]['duration']['text']} \n"
            )

                
#detalhamento da rota
                for leg in rota['legs']:
#detalhamento de cada ponto da rota
                    for index,step in enumerate(leg['steps']):
                        # Imprimindo as instruções e a distância
                        texto_instrucoes = f"{step['html_instructions']} ({step['distance']['text']} - {step['duration']['text']})"
                        texto_passos = ""
                        # Adicionalmente, verificando se é um passo de trânsito e imprimindo o local de desembarque
                        if 'transit_details' in step:
                            transit_details = step['transit_details']
                            estacao_embarque = self.conecta_estacao_com_linha(transit_details['departure_stop']['name'])
                            status_estacao_embarque = self.captura_status_estacao(estacao_embarque)
                            informacao_estacao_embarque = self.gerar_texto_referente_estacoes(estacao_embarque,status_estacao_embarque) if self.gerar_texto_referente_estacoes(estacao_embarque,status_estacao_embarque) else None
                            
                            estacao_desembarque = self.conecta_estacao_com_linha(transit_details['arrival_stop']['name'])
                            status_estacao_desembarque = self.captura_status_estacao(estacao_desembarque)
                            informacao_estacao_desembarque = self.gerar_texto_referente_estacoes(estacao_desembarque,status_estacao_desembarque) if self.gerar_texto_referente_estacoes(estacao_desembarque,status_estacao_desembarque) else None

                            texto_passos = (
                        f"Embarque em: {transit_details['departure_stop']['name']} \n"
                        f"{informacao_estacao_embarque} \n"
                        f"Desembarque em: {transit_details['arrival_stop']['name']} \n"
                        f"{informacao_estacao_desembarque} \n"
                        f"Em direção a: {transit_details['headsign']} \n"
                        f"Linha: {transit_details['line']['name']} \n"
                        f"Número de estações até o destino: {transit_details['num_stops']}"
                    )
                        descricao_rota[f"step: {index}"] =[texto_instrucoes, texto_passos]
            
        
            resumo_rota_str = str(resumo_rota)
            descricao_rota_str = str(descricao_rota)
            return resumo_rota_str.encode("utf-8"), descricao_rota_str.encode("utf-8")
        else:
            print("Não foi possível calcular a rota.")
            return None, None

if __name__ == "__main__":
    from calcula_rota import CalcularRota
    endOrigin = "Av. Miguel Ignácio Curi, 111 - Artur Alvim, São Paulo - SP, 08295-005"
    endDest = "Praça Roberto Gomes Pedrosa, 1 - Morumbi, São Paulo - SP, 05653-070"
    calcular_rota = CalcularRota(endOrigin,endDest)
    rota = calcular_rota.calcular_melhor_rota()
    roteiro = DescreveRoteiroRota(rota)
    resumo_rota,descricao_rota = roteiro.passo_a_passo_rota()
    print("Resumo Rota:")
    print(resumo_rota)

    print("Descrição Rota")
    print(descricao_rota)
