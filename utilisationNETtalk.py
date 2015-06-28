from NETtalk import *
import pickle

with open('ReseauNETtalk.pkl', 'rb') as fichier:
	R = pickle.load(fichier)

R = Reseau()

s = ""
mot = "toto"
for k in range(len(mot)):
	res = R.calcule(mot,k)
	print(R.Out)
	s+=R.phonemeOfSortie()
print(s)

