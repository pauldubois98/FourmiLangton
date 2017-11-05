from tkinter import *


class Controler(Frame):
    def __init__(self, root, fourmie, **arg):
        #class init
        Frame.__init__(self, root, relief='ridge', borderwidth=5, \
                       padx=10, pady=10, **arg)

        #fourmie associée
        self.fourmie=fourmie

        ##controls
        #variable
        self.wait=IntVar()
        #scale
        s=Scale(self, label="Temps (ms) d'une étape", from_=1, to_=1000,\
              variable=self.wait, orient='horizontal', length=200,\
              relief='solid')
        s.grid(row=1, column=1, columnspan=3)
        #bouton ON/OFF
        self.btOnOff=Button(self, text="ON", command=self.ONOFF,\
                            bg='green', activebackground='black', \
                            activeforeground='white', width=5)
        self.btOnOff.grid(row=2, column=1)
        #bouton 1 etape
        self.bt1=Button(self, text="1 étape", command=self.step, bg='grey')
        self.bt1.grid(row=2, column=3)
        
        #deplacement
        self.fourmie.grille[0].can.bind('<Button-1>', self.mouseDown, add='+')
        self.fourmie.grille[0].can.bind('<Button1-Motion>', self.mouseMove, add='+')
        self.fourmie.grille[0].can.bind('<Button1-ButtonRelease>', self.mouseUp, add='+')
        
        #variables
        self.ON=False

    def ONOFF(self, event=None):
        """starts/stops the continuous movement"""
        if self.ON:
            self.ON=False
            self.btOnOff.config(bg='green', text="ON")
        else:
            self.ON=True
            self.btOnOff.config(bg='red', text="OFF")
            self.continuer()

        
    def continuer(self, event=None):
        """continue the continuous movement"""
        if self.ON:
            if self.fourmie.move()=='error':
                #self.btOnOff.config(state=DISABLED)
                #self.bt1.config(state=DISABLED)
                self.ON=False
                self.btOnOff.config(bg='green', text="ON")
            #callback après 'wait' ms
            self.fourmie.grille[0].can.after(self.wait.get(), self.continuer)

    def step(self, event=None):
        """make one discontinuous movement"""
        self.fourmie.move()

    
    def mouseDown(self, event=None):
        """initialisation du mouvement utilisateur"""
        self.currentObject=None
        self.xBegin=event.x
        self.yBegin=event.y
        self.currentObject=self.fourmie.grille[0].\
                            can.find_closest(event.x, event.y)[0]

    def mouseMove(self, event=None):
        """mouvement de l'utilisateur"""
        dx=event.x-self.xBegin
        dy=event.y-self.yBegin
        if self.currentObject==self.fourmie.graphObj:
            self.fourmie.grille[0].can.move(self.currentObject, dx, dy)
            self.xBegin=event.x
            self.yBegin=event.y
        
    def mouseUp(self, event=None):
        """fin du mouvement utilisateur"""
        if self.currentObject==self.fourmie.graphObj:
            x=int(event.x/self.fourmie.largeurCase)
            y=int(event.y/self.fourmie.hauteurCase)
            #bouge graphiquement
            self.fourmie.grille[0].can.coords(self.fourmie.graphObj, \
                               self.fourmie.largeurCase*(x+0.5), \
                               self.fourmie.hauteurCase*(y+0.5))
            self.fourmie.x=x
            self.fourmie.y=y
            self.currentObject=None




