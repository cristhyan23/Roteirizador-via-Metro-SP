## Roteiro de Viagem - Transporte Público

Este projeto é uma aplicação web Flask que ajuda os usuários a encontrar a melhor rota de transporte público entre dois endereços, gerando um roteiro detalhado e humanizado, utilizando a API do Google Maps e informações sobre o status das linhas de trem e metrô. 

**Funcionalidades:**

* **Busca de Rotas:** Encontre a melhor rota de transporte público entre dois endereços inseridos pelo usuário.
* **Roteiro Detalhado:** O aplicativo gera um roteiro detalhado com instruções passo-a-passo, incluindo informações sobre embarque, desembarque, linhas envolvidas e status das estações.
* **Mapa Interativo:** Visualize a rota no mapa do Google Maps com marcadores para cada ponto do trajeto.
* **Integração com a API do Google Maps:** Utiliza a API de direções do Google Maps para calcular a melhor rota de transporte público.
* **Status das Linhas:** O aplicativo consulta informações sobre o status atual das linhas de trem e metrô (operação normal, problemas, etc.) para fornecer um roteiro mais preciso e atualizado.

**Tecnologias Utilizadas:**

* **Flask:** Framework web para Python.
* **Google Maps API:** API para serviços de mapas e direções do Google.
* **Google Generative AI:** Modelo de inteligência artificial para gerar textos humanizados e personalizados.
* **BeautifulSoup:** Biblioteca para análise de conteúdo HTML.
* **Requests:** Biblioteca para fazer requisições HTTP.
* **Pandas:** Biblioteca para manipulação e análise de dados.
* **fuzzywuzzy:** Biblioteca para calcular a similaridade entre strings.
* **HTML, CSS, JavaScript:** Linguagens web para a interface do usuário.

**Instalação:**

1. **Instale o Python:** Certifique-se de ter o Python instalado em sua máquina.
2. **Clone o repositório:** Clone o repositório deste projeto para sua máquina local usando o comando: `git clone https://github.com/seu-usuario/roteiro-viagem`.
3. **Crie um arquivo `.env`:** Copie o arquivo `.env.example` para `.env` e adicione suas chaves de API do Google Maps e Google Generative AI.
4. **Instale as dependências:** Execute o comando `pip install -r requirements.txt` para instalar as bibliotecas necessárias.

**Execução:**

1. Navegue até o diretório raiz do projeto.
2. Execute o comando `flask run` para iniciar o servidor.
3. Acesse o aplicativo em `http://127.0.0.1:5000/` em seu navegador.

**Contribuições:**

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, solicitar funcionalidades e enviar pull requests.

**Licença:**

Este projeto está licenciado sob a licença [MIT](LICENSE).

**Observações:**

* Este projeto é um trabalho em andamento e pode conter bugs ou funcionalidades incompletas.
* As informações sobre o status das linhas de trem e metrô são coletadas do site da Viamobilidade e podem não ser atualizadas em tempo real.
* O aplicativo utiliza APIs externas, e seus termos de serviço devem ser respeitados.

**Agradecimentos:**

* Agradecimentos ao Google pela API de direções do Google Maps e ao Google Generative AI.
* Agradecimentos à Viamobilidade pela disponibilidade das informações sobre as linhas de trem e metrô.

**Recursos Úteis:**

* [Documentação do Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [API do Google Maps](https://developers.google.com/maps)
* [Google Generative AI](https://generativeai.google.com)
* [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
* [Requests](https://requests.readthedocs.io/en/latest/)
* [Pandas](https://pandas.pydata.org/docs/)
* [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/)
