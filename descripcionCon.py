import sys
import os
from PyQt5 import QtWidgets
from Vistas.descripcion import Ui_MainWindow_descripcion
import pandas as pd

myDir = os.getcwd()
sys.path.append(myDir)


class VentanaDescripcion(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaDescripcion, self).__init__()
        self.ui = Ui_MainWindow_descripcion()
        self.ui.setupUi(self)
        # -----------------------Eventos-----------------------------------------------
        self.ui.Button_buscar.clicked.connect(self.listaDescripcion)

    # -----------------------Fin eventos-------------------------------------------

    def listaDescripcion(self):
        df = pd.read_csv('Datos/data.csv')
        # df_habitos = pd.read_csv('data/DatosHabitos.csv')
        # df_sinFisicos = pd.read_csv('data/DatosSintomasFisicos.csv')
        # df_sinEmocion = pd.read_csv('data/DatosSintomasEmocionales.csv')
        try:
            fecha = self.ui.dateEdit_descripcion.text()
            indice = df[df['fecha'] == fecha].index.tolist()
            dia_ciclo = df['dia-ciclo'].values[indice]
            self.ui.label_diaCiclo.setText('Día del ciclo: ' + str(dia_ciclo[0]))
            numero_ciclo = df['numero-ciclo'].values[indice]
            self.ui.label_numeroCiclo.setText('Número de ciclo: ' + str(numero_ciclo[0]))
            fase_ciclo = df['fase-ciclo'].values[indice]
            self.ui.label_faseCiclo.setText('Fase del ciclo: ' + str(fase_ciclo[0]))
            fase_lunar = df['fase-lunar'].values[indice]
            self.ui.label_faseLunar.setText('Fase lunar: ' + str(fase_lunar[0]))
            notas_emocio = df['notas-emocionales'].values[indice]
            self.ui.label_notasEmocionales.setText(str(notas_emocio[0]))
            notas_alime = df['notas-alimentacion'].values[indice]
            self.ui.label_notasAlimentacion.setText(str(notas_alime[0]))
            if (df['irritable'].iloc[indice] == 1).bool():
                self.ui.label_irritable.setText('Estuve irritable')
            else:
                self.ui.label_irritable.setText('No estuve irritable')
            if (df['atencion-concentracion'].iloc[indice] == 1).bool():
                self.ui.label_atencionConc.setText('Tuve atención y concentración')
            else:
                self.ui.label_atencionConc.setText('Estuve desconcentrada')
            if (df['sensible'].iloc[indice] == 1).bool():
                self.ui.label_sensible.setText('Sensible')
            else:
                self.ui.label_sensible.setText('No estuve sensible')
            if (df['triste'].iloc[indice] == 1).bool():
                self.ui.label_triste.setText('Triste')
            else:
                self.ui.label_triste.setText('No hubo tristeza')
            if (df['alegre'].iloc[indice] == 1).bool():
                self.ui.label_alegre.setText('Alegre')
            else:
                self.ui.label_alegre.setText('Sin alegría')
            if (df['tranquila'].iloc[indice] == 1).bool():
                self.ui.label_tranquila.setText('Tranquila')
            else:
                self.ui.label_tranquila.setText('No hubo tranquilidad')
            if (df['tensionada'].iloc[indice] == 1).bool():
                self.ui.label_tensionada.setText('Tensionada')
            else:
                self.ui.label_tensionada.setText('No hubo tensión')
            if (df['hinchazon'].iloc[indice] == 1).bool():
                self.ui.label_hinchazon.setText('Hinchazón')
            else:
                self.ui.label_hinchazon.setText('Sin hinchazón')
            if (df['acne'].iloc[indice] == 1).bool():
                self.ui.label_acne.setText('Acné')
            else:
                self.ui.label_acne.setText('No hubo acné')
            if (df['dolor-ovarios'].iloc[indice] == 1).bool():
                self.ui.label_dolorOvarios.setText('Dolor de ovarios')
            else:
                self.ui.label_dolorOvarios.setText('Sin dolor de ovarios')
            if (df['dolor-lumbar'].iloc[indice] == 1).bool():
                self.ui.label_dolorLumbar.setText('Dolor lumbar')
            else:
                self.ui.label_dolorLumbar.setText('Sin dolor lumbar')
            if (df['cansancio'].iloc[indice] == 1).bool():
                self.ui.label_cansancio.setText('Cansancio')
            else:
                self.ui.label_cansancio.setText('No hubo cansancio')
            if (df['pecho-sensible'].iloc[indice] == 1).bool():
                self.ui.label_pechoSensible.setText('Pecho sensible')
            else:
                self.ui.label_pechoSensible.setText('No hubo pecho sensible')
            if (df['antojos'].iloc[indice] == 1).bool():
                self.ui.label_antojos.setText('Antojos')
            else:
                self.ui.label_antojos.setText('Sin antojos')
            if (df['deseo-sexual'].iloc[indice] == 1).bool():
                self.ui.label_deseoSexual.setText('Deseo sexual')
            else:
                self.ui.label_deseoSexual.setText('Sin deseo sexual')
            tipo_sangrad = df['tipo-sangrado'].values[indice]
            self.ui.label_tipoSangrad.setText('Tipo de sangrado: ' + str(tipo_sangrad[0]))
            tipo_flujo = df['tipo-flujo'].values[indice]
            self.ui.label_tipoFlujo.setText('Tipo de flujo: ' + str(tipo_flujo[0]))
            sensaci_energia = df['sensacion-energia'].values[indice]
            self.ui.label_sensacEnergia.setText('Sensación de energía: ' + str(sensaci_energia[0]))
            sensaci_vulvar = df['sensacion-vulvar'].values[indice]
            self.ui.label_sensacVulvar.setText('Sensación vulvar: ' + str(sensaci_vulvar[0]))
            heces = df['heces'].values[indice]
            self.ui.label_heces.setText('Heces: ' + str(heces[0]))
            sueno = df['sueño'].values[indice]
            self.ui.label_sueno.setText('Horas de sueño: ' + str(sueno[0]))
            ayuno = df['ayuno'].values[indice]
            self.ui.label_ayuno.setText('Horas de ayuno: ' + str(ayuno[0]))
            if (df['relaciones-sexuales'].iloc[indice] == 1).bool():
                self.ui.label_relacionSexuales.setText('Relaciones sexuales')
            else:
                self.ui.label_relacionSexuales.setText('Sin relaciones sexuales')
            carbohidratos = df['carbohidratos'].values[indice]
            self.ui.label_carbohidratos.setText('Carbohidratos consumidos: ' + str(carbohidratos[0]))
            ejer_fuerza = df['ejercicio-fuerza'].values[indice]
            self.ui.label_ejercicioFuerza.setText('Ejercicio de fuerza: ' + str(ejer_fuerza[0]))
            ejer_cardio = df['ejercicio-cardio'].values[indice]
            self.ui.label_ejercicioCardio.setText('Ejercicio de cardio: ' + str(ejer_cardio[0]))
        except IndexError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText('Fecha no encontrada. Intente de nuevo')
            msg.setWindowTitle("Error")
            msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaDescripcion()
    ventana.show()
    sys.exit(app.exec_())
