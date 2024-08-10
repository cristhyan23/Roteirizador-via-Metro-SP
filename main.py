from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv() # Carregar variáveis de ambiente do arquivo .env



#inicializa a aplicação flask
app = Flask(__name__,static_folder='static')
app.secret_key= os.urandom(24)
# Set the folder where uploaded files will be saved
app.config['UPLOAD_FOLDER'] = 'uploads'

#Roda a aplicação
if __name__ == "__main__":
    from views import *
    app.run(debug=True)