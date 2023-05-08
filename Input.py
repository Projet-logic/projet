from tkinter import *
from tkinter import messagebox
import tkinter as tk

"""

@author: Tang Khac Vinh

"""
#---------------------------------------------------------------------------------#
"""
Enregistrez les paramètres de la taille de la grille de jeu et des îles dans le fichier information.txt
"""
def save_to_file():
    # Ouvrir le fichier avec l'option d'écriture, créer le fichier si le fichier n'existe pas
    with open("information.txt", "w") as f:
        # Enregistrez la valeur "liste" dans le fichier, avec le nom
        f.write("La liste des iles: ")
        f.write(str(informations["liste"]))
        f.write("\n")
        # Enregistrez la valeur "taille" dans le fichier, avec le nom
        f.write("La taille de la grille: ")
        f.write(str(informations["taille"]))
        f.write("x")
        f.write(str(informations["taille"]))
        f.write("\n")

#---------------------------------------------------------------------------------#
"""
initialiser un dictionnaire contenant des valeurs globales à stocker après import
"""

informations = {
    "liste": None,
    "taille": None
}

#---------------------------------------------------------------------------------#
"""
créer une fenêtre d'interface pour saisir les valeurs nécessaires à la création du jeu
"""
class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Hashiwokakero Solve")
        root.geometry("500x500+100+100")
        root.config(bg="white")

        
        # Entrer la taille
        self.size_label = tk.Label(self.master, text="La taille du jeux:")
        self.size_label.grid(row=0, column=0)
        self.size_entry = tk.Entry(self.master)
        self.size_entry.grid(row=0, column=1)
        
        # Entrer les valeurs d'une ile
        self.row_label = tk.Label(self.master, text="Le position de l'axe horizontal :")
        self.row_label.grid(row=1, column=0)
        self.row_entry = tk.Entry(self.master)
        self.row_entry.grid(row=1, column=1)
        
        self.col_label = tk.Label(self.master, text="position de l'axe vertical:",font=("Arial", 10))
        self.col_label.grid(row=2, column=0)
        self.col_entry = tk.Entry(self.master)
        self.col_entry.grid(row=2, column=1)
        
        self.val_label = tk.Label(self.master, text="la valeur de l'ile:",font=("Arial", 10))
        self.val_label.grid(row=3, column=0)
        self.val_entry = tk.Entry(self.master)
        self.val_entry.grid(row=3, column=1)
        
        # Bouton de contrôle
        self.check_button = tk.Button(self.master, text="Check", command=self.check_values, font=("Arial", 15), bg="yellow", fg="black")
        self.check_button.grid(row=4, column=0, columnspan=2)
        
        # Bouton d'enregistrer
        self.save_button = tk.Button(self.master, text="Save", command=self.save_values,font=("Arial", 15), bg="yellow", fg="black")
        self.save_button.grid(row=4, column=2, columnspan=2)
        
        # Bouton d'affichage
        self.show_button = tk.Button(self.master, text="Show", command=self.show_values,font=("Arial", 15), bg="yellow", fg="black")
        self.show_button.grid(row=10, column=0, columnspan=2)
        
        # Button des infos
        self.info_button = tk.Button(self.master, text="Save_info", command=self.save_informations,font=("Arial", 15), bg="yellow", fg="black")
        self.info_button.grid(row=10, column=2, columnspan=2)
        
        # Button de quitter le frame
        self.quit_button = tk.Button(self.master, text="quit", command=self.quit,font=("Arial", 15), bg="yellow", fg="black")
        self.quit_button.grid(row=16, column=1, columnspan=2)
        
        # Liste des tuples
        self.values = []
    
    #fonction qui vérifie les conditions d'initialisation d'une île    
    def check_values(self):
        try:
            a = int(self.size_entry.get())
            x = int(self.row_entry.get())
            y = int(self.col_entry.get())
            z = int(self.val_entry.get())
            if x <= a and y <= a and 1 <= z <= 8:
                tk.messagebox.showinfo("Résultat", "Okay, les valeurs sont valides.")
            else:
                tk.messagebox.showerror("Résultat", "Ah mince, les valeurs sont valides.")
        except ValueError:
            tk.messagebox.showerror("Erreur", "Veuillez saisir uniquement des nombres entiers.")
    
    #fonction qui stocke les valeurs des îles validées
    def save_values(self):
        try:
            a = int(self.size_entry.get())
            x = int(self.row_entry.get())
            y = int(self.col_entry.get())
            z = int(self.val_entry.get())
            if x <= a and y <= a and 1 <= z <= 8:
                self.values.append((x, y, z))
                tk.messagebox.showinfo("Résultat", "Valeurs enregistrées")
            else:
                tk.messagebox.showerror("Résultat", "Valeurs PAS enregistrées")
        except ValueError:
            tk.messagebox.showerror("Erreur", "Veuillez saisir uniquement des nombres entiers.")
    
    #la fonction nous indique quelles valeurs nous avons des îles
    def show_values(self):
        a = self.size_entry.get()
        values_str = f"La taille: {a}\nValeur: {self.values}"
        tk.messagebox.showinfo("Valeur", values_str)
        
    #la fonction qui enregistre la valeur que vous souhaitez entrer est disponible dans la grille de jeu
    def save_informations(self):
        informations["liste"] = self.values
        informations["taille"] = self.size_entry.get()
        
    #la fonction qui nous aide de quitter
    def quit(self):
        self.master.quit()

        
root = tk.Tk()
interface = Interface(root)
root.mainloop()

#---------------------------------------------------------------------------------#
save_to_file()
