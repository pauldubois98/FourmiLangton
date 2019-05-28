from tkinter import *

class MenuBar(Menu):
    def __init__(self, root, **arg):
        #Barre de menu
        self.menuBar=Menu(root)

        #Menu Simulation
        self.menuSimul=Menu(self.menuBar, tearoff=0)
        #bouton pour ajouter une fourmi
        self.menuSimul.add_command(label="Ajouter une fourmi", \
                                   activebackground='green',\
                                   activeforeground='black', \
                                   command=None)
        #bouton pour supprimer une fourmi
        self.menuSimul.add_command(label="Supprimer une fourmi", \
                                   activebackground='red',\
                                   activeforeground='black', \
                                   command=None)
        #bouton pour remettre tout blanc
        self.menuSimul.add_command(label="Tout blanc", \
                                   activebackground='white',\
                                   activeforeground='light grey', \
                                   command=None)

        self.menuBar.pack()
        


if __name__=='__main__':
    app=Tk()
    
    
    menu=MenuBar(app)
    
    app.mainloop()
