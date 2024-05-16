# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import Zoo.UI_PY.Dialog_animal
from PyQt5 import QtWidgets

from Zoo.Classes.Classe_Enclos import Enclos

from Zoo.Classes.Classe_Oiseau import Oiseau
from Zoo.Classes.Classe_Reptile import Reptile
from Zoo.Classes.Classe_Mammifere import Mammifere
######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreanimal(QtWidgets.QDialog, Zoo.UI_PY.Dialog_animal.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreanimal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue animal")
        self.comboBox_enclos_animal.clear()
        self.label_erreur_numero_animal_invalide.setVisible(False)
        self.label_erreur_numero_animal_existe_pas.setVisible(False)
        self.label_erreur_numero_animal_existe.setVisible(False)
        self.label_erreur_poids_animal.setVisible(False)
        self.label_erreur_longueur_bec.setVisible(False)

        self.comboBox_couleur_poil.setEnabled(False)
        self.lineEdit_longueur_bec.setEnabled(False)
        self.comboBox_venimeux.setEnabled(False)

        self.comboBox_famille_animal.currentTextChanged.connect(lambda: self.changer_disposition())
        # instaciation d'enclos
        enclos1 = Enclos()
        enclos1.numero_enclos = "12345ABC"
        enclos1.list_enclos.append(enclos1)
        enclos2 = Enclos()
        enclos2.numero_enclos = "18345ABC"
        enclos2.list_enclos.append(enclos2)
        enclos3 = Enclos()
        enclos3.numero_enclos = "16345ABC"
        enclos3.list_enclos.append(enclos3)
        enclos4 = Enclos()
        enclos4.numero_enclos = "13345ABC"
        enclos4.list_enclos.append(enclos4)

        for enclos in Enclos.list_enclos:
            self.comboBox_enclos_animal.addItem(enclos.numero_enclos)

    def changer_disposition(self):
        if self.comboBox_famille_animal.currentText() == "Mammifères":
            self.comboBox_couleur_poil.setEnabled(True)
            self.lineEdit_longueur_bec.setEnabled(False)
            self.comboBox_venimeux.setEnabled(False)
        elif self.comboBox_famille_animal.currentText() == "Oiseaux":
            self.lineEdit_longueur_bec.setEnabled(True)
            self.comboBox_couleur_poil.setEnabled(False)
            self.comboBox_venimeux.setEnabled(False)
        else:
            self.comboBox_venimeux.setEnabled(True)
            self.lineEdit_longueur_bec.setEnabled(False)
            self.comboBox_couleur_poil.setEnabled(False)


    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        verification = False
        if self.comboBox_famille_animal.currentText() == "Mammifères":
            animal = Oiseau()
            try:
                animal.longueur_bec = self.lineEdit_longueur_bec.text()
            except ValueError:
                self.label_erreur_longueur_bec.setVisible(True)
                verification = True
        elif self.comboBox_famille_animal.currentText() == "Oiseaux":
            animal = Reptile()
            animal.venimeux = self.comboBox_venimeux.currentText()
        else:
            animal = Mammifere()
            animal.couleur_poil = self.comboBox_couleur_poil.currentText()

        try:
            animal.numero_animal = self.lineEdit_numero_animal.text()
        except ValueError:
            self.label_erreur_numero_animal_invalide.setVisible(True)
            verification = True
        animal.surnom = self.lineEdit_surnom_animal.text()

        try:
            animal.poids = int(self.lineEdit_poids_animal.text())
        except ValueError:
            self.label_erreur_poids_animal.setVisible(True)
            verification = True

        animal.famille = self.comboBox_famille_animal.currentText()
        for enclos in Enclos.list_enclos:
            if self.comboBox_enclos_animal.currentText() == enclos.numero_enclos:
                animal.enclos = enclos

        if verification:
            return
        animal.serialiserAnimal()
        self.close()