import pytest
from datetime import datetime
from Classe_Enclos import Enclos
from Classe_Veterinaire import Veterinaire

@pytest.mark.parametrize("list_animal, grandeur_enclos, valeur_prevue", [
    (["1", "2"], "petit", True),
(["1", "2", "3"], "petit", False),
(["1", "2", "3", "4"], "moyen", True),
(["1", "2", "3", "4", "5"], "moyen", False),
(["1", "2", "3", "4", "5", "6"], "grand", True),
(["1", "2", "3", "4", "5", "6", "7"], "grand", False)
])

def test_nom(list_animal, grandeur_enclos, valeur_prevue):
    enclos = Enclos()
    enclos.list_animeaux = list_animal
    enclos.type = grandeur_enclos

    assert enclos.estAdapte() == valeur_prevue

@pytest.mark.parametrize("date_naissance, valeur_prevue", [
    (datetime(1980, 4, 4), False),
(datetime(1960, 4, 4), True),
(datetime(1964, 4, 4), False),
(datetime(2000, 4, 4), False),
(datetime(1950, 4, 4), True),
(datetime(1940, 4, 4), True),
(datetime(1944, 4, 4), True)
])
def test_nom(date_naissance, valeur_prevue):
    veterinaire = Veterinaire()
    veterinaire.Date_naiss = date_naissance
    assert veterinaire.prendreRetraite() == valeur_prevue