import customtkinter as ctk
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

        ctk.CTkButton(self, text="Ajouter", command=self.ajouter).pack()

    def ajouter(self):
        s = Salle(self.code.get(), self.desc.get(), self.cat.get(), int(self.cap.get()))
        self.service.ajouter_salle(s)