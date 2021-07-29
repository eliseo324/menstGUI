#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 20:58:55 2021

@author: Eliseo Vargas
"""
import os
import sys
import pandas as pd
import PyQt5.QtWidgets
import Vistas.formularioInicial
import graficaDash

myDir = os.getcwd()
sys.path.append(myDir)


class VentanaMenu(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaMenu, self).__init__()
        # self.ve_grafica = graficaCon.VentanaGrafica()
        self.ve_grafica = graficaDash.VentanaGrafica()
        self.ui = Vistas.formularioInicial.Ui_Main_menstGUI()
        self.ui.setupUi(self)
        # -----------------------Eventos-----------------------------------------------
        self.ui.Button_grafica.clicked.connect(self.abrirGrafica)
        self.ui.Button_guardar_main.clicked.connect(self.guardarMenu)

    # -----------------------Fin eventos-------------------------------------------
    def guardarMenu(self):
        try:
            if self.ui.checkBox_relaSexual.isChecked():
                rela_sexual = 1
            else:
                rela_sexual = 0
            if self.ui.groupBox_ejercicio.isChecked():
                ejercicio = 1
            else:
                ejercicio = 0
            if self.ui.checkBox_hinchazon.isChecked():
                hinchazon = 1
            else:
                hinchazon = 0
            if self.ui.checkBox_acne.isChecked():
                acne = 1
            else:
                acne = 0
            if self.ui.checkBox_dolovarios.isChecked():
                dolovarios = 1
            else:
                dolovarios = 0
            if self.ui.checkBox_dolumbar.isChecked():
                dolumbar = 1
            else:
                dolumbar = 0
            if self.ui.checkBox_cansancio.isChecked():
                cansancio = 1
            else:
                cansancio = 0
            if self.ui.checkBox_psensible.isChecked():
                psensible = 1
            else:
                psensible = 0
            if self.ui.checkBox_antojos.isChecked():
                antojos = 1
            else:
                antojos = 0
            if self.ui.checkBox_deseoSexual.isChecked():
                deseo_sexual = 1
            else:
                deseo_sexual = 0
            if self.ui.checkBox_irritable.isChecked():
                irritable = 1
            else:
                irritable = 0
            if self.ui.checkBox_atenConcent.isChecked():
                aten_concent = 1
            else:
                aten_concent = 0
            if self.ui.checkBox_sensible.isChecked():
                sensible = 1
            else:
                sensible = 0
            if self.ui.checkBox_triste.isChecked():
                triste = 1
            else:
                triste = 0
            if self.ui.checkBox_alegre.isChecked():
                alegre = 1
            else:
                alegre = 0
            if self.ui.checkBox_tranquila.isChecked():
                tranquila = 1
            else:
                tranquila = 0
            if self.ui.checkBox_tensionada.isChecked():
                tensionada = 1
            else:
                tensionada = 0
            data = [[self.ui.spinBox_diaCiclo.value(),
                     self.ui.spinBox_numCiclo.value(),
                     self.ui.dateEdit_fecha.text(),
                     str(self.ui.comboBox_faciclo.currentText()),
                     str(self.ui.comboBox_falunar.currentText()),
                     round(self.ui.doubleSpinBox_temperatura.value(), 2),
                     str(self.ui.line_heces.text()),
                     float(self.ui.line_sueno.text()),
                     float(self.ui.line_ayuno.text()),
                     rela_sexual,
                     str(self.ui.comboBox_carbohidratos.currentText()),
                     ejercicio,
                     str(self.ui.comboBox_ejerFuerza.currentText()),
                     str(self.ui.comboBox_ejerCardio.currentText()),
                     hinchazon,
                     acne,
                     dolovarios,
                     dolumbar,
                     cansancio,
                     psensible,
                     antojos,
                     deseo_sexual,
                     str(self.ui.comboBox_tsangrado.currentText()),
                     str(self.ui.comboBox_tflujo.currentText()),
                     str(self.ui.comboBox_sensEnergia.currentText()),
                     str(self.ui.comboBox_sensVulvar.currentText()),
                     irritable,
                     aten_concent,
                     sensible,
                     triste,
                     alegre,
                     tranquila,
                     tensionada,
                     self.ui.text_emociones.toPlainText(),
                     self.ui.text_alimentacion.toPlainText()
                     ]]
            df = pd.DataFrame(data)
            df.to_csv('Datos/data.csv', index=False, mode="a", header=not os.path.isfile('Datos/data.csv'))

            self.ui.spinBox_diaCiclo.clear()
            self.ui.text_emociones.clear()
        except ValueError:
            msg = PyQt5.QtWidgets.QMessageBox()
            msg.setIcon(PyQt5.QtWidgets.QMessageBox.Information)
            msg.setText('Faltan campos por llenar')
            msg.setWindowTitle("Advertencia")
            msg.exec_()

    # ------------------------------Abrir ventanas---------------------------------
    def abrirGrafica(self):
        self.ve_grafica.run_server(debug=True)


# ------------------------------Fin abrir ventatas---------------------------------

if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ventana = VentanaMenu()
    ventana.show()
    sys.exit(app.exec_())
