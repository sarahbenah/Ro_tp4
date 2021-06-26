#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

#Exercice 1 qst 1 :
def lancerUnDe():
    d = random.randint(1,6)#La fonction randint est utile pour simuler un lancer de dé 
    return d

#Exercice 1 qst 2 :
def lancerDeNFois():
    listeDeDe = [] #la liste pour l'instant est vide
    print('\ncombien de fois voulez-vous lancer votre dé: ')
    n = inputNumber(' n= ')
    for i in range(n):
        d = lancerUnDe() #on lance un dé
        listeDeDe.append(d) #on ajoute le résultat à la liste
    return listeDeDe

#Exercice 1 qst 3 :
def chercher(n):
    myList=[]
    myList=lancerDeNFois() #on lance notre dé n fois
    print('\n Afficher la liste obtient: ', myList)
    a=myList.count(n) #calculer le nombre d’apparitions de la face 6
    return a

#Exercice 1 qst 4 :

def lancerjusqua6():
    listeDeDe = []
    s=0
    d=lancerUnDe() #on lance notre dé
    while d != 6: #on verfier notre résultat 
        listeDeDe.append(d)
        s=s+1  #calculer le nombre de fois avant d'obtenir le premier 6
        d=lancerUnDe()
    listeDeDe.append(d)
    return s , listeDeDe

#Exercice 1 qst 5 :

def lancerpiece():
    d = random.randint(1,2)
    if d == 1:
        return "Face" 
    else:
        return "Pile"
    
def lancerpieceNFois():
    listeDepiece= [] #la liste pour l'instant est vide
    print('\n combien de fois voulez-vous lancer votre piéce de monnaie : ')
    n = inputNumber(' n= ')
    for i in range(n):
        d = lancerpiece() #on lance une piéce
        listeDepiece.append(d) #on ajoute le résultat à la liste
    return listeDepiece   
    

#verification d'input (int)

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break    
    
#MAIN______________________________________________________________________________________________________________
print('\n Exercice 1: ')
print('\n Question 1: ')
print('lancer un dé une seul fois: ',lancerUnDe())

print('\n Question 2: ')
print('\n lancer un dé n fois: ',lancerDeNFois())

print('\n Question 3: ')
print('\n le nombre d’apparitions de la face 6 : ', chercher(6))

print('\n Question 4: ')
z=[]
s,z=lancerjusqua6()
print('\n le nombre de fois avant \'6\' est: ', s,' dans la liste  :',z)

print('\n Question 5: ')
print('\n lancer une piece n fois : ', lancerpieceNFois())

