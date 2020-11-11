# -*- coding: utf-8 -*-
"""
Authors: Grégoire & Geoffroy Thoumyres
"""


# Imports
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from datetime import datetime
import numpy as np
import pandas as pd
import os


class ApplicationWindow(QMainWindow):
    """The potager main application window and all its containers.

    Attributes:
        title (str): Title of the potager application window.
    """

    def __init__(self, title=''):
        """
        Initialization of thepotager main application window.

        When an application window is called, the header parameters and the
        containers are initialize and should not be modified.

        Args:
            title (str): the main application window's title
        """
        super().__init__()

        self.bdd = pd.read_csv('../src/data/bdd.csv', delimiter=';')
        self.potager = pd.read_csv('../src/data/potager.csv', delimiter=';')
        self.bdd_size = len(self.bdd)
        self.potager_size = len(self.potager)

        # state variable for the potager_btns & side_veg_btns
        self.fun_square_potager = 'Information'
        self.fun_square_side = 'Information'
        self.tmp_button = 'None'

        self.title = title      # title of the window
        self.__set_window()     # window containers

    def __set_window(self):
        """Establishment of the bathymetry-prediction window's canvas.

        This methods set up the front-end header parameters, the menu bar, all
        the canvas (either static and dynamic) and all the buttons.

        """

        global currentDay, currentMonth, currentYear
        currentDay = datetime.now().day
        currentMonth = datetime.now().month
        currentYear = datetime.now().year



        # define the window title, icon & geometry
        self.setWindowIcon(QIcon('../src/data/icon/potager2.png'))
        self.setWindowTitle(self.title)
        # geometry = QDesktopWidget().availableGeometry()           # adapt to the screen's geometry
        # self.setFixedSize(geometry.width(), geometry.height())
        self.setFixedSize(1900, 1000)

        self.__b_width = 300    # width of the buttons
        self.__b_height = 50    # height of the buttons
        self.__b_shift = 50     # shift of the buttons
        self.__mb_height = 30   # height of the menu bar

        self.maxw = self.width() - self.__b_width  # Max width
        self.maxh = self.height() - self.__mb_height - self.__b_height  # Max height
        self.right_b_width = self.__b_width  # Button width

        # Widgets init
        self.the_potager()
        self.side_vegetables()
        self.menu_bar()
        self.my_calendar()
        self.buttons()
        self.resize_and_move()

        self.show()

    # Widgets initialization
    def menu_bar(self):
        """Establishment of the front-end and back-end menu bar.
        Classically, the available menus are: File, Edit, Help
        """
        # menu front-end
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')

        # exit button action
        exit_button = QAction('Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip('Exit application')
        exit_button.triggered.connect(self.close)
        file_menu.addAction(exit_button)

    def buttons(self):
        # close button
        self.close_btn = QPushButton('Exit', self)
        self.close_btn.setToolTip('Exit Application')
        self.close_btn.clicked.connect(self.close)

        # information button
        self.information_btn = QPushButton('Information', self)
        self.information_btn.setToolTip('En savoir plus sur un légume')
        self.information_btn.clicked.connect(self.information)

        # planter button
        self.planter_btn = QPushButton('Planter', self)
        self.planter_btn.setToolTip('Planter de la verdure dans un carré spécifique')
        self.planter_btn.clicked.connect(self.planter)
        self.planter_btn.setStyleSheet("QPushButton {background-color: #3e9932}")

        # recolter button
        self.recolter_btn = QPushButton('Recolter', self)
        self.recolter_btn.setToolTip('Recolter de la verdure dans un carré spécifique')
        self.recolter_btn.clicked.connect(self.recolter)
        self.recolter_btn.setStyleSheet("QPushButton {background-color: #f7f1eb; color: black;}")

        # today button : reset the day to the actual one
        self.today_btn = QPushButton('Today', self)
        self.today_btn.setToolTip("Reset la date à aujourd'hui")
        self.today_btn.clicked.connect(self.today)

        # today button : reset the day to the actual one
        self.ajouter_btn = QPushButton('Ajouter légume', self)
        self.ajouter_btn.setToolTip("Ajouter une plantation à la base de donnée")
        self.ajouter_btn.clicked.connect(self.ajouter)

        # today button : reset the day to the actual one
        self.retirer_btn = QPushButton('Retirer légume', self)
        self.retirer_btn.setToolTip("Retirer une plantation de la base de donnée")
        self.retirer_btn.clicked.connect(self.retirer)

        # clear button : remet à zéro le potager
        self.clear_btn = QPushButton('Clear', self)
        self.clear_btn.setToolTip('Remet à zéro le potager')
        self.clear_btn.clicked.connect(self.clear)
        self.clear_btn.setStyleSheet("QPushButton {background-color: #f52f2f}")

        # save button : save the dataset as it is
        self.save_btn = QPushButton('Save', self)
        self.save_btn.setToolTip("Sauvegarde le potager dans l'état actuel")
        self.save_btn.clicked.connect(self.save)
        self.save_btn.setStyleSheet("QPushButton {background-color: #46a2db}")

    def my_calendar(self):

        # LCD
        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(10)
        self.lcd.setSegmentStyle(0)
        self.lcd.display(f'{currentDay} {currentMonth} {currentYear}')

        # CALENDAR
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.monthShown()
        self.calendar.setMinimumDate(QDate(currentYear - 1, currentMonth, 1))
        self.calendar.setMaximumDate(QDate(currentYear + 1, currentMonth, 1))
        self.calendar.setSelectedDate(QDate(currentYear, currentMonth, currentDay))
        self.calendar.clicked.connect(self.display_date)

    def the_potager(self):
        # 6 3*3squares = 1 potager
        cx = int(self.width() / 2 - 240)
        cy = int(self.height() / 2 - 300)
        self.potager_btns = pd.DataFrame([], columns=['lx', 'ly', 'Lx', 'Ly', 'button'])
        for lx in range(3):
            for ly in range(3):
                for Lx in range(3):
                    for Ly in range(2):
                        id_CARRE = Ly + 2 * Lx
                        id_carre = ly + 3 * lx
                        button = QPushButton(self)
                        leg = self.potager[(self.potager['id_CARRE']==id_CARRE) & (self.potager['id_carre']==id_carre)]['Présent'].values[0]
                        if str(leg)=='nan':
                            leg = ''
                        else:
                            icon = self.bdd[self.bdd['Nom'] == leg]['Icon'].values[0]
                            button.setIcon(QIcon(QPixmap('../src/data/img/' + icon)))
                            button.setIconSize(QSize(60, 60))
                        button.setObjectName(f'{leg},{lx*3+ly},{Lx*2+Ly}')
                        button.setStyleSheet('QPushButton {background-color: #828594; color: black;}')
                        button.clicked.connect(self.selected_square)

                        button.resize(70, 70)
                        button.move(cx + ly * 75 + Ly * 240, cy + lx * 75 + Lx * 240)
                        df = pd.DataFrame([[lx, ly, Lx, Ly, button]], columns=['lx', 'ly', 'Lx', 'Ly', 'button'])
                        self.potager_btns = self.potager_btns.append(df)
        self.potager_btns.reset_index(drop=True)

    def side_vegetables(self):
        self.side_veg_btns = pd.DataFrame([], columns=['id', 'x', 'y', 'Nom', 'button'])
        icons = self.bdd['Icon']
        noms = self.bdd['Nom']
        n = int(np.sqrt(self.bdd_size)) + 1
        for i in range(self.bdd_size):
            x, y = int(i / n), i % n
            button = QPushButton(self)
            button.setObjectName(noms[i])
            button.clicked.connect(self.selected_vegetable)
            button.setIcon(QIcon(QPixmap('../src/data/img/' + icons[i])))
            button.setStyleSheet('QPushButton {background-color: #828594; color: black;}')
            button.setIconSize(QSize(60, 60))
            button.resize(60, 60)
            button.move(self.width() - 10 - 62 * (y + 1), self.__mb_height + 200 + 62 * x)
            df = pd.DataFrame([[i, x, y, noms[i], button]], columns=['id', 'x', 'y', 'Nom', 'button'])
            self.side_veg_btns = self.side_veg_btns.append(df)
        self.side_veg_btns.reset_index(drop=True)

    def resize_and_move(self):
        """
        resize and move all the widgets
        """

        # Date
        self.lcd.resize(200, 50)
        self.lcd.move(int(self.width() / 2) - 100, 50 + self.__mb_height)

        self.today_btn.resize(60, 20)
        self.today_btn.move(int(self.width() / 2) - 30, 30 + self.__mb_height)

        self.calendar.resize(320, 200)
        self.calendar.move(int(self.width() / 40), int((self.height() / 2) - 160 + self.__mb_height))

        # Right Buttons
        self.information_btn.resize(self.right_b_width, self.__b_height)
        self.information_btn.move(self.maxw, self.maxh - 5 * self.__b_height)

        self.planter_btn.resize(self.right_b_width, self.__b_height)
        self.planter_btn.move(self.maxw, self.maxh - 4 * self.__b_height)

        self.recolter_btn.resize(self.right_b_width, self.__b_height)
        self.recolter_btn.move(self.maxw, self.maxh - 3 * self.__b_height)

        self.save_btn.resize(self.right_b_width, self.__b_height)
        self.save_btn.move(self.maxw, self.maxh - 2 * self.__b_height)

        self.close_btn.resize(self.right_b_width, self.__b_height)
        self.close_btn.move(self.maxw, self.maxh)

        # Left Buttons
        self.retirer_btn.resize(self.right_b_width, self.__b_height)
        self.retirer_btn.move(0, self.maxh - 4 * self.__b_height)

        self.ajouter_btn.resize(self.right_b_width, self.__b_height)
        self.ajouter_btn.move(0, self.maxh - 3 * self.__b_height)

        self.clear_btn.resize(self.right_b_width, self.__b_height)
        self.clear_btn.move(0, self.maxh - 2 * self.__b_height)

    def clear_side_background(self):
        for button in self.side_veg_btns['button']:
            button.setStyleSheet('QPushButton {background-color: #828594; color: black;}')

    # Widgets clicked actions
    def ajouter(self):
        print('Ajouter')

    def retirer(self):
        print('Retirer')

    def clear(self):
        self.fun_square_potager = 'Planter'
        for button in self.potager_btns['button']:
            button.setStyleSheet('QPushButton {background-color: #828594; color: black;}')
            button.setIcon(QIcon())
        self.clear_side_background()

    def information(self):
        self.fun_square_side = 'Information'
        if self.fun_square_potager == 'Planter':
            self.tmp_button.setStyleSheet('QPushButton {background-color: #828594; color: black;}')
        self.fun_square_potager = 'Information'
        self.clear_side_background()
        print("Je veux en savoir plus")

    def planter(self):
        if self.fun_square_potager == 'Planter':
            self.tmp_button.setStyleSheet('QPushButton {background-color: #828594; color: black;}')
            self.clear_side_background()
        self.fun_square_potager = 'Planter'
        print("J'ai planté de la verdure")

    def recolter(self):
        if self.fun_square_potager == 'Planter':
            self.tmp_button.setStyleSheet('QPushButton {background-color: #828594; color: black;}')
            self.clear_side_background()
        self.fun_square_potager = 'Recolter'
        print("J'ai retiré de la verdure")

    def selected_square(self):
        ids = self.sender().objectName().split(',')
        if self.fun_square_potager == 'Planter':
            if not self.tmp_button == 'None':
                self.tmp_button.setStyleSheet('QPushButton {background-color: #828594; color: black;}')
            self.tmp_button = self.sender()
            self.sender().setStyleSheet('QPushButton {background-color: red; color: black;}')
            self.fun_square_side = 'Planter'
            # l = self.remplir_case(ids[2], ids[1])
            # print(l)
            v = ['Carotte', 'Aubergine']
            j = ['Pois', 'Haricots grimpants']
            o = ['Chou de Chine']
            r = ['Poirée', 'Radis']
            for button in self.side_veg_btns['button']:
                for nom in v:
                    if nom == button.objectName():
                        button.setStyleSheet('QPushButton {background-color: green;}')
                for nom in j:
                    if nom == button.objectName():
                        button.setStyleSheet('QPushButton {background-color: yellow;}')
                for nom in o:
                    if nom == button.objectName():
                        button.setStyleSheet('QPushButton {background-color: orange;}')
                for nom in r:
                    if nom == button.objectName():
                        button.setStyleSheet('QPushButton {background-color: red;}')

        elif self.fun_square_potager == 'Recolter':
            self.sender().setStyleSheet('QPushButton {background-color: white; color: black;}')
            self.sender().setIcon(QIcon())
        elif self.fun_square_potager == 'Information':
            self.infopage(self.bdd[self.bdd['Nom'] == ids[0]])
        # self.fun_square_potager = 'Information'

    def msgbtn(i):
        print("Button pressed is:", i.text())

    def infopage(self, df_legume):
        nom = df_legume['Nom'].values[0]
        description = df_legume['Description'].values[0]
        if str(description)=='nan':
            description = ''
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(nom)
        msg.setInformativeText(description)
        msg.setWindowTitle("Info ")
        msg.buttonClicked.connect(self.msgbtn)
        msg.exec_()
        print("Info :", nom)

    def selected_vegetable(self):
        df_legume = self.bdd[self.bdd['Nom'] == self.sender().objectName()]
        print('button droite', df_legume['Nom'].values[0])
        if self.fun_square_side == 'Information':
            self.infopage(df_legume)
        elif self.fun_square_side == 'Planter':
            self.tmp_button.setObjectName(df_legume['Nom'].values[0])
            self.tmp_button.setIcon(QIcon(QPixmap('../src/data/img/' + df_legume['Icon'].values[0])))
            self.tmp_button.setIconSize(QSize(70, 70))
        # elif self.fun_square_potager == 'Planter'

    def today(self):
        self.calendar.setSelectedDate(QDate(currentYear, currentMonth, currentDay))
        self.lcd.display(f'{currentDay} {currentMonth} {currentYear}')

    def display_date(self, qDate):
        day = str(qDate.day())
        month = str(qDate.month())
        year = str(qDate.year())
        self.lcd.display(f'{day}/{month}/{year}')

    def remplir_case(self, id_CARRE, id_carre):
        print('hey1')
        tmp = []
        retour = []
        listelegume = self.bdd['Nom'].values
        print('hey2')
        for i in range(len(listelegume)):
            print(i)
            legume = listelegume[i]
            print(legume)
            """Tests des petits carrés"""
            petitimpossible = self.estImpossible_petit(legume, id_CARRE, id_carre)
            print('prout')
            petitaeviter = self.estAeviter_petit(legume, id_CARRE, id_carre)
            print('prout')
            petitideal = self.estIdeal_petit(legume, id_CARRE, id_carre)
            print('prout')
            """Tests des grands carrés """
            grandimpossible = self.estImpossible_grand(legume, id_CARRE, id_carre)
            print('prout')
            grandaeviter = self.estAeviter_grand(legume, id_CARRE, id_carre)
            print('prout')
            grandideal = self.estIdeal_grand(legume, id_CARRE, id_carre)
            print('prout')
            if petitimpossible or grandimpossible:
                tmp.append('r')
            elif petitaeviter or grandaeviter:
                tmp.append('o')
            elif petitideal or grandideal:
                tmp.append('v')
            else:
                tmp.append('j')
        rouge = []
        orange = []
        jaune = []
        vert = []
        for i in range(len(tmp)):
            if tmp[i]=='r':
                rouge.append(listelegume[i])
            elif tmp[i] == 'o':
                orange.append(listelegume[i])
            elif tmp[i] == 'j':
                jaune.append(listelegume[i])
            else:
                vert.append(listelegume[i])

        retour.append(rouge)
        retour.append(orange)
        retour.append(jaune)
        retour.append(vert)
        return retour

    def placer_legume(self, legume):
        """
            'r' = rouge
            'o' = orange
            'j' = jaune
            'v' = vert
        """
        petitimpossible: bool
        petitaeviter: bool
        petitideal: bool
        grandimpossible: bool
        grandaeviter: bool
        grandideal: bool

        retour = []
        for n in range(6):
            truc = []
            for m in range(9):
                truc.append('n')
            retour.append(truc)
        for i in range(6):
            for j in range(9):
                if self.estOccupe_petit(legume, i, j):
                    retour[i][j] = 'n'
                else:
                    """Tests des petits carrés"""
                    petitimpossible = self.estImpossible_petit(legume, i, j)
                    petitaeviter = self.estAeviter_petit(legume, i, j)
                    petitideal = self.estIdeal_petit(legume, i, j)
                    """Tests des grands carrés """
                    grandimpossible = self.estImpossible_grand(legume, i, j)
                    grandaeviter = self.estAeviter_grand(legume, i, j)
                    grandideal = self.estIdeal_grand(legume, i, j)
                    if petitimpossible or grandimpossible:
                        retour[i][j] = 'r'
                    elif petitaeviter or grandaeviter:
                        retour[i][j] = 'o'
                    elif petitideal or grandideal:
                        retour[i][j] = 'v'
                    else:
                        retour[i][j] = 'j'
        return retour

    def save(self):
        print('Sauvegarde effectuée')
        self.potager.to_csv('../src/data/potager.csv', sep=';')
        self.fun_square_side = 'Information'
        if self.fun_square_potager == 'Planter':
            self.tmp_button.setStyleSheet('QPushButton {background-color: #828594; color: black;}')
        self.fun_square_potager = 'Information'
        self.clear_side_background()

    # Geo func
    def estImpossible_grand(self, legume, id_CARRE, id_carre):
        """Prend en argument un légume, le dataset et la coordonnées du GRAND carré (id_CARRE) et celle du PETIT carré (id_carre) pour renvoyer True si l'emplacement est impossible et False s'il est possible"""
        retour: bool = False

        return retour

    def estIdeal_grand(self, legume, id_CARRE, id_carre):
        """Prend en argument un légume, le dataset et les coordonnées du carré pour renvoyer True si l'emplacement est idéal et False s'il ne l'est pas"""
        retour: bool = False

        return retour

    def estAeviter_grand(self, legume, id_CARRE, id_carre):
        """Prend en argument un légume, le dataset et les coordonnées du carré pour renvoyer True si l'emplacement est à éviter et False s'il ne l'est pas"""
        retour: bool = False
        voisins = self.voisins_grand(id_carre)
        nepasplanterpresde = (self.bdd[self.bdd['Nom'] == legume]['Eloigner de'].values[0])
        legumesducarre = []
        for n in voisins:
            temp = self.potager[(self.potager['id_CARRE'] == id_CARRE)]
            legumepresent = temp[(temp['id_carre'] == n)]['Présent'].values[0]
            legumesducarre.append(legumepresent)
        if type(nepasplanterpresde) != float:
            if len(nepasplanterpresde) != 1:
                nepasplanterpresde = nepasplanterpresde.split(',')
            for n in legumesducarre:
                for m in nepasplanterpresde:
                    if n == m:
                        retour = True
        return retour

    def voisins_grand(self, x):
        """Renvoie les petits carrés voisins (en comptant les diagonales) du carré de coordonnées x"""
        retour = []
        if x ==0:
            retour = [1, 3, 4]
        elif x == 1:
            retour = [0, 2, 3, 4, 5]
        elif x == 2:
            retour = [1, 4, 5]
        elif x == 3:
            retour = [0, 1, 4, 6, 7]
        elif x == 4:
            retour = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        elif x == 5:
            retour = [1, 2, 4, 7, 8]
        elif x == 6:
            retour = [3, 4, 7]
        elif x == 7:
            retour = [3, 4, 5, 6, 8]
        else:
            retour = [4, 5, 7]
        return retour

    def estOccupe_petit(self, legume, id_CARRE, id_carre):
        """Prend en argument un légume, le dataset et les coordonnées du carré pour renvoyer True si l'emplacement est occupé et False s'il ne l'est pas"""
        temp = self.potager[(self.potager['id_carre'] == id_carre)]
        present = temp[(temp['id_CARRE'] == id_CARRE)]['Présent'].values[0]
        if type(present) != float:
            return True
        else:
            return False

    def estImpossible_petit(self, legume, id_CARRE, id_carre):
        global raison
        """Prend en argument un légume, le dataset et les coordonnées du carré pour renvoyer True si l'emplacement est impossible et False s'il est possible"""
        retour: bool = False
        """TEST EMPLACEMENT"""
        emplacement = self.bdd[self.bdd['Nom'] == legume]['Emplacement'].values[0]
        if emplacement == "Au milieu":
            if id_CARRE != 4:
                retour = True
        elif emplacement == "Au bord":
            if id_CARRE == 4:
                retour = True
        return retour

    def estIdeal_petit(self, legume, id_CARRE, id_carre):
        """Prend en argument un légume, le dataset et les coordonnées du carré pour renvoyer True si l'emplacement est idéal et False s'il ne l'est pas"""
        retour: bool = False
        planterapres = self.bdd[(self.bdd['Nom'] == legume)]['Rapprocher de'].values[0]
        if np.isnan(planterapres):
            planterapres = []
        temp = self.potager[(self.potager['id_CARRE'] == id_CARRE)]
        print('ids', id_CARRE, id_carre)
        print('hey1', planterapres)
        print('hey2', temp)
        print('hey3', temp['id_carre'])

        dernierplante = temp[(temp['id_carre'] == id_carre)]['Passé'].values[0]
        print(planterapres, temp, dernierplante)
        if type(planterapres[0]) != float:
            if len(planterapres) != 1:
                planterapres = planterapres.split(', ')
            for n in planterapres:
                if n == dernierplante:
                    retour = True
        return retour

    def estAeviter_petit(self, legume, id_CARRE, id_carre):
        """Prend en argument un légume, le dataset et les coordonnées du carré pour renvoyer True si l'emplacement est à éviter et False s'il ne l'est pas"""
        retour: bool = False
        # <3
        return retour



# class InfoWindow(QMainWindow):
#
#     def __init__(self, parent=None):
#         super(InfoWindow, self).__init__(parent)
#         self.title = 'Informations'
#         self.setWindowTitle(f'{self.title} (nom du légume)')
#
#         self.setGeometry(300, 500, 300, 0)
#         self.text = QLabel(self)
#         self.text.setText("Un jour il y aura self.bdd['Description']")


# class ChoiceWindow(QMainWindow):
#
#     def __init__(self, parent=None):
#         super(ChoiceWindow, self).__init__(parent)
#         self.title = 'Choix de la plantation'
#         # self.setGeometry(300, 500, 300, 0)
#         # self.a = QLabel('some infos sur la patate', self)
#         layout = QGridLayout(self)
#         images = os.listdir('../src/data/img/')
#         n = int(np.sqrt(len(images))) + 1
#         for i in range(len(images)):
#             button = QPushButton(self)
#             button.clicked.connect(self.choice)
#             button.setFixedSize(70, 70)
#             button.setIconSize(QSize(70, 70))
#             button.setStyleSheet('QPushButton {background-color: #828594; color: black;}')
#             button.setIcon(QIcon(QPixmap('../src/data/img/' + images[i])))
#             x, y = int(i/n), i%n
#             layout.addWidget(button, x, y)
#         layout.setHorizontalSpacing(5)
#         layout.setAlignment(Qt.AlignCenter)
#         self.central_widget = QWidget(self)
#         self.central_widget.setLayout(layout)
#         self.setCentralWidget(self.central_widget)
#         # self.setGeometry(300, 500, 300, 500)
#
#     def choice(self):
#         self.close()


