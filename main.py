from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


# python -m PyQt5.uic.pyuic -x raw_window.ui -o raw_window.py

class Ui_MainWindow(object):
    """
    Main window setup and button preparation aswell as linking button actions to functions.
    And creates a global dataframe for all registered callsings.
    """

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 771, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.intend_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.intend_label.setObjectName("intend_label")
        self.gridLayout.addWidget(self.intend_label, 0, 2, 1, 1)
        self.callsing_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.callsing_input.setClearButtonEnabled(False)
        self.callsing_input.setObjectName("callsing_input")
        self.gridLayout.addWidget(self.callsing_input, 1, 1, 1, 1)
        self.intend_input = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.intend_input.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.intend_input.setObjectName("intend_input")
        self.intend_input.addItem("")
        self.intend_input.addItem("")
        self.intend_input.addItem("")
        self.gridLayout.addWidget(self.intend_input, 1, 2, 1, 1)
        self.target_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.target_label.setObjectName("target_label")
        self.gridLayout.addWidget(self.target_label, 0, 3, 1, 1)
        self.weapons_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.weapons_label.setObjectName("weapons_label")
        self.gridLayout.addWidget(self.weapons_label, 0, 4, 1, 1)
        self.register_trigger = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.register_trigger.setObjectName("register_trigger")
        self.gridLayout.addWidget(self.register_trigger, 1, 5, 1, 1)
        self.callsing_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.callsing_label.setObjectName("callsing_label")
        self.gridLayout.addWidget(self.callsing_label, 0, 1, 1, 1)
        self.clear_trigger = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clear_trigger.setObjectName("clear_trigger")
        self.gridLayout.addWidget(self.clear_trigger, 1, 6, 1, 1)
        self.weapons_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.weapons_input.setObjectName("weapons_input")
        self.gridLayout.addWidget(self.weapons_input, 1, 4, 1, 1)
        self.target_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.target_input.setObjectName("target_input")
        self.gridLayout.addWidget(self.target_input, 1, 3, 1, 1)
        self.recorded_display = QtWidgets.QTableWidget(self.centralwidget)
        self.recorded_display.setGeometry(QtCore.QRect(10, 80, 771, 511))
        self.recorded_display.setShowGrid(True)
        self.recorded_display.setGridStyle(QtCore.Qt.SolidLine)
        self.recorded_display.setObjectName("recorded_display")
        self.recorded_display.setColumnCount(4)
        self.recorded_display.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.recorded_display.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.recorded_display.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.recorded_display.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.recorded_display.setHorizontalHeaderItem(3, item)
        self.recorded_display.horizontalHeader().setVisible(True)
        self.recorded_display.horizontalHeader().setCascadingSectionResizes(False)
        self.recorded_display.horizontalHeader().setDefaultSectionSize(173)
        self.recorded_display.horizontalHeader().setSortIndicatorShown(True)
        self.recorded_display.horizontalHeader().setStretchLastSection(False)
        self.recorded_display.verticalHeader().setCascadingSectionResizes(False)
        self.recorded_display.verticalHeader().setSortIndicatorShown(False)
        self.recorded_display.verticalHeader().setStretchLastSection(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Setup of the global dataframe that holds all Data
        global data
        data = pd.DataFrame(columns=("call", "intend", "target", "weapons"))

        self.register_trigger.clicked.connect(lambda: self.add_item())
        self.clear_trigger.clicked.connect(lambda: self.remove_item())

    """
    Filling of the UI with text and arrangement.
    """

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.intend_label.setText(_translate("MainWindow", "Intend"))
        self.intend_input.setItemText(0, _translate("MainWindow", "SEAD"))
        self.intend_input.setItemText(1, _translate("MainWindow", "CAS"))
        self.intend_input.setItemText(2, _translate("MainWindow", "CAP"))
        self.target_label.setText(_translate("MainWindow", "Target Area"))
        self.weapons_label.setText(_translate("MainWindow", "Weapons"))
        self.register_trigger.setText(_translate("MainWindow", "Register"))
        self.callsing_label.setText(_translate("MainWindow", "Callsing"))
        self.clear_trigger.setText(_translate("MainWindow", "Clear"))
        self.recorded_display.setSortingEnabled(True)
        item = self.recorded_display.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Callsign"))
        item = self.recorded_display.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Intend"))
        item = self.recorded_display.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Target Area"))
        item = self.recorded_display.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Weapons"))

    """
    Reads input fields and returns a pandas Series with the right indexes for later assignment
    """

    def read_inputs(self):
        new = pd.Series(data={"call": self.callsing_input.text(), "intend": self.intend_input.currentText(),
                              "target": self.target_input.text(), "weapons": self.weapons_input.text()})
        return new

    """
    Resets inputs to initial state:
    """

    def clear_inputs(self):
        self.callsing_input.setText("")
        self.intend_input.setCurrentText("SEAD")
        self.target_input.setText("")
        self.weapons_input.setText("")

    """
    ADDs or updates the table with the new inputs from the text boxes. Is called on Register button press. 
    If the callsing already exists it just updates the new fields, if some where left empty they stay unchanged.
    It updates the general data Dataframe as well as the displayed table and then resets inputs to standards.
    """

    def add_item(self):
        new_data = self.read_inputs()

        if new_data[0] in data.values:

            index = data.index[data["call"] == new_data[0]][0]
            new_data = new_data.drop("call")

            if new_data["intend"] == data.iloc[index][1]:
                new_data = new_data.drop("intend")

            if new_data["target"] == "":
                new_data = new_data.drop("target")

            if new_data["weapons"] == "":
                new_data = new_data.drop("weapons")
            data.iloc[index].update(new_data)

            for i in range(len(data.iloc[index])):
                self.recorded_display.setItem(index, i, QtWidgets.QTableWidgetItem(str(data.iloc[index][i])))




        else:
            data.loc[len(data)] = new_data
            rowPosition = self.recorded_display.rowCount()
            self.recorded_display.insertRow(rowPosition)

            for i in range(len(new_data)):
                self.recorded_display.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(new_data[i])))

        self.clear_inputs()

    """
    Triggered by Clear button if the callsing exists 
    it removes it from the displayed table aswell as the general Dataframe
    """

    def remove_item(self):
        global data

        to_remove = self.callsing_input.text()
        if to_remove in data.values:
            index = data.index[data["call"] == to_remove][0]
            self.recorded_display.removeRow(index)

            data = data.drop(index)
            data = data.reset_index()

        self.clear_inputs()


if __name__ == "__main__":
    import sys

    global data
    data = pd.DataFrame(columns=("call", "intend", "target", "weapons"))

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
