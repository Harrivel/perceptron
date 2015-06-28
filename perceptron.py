from numpy import *

class perceptronUneCouche:
	def __init__(self, n):
		self.poids = [0.5]*n
		self.poids.append(1)  # on rajoute theta au dernier

	def HeavySide(self,s):
		if s>= 0 :
			return 1
		else : 
			return 0

	def sigmoide(self,s,T=1):
		return 1/(1+exp(-s/T))

	def dSigmoide(self,s,T=1):
		e = exp(-s/T)
		return 1/T*e/((1+e)**2)

	def calcul(self,entree, fonctionSeuil):
		fonctionSeuil = self.HeavySide
		s = 0
		for i in range(len(entree)):
			s += entree[i]*self.poids[i]
		s+= -self.poids[-1]
		return fonctionSeuil(s)

	def apprentissage(self, entree, reponse, pas = 0.3):
		reponseCalculee = self.calcul(entree, self.HeavySide)
		if reponseCalculee != reponse : 
			for i in range(len(entree)):
				self.poids[i] += pas*(reponse- reponseCalculee)*entree[i]
		pass

	def apprentissageWidrowHoff(self, entree, reponse, pas = 0.3):
		reponseCalculee = self.calcul(entree, self.sigmoide)
		s = self.calcul(entree, lambda x:x)
		derivee = self.dSigmoide(s)
		for i in range(len(entree)):
			self.poids[i] += pas*entree[i]*(reponse- reponseCalculee)*derivee
		self.poids[-1] += -pas*derivee*(reponse- reponseCalculee)
		pass

# numérotation :
#  -- 0 --
# |       |
# 1       2
# |       |
#  -- 3 --
# |       |
# 4       5
# |       |
#  -- 6 --
base = [
[1,1,1,0,1,1,1], 
[0,0,1,0,0,1,0], 
[1,0,1,1,1,0,1],
[1,0,1,1,0,1,1], 
[0,1,1,1,0,1,0],
[1,1,0,1,0,1,1],
[1,1,0,1,1,1,1],
[1,0,1,1,0,0,0],
[1,1,1,1,1,1,1],
[1,1,1,1,0,1,1]
]

P = perceptronUneCouche(7)
print(P.calcul(base[0], P.HeavySide))

# Apprentissage : au bout de 6 passes ça marche. 
# for i in range(6):
# 	for k in range(len(base)):
# 		P.apprentissage(base[k], k % 2)

# for k in range(len(base)):
# 	print("k=", k, " et réponse : ", P.calcul(base[k], P.HeavySide))

# Apprentissage : au bout de 12 passes ça marche. 
for i in range(12):
	for k in range(len(base)):
		P.apprentissageWidrowHoff(base[k], k % 2)

for k in range(len(base)):
	print("k=", k, " et réponse : ", P.calcul(base[k], P.sigmoide))

		