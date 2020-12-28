# Implémentation de l'approche d'estimation du livre de Michael Ong.

import numpy as np

# Matrice de corrélation des défaillances de 3 catégories d'entreprises.
corr_mat = np.array([[1,0.2981, 0.5345], 
                	 [0.2981,1,0.5976], 
					 [0.5345, 0.5976,1]])

# Décomposition de Cholesky de la matrice de corrélation
L = np.linalg.cholesky(corr_mat)

# Génération de 3 points de défaillances (Default Points) via une Loi Normale Inverse:
from scipy.stats import norm
DPoint = np.array([norm.ppf(0.1), norm.ppf(0.2), norm.ppf(0.9)])	# generate random vector of 3 default points for each company

# Paramètres:
EAD = [1000, 7000, 4000]	# EAD (Exposure at Default)
LGD  = 0.2					# LGD (Loss Given Default) moyen
Loss_Distribution = []		# Liste vide des données de la distribution finale à estimer

# Méthode de simulation:

def Monte_Carlo():

	Total_Loss = []
	TLoss = 0
	for i in range(0,10):
	    asset_values = np.array(np.random.normal(0,1,3))
	    x = np.matmul(asset_values, L)
	            
	    if asset_values[0] < DPoint[0]:			# default condition for company 1
	        L1 = EAD[0]*LGD
	        Total_Loss.append(L1)

	    elif asset_values[1] < DPoint[1]:		# default condition for company 2
	        L2 = EAD[1]*LGD
	        Total_Loss.append(L2)

	    elif asset_values[2] < DPoint[2]:   	# default condition for company 3
	        L3 = EAD[2]*LGD
	        Total_Loss.append(L3)

	    else:
	    	return None

	for i in Total_Loss:
	    TLoss = TLoss + i

	Loss_Distribution.append(TLoss) 

# Boucle de simulation:
iterations = 10_000
for i in range(0,iterations):
        Monte_Carlo()

print("The Distribution of Losses is:")
print(Loss_Distribution)

# Loss_Distribution aura désormais 10.000 observations que l'on pourrait tracer sur un histogramme pour afficher la Distribution des Pertes.
# La liste pourra être utilisée par la suite pour calculer toutes les grandeurs importantes: Perte Espérée, Perte Maximale, Perte Extrême, Intervalles de Confiance, etc.
