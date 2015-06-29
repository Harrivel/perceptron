from NETtalk import *
import pickle

dicoFinal = np.load('dicoFinal.npy')
print("taille du dico : ", len(dicoFinal))

dicoBase = []
nbBase = 100
for i in range(nbBase):
	dicoBase.append(dicoFinal[np.random.randint(1,len(dicoFinal))])

np.save('dicoBase', dicoBase)