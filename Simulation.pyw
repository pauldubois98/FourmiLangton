from Grille import *
from Fourmie import *
from Controler import *

class Simulation(Frame):
    def __init__(self, root=None, haut=10, height=500, larg=-1, width=-1, \
                 fourmieSet=1, **arg):
        #intelligent var assignment
        if larg==-1:
            larg=haut
        if width==-1:
            width=height
        self.fourmieSet=fourmieSet

        #class init
        Frame.__init__(self, root, **arg)
        #window title
        self.master.title('Simulation de la Fourmie de Langton')

        
        #cadre tour les boutons de controles (top)
        top=Frame(self)
        top.pack()

        #canvas
        self.can=Canvas(self, height=500, width=500)
        self.can.pack(padx=2, pady=1)
        #grille
        self.grille=Grille(self.can, haut, larg)
        
        ###boutons de controles (top)
        #ajout
        b=Button(top, text='Ajouter une fourmie', \
               command=self.createFourmie, bg='light grey', fg='green')
        b.grid(row=1, column=1)
        #suppression
        b=Button(top, text='Supprimer une fourmie', \
               command=self.deleteFourmie, bg='dark grey', fg='red')
        b.grid(row=1, column=3)
        #RAZ
        b=Button(top, text='Tout balnc', \
               command=self.grille.RAZ, bg='white', fg='light grey')
        b.grid(row=1, column=2)
        
        ###controlers
        #cadre
        self.contr=Frame(self)
        self.contr.pack()
        #fourmie(s?) & controller(s)
        self.fourmies=[]
        self.controlers=[]
        self.createFourmie()
        self.createFourmie()

        
        #self-pack
        self.pack()


    def createFourmie(self, event=None):
        if len(self.fourmies)<5:
            f=Fourmie(self.grille, int(self.grille.haut/2), \
                      int(self.grille.larg/2),\
                      fourmieSet=self.fourmieSet)
            self.fourmies.append(f)
            #controler
            c=Controler(self.contr, f)
            self.controlers.append(c)
            c.grid(column=len(self.fourmies), row=1)

    def deleteFourmie(self, event=None):
        if self.fourmies!=[]:
            self.fourmies[len(self.fourmies)-1].effacer()
            del self.fourmies[len(self.fourmies)-1]
            self.controlers[len(self.controlers)-1].destroy()
            del self.controlers[len(self.controlers)-1]


#test
if __name__=='__main__':
    fen=Tk()
    S=Simulation(fen, 10, 600, fourmieSet=1)
    
    fen.mainloop()

