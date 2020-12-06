import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt


#Criando dados de perfis dos consumidores
tam = 20000
perfil_1 = np.zeros((1, tam))
cores1 = [2, 1]
estilos = [1, 3, 9]
idade = np.random.randint(18,36, size=(1, tam))
localidade = np.random.randint(10,16, size=(1, tam))
faixa_Salarial  = np.random.randint(500, 1045, size=(1, tam))
estado_Civil = tecnologia = np.zeros((1, tam))
produto = np.random.randint(2, size=(1, tam))
valor_max = np.random.randint(800, 1000, size=(1, tam))
Cor = np.random.choice(cores1, size=(1, tam))
tecnologia = np.zeros((1, tam))
utilidade =  np.zeros((1, tam))
estilos_Decora = np.random.choice(estilos, size=(1, tam))
list = (idade, localidade, faixa_Salarial,estado_Civil, produto, valor_max,Cor,tecnologia,utilidade, estilos_Decora)
for i in list:
    perfil_1= np.vstack((perfil_1,i))
perfil_1 = perfil_1.T


perfil_2 = np.ones((1, tam))
cores2 = [0,1]
loc= [26, 12, 13, 14]
estilos2 = [1,6,8]
idade = np.random.randint(29,44, size=(1, tam))
localidade = np.random.choice(loc, size=(1, tam))
faixa_Salarial  = np.random.randint(1045, 3135, size=(1, tam))
estado_Civil = np.ones((1, tam))
produto = np.random.randint(1,3, size=(1, tam))
valor_max = np.random.randint(800, 2000, size=(1, tam))
Cor = np.random.choice(cores2, size=(1, tam))
tecnologia = np.zeros((1, tam))
utilidade =  np.zeros((1, tam))
estilos_Decora = np.random.choice(estilos2, size=(1, tam))
list = (idade, localidade, faixa_Salarial,estado_Civil, produto, valor_max,Cor,tecnologia,utilidade, estilos_Decora)
for i in list:
    perfil_2= np.vstack((perfil_2,i))
perfil_2 = perfil_2.T


perfil_3 = np.ones((1, tam))+1
cores3 = [2, 1]
estilos3 = [3,4,5,7]
idade = np.random.randint(45,61, size=(1, tam))
localidade = np.random.randint(22,26, size=(1, tam))
faixa_Salarial  = np.random.randint(1045, 5225, size=(1, tam))
estado_Civil = np.random.randint(2, size=(1, tam))
produto = np.random.randint(2,4, size=(1, tam))
valor_max = np.random.randint(1500, 4000, size=(1, tam))
Cor = np.random.choice(cores3, size=(1, tam))
tecnologia = np.random.randint(2, size=(1, tam))
utilidade =  np.random.randint(2, size=(1, tam))
estilos_Decora = np.random.choice(estilos3, size=(1, tam))
list = (idade, localidade, faixa_Salarial,estado_Civil, produto, valor_max,Cor,tecnologia,utilidade, estilos_Decora)
for i in list:
    perfil_3= np.vstack((perfil_3,i))
perfil_3 = perfil_3.T

perfil_4 = np.ones((1, tam))+2
cores4 = [2,1,4,0]
estilos4 = [2,8,3,4,5]
idade = np.random.randint(53,78, size=(1, tam))
localidade = np.random.randint(10,23, size=(1, tam))
faixa_Salarial  = np.random.randint(5225, 15000, size=(1, tam))
estado_Civil = np.random.randint(2, size=(1, tam))
produto = np.random.randint(4,6, size=(1, tam))
valor_max = np.random.randint(4000, 8000, size=(1, tam))
Cor = np.random.choice(cores4, size=(1, tam))
tecnologia = np.ones((1, tam))
utilidade =  np.ones((1, tam))
estilos_Decora = np.random.choice(estilos4, size=(1, tam))
list = (idade, localidade, faixa_Salarial,estado_Civil, produto, valor_max,Cor,tecnologia,utilidade, estilos_Decora)
for i in list:
    perfil_4= np.vstack((perfil_4,i))
perfil_4 = perfil_4.T


perfil_5 = np.ones((1, tam))+3
cores5 = [2, 1, 4, 3]
estilos5 = [2,9,3,4,5]
idade = np.random.randint(29,53, size=(1, tam))
localidade = np.random.randint(18,26, size=(1, tam))
faixa_Salarial  = np.random.randint(5225, 20000, size=(1, tam))
estado_Civil = np.random.randint(2, size=(1, tam))
produto = np.random.randint(4,6, size=(1, tam))
valor_max = np.random.randint(5000, 10000, size=(1, tam))
Cor = np.random.choice(cores5, size=(1, tam))
tecnologia = np.ones((1, tam))
utilidade =  np.ones((1, tam))
estilos_Decora = np.random.choice(estilos5, size=(1, tam))
list = (idade, localidade, faixa_Salarial,estado_Civil, produto, valor_max,Cor,tecnologia,utilidade, estilos_Decora)
for i in list:
    perfil_5= np.vstack((perfil_5,i))
perfil_5 = perfil_5.T

PerfilGeral = np.zeros((1,11))
PerfilGeral= np.vstack((PerfilGeral,perfil_1))
PerfilGeral= np.vstack((PerfilGeral,perfil_2))
PerfilGeral= np.vstack((PerfilGeral,perfil_3))
PerfilGeral= np.vstack((PerfilGeral,perfil_4))
PerfilGeral= np.vstack((PerfilGeral,perfil_5))

PerfilGeral = PerfilGeral[1:]

PerfilGeral = shuffle(PerfilGeral)

X = PerfilGeral [:,1:]
y = PerfilGeral [:,:1]
y = y.astype(int)
y = to_categorical(y)


# Dividindo o dataset em dados de treino e de teste.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 100)

# Normalização dos dados.
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Construindo a IA
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard
from tensorflow.keras import regularizers

input_dim = X_train.shape[1]
output_dim = y_train.shape[1]

nb_epoch = 100
batch_size = 32
input_layer = Input(shape=(input_dim,))

input = Dense(input_dim, activation='sigmoid', activity_regularizer=regularizers.l1(10e-50))(input_layer)
hidden_layer = (Dense(14, activation="relu")(input))
hidden_layer = Dense(14, activation='relu')(hidden_layer)
hidden_layer = Dense(10, activation='relu')(hidden_layer)
output = Dense(output_dim, activation='softmax')(hidden_layer)

IA = Model(inputs=input_layer, outputs=output)

IA.compile(optimizer='adam',
                    loss='categorical_crossentropy',
                    metrics=['accuracy'])

checkpointer = ModelCheckpoint(filepath="model_seqs2.h5",
                               verbose=0,
                               save_best_only=True)

tensorboard = TensorBoard(log_dir='./logs',
                          histogram_freq=0,
                          write_graph=True,
                          write_images=True)

history = IA.fit(X_train, y_train,
                          epochs=nb_epoch,
                          batch_size=batch_size,
                          shuffle=True,
                          validation_data=(X_test, y_test),
                          verbose=1,
                          callbacks=[checkpointer, tensorboard]).history

#Carregando memória da IA salva
IA = load_model('model_seqs2.h5')
print(f'Min Loss:{np.min(history["loss"])}')
print(f'Max Accuracy:{np.max(history["accuracy"])}')
Client_01 = IA.predict(sc.transform(np.array([[48,22,4722,0,2,2341,2,1,1,4]])))
for i in Client_01:
    if i[0] > 0.5:
            print('Cliente JOÃO possui: PERFIL O1')
    if i[1] > 0.5:
            print('Cliente JOÃO possui: PERFIL O2')
    if i[2] > 0.5:
            print('Cliente JOÃO possui: PERFIL O3')
    if i[3] > 0.5:
            print('Cliente JOÃO possui: PERFIL O4')
    if i[4] > 0.5:
            print('Cliente JOÃO possui: PERFIL O5')

#Plot
plt.plot(history['loss'])
plt.plot(history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')

plt.plot(history['accuracy'])
plt.plot(history['val_accuracy'])
plt.title('model acc')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train loss', 'test loss', 'train acc', 'test acc'], loc='upper right')
plt.show()
