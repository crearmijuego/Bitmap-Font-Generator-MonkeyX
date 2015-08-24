
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanabitmap.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PIL import Image,ImageDraw,ImageFont
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(326, 137)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 51, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEditSeparacion = QtGui.QLineEdit(self.centralwidget)
        self.lineEditSeparacion.setGeometry(QtCore.QRect(90, 10, 71, 25))
        self.lineEditSeparacion.setObjectName(_fromUtf8("lineEditSeparacion"))
        self.lineEditTamano = QtGui.QLineEdit(self.centralwidget)
        self.lineEditTamano.setGeometry(QtCore.QRect(90, 40, 71, 25))
        self.lineEditTamano.setObjectName(_fromUtf8("lineEditTamano"))
        self.pushButtonAbrir = QtGui.QPushButton(self.centralwidget)
        self.pushButtonAbrir.setGeometry(QtCore.QRect(20, 100, 85, 27))
        self.pushButtonAbrir.setObjectName(_fromUtf8("pushButtonAbrir"))
        self.pushButtonGenerar = QtGui.QPushButton(self.centralwidget)
        self.pushButtonGenerar.setGeometry(QtCore.QRect(200, 100, 101, 27))
        self.pushButtonGenerar.setObjectName(_fromUtf8("pushButtonGenerar"))
        self.pushButtonPrevisualizar = QtGui.QPushButton(self.centralwidget)
        self.pushButtonPrevisualizar.setGeometry(QtCore.QRect(110, 100, 85, 27))
        self.pushButtonPrevisualizar.setObjectName(_fromUtf8("pushButtonPrevisualizar"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 10, 101, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 30, 101, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 50, 131, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 221, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.lineEditSeparacion.setText("32")
        self.lineEditTamano.setText("32")
        caracts = [' ','!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~',' ']

        self.rutafont = ""





        def previsualizar():
            widthcell=int(self.lineEditSeparacion.text())
            fontsize =int(self.lineEditTamano.text())
            font = ImageFont.truetype(self.rutafont, fontsize)

            img2 = Image.new("RGBA",(8*widthcell,150),(0,0,0,0))
            draw2 = ImageDraw.Draw(img2)

            posicion=widthcell/2
            posicionsumar=widthcell

            mayor = 1
            count =0
            for caract in caracts:
                count +=1
                w, h = draw2.textsize(caract,font=font)
                if h> mayor:
                    mayor=h
                if count==96:
                    countpreview =0
                    posicionpreview = widthcell/2
                    heigthcell=int(mayor+(mayor/2))
                    heightcaracter = mayor
                    self.img = Image.new("RGBA",(len(caracts)*widthcell,heigthcell),(255,255,255,0))
                    draw = ImageDraw.Draw(self.img)
                    for caract in caracts:
                        countpreview +=1
                        w, h = draw.textsize(caract,font=font)
                        draw.text((posicion-(w/2),(heigthcell/2)-(heightcaracter/2)),caract,font=font);
                        posicion +=posicionsumar
                        if countpreview>=17 and countpreview<=20 or countpreview>=34 and countpreview<=37:
                            draw2.text((posicionpreview-(w/2),(heigthcell/2)-(heightcaracter/2)),caract,font=font);
                            posicionpreview +=posicionsumar

            img2.show()

        def mensaje():
            msg = QtGui.QMessageBox.information(None,
                    "Exito", 'Se guardo el Bitmap font : font.png')

        def generar():
            self.img.save("font.png","PNG");
            mensaje()

        def abrir():
            filename = QtGui.QFileDialog.getOpenFileName(None, 'Abrir Font', '/',"Font *.ttf, *.otf (*.ttf *.otf)")
            if filename:
                fileInfo = QtCore.QFileInfo(filename)
                nameinfo = str(fileInfo.fileName())
                self.label_6.setText(nameinfo)
                self.rutafont = filename

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButtonGenerar, QtCore.SIGNAL(_fromUtf8("clicked()")), generar)
        QtCore.QObject.connect(self.pushButtonPrevisualizar, QtCore.SIGNAL(_fromUtf8("clicked()")), previsualizar)
        QtCore.QObject.connect(self.pushButtonAbrir, QtCore.SIGNAL(_fromUtf8("clicked()")), abrir)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "BitmapFont MonkeyX Beta - Crearmijuego", None))
        self.label.setText(_translate("MainWindow", "Separacion", None))
        self.label_2.setText(_translate("MainWindow", "Tamaño", None))
        self.pushButtonAbrir.setText(_translate("MainWindow", "Abrir Fuente", None))
        self.pushButtonGenerar.setText(_translate("MainWindow", "Guardar", None))
        self.pushButtonPrevisualizar.setText(_translate("MainWindow", "Generar y Ver", None))
        self.label_3.setText(_translate("MainWindow", "Desarrollado por: ", None))
        self.label_4.setText(_translate("MainWindow", "Luis Francisco", None))
        self.label_5.setText(_translate("MainWindow", "Twitter:  @crearmijuego", None))
        self.label_6.setText(_translate("MainWindow", "Fuente", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())