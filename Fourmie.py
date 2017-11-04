from tkinter import *
from PIL import Image


class Fourmie(object):
    def __init__(self, grille, init_x=0, init_y=0, init_orient=3, fourmieSet=1):
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
        if fourmieSet==0:
            noms=['fourmieDroite','fourmieBas',\
                  'fourmieGauche','fourmieHaut']
        else:
            noms=['fourmieDroiteBis','fourmieBasBis',\
                  'fourmieGaucheBis','fourmieHautBis']
        self.img=[PhotoImage(file=noms[i]+'.png').subsample(zoom) for i in range(4)]
        #initialisation de l'objet graphique
        self.graphObj=grille.can.create_image(self.largeurCase*(self.x+0.5), \
                                              self.hauteurCase*(self.y+0.5), \
                                              image=self.img[0])
    
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
            self.x+=1
            if self.x>=self.grille[0].larg:
                #print('out')
                return 'error'
        elif self.orient==1:
            self.y+=1
            if self.y>=self.grille[0].haut:
                #print('out')
                return 'error'
        elif self.orient==2:
            self.x-=1
            if self.x<0:
                #print('out')
                return 'error'
        elif self.orient==3:
            self.y-=1
            if self.y<0:
                #print('out')
                return 'error'
        #bouge graphiquement
        self.grille[0].can.coords(self.graphObj, \
                               self.largeurCase*(self.x+0.5), \
                               self.hauteurCase*(self.y+0.5))
        self.grille[0].can.itemconfigure(self.graphObj, \
                                         image=self.img[self.orient])

    def effacer(self):
        self.grille[0].can.delete(self.graphObj)

        
