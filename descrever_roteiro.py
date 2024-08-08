#-- coding:utf-8 --

class DescreveRoteiro:
    def __init__(self, rotas):
        self.rotas = rotas

    def passo_a_passo_rota(self):
        if self.rotas:
            resumo_rota = ""
            decricao_rota = {}
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
                            texto_passos = (
                        f"Embarque em: {transit_details['departure_stop']['name']} \n"
                        f"Desembarque em: {transit_details['arrival_stop']['name']} \n"
                        f"Em direção a: {transit_details['headsign']} \n"
                        f"Linha: {transit_details['line']['name']} \n"
                        f"Número de estações até o destino: {transit_details['num_stops']}"
                    )
                        decricao_rota[f"step: {index}"] =[texto_instrucoes, texto_passos]
            return resumo_rota,decricao_rota
        else:
            print("Não foi possível calcular a rota.")
            return None, None

if __name__ == "__main__":
    from calcula_rota import CalcularRota
    endOrigin = "Av. Miguel Ignácio Curi, 111 - Artur Alvim, São Paulo - SP, 08295-005"
    endDest = "Praça Roberto Gomes Pedrosa, 1 - Morumbi, São Paulo - SP, 05653-070"
    calcular_rota = CalcularRota(endOrigin,endDest)
    rota = calcular_rota.calcular_melhor_rota()
    roteiro = DescreveRoteiro(rota)
    resumo_rota,descricao_rota = roteiro.passo_a_passo_rota()
    print(resumo_rota)
    print("\n")
    print(descricao_rota)