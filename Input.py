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
        f.write(" ")
        f.write("x")
        f.write(" ")
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
        self.master.title("Hashiwokakero Solver")
        root.geometry("810x260+100+100")
        root.config(bg="#C2D4B4")

        self.hello_label = tk.Label(self.master, text="Welcome to Mr.Astor's class", font=("Lucida Bright", 15))
        self.hello_label.grid(row=0, column=0, padx=5, pady=5)
        self.hello_label.config(bg="#C2D4B4")


        self.info_label = tk.Label(self.master, text=" OMG You have manually ", font=("Lucida Bright", 15))
        self.info_label.grid(row=100, column=0, padx=5, pady=5)
        self.info_label.config(bg="#C2D4B4")
        self.info_label = tk.Label(self.master, text=" expanded the window !", font=("Lucida Bright", 15))
        self.info_label.grid(row=101, column=0, padx=5, pady=5)
        self.info_label.config(bg="#C2D4B4")
                
        self.person_label = tk.Label(self.master, text="Now, You wanna be", font=("Lucida Bright", 15))
        self.person_label.grid(row=101, column=1, padx=5, pady=5)
        self.person_label.config(bg="#C2D4B4")


        # Entrer la taille
        self.size_label = tk.Label(self.master, text="La taille du jeux:",font=("Times New Roman", 10))
        self.size_label.grid(row=8, column=0)
        self.size_label.config(bg="#C2D4B4")
        self.size_entry = tk.Entry(self.master)
        self.size_entry.grid(row=9, column=0)
        
        # Entrer les valeurs d'une ile
        self.row_label = tk.Label(self.master, text="Position de l'axe horizontal :", font=("Times New Roman", 10))
        self.row_label.grid(row=4, column=1)
        self.row_label.config(bg="#C2D4B4")
        self.row_entry = tk.Entry(self.master)
        self.row_entry.grid(row=5, column=1)
        
        self.col_label = tk.Label(self.master, text="Position de l'axe vertical:",font=("Times New Roman", 10))
        self.col_label.grid(row=8, column=1)
        self.col_label.config(bg="#C2D4B4")
        self.col_entry = tk.Entry(self.master)
        self.col_entry.grid(row=9, column=1)
        
        self.val_label = tk.Label(self.master, text="Valeur de l'ile:",font=("Times New Roman", 10))
        self.val_label.grid(row=8, column=3)
        self.val_label.config(bg="#C2D4B4")
        self.val_entry = tk.Entry(self.master)
        self.val_entry.grid(row=9, column=3)
            
        # Bouton de contrôle
        self.check_button = tk.Button(self.master, text="Check", command=self.check_values, font=("Times New Roman", 20), bg="pink", fg="black")
        self.check_button.grid(row=11, column=1, columnspan=1)
        
        # Bouton d'enregistrer
        self.save_button = tk.Button(self.master, text="Save", command=self.save_values,font=("Times New Roman", 13), bg="pink", fg="black")
        self.save_button.grid(row=20, column=4, columnspan=1)
        
        # Bouton d'affichage
        self.show_button = tk.Button(self.master, text="Show", command=self.show_values,font=("Times New Roman", 13), bg="pink", fg="black")
        self.show_button.grid(row=20, column=5, columnspan=1)
        
        # Button des infos
        self.info_button = tk.Button(self.master, text="Put_Value", command=self.save_informations,font=("Times New Roman", 13), bg="pink", fg="black")
        self.info_button.grid(row=20, column=6, columnspan=1)
        
        # Button de quitter le frame
        self.quit_button = tk.Button(self.master, text="Quit", command=self.quit,font=("Times New Roman", 20), bg="pink", fg="black")
        self.quit_button.grid(row=30, column=1, columnspan=1)
        
        # Button de joke     
        self.Vinh_button = tk.Button(self.master, text="Vinh", command=self.Vinh, font=("Times New Roman", 13), bg="pink", fg="black")
        self.Vinh_button.grid(row=102, column=1, columnspan=1)
        self.Yu_button = tk.Button(self.master, text="Yuchen", command=self.Yu, font=("Times New Roman", 13), bg="pink", fg="black")
        self.Yu_button.grid(row=103, column=1, columnspan=1)
        self.Mo_button = tk.Button(self.master, text="Moham", command=self.Mo, font=("Times New Roman", 13), bg="pink", fg="black")
        self.Mo_button.grid(row=104, column=1, columnspan=1)
        
        # Liste des tuples
        self.values = []
        
    #fonction qui vérifie les conditions d'initialisation d'une île    
    def check_values(self):
        try:
            a = int(self.size_entry.get())
            x = int(self.row_entry.get())
            y = int(self.col_entry.get())
            z = int(self.val_entry.get())
            if 0 <= x < a and 0 <= y < a and 1 <= z <= 8:
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
            if 0 <= x < a and 0 <= y < a and 1 <= z <= 8:
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
        
    def Vinh(self):
        tk.messagebox.showinfo("Who is Vinh","I am Spider Man with yasuo's tornado and Mbappe's speed !")
        
    def Yu(self):
        tk.messagebox.showinfo("Who is Yu","I dont know this man")
        
    def Mo(self):
        tk.messagebox.showinfo("Who is Mo","I dont know this man")
        
    

    #la fonction qui nous aide de quitter
    def quit(self):
        self.master.quit()

        
root = tk.Tk()
interface = Interface(root)
root.mainloop()

#---------------------------------------------------------------------------------#
save_to_file()
