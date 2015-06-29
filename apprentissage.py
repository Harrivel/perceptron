from NETtalk import *
import matplotlib.pyplot as plt 		# tracé de courbe


R = Reseau()
# with open('ReseauNETtalk.pkl', 'rb') as fichier:
# 	R = pickle.load(fichier)

# dicoFinal = np.load('dicoFinal.npy')
# print("taille du dico : ", len(dicoFinal))

dico = np.load('dicoBase.npy')
print("taille du dico : ", len(dico))

nbMots = 0
nbPasse = 2
erreurs = []
for p in range(nbPasse) :
	print("passe", p+1)
	for k in range(len(dico)):
		# pour voir l'évolution
		if k%(len(dico)//20) == 0 :
			print((100*k)//len(dico), "%")
		R.apprentissage(dico[k][0], dico[k][1])
		nbMots +=1
		erreurs.append(R.erreur(dico))
print("nb mots entrés :", nbMots)


with open('ReseauNETtalk.pkl', 'wb') as fichier:
	pickle.dump(R, fichier, pickle.HIGHEST_PROTOCOL)

np.save('erreurs', erreurs)

plt.plot(erreurs)

