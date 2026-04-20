import customtkinter as ctk
from tkinter import ttk
from services.services_salle import ServiceSalle
from models.salle import Salle

class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.service = ServiceSalle()

        self.code = ctk.CTkEntry(self)
        self.code.pack()

        self.desc = ctk.CTkEntry(self)
        self.desc.pack()

        self.cat = ctk.CTkEntry(self)
        self.cat.pack()

        self.cap = ctk.CTkEntry(self)
        self.cap.pack()
        self.tree = ttk.Treeview(self, columns=("code", "desc", "cat", "cap"), show="headings")

        self.tree.heading("code", text="Code")
        self.tree.heading("desc", text="Description")
        self.tree.heading("cat", text="Categorie")
        self.tree.heading("cap", text="Capacite")

        self.tree.pack(fill="both", expand=True)
        self.lister()

        ctk.CTkButton(self, text="Ajouter", command=self.ajouter).pack()

    def ajouter(self):
        s = Salle(self.code.get(), self.desc.get(), self.cat.get(), int(self.cap.get()))
        self.service.ajouter_salle(s)

def lister(self):
    self.tree.delete(*self.tree.get_children())

    liste = self.service.recuperer_salles()

    for s in liste:
        self.tree.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))