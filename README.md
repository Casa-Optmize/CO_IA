# INTELIGÊNCIA ARTIFICIAL PARA PREDIÇÃO DO PERFIL DE CONSUMIDORES

### Como Usar a Rede DEEP LEARNING Treinada

1. Download do git:https://github.com/Casa-Optmize/CO_IA
2. Descompactar os arquivos em rar na pasta dados
3. Abrir IA_memory.py como arquivo python 3.6 ou +

### Como treinar o modelo da IA

1. Download do https://github.com/Casa-Optmize/CO_IA.git
2. Descompactar os arquivos em rar na pasta dados
3. Abrir Predict.py como arquivo python 3.6 ou +

### Requirements mínimos da solução
* Windows or Linux
* Python 3.68 
* Keras==2.4.3
* matplotlib==3.3.2
* numpy==1.18.5
* sklearn==0.0
* tensorflow==2.2


### Dataset
Os dados de 100 mil consumidores foram criados para a solução como MVP, lenvando as seguintes carácteisticas, que, a priori, serão coletadas do aplicativo.

##### INFORMAÇÕES DO FORM/APP UTILIZADAS NA IA
##### DADOS DE PERFIL/CADASTRO

- Idade: até 28, 29-36, 37-44, 45-52, 53-60, acima de 60
- Localização/cep: 0-26
- Faixa Salarial: Até um salário mínimo, mais de 1 a 3, mais de 3 a 5, acima de 5
- Estado civil: Casado=1, solteiro=0



##### DADOS DA COMPRA.
- O que deseja comprar: Produto 1 a Produto 6
- Valor máximo: 800 a 15000
- Cor: Azul=4, branco=0, cinza=2, preto =1, marrom=3
- Tecnologia: Simples=1, Alta tecnologia =2
- Utilidade: Básico=1, completo=0
- Estilos de Decoração: clássico=0, rústico=1, luxuoso=2, moderno=3, industrial=4, minimalista=5, Popular=6, Retrô=7, Escandinava=8, Vintage=9.

###### Perfil 1
- Idade: 18 até 28, 29-36, 	
- Localidade: 10 a 16
- Faixa Salarial: Até um salário mínimo,
- Estado civil: Solteiro = 0
- O que deseja comprar: Produto 0 ou 1
- Valor máximo: de 800 a 1000
- Cor: cinza, preto, 
- Tecnologia: Simples
- Utilidade: Básico
- Estilos de Decoração: Clássico, moderno, Vintage.

###### Perfil 2
- Idade: 29-36, 37-44,	
- Sexo: Masculino e feminino
- Localidade: 26,12, 13, 14
- Faixa Salarial: mais de 1 a 2
- Estado civil: Casado =1
- O que deseja comprar: Produto 2 ou 3
- Valor máximo: de 800 a 2000
- Cor: branco, preto
- Tecnologia: Simples
- Utilidade: Básico
- Estilos de Decoração: rústico, Popular, Escandinava.

###### Perfil 3
- Idade: 45-52, 53-60	
- Localidade: 22 a 25
- Faixa Salarial: mais de 1 a 3, mais de 3 a 5
- Estado civil: Casado e Solteiro
- O que deseja comprar: Produto 2 ou 3
- Valor máximo: de 1500 a 4000
- Cor: cinza, preto 
- Tecnologia: Simples e tecnológico
- Utilidade: Básico e completo
- Estilos de Decoração: moderno, industrial, minimalista, Retrô.

###### Perfil 4
- Idade: 53-60, acima de 60	
- Localidade: 10 a 22
- Faixa Salarial: acima de 5
- Estado civil: Casado e Solteiro
- O que deseja comprar: Produto 4 a 6
- Valor máximo: de 4000 a 8000
- Cor: Azul, branco, cinza, preto 
- Tecnologia: Tecnológico
- Utilidade: Completo
- Estilos de Decoração: luxuoso, industrial, minimalista, Escandinava.

###### Perfil 5
- Idade: 29-36, 37-44, 45-52	
- Sexo: Masculino e feminino
- Localidade: 18 a 26
- Faixa Salarial: acima de 5
- Estado civil: Casado e Solteiro
- O que deseja comprar: Produto 4 a 6
- Valor máximo: de 4000a 10000
- Cor: cinza, preto, azul, marrom
- Tecnologia: tecnológico
- Utilidade: Completo
- Estilos de Decoração: Luxuoso, Moderno, Industrial, Minimalista, Vintage.



### Codigo de Treinamento da rede realiza as seguintes ações.

0. Usa o Predict.py
1. Na primeira etapa do codigo são criados dados randomicamente com características de usuários, conforme pesquisa.
2. Distribuição dos dados para treino e teste e padronização dos dados em uma escala de 0 a 1.
3. Entrada na IA
4. Salva o modelo

### Codigo carregado no servidor.

0. Usa o IA_memory.py
1. Carrega o modelo "model_seqs2.h5".
2. Insere as características do novo usuário do app.
3. Predição do Perfil do Usuário - Para o caso de teste o perfil do usuário João foi identificado corretamente como 3.

### Resultados
O modelo chega a apresentar acurácia de 99,9% para aprendizagem das correlações exitentes nas variáveis categóricas do estudo. A função loss chega a obter resultados de 4x10-7.
Para os testes realizados com a inserção dos dados. Os resultados foram obtidos com êxito na identificação do Perfil do cliente simulado no código.

##### Resultado para 100 mil dados de entrada com execução em 100 épocas.
<img src="/Figure_1.png" alt="Koa middleware framework for nodejs"/>

