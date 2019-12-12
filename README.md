# Projeto final da disciplina de Programação para Redes

Professor: Charles Cesar Magno de Freitas

Turma: Programação para Redes - 2019.2;

Alunos: Felipe da Silva Costa e Guilherme Souza Anizio

# Objetivo

Utilizando a linguagem Python em conjunto com a plataforma Arduino, o projeto tem como objetivo a obtenção de dados de dois sensores (DHT11 e MQ2);
bem como seu armazenamento em um banco de dados e suas visualizações.

#Primeiro instale o git em sua máquina: ```sudo apt install git```.

#Em seguida clone este repositório ```***``` e entre nele.

# Configurando o ambiente:
  #Instale o Python e pip3: ```sudo apt install python3 python3-pip```.
  
  #Instale as dependências para o Python: ```sudo pip3 install -r requirements.txt ```
  
  #Substitua a variável ```ip_servidor``` dos arquivos [APP.py](Codigos/APP.py), [Arduino.py](Codigos/Arduino.py) e [Cliente.py](Codigos/Cliente.py) para o respectivo IP das máquinas.
  
  #Faça o upload do arquivo [CodigoArduino.ino](Arduino/CodigoArduino.ino) para o seu Arduino.

# Execução

  #Execute o arquivo [APP.py](Codigos/APP.py) no servidor.
  
  #Execute os arquivos [Arduino.py](Codigos/Arduino.py) e [Cliente.py](Codigos/Cliente.py) na máquina cliente.


  1) O codigo [Arduino.py](Codigo/Arduino.py) receberá os dados enviados do Arduino para a porta serial e enviá-los ao servidor.
  2) O codigo [Cliente.py](Codigo/Cliente.py) faz requisições ao servidor em busca dos dados definidos em tempo real pelo cliente.
  3) Após os dados serem obtidos, o codigo [Cliente.py](Codigos/Cliente.py) salva em um arquivo no formato JSON e exibe a média     dos mesmos para o usuário. O usuário tem quatro opções de consulta: temperatura, humidade, gás e todas as anteriores.
  
  Circuito do arduino:
  
  <p align="center">
    <img src="IMG/Circuito.jpeg" alt="imagem do circuito arduino">
</p>
