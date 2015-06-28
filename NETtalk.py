import numpy as np
import pickle

E1 = 10.0


# phonemes = 'aiyuoOeE°2951@§3j8wpbtdkgfvszSZmnNlRxG-'
# phonemes = 'lmnoijkdef§ab8yzut5wp12sOgE@q°R9-'
phonemes = 'to-'
tailleOutput = len(phonemes)

def sortieOfPhoneme(c):
	index = phonemes.index(c)
	res = [0.]*len(phonemes)
	res[index] = 1.
	return res

# lettres = 'abcdefghijklmnopqrstuvwxyz:[]'
# lettres = 'abcdefilmnoprstu[]'
lettres = 'to'
nbLettre = 1 #2
tailleInput = (2*nbLettre+1)*len(lettres)
tailleCelluleInput = len(lettres)

tailleInter = 10 #30


indexLettres = {}
for i in range(len(lettres)):
	indexLettres[lettres[i]] = i


def sigmoide(s):
	return 1/(1+np.exp(-s))

def diffSigmoide(s):
	se = sigmoide(s)
	return se-se**2

alpha = 0.9
epsilon = 2.0

class Axone():
	"""docstring for Axone"""
	def __init__(self, n1,n2):
		self.w = -0.3 + 0.6*np.random.random()
		self.In = n1
		self.Out = n2
	

class Neurone():
	"""docstring for Neurone"""
	def __init__(self):
		super(Neurone, self).__init__()
		self.Inputs = []
		self.output = 0.
		self.delta = 0.

	def nouveauInput(self,n):
		self.Inputs.append(Axone(n, self))
		pass

	def E(self):
		s = 0.
		for a in self.Inputs : 
			s+= a.w * sigmoide(a.In.output)
		self.output = s
		return s

	def miseAJourOutput(self):
		self.output = self.E()
		pass


	def miseAJourPoids(self):
		for a in self.Inputs : 
			a.w= alpha*a.w+(1-alpha)*epsilon * a.Out.delta*sigmoide(a.In.output)

	def __repr__(self):
		return str(sigmoide(self.output))

class Reseau():
	"""docstring for Reseau"""

	def __init__(self):
		self.In = [Neurone() for k in range(tailleInput)]
		self.Out = [Neurone() for k in range(tailleOutput)]
		self.Inter = [Neurone() for k in range(tailleInter)] # 80

		for n1 in self.In : 
			for n2 in self.Inter : 
				n2.nouveauInput(n1)
		for n1 in self.Inter : 
			for n2 in self.Out : 
				n2.nouveauInput(n1)
		pass




	def reinitialise(self):
		for n in self.In : 
			n.output = 0.
		for n in self.Inter : 
			n.output = 0.
		for n in self.Out :
			n.output = 0.
		pass

	def entreeLettre(self,mot,k):
		self.reinitialise()
		for i in range(-nbLettre,nbLettre+1):
			try :
				index = indexLettres[mot[k+i]]
			except : 
				if k+i<0 :
					index = -2
				elif k+i > len(mot): 
					index = -1
				else : 
					index = 0
			self.In[tailleCelluleInput*(nbLettre+i)+index].output = E1 
		pass

	def phonemeOfSortie(self):
		M = sigmoide(self.Out[0].output)
		iMax = 0
		for i in range(1,len(self.Out)):
			if sigmoide(self.Out[i].output) >M:
				M = sigmoide(self.Out[i].output)
				iMax = i
		return phonemes[iMax]


	def calcule(self, mot,k):
		self.entreeLettre(mot,k)
		for n in self.Inter : 
			n.miseAJourOutput()
		for n in self.Out :
			n.miseAJourOutput()
		pass

	def reinitialiseDelta(self):
		for n in self.Inter:
			n.delta = 0.
		for n in self.In : 
			n.delta = 0.
		# for n in self.Out : 
		# 	n.delta = 0.
		pass

	def apprentissage(self, mot, phonemesVoulus):
		for k in range(len(mot)):
			# On calcule à la position k
			self.calcule(mot,k)
			# réinitialisation des delta
			self.reinitialiseDelta()
			# calcul de la sortie voulue
			pVoulu = sortieOfPhoneme(phonemesVoulus[k])
			# on met à jour le delta de la couche Output et Inter
			for i in range(len(self.Out)) : 
				# Mise à jour du delta de l'Output
				self.Out[i].delta = (pVoulu[i] - sigmoide(self.Out[i].output))*diffSigmoide(self.Out[i].output)
				# on met à jour delta Inter
				for a in self.Out[i].Inputs : 
					a.In.delta += self.Out[i].delta * a.w * diffSigmoide(a.In.output)
			# On met à jour les delta de In
			for n in self.Inter : 
				for a in n.Inputs : 
					a.In.delta += n.delta * a.w * diffSigmoide(a.In.output)
			# On met à jour les poids
			for n in self.Inter : 
				n.miseAJourPoids()
			for n in self.Out : 
				n.miseAJourPoids()
		pass


