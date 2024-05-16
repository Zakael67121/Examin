import UI_PY.Page_Gestionnaire_Enclos
from PyQt5 import QtWidgets

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class fenetre_gestion_enclos(QtWidgets.QDialog, UI_PY.Page_Gestionnaire_Enclos.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(fenetre_gestion_enclos, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue animal")
