from Zoo.Classes.Classe_Animal import Animal

from Zoo.Classes.Classe_Enclos import Enclos
from Zoo.Classes.Classe_Veterinaire import Veterinaire

class Mammifere(Animal):
    def __init__(self,  p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = "", p_enclos: Enclos = None,
                 p_list_veterinaires: list[Veterinaire] = [], p_couleur_poil: str = ""):

        # Héritage de Animal
        Animal.__init__(self, p_numero_animal, p_surnom, p_poids, p_famille, p_enclos,
                 p_list_veterinaires)

        # Propriéter de Mammifère
        self._couleur_poil = p_couleur_poil # Attribut privé

    @property
    def couleur_poil(self):
        return self._couleur_poil

    @couleur_poil.setter
    def couleur_poil(self, v_couleur_poil):
        if v_couleur_poil in ["noire", "blanche", "brune", "grise", "beige", "multi coulleurs"]:
            self._couleur_poil = v_couleur_poil
        else:
            raise ValueError("La couleur de poil peut être noire, blanche, brune, grise, beige ou multi couleurs")

    def __str__(self):
        return (f"Numero animal : {self._numero_animal}"
                f"Surnon : {self.surnom}"
                f"Poids : {self._poids}"
                f"Famille : {self._famille}"
                f"Liste des enclos : {self.enclos}"
                f"Liste des veterinaires : {self.list_veterinaires}"
                f"Couleur de Poil : {self.couleur_poil}")
