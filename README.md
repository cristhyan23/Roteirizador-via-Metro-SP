**Objetivo:** Esta aplicação web visa auxiliar usuários a planejar trajetos de transporte público na região metropolitana de São Paulo, utilizando a API do Google Maps e informações sobre o status das linhas de metrô e trem. 

**Público-alvo:** Usuários que desejam planejar viagens de transporte público na região metropolitana de São Paulo, buscando por rotas otimizadas e informações sobre o status das linhas.

**Funcionalidades:**

* **Busca de Rotas:**
    * O usuário insere o endereço de origem e destino no formulário da página inicial. 
    * A aplicação calcula a melhor rota de transporte público (trem e metrô) entre os endereços informados utilizando a API do Google Maps.
    * O sistema prioriza rotas que utilizam o transporte público, evitando caminhadas excessivas dentro de grandes terminais.
    * A aplicação considera o tráfego na hora de calcular a melhor rota, utilizando um modelo pessimista para estimativas.
* **Detalhes do Roteiro:**
    * A aplicação exibe um resumo da rota, incluindo pontos de partida e chegada, distância total e tempo estimado de viagem. 
    * O usuário pode visualizar uma descrição detalhada de cada etapa da rota, incluindo informações sobre as estações de embarque e desembarque. 
    * Para cada etapa que envolve transporte público, a aplicação exibe:
        * Nomes das estações de embarque e desembarque.
        * Linhas envolvidas, incluindo informações sobre baldeações.
        * Status da operação da linha (Operação Normal, Interrupção, etc.).
        * Detalhes adicionais sobre a linha (se houver), como informações sobre escadas rolantes, elevadores, etc.
* **Visualização no Mapa:**
    * A aplicação exibe um mapa interativo do Google Maps com a rota calculada.
    * A rota é representada por uma linha azul no mapa.
    * Marcadores coloridos são utilizados para indicar os pontos de partida, chegada e as estações de embarque e desembarque ao longo da rota.
    * O mapa é ajustado automaticamente para que todos os pontos da rota fiquem visíveis.

**Usabilidade:**

* **Interface Simples e Intuitiva:** A página inicial apresenta um formulário simples e intuitivo para a inserção dos endereços de origem e destino. 
* **Feedback Claro:** A aplicação fornece mensagens de erro e feedback claro para o usuário durante o processo de busca e geração do roteiro.
* **Informações Detalhadas:** O roteiro gerado inclui informações detalhadas sobre cada etapa, facilitando a compreensão do trajeto.
* **Mapa Interativo:** O mapa interativo do Google Maps permite que o usuário visualize a rota calculada de forma clara e intuitiva.
* **Informação Concisa:** A aplicação evita informações desnecessárias e se concentra em apresentar os dados relevantes para o planejamento da viagem.
* **Linguagem Natural:** As instruções e descrições do roteiro são escritas em linguagem natural e fáceis de entender.

**Cenários de Uso:**

* **Usuário busca por uma rota de metrô para um evento no centro de São Paulo:**
    * O usuário insere o endereço de sua casa e o endereço do evento no formulário da página inicial.
    * A aplicação calcula a melhor rota de metrô e exibe as informações detalhadas, incluindo as estações de embarque e desembarque, as linhas envolvidas e o tempo estimado de viagem.
    * O usuário visualiza a rota no mapa interativo e encontra a linha mais próxima de sua casa.
* **Usuário precisa se deslocar para um compromisso em outra cidade da região metropolitana:**
    * O usuário insere o endereço de sua casa e o endereço do compromisso.
    * A aplicação identifica a rota mais eficiente, utilizando uma combinação de metrô, trem e ônibus.
    * O roteiro é apresentado de forma clara, informando as estações de embarque e desembarque, as linhas envolvidas e o tempo estimado de viagem para cada etapa.

**Considerações:**

* A aplicação depende da disponibilidade e precisão da API do Google Maps para o cálculo de rotas.
* A aplicação utiliza dados coletados do site da Viamobilidade para informações sobre o status das linhas de metrô e trem. A precisão e atualização desses dados dependem da Viamobilidade.
* A aplicação é otimizada para a região metropolitana de São Paulo e pode não funcionar adequadamente para outras localidades. 

**Recursos Adicionais:**

* A aplicação pode ser aprimorada com recursos adicionais como:
    * Opção de escolher o modo de transporte preferido (metrô, trem, ônibus, etc.).
    * Integração com aplicativos de transporte público para fornecer informações sobre horários e previsões de chegada.
    * Opção de salvar ou compartilhar os roteiros gerados.
