import customtkinter as ctk
from tkinter import ttk
from services.services_salle import ServiceSalle
from models.salle import Salle


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("650x500")

        self.service = ServiceSalle()

        # 🔹 FRAME FORMULAIRE
        frame_form = ctk.CTkFrame(self)
        frame_form.pack(pady=10, padx=10, fill="x")

        # Code
        ctk.CTkLabel(frame_form, text="Code :").grid(row=0, column=0, padx=10, pady=5)
        self.code = ctk.CTkEntry(frame_form)
        self.code.grid(row=0, column=1, padx=10, pady=5)

        # Description
        ctk.CTkLabel(frame_form, text="Description :").grid(row=1, column=0, padx=10, pady=5)
        self.desc = ctk.CTkEntry(frame_form)
        self.desc.grid(row=1, column=1, padx=10, pady=5)

        # Categorie
        ctk.CTkLabel(frame_form, text="Categorie :").grid(row=2, column=0, padx=10, pady=5)
        self.cat = ctk.CTkEntry(frame_form)
        self.cat.grid(row=2, column=1, padx=10, pady=5)

        # Capacite
        ctk.CTkLabel(frame_form, text="Capacité :").grid(row=3, column=0, padx=10, pady=5)
        self.cap = ctk.CTkEntry(frame_form)
        self.cap.grid(row=3, column=1, padx=10, pady=5)

        # 🔹 FRAME BOUTONS
        frame_btn = ctk.CTkFrame(self)
        frame_btn.pack(pady=10)

        ctk.CTkButton(frame_btn, text="Ajouter", command=self.ajouter).grid(row=0, column=0, padx=5)
        ctk.CTkButton(frame_btn, text="Supprimer", command=self.supprimer).grid(row=0, column=1, padx=5)
        ctk.CTkButton(frame_btn, text="Modifier", command=self.modifier).grid(row=0, column=2, padx=5)

        # 🔹 TABLEAU
        self.tree = ttk.Treeview(self, columns=("code", "desc", "cat", "cap"), show="headings")

        self.tree.heading("code", text="Code")
        self.tree.heading("desc", text="Description")
        self.tree.heading("cat", text="Categorie")
        self.tree.heading("cap", text="Capacite")

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)


        self.lister()

    def lister(self):
        self.tree.delete(*self.tree.get_children())

        liste = self.service.recuperer_salles()

        for s in liste:
            self.tree.insert("", "end",
                             values=(s.code, s.description, s.categorie, s.capacite))


    def ajouter(self):
        try:
            s = Salle(
                self.code.get(),
                self.desc.get(),
                self.cat.get(),
                int(self.cap.get())
            )
            self.service.ajouter_salle(s)
            self.lister()
        except:
            print("Erreur ajout")


    def modifier(self):
        try:
            s = Salle(
                self.code.get(),
                self.desc.get(),
                self.cat.get(),
                int(self.cap.get())
            )
            self.service.modifier_salle(s)
            self.lister()
        except:
            print("Erreur modification")


    def supprimer(self):
        try:
            self.service.supprimer_salle(self.code.get())
            self.lister()
        except:
            print("Erreur suppression")