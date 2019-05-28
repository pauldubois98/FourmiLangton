from tkinter import *
from PIL import Image


class Fourmi(object):
    def __init__(self, grille, init_x=0, init_y=0, init_orient=3, fourmiSet=1):
        """init"""
        #variables
        self.grille=grille,
        self.x=init_x
        self.y=init_y
        #1:UP, 2:LEFT, 3:DOWN, 4/0:RIGHT
        self.orient=init_orient
        
        #variables de la grille
        self.largeurCase=grille.largeurCase
        self.hauteurCase=grille.hauteurCase

        #calcule du zoom
        zoom=int(120-1.6*grille.largeurCase)

        #images
        if fourmiSet==0:
            noms=['fourmiDroite','fourmiBas',\
                  'fourmiGauche','fourmiHaut']
        else:
            noms=['fourmiDroiteBis','fourmiBasBis',\
                  'fourmiGaucheBis','fourmiHautBis']
        self.img=[PhotoImage(file='img/'+noms[i]+'.png').subsample(zoom) for i in range(4)]
        #initialisation de l'objet graphique
        self.graphObj=grille.can.create_image(self.largeurCase*(self.x+0.5), \
                                              self.hauteurCase*(self.y+0.5), \
                                              image=self.img[init_orient])
    
    def move(self):
        """moves of 1 step"""
        #change the orientation
        if self.grille[0].get(self.x, self.y):
            self.orient=(self.orient+1)%4
        else:
            self.orient=(self.orient-1)%4
        #change la case de la grille
        self.grille[0].change(self.x, self.y)
        #bouge en x & y
        if self.orient==0:
            if self.x>=self.grille[0].larg-1:
                #print('out')
                return 'error'
            else:
                self.x+=1
        elif self.orient==1:
            if self.y>=self.grille[0].haut-1:
                #print('out')
                return 'error'
            else:
                self.y+=1
        elif self.orient==2:
            if self.x<1:
                #print('out')
                return 'error'
            else:
                self.x-=1
        elif self.orient==3:
            if self.y<1:
                #print('out')
                return 'error'
            else:
                self.y-=1
        
        #bouge graphiquement
        self.grille[0].can.coords(self.graphObj, \
                               self.largeurCase*(self.x+0.5), \
                               self.hauteurCase*(self.y+0.5))
        self.grille[0].can.itemconfigure(self.graphObj, \
                                         image=self.img[self.orient])

    def effacer(self):
        self.grille[0].can.delete(self.graphObj)

        

