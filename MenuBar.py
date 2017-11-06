from tkinter import *
import webbrowser

#classe barre de menu type pour un jeu
class menuSimulation(Menu):
    def __init__(self, boss=None, \
                 commandRestartBig=None, commandRestartSmall=None, \
                 commandAjouterFourmie=None, commandSupprimerFourmie=None,\
                 commandActiverFourmies=None, commandToutBlanc=None):
        ###MENUS
        self.barreMenu=Menu(boss)
        
        ##Menu de la simulation
        self.menuSimul=Menu(self.barreMenu, tearoff=0)
        #bouton pour recommencer une simulation (grandes cases)
        self.menuSimul.add_command(label="Simulation - grandes cases", \
                                 activebackground='green', \
                                 command=commandRestartBig)
        #bouton pour recommencer une simulation (petites cases)
        self.menuSimul.add_command(label="Simulation - petites cases", \
                                 activebackground='blue', \
                                 command=commandRestartSmall)
        #séparateur
        self.menuSimul.add_separator()
        #bouton pour quitter le jeu
        self.menuSimul.add_command(label="Quitter", \
                                 accelerator='Ctrl-Q', \
                                 activebackground='red', \
                                 command=boss.master.destroy)
        #cascade
        self.barreMenu.add_cascade(label="Simulation", menu=self.menuSimul)

        ##Menu de Controle
        self.menuControle=Menu(self.barreMenu, tearoff=0)
        #bouton pour commencer
        self.menuControle.add_command(label="Ajouter une fourmie", \
                                 accelerator='Ctrl-N', \
                                 activebackground='light green',\
                                 activeforeground='black',\
                                 command=commandAjouterFourmie)
        #bouton pour les options
        self.menuControle.add_command(label="Supprimer une fourmie", \
                                 accelerator='Ctrl-D', \
                                 activebackground='#FFB970',\
                                 activeforeground='black',\
                                 command=commandSupprimerFourmie)

        #bouton pour tout activer
        self.menuControle.add_command(label="Activer/Desactiver Toutes", \
                                 accelerator='Ctrl-A', \
                                 activebackground='light blue',\
                                 activeforeground='black',\
                                 command=commandActiverFourmies)
        #séparateur
        self.menuControle.add_separator()
        #bouton pour remettre le damier tout blanc
        self.menuControle.add_command(label="Damier Blanc", \
                                 accelerator='Ctrl-E', \
                                 activeforeground='light grey',\
                                 activebackground='white',\
                                 command=commandToutBlanc)
        #cascade
        self.barreMenu.add_cascade(label="Controles", menu=self.menuControle)
        
        #Menu d'aide
        self.menuAide=Menu(self.barreMenu, tearoff=0)
        #bouton pour afficher les règles du jeu
        self.menuAide.add_command(label="Fourmie de Langton",
                                  activebackground='dark grey', \
                                  activeforeground='black', \
                                  command=lambda: webbrowser.open\
                                  ("https://fr.wikipedia.org/wiki/Fourmi_de_Langton"))
        #bouton pour avoir des infos sur le dévellopeur, ses autres jeux...
        self.menuAide.add_command(label="About me", \
                                  activebackground='black', \
                                  command=lambda: webbrowser.open\
                                  ("https://pauldubois98.github.io/prgm"))
        #cascade
        self.barreMenu.add_cascade(label="Aide", menu=self.menuAide)


        #configuration
        boss.master.config(menu=self.barreMenu)
        
        
        ###RACCOURCITS
        boss.master.bind("<Control-q>", lambda a: boss.master.destroy())
        boss.master.bind("<Control-n>", lambda a: commandAjouterFourmie())
        boss.master.bind("<Control-d>", lambda a: commandSupprimerFourmie())
        boss.master.bind("<Control-a>", lambda a: commandActiverFourmies())
        boss.master.bind("<Control-e>", lambda a: commandToutBlanc())
        
        boss.bind("<a>", lambda: print("a"))
        

if __name__=='__main__':
    def nouv():
        print('Nouvelle Partie')
    def options():
        print('Options')
    fen=Tk()
    Fr=Frame(fen)
    M=menuSimulation(Fr, nouv, options)
    Fr.pack()
    fen.mainloop()
