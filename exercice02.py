#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np

# Exercice 2 qst 1 :
def vecteur_stochatique(vecteur):
    if sum(vecteur) == 1: #calculer la somme des coordonnées est verifier si égale a 1
        return True
    else:
        return False


# Exercice 2 qst 2 :
def verfier_matrice_caree(matrice):# vérifie si une matrice est carrée
    for v in matrice:
        if len(v) != len(matrice):#verfier si la 
            return False
        else:
            continue
    return True


def matrice_stochatique(matrice):# vérifie si une matrice est stochatique
    caree = verfier_matrice_caree(matrice)
    if caree == False:
        print("\nMatrice n'est pas carée")
        return False
    
    for v in matrice:
        if vecteur_stochatique(v) == False:
            return False
        else:
            continue
    return True
# Exercice 2 qst 3
def matrice_puissanceM(matrice, power):# matrice puissance M
    if matrice_stochatique(matrice) == False:
        print("\nMatrice non stochatique")
        return False
    np_matrice = np.array(matrice)
    powered = np.linalg.matrix_power(np_matrice, power)
    return powered

#MAIN______________________________________________________________________________________________________________
print('\n Exercice 2: ')
print('\n Question 1: ')

vecteur= input('\n introduire votre vecteur (exemple : 1/2/3/0 ou 0.2/0.3/0.5 ): ')
vecteur += '/' #*ici pour evité l'utilsation du split avec un vecteur sans '/' (evité l'echec)
tab = []
for i in vecteur.split('/'):
    try:
            tab.append(float(i))
    except:
            print ('Verifier vos informations (il faut que le vecteur soit des entier )')
            break
print('le vecteur ',tab,' est un vecteur stochatique: ',vecteur_stochatique(tab))

print('\n Question 2: ')

M = [[3, 1, 5], [9, 8, -1]]
C = [[0.5, 0.2, 0.3], [0.5, 0.0, 0.5], [0.25, 0.55, 0.20]]

a=matrice_stochatique(C)
print('\nla matrice M=', M,' :')
z=matrice_stochatique(M)
if z:
    print('\nla matrice M=', M,' est pas matrice stochatique ')
else:
    print('\nla matrice M=', M , ' n\'est pas matrice stochatique ')
print('\nla matrice C=', C ,' :')
a=matrice_stochatique(C)
if a:
    print('\nla matrice C=', C,' est pas matrice stochatique ')
else:
    print('\nla matrice C=', C , ' n\'est pas matrice stochatique ')
    
print('\n Question 3: ')
print('\nla matrice C=', C ,' :')
d = 2
print('\nla matrice C=', C , ' puissance ',d,' = \n',matrice_puissanceM(C, d))    


# In[ ]:




