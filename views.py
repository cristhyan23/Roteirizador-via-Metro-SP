from flask import render_template, request, redirect, flash, url_for, jsonify
import os
from dotenv import load_dotenv
from calcula_rota import CalcularRota
from descrever_roteiro import DescreveRoteiroRota
from humanizar_resposta import HumanizaResposta
from main import app
# Pegar a API Key do arquivo .env
google_maps_api_key = os.getenv('MAPS_API_KEY')
# Rota de início
@app.route("/")
def index():

    return render_template('index.html')

@app.route("/gerar_roteiro", methods=['POST'])
def gerar_roteiro():
    endOrigim = request.form.get('endOrigem')
    endDestino = request.form.get('endDestino')
    
    if not endOrigim:
        flash('Necessário informar o Endereço Origem!')
        return render_template('index.html')

    if not endDestino:
        flash('Necessário informar o Endereço Destino!')
        return render_template('index.html')

    calcula_rota = CalcularRota(endOrigim, endDestino)
    rota = calcula_rota.calcular_melhor_rota()
    roteiro = DescreveRoteiroRota(rota)
    resumo_rota, descricao_rota = roteiro.passo_a_passo_rota()
    
    humaniza = HumanizaResposta()
    roteiro_final = humaniza.humanizar_resposta_rota(resumo_rota, descricao_rota)

    return render_template('index.html', roteiro=roteiro_final,data=rota,api_key=google_maps_api_key)