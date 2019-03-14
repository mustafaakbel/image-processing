import sys
from tkinter import filedialog

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap


class GoruntuIsleme(QDialog):
    def __init__(self):
        super(GoruntuIsleme,self).__init__()
        loadUi('formtasarim.ui',self)
        self.setWindowTitle('Görüntü İşleme')
        self.btYukle.clicked.connect(self.fotoYukle)
        self.btReset.clicked.connect(self.fotoReset)
        self.btKaydet.clicked.connect(self.fotoKaydet)
        self.btNegatif.clicked.connect(self.fotoNegatif)
        self.btGri.clicked.connect(self.fotoGri)
        self.bt90derece.clicked.connect(self.foto90derece)
        self.btTersCevir.clicked.connect(self.fotoTersCevir)
        self.btAynalama.clicked.connect(self.fotoAyanalama)
        self.btOteleme.clicked.connect(self.fotoOteleme)
        self.btYakinlastir.clicked.connect(self.fotoYakinlastir)

    def fotoYukle(self):
        global fname
        global resim
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\',"Image files (*.jpg *.gif)")
        foto = Image.open(fname[0])
        self.fotograg = ImageQt(foto)
        pixMap = QPixmap.fromImage(self.fotograg)
        self.lbMesaj.setPixmap(pixMap)

    def fotoReset(self):
        self.lbMesaj.setPixmap(QPixmap(fname[0]))

    def fotoKaydet(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension='.jpg')
        if f:
            fname[0].save(f)
        f.close()

    def fotoNegatif(self):
        global islenmisfoto
        foto = Image.open(fname[0]).convert('RGB')
        for i in range(foto.size[0]):
            for j in range(foto.size[1]):
                r,g,b=foto.getpixel((i,j))
                foto.putpixel( (i,j), (255-r,255-g,255-b))
        self.fotograg = ImageQt(foto)
        islenmisfoto = self.fotograg
        pixMap = QPixmap.fromImage(self.fotograg)
        self.lbMesaj.setPixmap(pixMap)

    def fotoGri(self):
        foto = Image.open(fname[0]).convert('RGB')
        gri = Image.new('L', (foto.size[0], foto.size[1]))
        for i in range(foto.size[0]):
            for j in range(foto.size[1]):
                r, g, b = foto.getpixel((i,j))
                value = r * 299.0 / 1000 + g * 587.0 / 1000 + b * 114.0 / 1000
                value = int(value)
                gri.putpixel((i,j), value)
        self.fotograg = ImageQt(gri)
        pixMap = QPixmap.fromImage(self.fotograg)
        self.lbMesaj.setPixmap(pixMap)

    def foto90derece(self):
        foto = Image.open(fname[0]).convert('RGB')
        yeni = Image.new('RGB',  (foto.size[1], foto.size[0]))
        for i in range(foto.size[0]):
            for j in range(foto.size[1]):
                r, g, b = foto.getpixel((i,j))
                yeni.putpixel((j,((foto.size[0]-1)-i)), (r, g, b))
        self.fotograg = ImageQt(yeni)
        pixMap = QPixmap.fromImage(self.fotograg)
        self.lbMesaj.setPixmap(pixMap)

    def fotoTersCevir(self):
        foto = Image.open(fname[0]).convert('RGB')
        yeni = Image.new('RGB',  (foto.size[0],foto.size[1]))
        for i in range(foto.size[0]):
            for j in range(foto.size[1]):
                r, g, b = foto.getpixel((i,j))
                yeni.putpixel((i,((foto.size[1]-1)-j)), (r, g, b))
        self.fotograg = ImageQt(yeni)
        pixMap = QPixmap.fromImage(self.fotograg)
        self.lbMesaj.setPixmap(pixMap)

    def fotoAyanalama(self):
        foto = Image.open(fname[0]).convert('RGB')
        yeni = Image.new('RGB',  (foto.size[0],foto.size[1]))
        for i in range(foto.size[0]):
            for j in range(foto.size[1]):
                r, g, b = foto.getpixel((((foto.size[0]-1)-i),j))
                yeni.putpixel((i,j),(r, g, b))
        self.fotograg = ImageQt(yeni)
        pixMap = QPixmap.fromImage(self.fotograg)
        self.lbMesaj.setPixmap(pixMap)

    def fotoOteleme(self):
        foto = Image.open(fname[0]).convert('RGB')
        yeni = Image.new('RGB',  (foto.size[0],foto.size[1]))
        for i in range(0,(foto.size[0])):
            for j in range(0,(foto.size[1])):
                if i<100 or j<100:
                    yeni.putpixel((i, j), (0, 0, 0))
                else:
                    r, g, b = foto.getpixel((i-100,j-100))
                    yeni.putpixel((i, j), (r, g, b))
        self.fotograg = ImageQt(yeni)
        pixMap = QPixmap.fromImage(self.fotograg)
        self.lbMesaj.setPixmap(pixMap)

    def fotoYakinlastir(self):
        foto = Image.open(fname[0]).convert('RGB')
        yeni = Image.new('RGB',  (foto.size[0]*1.1,foto.size[1]))
        for i in range(0,(foto.size[0])):
            for j in range(0,(foto.size[1])):
                r,g,b = foto.getpixel((i,j))
                yeni.putpixel((i, j), (r, g, b))
        self.fotograg = ImageQt(yeni)
        pixMap = QPixmap.fromImage(self.fotograg)
        self.lbMesaj.setPixmap(pixMap)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget= GoruntuIsleme()
    widget.show()
    sys.exit(app.exec_())