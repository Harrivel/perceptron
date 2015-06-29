from NETtalk import *
import pickle
import matplotlib.pyplot as plt 		# tracé de courbe


with open('ReseauNETtalk.pkl', 'rb') as fichier:
	R = pickle.load(fichier)

# R = Reseau()

# R.calcule("youpi", 3)
# print(R.phonemeOfSortie())

s = ""
mot = "mener"
for k in range(len(mot)):
	res = R.calcule(mot,k)
	print(R.Out)
	s+=R.phonemeOfSortie()
print(s)

erreurs = np.load('erreurs.npy')
plt.plot(erreurs)
plt.show()