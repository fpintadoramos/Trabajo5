from reportlab.pdfgen.canvas import Canvas
from ui_design import Ui_MainWindow
import sys
from PySide6.QtWebEngineWidgets import QWebEngineView
import GestionarMuebles
import GestionarPedidos
from PySide6.QtWebEngineCore import QWebEngineSettings
from pathlib import Path
from pdfrw import PdfReader
from PySide6.QtCore import QUrl
from pdfrw.toreportlab import makerl
import pyqtgraph as pg
import pyqtgraph.exporters

from pdfrw.buildxobj import pagexobj

from PySide6.QtWidgets import QApplication,QPushButton, QMainWindow, QTableWidgetItem,QCheckBox, QWizard, QWizardPage, QFormLayout, QLineEdit, QLabel, QMessageBox, QSpinBox

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mueble = {"_id":"","nombre": "", "precio":"", "dimensiones":"", "cant":"0"}
        cont = 1
        if GestionarPedidos.pedidos.find():
            for x in GestionarPedidos.pedidos.find():
                cont += 1
        self.idPedido.setText(str(cont))
        self.dimensionesFinales.setDisabled(True)

        #QWizard para Eliminar
        self.wEliminar = QWizard()
        self.wEliminar.setWizardStyle(QWizard.ModernStyle)
        self.wEliminar.button(QWizard.FinishButton).clicked.connect(self.eliminar)
            #Pagina 1
        paginaEliminar = QWizardPage()
        paginaEliminar.setFinalPage(True)
        paginaEliminar.setTitle("Eliminar Mueble")
        eLayout = QFormLayout(paginaEliminar)
        eLabel = QLabel()
        eLabel.setText("Id del mueble")
        self.eId = QLineEdit()
        eLayout.addRow(eLabel, self.eId)
        self.wEliminar.addPage(paginaEliminar)

        #QWizard para Modificar
        self.wModificar = QWizard()
        self.wModificar.setWizardStyle(QWizard.ModernStyle)
        self.wModificar.button(QWizard.FinishButton).clicked.connect(self.modificar)
            #Pagina 1
        paginaMod1 = QWizardPage()
        paginaMod1.setTitle("Modificar mueble")
        layoutMod1 = QFormLayout(paginaMod1)
        idLabel = QLabel()
        idLabel.setText("ID de mueble a modificar")
        self.idMod = QLineEdit()
        layoutMod1.addRow(idLabel, self.idMod)
            #Pagina 2
        paginaMod2 = QWizardPage()
        paginaMod2.setTitle("Modificar mueble")
        layoutMod2 = QFormLayout(paginaMod2)
        nombreLabel = QLabel()
        nombreLabel.setText("Nuevo nombre")
        self.nomMod = QLineEdit()
        precioLabel = QLabel()
        precioLabel.setText("Nuevo precio")
        self.precioMod = QLineEdit()
        layoutMod2.addRow(nombreLabel, self.nomMod)
        layoutMod2.addRow(precioLabel, self.precioMod)
            #Pagina 3
        paginaMod3 = QWizardPage()
        paginaMod3.setTitle("Modificar mueble")
        layoutMod3 = QFormLayout(paginaMod3)
        paginaMod3.setFinalPage(True)
        alturaLabel = QLabel()
        alturaLabel.setText("Nueva altura")
        self.altMod = QLineEdit()
        anchoLabel = QLabel()
        anchoLabel.setText("Nuevo ancho")
        self.anchMod = QLineEdit()
        largoLabel = QLabel()
        largoLabel.setText("Nuevo largo")
        self.largMod = QLineEdit()
        layoutMod3.addRow(alturaLabel, self.altMod)
        layoutMod3.addRow(anchoLabel, self.anchMod)
        layoutMod3.addRow(largoLabel, self.largMod)

        #Añadir paginas
        self.wModificar.addPage(paginaMod1)
        self.wModificar.addPage(paginaMod2)
        self.wModificar.addPage(paginaMod3)

        #TablaProductos
        self.productos.setColumnCount(4)
        nombreColumnas = ("ID", "NOMBRE", "PRECIO", "DIMENSIONES")
        self.productos.setHorizontalHeaderLabels(nombreColumnas)
        #TableCantidades
        self.Cantidad.setColumnCount(3)
        nombreColumnas1 = ("ID", "NOMBRE", "CANTIDAD")
        self.Cantidad.setHorizontalHeaderLabels(nombreColumnas1)

        #Actualizar dimensiones finales
        self.alturaMueble.textChanged.connect(self.actDimensiones)
        self.anchoMueble.textChanged.connect(self.actDimensiones)
        self.largoMueble.textChanged.connect(self.actDimensiones)

        #Acciones
        self.addMueble.clicked.connect(self.añadir)
        self.listMuebles.clicked.connect(self.obtener)
        self.delMueble.clicked.connect(lambda: self.wEliminar.show())
        self.modMueble.clicked.connect(lambda: self.wModificar.show())

        #Pedidos
        self.hacerPedido.clicked.connect(self.realizarPedido)
        self.genInforme.clicked.connect(lambda: self.wInf.show())
        # WizardElegirInformePedido
        self.wInf = QWizard()
        paginaInf = QWizardPage()
        paginaInf.setTitle("Elegir pedido")
        paginaInf.setFinalPage(True)
        layoutInf = QFormLayout(paginaInf)
        pedidoInfLabel = QLabel()
        pedidoInfLabel.setText("ID de pedido")
        self.idInf = QSpinBox()
        layoutInf.addRow(pedidoInfLabel, self.idInf)
        self.wInf.addPage(paginaInf)
        self.wInf.button(QWizard.FinishButton).clicked.connect(self.generarInforme)

        self.todosPedidos = QPushButton(self.genPedidos)
        self.todosPedidos.setGeometry(180,120,150,54)
        self.todosPedidos.setText("Informe todos los pedidos")
        self.todosPedidos.clicked.connect(lambda: self.wPedidos.show())
        #WizardPedidos
        self.wPedidos = QWizard()
        self.wPedidos.button(QWizard.FinishButton).clicked.connect(self.informeTodosPedidos)
        paginaTodosPedidos = QWizardPage()
        paginaTodosPedidos.setTitle("Elegir numero de Pedidos")
        lPedidos = QFormLayout(paginaTodosPedidos)
        labelNum = QLabel()
        self.cantTotal = QCheckBox()
        self.cantTotal.setText("Incuir precio total.")
        labelNum.setText("Numero de pedidos")
        self.numPedidos = QSpinBox()
        lPedidos.addRow(labelNum, self.numPedidos)
        lPedidos.addRow(self.cantTotal)
        self.wPedidos.addPage(paginaTodosPedidos)

        #Visualizar pdf
        self.web = QWebEngineView(self.genPedidos)
        self.web.setGeometry(450,30,300,600)
        self.web.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

        self.obtenerCantidades()

    def informeTodosPedidos(self):
        cont = 0
        yStart = 550
        outfile = "Pedidos.pdf"
        template = PdfReader("TemplatePedidos.pdf", decompress=False).pages[0]
        template_obj = pagexobj(template)

        canvas = Canvas(outfile)
        precioTotal = 0
        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)
        while cont <= int(self.numPedidos.text()):
            data = {"_id":str(cont)}
            if GestionarPedidos.pedidos.find_one(data):
                p = GestionarPedidos.pedidos.find_one(data)
                
                m = {"_id": p['idProducto']}

                canvas.drawString(150, yStart, p['_id'])
                canvas.drawString(250, yStart, p['idProducto'])
                if GestionarMuebles.my_collection.find_one(m):
                    m = GestionarMuebles.my_collection.find_one(m)
                    precio = m["precio"]
                canvas.drawString(350, yStart, p['cantidad'])
                canvas.drawString(450, yStart, str(int(p['cantidad']) * int(precio))+ " €")
                precioTotal += int(p['cantidad']) * int(precio)
                
                yStart -= 24
            cont += 1

        if self.cantTotal.isChecked():
            canvas.drawString(350, 290, "Precio Total:")
            canvas.drawString(450, 290, str(precioTotal) + " €")
        

        self.graphWidget = pg.plot()
        self.graphWidget.setBackground('w')
        pen = pg.mkPen(color=(0,0,0))
        
        cantidad = []
        nombre = []
        if GestionarMuebles.my_collection.find():
            for x in GestionarMuebles.my_collection.find():
                
                cantidad.append(int(x['cant']))
                nombre.append(int(x['_id']))

        bg = pg.BarGraphItem(x = nombre, height = cantidad, width = 0.6, brush = 'g')
        self.graphWidget.addItem(bg)
        self.graphWidget.hide()

        exporter = pg.exporters.ImageExporter(self.graphWidget.plotItem)
        exporter.parameters()['width'] = 1000
        exporter.export('graphic.png')

        canvas.drawImage("graphic.png", 290, 600, width=250,height=200,mask=None)
        canvas.save()
        

    def rellenarInformePedido(self, idPedido:str):
        data = {"_id": idPedido, "idProducto":"", "cantidad":""}
        if  GestionarPedidos.pedidos.find():
            for x in GestionarPedidos.pedidos.find():
                if int(x["_id"]) == int(idPedido):
                    data["idProducto"] = x["idProducto"]
                    data["cantidad"] = x["cantidad"]
        outfile = "Pedido" + idPedido + ".pdf"
        template = PdfReader("Template.pdf", decompress=False).pages[0]
        template_obj = pagexobj(template)

        canvas = Canvas(outfile)

        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)

        yStart = 408
        
        canvas.drawString(220, yStart, data['_id'])
        canvas.drawString(177, yStart - 59, data['idProducto'])

        if GestionarMuebles.my_collection.find():
            for x in GestionarMuebles.my_collection.find():
                if int(x["_id"]) == int(idPedido):
                    nombre = x["nombre"]
                    precio = x["precio"]
        
        canvas.drawString(332, yStart - 59, nombre)
        canvas.drawString(450, yStart - 59, precio)
        canvas.drawString(220, yStart - 74, data['cantidad'])
        precioTotal = int(precio) * int(data["cantidad"])
        canvas.drawString(185, yStart - 120, str(precioTotal))
        canvas.save()

        rutaConPDF = Path("Pedido"+ idPedido + ".pdf")
        self.web.load(QUrl(rutaConPDF.absolute().as_uri()))

    def generarInforme(self):
        if GestionarPedidos.pedidos.find():
            for x in GestionarPedidos.pedidos.find():
                if int(x["_id"]) == int(self.idInf.value()):
                    self.rellenarInformePedido(str(x["_id"]))
        

    def realizarPedido(self):
        m = {"_id":"","nombre": "", "precio":"", "dimensiones":"", "cant":"0"}
        try:
            cant = int(self.cantidad.text())
            id = int(self.idMueblePedir.text())
            row = 0
            if GestionarMuebles.my_collection.find():
                for x in GestionarMuebles.my_collection.find():
                    if int(x["_id"]) == int(self.idMueblePedir.text()):
                        m["_id"] = x["_id"]
                        GestionarMuebles.my_collection.delete_one(m)
                        m["nombre"] = x["nombre"]
                        m["precio"] = x["precio"]
                        m["dimensiones"] = x["dimensiones"]
                        m["cant"] = str(int(x["cant"]) + cant)
                        GestionarMuebles.my_collection.insert_one(m)
                        self.añadirPedido()
                        self.obtenerCantidades()
                row += 1
        except Exception:
            mensaje = QMessageBox()
            mensaje.setText("La cantidad o el id no es un numero")
            mensaje.exec()
        

    def añadirPedido(self):
        p = {"_id":"", "idProducto":"", "cantidad":""}
        cont = 1
        if GestionarPedidos.pedidos.find():
            for x in GestionarPedidos.pedidos.find():
                cont += 1
        p["_id"] = str(cont)
        p["idProducto"] = self.idMueblePedir.text()
        p["cantidad"] = self.cantidad.text()
        GestionarPedidos.añadirPedido(p)
        self.idPedido.setText(str(cont+1))


    def actDimensiones(self):
        self.dimensionesFinales.setText(self.alturaMueble.text()+
                                        " x "+ self.anchoMueble.text()+
                                        " x "+ self.largoMueble.text())

    def añadir(self):
        try:
            id = int(self.idMueble.text())
            self.mueble["_id"] = self.idMueble.text()
            self.mueble["nombre"] = self.nombreMueble.text()
            try:
                precio = int(self.precioMueble.text())
                self.mueble["precio"] = self.precioMueble.text()
                try:
                    ancho = int(self.anchoMueble.text())
                    largo = int(self.largoMueble.text())
                    alto = int(self.alturaMueble.text())
                    self.mueble["dimensiones"] = self.dimensionesFinales.text()
                    GestionarMuebles.añadirMueble(self.mueble)
                except Exception:
                    mensaje = QMessageBox()
                    mensaje.setText("Algunas de las dimensiones no es un numero")
                    mensaje.exec()
            except Exception:
                mensaje = QMessageBox()
                mensaje.setText("El precio no es nu numero")
                mensaje.exec()
        except Exception:
                mensaje = QMessageBox()
                mensaje.setText("Id no es un numero")
                mensaje.exec()

        self.obtener()
    
    def obtenerCantidades(self):
        row = 0
        if GestionarMuebles.my_collection.find():
            for x in GestionarMuebles.my_collection.find():
                self.Cantidad.setRowCount(row+1)
                idDato = QTableWidgetItem(x["_id"])
                idDato.setTextAlignment(4)

                self.Cantidad.setItem(row, 0, idDato)
                self.Cantidad.setItem(row, 1, QTableWidgetItem(str(x["nombre"])))
                self.Cantidad.setItem(row, 2, QTableWidgetItem(x["cant"]))

                row += 1

    def obtener(self):
        row = 0
        if GestionarMuebles.my_collection.find():
            for x in GestionarMuebles.my_collection.find():
                self.productos.setRowCount(row+1)
                idDato = QTableWidgetItem(x["_id"])
                idDato.setTextAlignment(4)

                self.productos.setItem(row, 0, idDato)
                self.productos.setItem(row, 1, QTableWidgetItem(x["nombre"]))
                self.productos.setItem(row, 2, QTableWidgetItem(x["precio"]))
                self.productos.setItem(row, 3, QTableWidgetItem(x["dimensiones"]))

                row += 1

    def eliminar(self):
        try:
                id = int(self.eId.text())
                self.mueble["_id"] = self.eId.text()
                GestionarMuebles.eliminarMueble(self.mueble)
                if self.productos.rowCount() == 1:
                    self.productos.setRowCount(0)
        except Exception:
                mensaje = QMessageBox()
                mensaje.setText("Id no es un numero")
                mensaje.exec()    
        self.obtener()


    def modificar(self):
        m = {"_id":"","nombre": "", "precio":"", "dimensiones":"", "cant":"0"}
        m["_id"] = self.idMod.text()
        GestionarMuebles.eliminarMueble(m)
        m["nombre"] = self.nomMod.text()
        m["precio"] = self.precioMod.text()
        m["dimensiones"] = self.altMod.text() + " x " + self.anchMod.text() + " x " + self.largMod.text()
        GestionarMuebles.añadirMueble(m)
        self.obtener()



    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()