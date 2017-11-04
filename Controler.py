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
                self.btOnOff.config(state=DISABLED)
                self.bt1.config(state=DISABLED)
                self.ON=False
            #callback après 'wait' ms
            self.fourmie.grille[0].can.after(self.wait.get(), self.continuer)

    def step(self, event=None):
        """make one discontinuous movement"""
        self.fourmie.move()



#test
if __name__=='__main__':
    fen=Tk()
    
    C=Controler(fen, 0)
    C.pack()
    
    fen.mainloop()

