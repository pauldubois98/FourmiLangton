from tkinter import *
from random import random



class Grille(object):
    def __init__(self, canvas, casesHauteur=10, casesLargeur=10, grille=None, \
                 init_type=1):
        """intelligent init values"""
        self.can=canvas
        #grille intelligente
        if grille is None:
            init_type=init_type%5
            if init_type==0:
                self.grille=[[int(random()+0.5) for i in range(casesLargeur)] \
                             for j in range(casesHauteur)]
            elif init_type==1:
                self.grille=[[0 for i in range(casesLargeur)] \
                             for j in range(casesHauteur)]
            elif init_type==2:
                self.grille=[[(i+j)%2==0 for i in range(casesLargeur)] \
                             for j in range(casesHauteur)]
            elif init_type==3:
                self.grille=[[(i+j)%4==3 for i in range(casesLargeur)] \
                             for j in range(casesHauteur)]
            elif init_type==4:
                self.grille=[[(i+j)%6==1 for i in range(casesLargeur)] \
                             for j in range(casesHauteur)]
            self.larg=casesLargeur
            self.haut=casesHauteur
        else:
            self.larg=len(grille[0])
            self.haut=len(grille)
            self.grille=grille
        #longeur & largeur de cases
        self.largeurCase=int(int(canvas['width'])/self.larg)
        self.hauteurCase=int(int(canvas['height'])/self.haut)

        #initialisation graphique
        for j in range(self.haut):
            for i in range(self.larg):
                self.can.create_rectangle( \
                    self.largeurCase*i, self.hauteurCase*j, \
                    self.largeurCase*(i+1), self.hauteurCase*(j+1), \
                    fill='black' if self.grille[i][j] else 'white', \
                    width=0)

##        #deplacement
##        self.deplOK=[]
##        self.can.bind('<Button-1>', self.mouseDown)
##        self.can.bind('<Button1-Motion>', self.mouseMove)
##        self.can.bind('<Button1-ButtonRelease>', self.mouseUp)

    def __str__(self):
        """debug display"""
        return 'Grille Object:\n'+str(self.grille)

    def get(self, x, y):
        """retrun value of the grid at (x,y)"""
        try:
            return self.grille[y][x]
        except:
            return 'error'
    
    def change(self, x, y, val=None):
        """change the value of the grid at (x,y)"""
        if val is None:
            self.grille[y][x]=0 if self.grille[y][x] else 1
        else:
            self.grille[y][x]=val
        self.MAJ(x, y)

    def MAJ(self, x, y):
        """update the graphic display of cell (x,y)"""
        self.can.itemconfigure(y*self.larg+x+1, \
                               fill='black' if self.grille[y][x] else 'white')

    def RAZ(self):
        for j in range(self.haut):
            for i in range(self.larg):
                self.grille[i][j]=0
                self.can.itemconfigure(i*self.larg+j+1, fill='white')

    

#test
if __name__=='__main__':
    fen=Tk()
    can=Canvas(fen, height=500, width=800)
    can.pack()
    G=Grille(can, init_type=3)
    
    fen.mainloop()

