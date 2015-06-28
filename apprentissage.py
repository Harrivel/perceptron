from NETtalk import *


R = Reseau()
# with open('ReseauNETtalk.pkl', 'rb') as fichier:
# 	R = pickle.load(fichier)

# R.calcule("youpi", 3)
# print(R.phonemeOfSortie())

dicoFinal = np.load('dicoFinal.npy')
print("taille du dico : ", len(dicoFinal))

# for k in range(10,1000):
# 	if len(dicoFinal[k][0])<8:
# 		print("apprentissage du", k, "-ième mot :", dicoFinal[k][0])
# 		R.apprentissage(dicoFinal[k][0], dicoFinal[k][1])

print(dicoFinal[17])
for i in range(30):
	print("itération ", i)
	# R.apprentissage(dicoFinal[17][0], dicoFinal[17][1])
	R.apprentissage("toto", "to-t")



with open('ReseauNETtalk.pkl', 'wb') as fichier:
	pickle.dump(R, fichier, pickle.HIGHEST_PROTOCOL)

