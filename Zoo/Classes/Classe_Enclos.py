class Enclos:
    """
            Classe Enclos
            """

    # attribut de classe
    list_enclos = []
    nb_enclos = 0
    def __init__(self, p_numero_enclos: str = "", p_nom_enclos: str = "", p_taille: str = "", p_type: str = "",
                 p_localisation: str = "", p_list_animeaux: list = None):
        self._numero_enclos = p_numero_enclos # Attribut privé
        self._nom_enclos = p_nom_enclos # Attribut privé
        self._taille = p_taille # Attribut privé
        self._type = p_type # Attribut privé
        self._localisation = p_localisation # Attribut privé
        self.list_animeaux = p_list_animeaux # Attribut public


    @property
    def numero_enclos(self):
        return self._numero_enclos

    @numero_enclos.setter
    def numero_enclos(self, v_numero_enclos):
        if str(v_numero_enclos)[0:4].isnumeric() and str(v_numero_enclos)[5:].isalpha():
            self._numero_enclos = v_numero_enclos
        else:
            raise ValueError("Doit composer de 5 nombre entier puis suivie de 3 lettre")

    @property
    def nom_enclos(self):
        return self._nom_enclos
    @nom_enclos.setter
    def nom_enclos(self, v_nom_enclos):
        if str(v_nom_enclos).isalpha() and len(str(v_nom_enclos)) <= 25:
            self._nom_enclos = v_nom_enclos
        else:
            raise ValueError("Doit être composé d’un maximum de 25 lettres")

    @property
    def taille(self):
        return self._taille
    @taille.setter
    def _set_taille(self, v_taille):
        if v_taille in ["petit", "moyen", "grand"]:
            self._taille = v_taille
        else:
            raise ValueError("Vous devez entrer soit petit, soit moyen, grand.")

    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, v_type):
        if v_type in ["intérieur", "extérieur"]:
            self._type = v_type
        else:
            raise ValueError("Vous devez entrer soit intérieur ou extérieur.")

    @property
    def localisation(self):
        return self._localisation

    @localisation.setter
    def localisation(self, v_localisation):
        if v_localisation in ["A", "B", "C"]:
            self._localisation = v_localisation
        else:
            raise ValueError("Vous devez entrer soit A, B ou C.")

    def estAdapte(self):
        """
        Vérifier si l’enclos a une taille adaptée au nombre d’animaux qui y vivent
        :Return: True si la taille de l’enclos est adaptée et False sinon
        """
        if self._type == "petit" and len(self.list_animeaux) > 2:
            return False
        elif self._type == "moyen" and len(self.list_animeaux) > 4:
            return False
        elif self._type == "grand" and len(self.list_animeaux) > 6:
            return False
        else:
            return True