from Data.dao_salle import DataSalle
class ServiceSalle:
    def __init__(self):
        self.dao = DataSalle()
    def ajouter_salle(self, salle):
        if salle.capacite < 1:
            return False
        self.dao.insert_salle(salle)
        return True
    def modifier_salle(self, salle):
        self.dao.update_salle(salle)
    def supprimer_salle(self, code):
        self.dao.delete_salle(code)
    def rechercher_salle(self, code):
        return self.dao.get_salle(code)
    def recuperer_salles(self):
        return self.dao.get_salles()