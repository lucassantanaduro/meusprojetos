'''Este é meu primeiro modelo de aprendizado de
maquinha usando regressão linear simples.
'''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#carregando dataset
dataset = pd.read_csv('tempo_salarios.csv')
#separando variaveis idependentes e dependentes
X = dataset.iloc[:,:-1].values#coluna anos de experiencia
y = dataset.iloc[:,1].values#coluna salarios
#dividindo o dataset entre treino e teste (Divisão de amostra com verificação cruzada/cross-validation)
X_train, X_test, y_train, y_test = train_test_split(\
    X,y,test_size=1/3, random_state=0)
#ajustando o modelo de regressão linear para o dataset de treino
regressor = LinearRegression()
#prevendo o valor de y usando os valores de teste
regressor.fit(X_train,y_train)
y_pred = regressor.predict(X_test)#dataset de treino
#visualizar os resultados de treino/plotando todos os pontos da amostra
plt.figure(figsize=(15,8))
plt.plot(X,y,'Dr')
plt.title('Salario x Experiência')
plt.xlabel('Anos de Experiência')
plt.ylabel('Salario')
plt.show()
#visualizar os resultados de Teste/plotando modelo linear obtido atraves dos treinos
plt.figure(figsize=(15,8))
plt.plot(X_test,y_test,'Dr')
plt.plot(X_train,regressor.predict(X_train),color= 'blue')
plt.title('Salario x Experiência')
plt.xlabel('Anos de Experiência')
plt.ylabel('Salario')
plt.show()
#Modelo aprovado pois previu com acerto a relação entre as
# variaveis idependente(AnosDeExperiencia) e dependente(Salario)