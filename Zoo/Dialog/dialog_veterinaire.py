# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.Dialog_veterinaire
from PyQt5 import QtWidgets

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreveterinaire(QtWidgets.QDialog, UI_PY.Dialog_veterinaire.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreveterinaire, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Vétérinaire")
