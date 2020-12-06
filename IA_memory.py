import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
IA = load_model('model_seqs2.h5')
#IA Analizando um novo cliente
dataClient = np.array([[48,22,4722,0,2,2341,2,1,1,4]])
Client_01 = IA.predict(sc.transform(dataClient))
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