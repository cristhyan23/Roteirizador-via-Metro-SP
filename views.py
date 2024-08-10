from flask import render_template, request, flash, send_from_directory
import os
from dotenv import load_dotenv
from calcula_rota import CalcularRota
from descrever_roteiro import DescreveRoteiroRota
from humanizar_resposta import HumanizaResposta
from main import app
load_dotenv()
# Pegar a API Key do arquivo .env
google_maps_api_key = os.getenv('MAPS_API_KEY')
# Rota de início
@app.route("/")
def index():
    return render_template('index.html',api_key=google_maps_api_key)

@app.route('/files/<path:path>')
def send_static(path):
    return send_from_directory('files', path)

@app.route('/icon_map/<path:path>')
def send_img(path):
    return send_from_directory('icon_map', path)




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
    coordenadas = calcula_rota.gerar_lat_e_long_enderecos(rota)
    print(coordenadas)
    return render_template('index.html', roteiro=roteiro_final,coordenadas=coordenadas,endOrigem=endOrigim,endDestino=endDestino,api_key=google_maps_api_key)