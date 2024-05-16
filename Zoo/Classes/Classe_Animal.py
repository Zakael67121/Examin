from Zoo.Classes.Classe_Enclos import Enclos
from Zoo.Classes.Classe_Veterinaire import Veterinaire

import json
class Animal:
    """
        Classe Animal
        """
    # attribut de classe
    ls_animaux = []
    nb_animaux = 0
    def __init__(self, p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = "", p_enclos: Enclos = None,
                 p_list_veterinaires: list[Veterinaire] = []):
        self._numero_animal = p_numero_animal # Attribut privé
        self.surnom = p_surnom # Attribut public
        self._poids = p_poids # Attribut privé
        self._famille = p_famille # Attribut privé
        self.enclos = p_enclos # Attribut public
        self.list_veterinaires = p_list_veterinaires # Attribut public


    def _get_numero_animal(self):
        return self._numero_animal
    def _set_numero_animal(self, v_numero_animal):

        if str(v_numero_animal)[0:1].isalpha() and str(v_numero_animal)[2] == "-" and str(v_numero_animal)[3:].isnumeric() and len(str(v_numero_animal)) == 8:
            self._numero_animal = v_numero_animal
        else:
            raise ValueError("Vous devez commencer par deux lettres suivies d’un tiret puis de cinq chiffres")

    numero_animal = property(_get_numero_animal, _set_numero_animal)

    def _get_poids(self):
        return self._poids
    def _set_poids(self, v_poid):

        if isinstance(v_poid, int) and v_poid >= 15:
            self._poids = v_poid
        else:
            raise ValueError("le poid dois être supérieur a 15Ib et doit être un nombre entier")

    poids = property(_get_poids, _set_poids)

    def _get_famille(self):
        return self._famille
    def _set_famille(self, v_famille):
        if v_famille == "Mammifères" or v_famille == "Oiseaux" or v_famille == "reptiles":
            self._famille = v_famille
        else:
            raise ValueError("L'animal doit être soit un mammifères, soit un oiseaux, soit un reptiles")

    famille = property(_get_famille, _set_famille)

    def ajouterEnclosVeterinaire(self, numero_emp, enclos):
        """
        associer un vétérinaire a un enclos
        :numero_emp: Numéros de l'employer
        : enclos: objet enclos
        """
        for employer in Veterinaire.ls_veterinaire:
            if employer.Numero_emp == numero_emp:
                employer.list_enclos.append(enclos)
                return True
        return False

    def serialiserAnimal(self):
        with open(file=f"{self._numero_animal}.json", mode="w", encoding="utf-8") as file:
            json.dump(str(self), file, ensure_ascii=False, indent=4)
        self.ls_animaux.append(self)


    def __str__(self):
        return (f"Numero animal : {self._numero_animal}"
                f"Surnon : {self.surnom}"
                f"Poids : {self._poids}"
                f"Famille : {self._famille}"
                f"Liste des enclos : {self.enclos}"
                f"Liste des veterinaires : {self.list_veterinaires}")


