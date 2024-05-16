from Zoo.Classes.Classe_Animal import Animal

from Zoo.Classes.Classe_Enclos import Enclos
from Zoo.Classes.Classe_Veterinaire import Veterinaire

class Reptile(Animal):
    def __init__(self,  p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = "", p_enclos: Enclos = None,
                 p_list_veterinaires: list[Veterinaire] = [], p_venimeux: bool = False):

        # Héritage de Animal
        Animal.__init__(self, p_numero_animal, p_surnom, p_poids, p_famille, p_enclos,
                 p_list_veterinaires)

        # Propriéter de Reptile
        self._venimeux = p_venimeux # Attribut privé

    @property
    def venimeux(self):
        return self._venimeux

    @venimeux.setter
    def venimeux(self, v_venimeux):
        if v_venimeux in ["True", "False", 1, 0]:
            if v_venimeux == "True" or v_venimeux == 1:
                self._venimeux = True
            elif v_venimeux == "False" or v_venimeux == 0:
                self._venimeux = False
        else:
            raise ValueError("Vous devez entrer [True ou False] ou [1 ou 0]")