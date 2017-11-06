from tkinter import *
import webbrowser

#classe barre de menu type pour un jeu
class menuSimulation(Menu):
    def __init__(self, boss=None, commandRestart=None, \
                 commandAjouterFourmie=None, commandSupprimerFourmie=None,\
                 commandActiverFourmies=None, commandToutBlanc=None):
        ###MENUS
        self.barreMenu=Menu(boss)
        
        ##Menu de la simulation
        self.menuSimul=Menu(self.barreMenu, tearoff=0)
        #bouton pour recommencer le jeu
        self.menuSimul.add_command(label="Restart", \
                                 activebackground='green', \
                                 command=commandRestart)
        #bouton pour fermer le menu
        self.menuSimul.add_command(label="Fermer", \
                                 activebackground='orange')
        #séparateur
        self.menuSimul.add_separator()
        #bouton pour quitter le jeu
        self.menuSimul.add_command(label="Quitter          Ctrl+Q", \
                                 activebackground='red', \
                                 command=boss.master.destroy)
        #cascade
        self.barreMenu.add_cascade(label="Simulation", menu=self.menuSimul)

        ##Menu de Controle
        self.menuControle=Menu(self.barreMenu, tearoff=0)
        #bouton pour commencer
        self.menuControle.add_command(label="Ajouter une fourmie", \
                                 activebackground='light green',\
                                 activeforeground='black',\
                                 command=commandAjouterFourmie)
        #bouton pour les options
        self.menuControle.add_command(label="Supprimer une fourmie", \
                                 activebackground='#FFB970',\
                                 activeforeground='black',\
                                 command=commandSupprimerFourmie)

        #bouton pour tout activer
        self.menuControle.add_command(label="Activer/Desactiver Toutes", \
                                 activebackground='light blue',\
                                 activeforeground='black',\
                                 command=commandActiverFourmies)
        #séparateur
        self.menuControle.add_separator()
        #bouton pour remettre le damier tout blanc
        self.menuControle.add_command(label="Damier Blanc", \
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
        boss.bind("<Control-q>", boss.master.destroy)
        

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
