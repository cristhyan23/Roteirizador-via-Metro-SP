# coding: utf-8
import google.generativeai as genai
import os
import re
from dotenv import load_dotenv

load_dotenv()

class HumanizaResposta:

    def __init__(self):
        self.gemini_model = 'gemini-1.5-flash'
        genai.configure(api_key=os.environ["AI_API_KEY"])
        # The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
        self.model = genai.GenerativeModel(self.gemini_model)
    
    def aplicar_negrito(self,texto):
        # Substitui os textos entre ** por <strong>texto</strong>
        return re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', texto)

    def humanizar_resposta_rota(self,resumo_roteiro,descricao_roteiro):
        prompt = f"""
        Sua função é gerar instruções detalhadas para um usuário que deseja realizar um trajeto de metrô. Você receberá um resumo do trajeto e um dicionário com a descrição detalhada de cada etapa.
        **Se os endereços de origem e destino for diferente da região metropolitana de São Paulo , informar que você não poderá efetuar esse trajeto**
        ** Para parte do roteiro que precise pegar linha de onibus não informar o status da linha e nem informações como se existe escalas rolantes, elevadores , etc...**
        ** adicionar tag html para fazer a divisão do roteiro entre paragrafos **
        ** Não adicione título do roteiro**
        **Dados de Entrada:**
* **Resumo do trajeto:** Uma breve descrição do ponto de partida, destino e principais pontos de interesse.
* **Descrição detalhada:** Um dicionário onde cada chave representa uma etapa do trajeto e o valor associado contém informações como:
    * Estação de origem e destino
    * Linhas envolvidas (se houver baldeação)
    * Tempo estimado de viagem
    * Observações relevantes (por exemplo, escadas rolantes, elevadores, pontos de interesse próximos, status da operação da linha)
**Saída Esperada:**
* **Instruções claras e concisas:** Explique cada etapa do trajeto de forma simples, utilizando linguagem natural e evitando termos técnicos.
* **Informações sobre as linhas:** Indique as linhas envolvidas em cada etapa, alertando o usuário sobre a necessidade de baldeação quando necessário.
* **Informações dos status de operação das linhas:** Indique o status da operação da linha em questão se está em Operação Normal ou outro status, e adicione os comentários a respeito do mesmo   
* **Tempo e distância total:** Informe o tempo estimado de viagem e a distância total do trajeto.
* **Observações:** Inclua qualquer observação relevante para o usuário, como a existência de escadas rolantes, elevadores ou pontos de interesse próximos.
* **Mensagem positiva:** Finalize com uma mensagem encorajadora, como "Boa viagem!"
**Informações geradas para criar o Roteiro:**
Resumo do trajeto = {resumo_roteiro}
Descrição detalhada = {descricao_roteiro}

"""
        resposta = self.model.generate_content(
            [prompt],
            stream=True
        )
        resposta.resolve()
        resultado = ""
        try:
            resultado = resposta.text
        except ValueError:
            return "Não foi possível gerar o roteiro"
        if resultado:
            resultado = self.aplicar_negrito(resultado)
            return resultado



if __name__ == "__main__":
    from calcula_rota import CalcularRota
    from descrever_roteiro import DescreveRoteiroRota
    endOrigin = "Av. dos Autonomistas, 896 - Vila Yara, Osasco - SP, 06020-010"
    endDest = "Av. Prof. Fonseca Rodrigues, 2001 - Alto de Pinheiros, São Paulo - SP, 05317-020"
    
    # CALL NESSEÁRIO PARA RODAR O SISTEMA
    calcular_rota = CalcularRota(endOrigin,endDest)
    rota = calcular_rota.calcular_melhor_rota()
    roteiro = DescreveRoteiroRota(rota)
    resumo_rota,descricao_rota = roteiro.passo_a_passo_rota()
    humaniza = HumanizaResposta()


