from Grille import *
from Fourmi import *
from Controler import *
from MenuBar import *

class Simulation(Frame):
    def __init__(self, root=None, haut=10, height=500, larg=-1, width=-1, \
                 fourmiSet=1, **arg):
        #intelligent var assignment
        if larg==-1:
            larg=haut
        if width==-1:
            width=height
        self.fourmiSet=fourmiSet

        #class init
        Frame.__init__(self, root, **arg)
        #window title
        self.master.title('Simulation de la Fourmi de Langton')

        
        #cadre tour les boutons de controles (top)
        top=Frame(self)
        top.pack()

        #canvas
        self.can=Canvas(self, height=500, width=500)
        self.can.pack(padx=2, pady=1)
        #grille
        self.grille=Grille(self.can, haut, larg)

        ##Menu
        m=menuSimulation(self, self.newBig, self.newSmall, self.createFourmi, \
                         self.deleteFourmi, self.allONOFF, self.grille.RAZ)
        
##        ###Boutons de controles (top)
##        #ajout
##        b=Button(top, text='Ajouter une fourmi', \
##               command=self.createFourmi, bg='light grey', fg='green')
##        b.grid(row=1, column=1)
##        #suppression
##        b=Button(top, text='Supprimer une fourmi', \
##               command=self.deleteFourmi, bg='dark grey', fg='red')
##        b.grid(row=1, column=3)
##        #RAZ
##        b=Button(top, text='Tout balnc', \
##               command=self.grille.RAZ, bg='white', fg='light grey')
##        b.grid(row=1, column=2)
##        #Toutes les fourmis ON:
##        b=Button(top, text='Toutes ON/OFF', \
##               command=self.allONOFF, bg='light blue')
##        b.grid(row=1, column=4)
        
        ###controlers
        #cadre
        self.contr=Frame(self)
        self.contr.pack(padx=5, pady=5)
        #fourmi(s?) & controller(s)
        self.fourmis=[]
        self.controlers=[]
        self.createFourmi()
        self.createFourmi()


    def createFourmi(self, event=None):
        if len(self.fourmis)<5:
            f=Fourmi(self.grille, int(self.grille.haut/2), \
                      int(self.grille.larg/2),\
                      fourmiSet=self.fourmiSet)
            self.fourmis.append(f)
            #controler
            c=Controler(self.contr, f)
            self.controlers.append(c)
            c.grid(column=len(self.fourmis), row=1)
        else:
            self.bell()

    def deleteFourmi(self, event=None):
        if self.fourmis!=[]:
            self.fourmis[len(self.fourmis)-1].effacer()
            del self.fourmis[len(self.fourmis)-1]
            self.controlers[len(self.controlers)-1].destroy()
            del self.controlers[len(self.controlers)-1]
        else:
            self.bell()

    def allONOFF(self, event=None):
        for c in self.controlers:
            c.btOnOff.invoke()

    def newBig(self, event=None):
        self.master.destroy()
        app=Tk()
        S=Simulation(app, 10, 600, fourmiSet=0)
        S.pack()
        app.mainloop()

    def newSmall(self, event=None):
        self.master.destroy()
        app=Tk()
        S=Simulation(app, 60, 600, fourmiSet=1)
        S.pack()
        app.mainloop()


#test
if __name__=='__main__':
    app=Tk()
    
    S=Simulation(app, 60, 600, fourmiSet=1)
    S.pack()
    
    app.mainloop()

