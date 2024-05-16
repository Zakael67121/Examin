from Zoo.Classes.Classe_Animal import Animal

from Zoo.Classes.Classe_Enclos import Enclos
from Zoo.Classes.Classe_Veterinaire import Veterinaire

class Oiseau(Animal):
    def __init__(self,  p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = "", p_enclos: Enclos = None,
                 p_list_veterinaires: list[Veterinaire] = [], p_longueur_bec: int = 0):

        # Héritage de Animal
        Animal.__init__(self, p_numero_animal, p_surnom, p_poids, p_famille, p_enclos,
                 p_list_veterinaires)

        # Propriéter de Oiseau
        self._longueur_bec = p_longueur_bec # Attribut privé

    @property
    def longueur_bec(self):
        return self._longueur_bec

    @longueur_bec.setter
    def longueur_bec(self, v_longueur_bec):
        if isinstance(v_longueur_bec, int) and int(v_longueur_bec) >= 0:
            self._longueur_bec = v_longueur_bec
        else:
            raise ValueError("la longueur de bec doit être une valeur réelle positive")