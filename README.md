
###  Artificial Intelligence Project - Reinforced Learning Algorithm - Modified QLearning - Universidade dos Açores 2020/2021  ###



###  Base code  ###

  Agent0_minotauro_RL (project)
  
  - example.py (client file)
  - main.py (server file)
  - config.json - Json file used to configure the connection, and map (environment) details such as rewards, goal_coordinates, target_coordinates, object_map.
 
 
###  Modified Code  ###

- example.py - This file contains the Client side of the software, which when connected to main.py (Server) will allow the modified QLearning algorithm to start exploring the world during a predefined number of episodes. Each episode contains one exploration ending when the agent finds the goal position (G), or the (Target) position, in some cases.
  
- We were proposed to modify the provided code, coding it with the necessary instructions to be able to produce the following:
  
    - Once an episode is completed, the information regarding the reward for each action (per position) is filled in the QLearning table (qTable in our case).

    - Once a predefined number of episodes is completed, the QLearning table will be filled with the best rewards for each of the explored world positions, information that will            then be used to graphically represent the best policy for each of those positions. This is done by use of the "marrow" function, which prints directional arrows in the world map, pointing the best possible move for each position.


###  Project Goals  ###

O objetivo deste projeto foi o implementar o algoritmo Q-Learning adaptado, inserido no contexto da Aprendizagem por Reforço. O Agente é colocado num ambiente simples, onde é colocada uma casa objetivo (G) e em alguns cenários um alvo (T). Dependendo do número de episódios, e à medida que o número destes é incrementado, o agente consegue melhor preencher a matriz Q-learning com as políticas, através do cálculo da recompensa, estado a estado, sendo que por fim, e no caso de serem utilizados episódios suficientes, estas apresentam os resultados (políticas) a convergir para a casa objetivo (G).

###  Notes  ###

O algoritmo utilizado foi o Q-learning adaptado, em que o agente através de uma exploração aleatória do mundo contabilizada em vários episódios, vai calculando o melhor comportamento a ter para cada um dos estados do mapa. Cada episódio termina quando o agente atinge a casa objetivo (G) ou a casa alvo (T). Ao fim de um determinado número de episódios, é alterada a matriz Q-learning, com as recompensas para cada estado e ação, sendo então apresentadas as melhores escolhas do agente, denonimadas de “políticas”. Estas são representativas do comportamento ótimo do agente, em cada posição do tabuleiro e baseadas no cálculo da recompensa para cada ação, em relação a cada estado.

O cálculo de Q é efetuado através da soma de cada recompensa “r” com a multiplicação entre a parâmetro de desconto “y”, cujo valor utilizado foi de 0,9 e a maior recompensa para cada estado e ação. O agente desloca-se aleatoriamente até encontrar o objetivo, ou o target, e quando o faz, ajustam-se os valores da matriz Q-learning, ao fim de cada episódio. Quando terminados os episódios, são então representadas, com setas, as políticas finais calculadas pelo algoritmo, baseadas nos valores de maior recompensa presente na matriz. Caso haja empate de valores, a prioridade de escolha definida foi Norte, Este, Sul, Oeste.


## Como correr:

### Servidor:  

Na linha de comandos, **a partir do diretório principal do projeto**, executar:  
    ```python3 server/main.py```  
  
### Cliente:  

Na linha de comandos, **a partir do diretório principal do projeto**, executar:  
    ```python3 client/example.py```  
    

###  Programmers  ###

|    André Sousa    |    Bruno Viveiros    |    Gonçalo Almeida    |


