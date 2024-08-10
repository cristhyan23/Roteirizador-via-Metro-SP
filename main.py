from flask import Flask
#inicializa a aplicação flask
app = Flask(__name__,static_folder='static')

#Roda a aplicação
if __name__ == "__main__":
    from views import *
    app.run(debug=True, port=5000,host='0.0.0.0')