import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication  # , QVBoxLayout
from Vistas.grafica import Ui_MainWindow_grafica
from descripcionCon import VentanaDescripcion
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
import matplotlib
import pandas as pd

matplotlib.use('Qt5Agg')
myDir = os.getcwd()
sys.path.append(myDir)


class GraficaWidget(FigureCanvasQTAgg):
    def __init__(self, parent=None, dpi=140):
        figura = Figure(dpi=dpi)
        # figura.autofmt_xdate()
        self.ejes1 = figura.add_subplot(111)
        # self.ejes2 = figura.add_subplot(212)
        super(GraficaWidget, self).__init__(figura)
        figura.tight_layout()


class VentanaGrafica(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaGrafica, self).__init__()
        self.ven_descripcion = VentanaDescripcion()
        self.ui = Ui_MainWindow_grafica()
        self.ui.setupUi(self)
        # self.initWidget()
        self.grafica()
        # -----------------------Eventos-----------------------------------------------
        self.ui.Button_descripcion.clicked.connect(self.abrirDescripcion)

    # -----------------------Fin eventos-------------------------------------------

    def grafica(self):
        self.canvas = GraficaWidget(self)
        self.toolbar = Navi(self.canvas, self.ui.centralwidget)
        self.ui.horizontalLayout.addWidget(self.toolbar)
        self.ui.verticalLayout.addWidget(self.canvas)
        # df_main = pd.read_csv('data/Datosmain.csv')
        # df_habitos = pd.read_csv('data/DatosHabitos.csv')
        # x1 = df_main['fecha']
        # y1 = df_habitos['temperatura']
        df = pd.read_csv('Datos/data.csv')
        x1 = df['fecha']
        y1 = df['temperatura']
        self.canvas.ejes1.plot_date(x1, y1, fmt='bo--')
        self.canvas.ejes1.set_xlabel('Fecha')
        self.canvas.ejes1.set_ylabel('Temperatura')
        self.canvas.ejes1.xaxis.set_tick_params(rotation=45)  # , labelsize=10)
        self.canvas.ejes1.grid(True)
        self.canvas.draw()

    def abrirDescripcion(self):
        pass
        self.ven_descripcion.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaGrafica()
    ventana.show()
    sys.exit(app.exec_())
