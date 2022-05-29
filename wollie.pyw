import sys, os
from os import listdir, walk
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import * # QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from wollie_design import * # импорт файла с интерфейсом галереи 
from start_widget import  * # импорт файла с GUI
from wollieresult_design import *
from info_design import *
from PIL import Image, ExifTags #pip install pillow
from PIL.ExifTags import TAGS
import exifread
import pandas as pd

#для карты
import sys
import io
import folium  # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView # pip install PyQtWebEngine

class StartWindow(QtWidgets.QMainWindow):

    def __init__(self):
        #super - возможность использования в классе потомке, методов класса-родителя
        super(StartWindow, self).__init__()
        self.ui = Ui_start_window()
        self.ui.setupUi(self)
        self.show()
        self.ui.start_button.clicked.connect(self.start_button_clicked)
        self.ui.result_button.clicked.connect(self.result_button_clicked)

    def start_button_clicked(self):
        curr_path = QtCore.QDir.currentPath() #+ "/images"
        main_image_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Выбрать фото", curr_path ,"*.bmp *.png *.gif *.tiff *.jpg *.jpeg *.JPG")
        if main_image_path:
            window = wollie(main_image_path, self)
            window.setGeometry(QtWidgets.QStyle.alignedRect(QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter, window.size(), self.geometry()))
            window.show()

    def result_button_clicked(self):
        curr_path = QtCore.QDir.currentPath() #+ "/images"
        main_image_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Выбрать папку с результатами", curr_path ,"*.bmp *.png *.gif *.tiff *.jpg *.jpeg *.JPG")
        if main_image_path:
            window = wollieresult(main_image_path, self)
            window.setGeometry(QtWidgets.QStyle.alignedRect(QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter, window.size(), self.geometry()))
            window.show()


class wollie(QtWidgets.QWidget):
    def __init__(self, main_image_path, parent = StartWindow):
        super().__init__(parent, QtCore.Qt.Window)
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self)
        self.ui2.main_image.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.pixmap = QPixmap(main_image_path) #оригинальная версия главной картинки, нужна для сброса и обновления
        self.image_scale = QImage(main_image_path) #версия картинки с увеличением
        self.image = QImage( main_image_path) #оригинальная картинка
        self.pixmap_zoom = QPixmap(self.image) #для отрисовки увеличенной картинки 
        self.ui2.main_image.setAlignment(Qt.AlignCenter)
        self.ui2.main_image.installEventFilter(self)
        self.setWindowModality(2) #начальное окно станет неактивным, пока запущена галерея

        # просмотр файлов каталоге и добавление превью в виджет
        self.directory = main_image_path[:main_image_path.rfind("/")] #дирректория, в которой открыли картинку
        main_image_name = main_image_path[main_image_path.rfind("/")+1:]
    
        self.list_files = listdir(self.directory) #все файлы в папке
        #удаление не картинок из списка
        self.list_files=[x for x in self.list_files if any([x.endswith(y) for y in ('bmp', 'png', 'gif', 'tiff', 'jpg', 'jpeg', 'JPG')])]

        self.number_main_im = self.list_files.index(main_image_name)
        self.number_mini_im_1 = (self.number_main_im - 2) % len(self.list_files) #нужен для реализиции стрелок превью

        #насройка превью
        if len(self.list_files) >= 5:
            self.pixmap_mini1 = (QtGui.QPixmap(self.directory + "/" + self.list_files[self.number_main_im-2]))
            self.ui2.mini_image_1.setScaledContents(True)
        if len(self.list_files) >= 3:
            self.pixmap_mini2 = (QtGui.QPixmap(self.directory + "/" + self.list_files[self.number_main_im-1]))
            self.ui2.mini_image_2.setScaledContents(True)
        self.pixmap_mini3 = (QtGui.QPixmap(self.directory + "/" + self.list_files[self.number_main_im]))
        self.ui2.mini_image_3.setScaledContents(True)
        if len(self.list_files) >= 2:
            self.pixmap_mini4 = (QtGui.QPixmap(self.directory + "/" + self.list_files[(self.number_main_im+1) % len(self.list_files)]))
            self.ui2.mini_image_4.setScaledContents(True)
        if len(self.list_files) >= 4:
            self.pixmap_mini5 = (QtGui.QPixmap(self.directory + "/" + self.list_files[(self.number_main_im+2) % len(self.list_files)]))
            self.ui2.mini_image_5.setScaledContents(True)
        
        self.set_mini_pixmap()

        #кнопки
        self.ui2.main_right_arrow.clicked.connect(self.main_right_arrow_clicked)
        self.ui2.main_left_arrow.clicked.connect(self.main_left_arrow_clicked)
        self.ui2.mini_right_arrow.clicked.connect(self.mini_right_arrow_clicked)
        self.ui2.mini_left_arrow.clicked.connect(self.mini_left_arrow_clicked)
        self.ui2.info_button.clicked.connect(self.info_clicked)
        self.ui2.map_button.clicked.connect(self.map_clicked)
        self.ui2.all_button.clicked.connect(self.allmap_clicked)
        self.ui2.count_button.clicked.connect(self.count_clicked)
        self.ui2.allcount_button.clicked.connect(self.allcount_clicked)
        self.ui2.result_button.clicked.connect(self.result_clicked)

        self.zoom = 1 #текущий зум     
        self.position = [0, 0] #левый верхний угол картинки

        self.Events()


    def update_zoom(self):
        #для перерисовки изображения с зумом
        if not self.image_scale.isNull():
            x, y = self.position
            x = x if (x <= self.image_scale.width() - self.ui2.main_image.width()) \
                else (self.image_scale.width() - self.ui2.main_image.width())
            y = y if (y <= self.image_scale.height() - self.ui2.main_image.height()) \
                else (self.image_scale.height() - self.ui2.main_image.height())
            x = x if (x >= 0) else 0
            y = y if (y >= 0) else 0
            self.position = (x, y)

            self.pixmap_zoom = QPixmap(self.ui2.main_image.size())
            self.pixmap_zoom.fill(QtCore.Qt.white) 
            # рисование pixmap с зумом
            painter = QPainter()
            painter.begin(self.pixmap_zoom)
            painter.drawImage(QtCore.QPoint(0, 0), self.image_scale,
                    QtCore.QRect(int(self.position[0]), int(self.position[1]), int(self.ui2.main_image.width()),\
                    int(self.ui2.main_image.height())) )
            painter.end()
            self.ui2.main_image.setPixmap(self.pixmap_zoom)
        else:
            pass

    def Events(self):
        # События мыши
        self.ui2.main_image.mousePressEvent = self.mousePressAction
        self.ui2.main_image.mouseMoveEvent = self.mouseMoveAction
        self.ui2.main_image.mouseReleaseEvent = self.mouseReleaseAction
        self.ui2.plus_zoom.clicked.connect(self.zoom_plus)
        self.ui2.min_zoom.clicked.connect(self.zoom_minus)
        self.ui2.reset_button.clicked.connect(self.reset_zoom)
        self.ui2.main_image.mouseDoubleClickEvent = self.mouse_zoom

    def mousePressAction(self, QMouseEvent):        
        x, y = QMouseEvent.pos().x(), QMouseEvent.pos().y()
        self.pressed = QMouseEvent.pos() # координаты мыши
        self.old = self.position         

    def mouseMoveAction(self, QMouseEvent):
        if self.zoom > 1:
            self.pixmap_zoom = QPixmap(self.ui2.main_image.size())
            self.pixmap_zoom.fill(QtCore.Qt.white)   
            x, y = QMouseEvent.pos().x(), QMouseEvent.pos().y()
            if self.pressed:
                dx, dy = x - self.pressed.x(), y - self.pressed.y() # вычисление перемещения картинки с зумом
                self.position = self.old[0] - dx, self.old[1] - dy 
                self.update_zoom()

    def mouseReleaseAction(self, QMouseEvent):
        self.pressed = None

    def mouse_zoom(self, QMouseEvent):
        self.zoom += 1
        if self.zoom == 2:
            x, y = QMouseEvent.pos().x(),QMouseEvent.pos().y()
            self.position = (x, y)
        else:
            x, y = self.position
            x += QMouseEvent.pos().x()
            y += QMouseEvent.pos().y()
            self.position = (x, y)
        self.image_scale = self.image.scaled(self.ui2.main_image.width() * self.zoom, self.ui2.main_image.height() * self.zoom, QtCore.Qt.KeepAspectRatio)
        self.update_zoom()

    def zoom_plus(self):    
        self.zoom += 1
        x, y = self.position
        x += self.ui2.main_image.width()/2
        y += self.ui2.main_image.height()/2
        self.position = (x, y)
        self.image_scale = self.image.scaled(self.ui2.main_image.width() * self.zoom, self.ui2.main_image.height() * self.zoom, QtCore.Qt.KeepAspectRatio)
        self.update_zoom()

    def zoom_minus(self):
        if self.zoom > 1:
            self.zoom -= 1
            x, y = self.position
            x -= self.ui2.main_image.width()/2
            y -= self.ui2.main_image.height()/2
            self.position = (x, y)
            if self.zoom == 1:
                self.position = [0,0]
                self.ui2.main_image.setPixmap(self.pixmap.scaled( \
                self.ui2.main_image.width(), self.ui2.main_image.height(), QtCore.Qt.KeepAspectRatio))
                self.image_scale = self.ui2.main_image
            else:
                self.image_scale = self.image.scaled(self.ui2.main_image.width() * self.zoom, \
                    self.ui2.main_image.height() * self.zoom, QtCore.Qt.KeepAspectRatio)
                self.update_zoom()

    def reset_zoom(self):
        self.zoom = 1
        self.position = [0, 0]
        self.ui2.main_image.setPixmap(self.pixmap.scaled( 
                self.ui2.main_image.width(), self.ui2.main_image.height(), QtCore.Qt.KeepAspectRatio))

    def keyPressEvent(self, eventQKeyEvent):
        key = eventQKeyEvent.key() #проверка, какая кнопка нажата
        #W = 87 - вверх; A = 65 - влево; S = 83 - вниз; D = 68 - вправо
        self.old = self.position
        if self.zoom > 1:
            dx, dy = self.ui2.main_image.width()/2, self.ui2.main_image.height()/2
            if key == 87 or key == 1062:
                self.position = self.old[0], self.old[1] - dy
            elif key == 83 or key == 1067:
                self.position = self.old[0], self.old[1] + dy
            elif key == 65 or key == 1060:
                self.position = self.old[0] - dx, self.old[1]
            elif key == 68 or key == 1042:
                self.position = self.old[0] + dx, self.old[1] 
            self.update_zoom()

    def eventFilter(self, source, event): 
        #функция для перирисовки изображения при смене размера виджета с сохранением пропорций
        if (event.type() == QtCore.QEvent.Resize):
            self.zoom = 1
            if (source is self.ui2.main_image):
                self.ui2.main_image.setPixmap(self.pixmap.scaled( 
                    self.ui2.main_image.width(), self.ui2.main_image.height(), QtCore.Qt.KeepAspectRatio))
        return super(wollie, self).eventFilter(source, event)

    def main_right_arrow_clicked(self):
        self.zoom = 1
        self.position = [0, 0]
        self.number_main_im += 1 #перенос номера главного изображения
        self.number_main_im %= len(self.list_files)
        self.number_mini_im_1 = (self.number_main_im - 2) % len(self.list_files) #перенос номера первого изображения превью
        number_main_im, list_files, directory,list_files = self.number_main_im, self.list_files, self.directory, self.list_files

        self.pixmap = (QtGui.QPixmap(directory + "/" + list_files[number_main_im]))
        self.pixmap_zoom = self.pixmap
        self.image = QImage(self.directory + "/" + self.list_files[self.number_main_im])
        if len(list_files) >= 5:
            self.pixmap_mini1 = (QtGui.QPixmap(directory + "/" + list_files[number_main_im-2]))
        if len(list_files) >= 3:
            self.pixmap_mini2 = (QtGui.QPixmap(directory + "/" + list_files[number_main_im-1]))
        self.pixmap_mini3 = (QtGui.QPixmap(directory + "/" + list_files[number_main_im]))
        if len(list_files) >= 2:
            self.pixmap_mini4 = (QtGui.QPixmap(directory + "/" + list_files[(number_main_im+1) % len(list_files)]))
        if len(list_files) >= 4:
            self.pixmap_mini5 = (QtGui.QPixmap(directory + "/" + list_files[(number_main_im+2) % len(list_files)]))

        self.ui2.main_image.setPixmap(self.pixmap_zoom.scaled( 
                    self.ui2.main_image.size(), QtCore.Qt.KeepAspectRatio))
        self.image_scale = self.ui2.main_image
        self.set_mini_pixmap() 

        #закрывает окно с информацией при переключении картинки
        if hasattr(self,'info_window'): 
            self.info_window.close()       

    def main_left_arrow_clicked(self):
        self.zoom = 1
        self.position = [0, 0]
        self.number_main_im -= 1 #перенос номера главного изображения
        self.number_mini_im_1 = (self.number_main_im - 2) % len(self.list_files) #перенос номера первого изображения превью

        if self.number_main_im == -1:
            self.number_main_im = len(self.list_files)-1
        number_main_im, list_files, directory,list_files = self.number_main_im, self.list_files, self.directory, self.list_files

        self.pixmap = (QtGui.QPixmap(directory + "/" + list_files[number_main_im]))
        self.pixmap_zoom = self.pixmap
        self.image = QImage(self.directory + "/" + self.list_files[self.number_main_im])
        if len(self.list_files) >= 5:
            self.pixmap_mini1 = (QtGui.QPixmap(directory + "/" + list_files[number_main_im-2]))
        if len(self.list_files) >= 3:
            self.pixmap_mini2 = (QtGui.QPixmap(directory + "/" + list_files[number_main_im-1]))
        self.pixmap_mini3 = (QtGui.QPixmap(directory + "/" + list_files[number_main_im]))
        if len(self.list_files) >= 2:
            self.pixmap_mini4 = (QtGui.QPixmap(directory + "/" + list_files[(number_main_im+1) % len(list_files)]))
        if len(self.list_files) >= 4:
            self.pixmap_mini5 = (QtGui.QPixmap(directory + "/" + list_files[(number_main_im+2) % len(list_files)]))
        
        self.ui2.main_image.setPixmap(self.pixmap_zoom.scaled( 
            self.ui2.main_image.size(), QtCore.Qt.KeepAspectRatio))
        self.set_mini_pixmap()

        #закрывает окно с информацией при переключении картинки
        if hasattr(self,'info_window'):
            self.info_window.close()

    def mini_right_arrow_clicked(self):
        i, list_files, directory,list_files = self.number_mini_im_1, self.list_files, self.directory, self.list_files
        self.number_mini_im_1 = (self.number_mini_im_1 + 1) % len(list_files) #перенос номера первого изображения превью

        self.pixmap_mini1 = (QtGui.QPixmap(directory + "/" + list_files[(i+1) % len(list_files)]))
        self.pixmap_mini2 = (QtGui.QPixmap(directory + "/" + list_files[(i+2) % len(list_files)]))
        self.pixmap_mini3 = (QtGui.QPixmap(directory + "/" + list_files[(i+3) % len(list_files)]))
        self.pixmap_mini4 = (QtGui.QPixmap(directory + "/" + list_files[(i+4) % len(list_files)]))
        self.pixmap_mini5 = (QtGui.QPixmap(directory + "/" + list_files[(i+5) % len(list_files)]))
        self.set_mini_pixmap()
        
    def mini_left_arrow_clicked(self):
        i, list_files, directory,list_files = self.number_mini_im_1, self.list_files, self.directory, self.list_files
        self.number_mini_im_1 = (self.number_mini_im_1 - 1) % len(list_files) #перенос номера первого изображения превью

        self.pixmap_mini1 = (QtGui.QPixmap(directory + "/" + list_files[(i-1) % len(list_files)]))
        self.pixmap_mini2 = (QtGui.QPixmap(directory + "/" + list_files[(i) % len(list_files)]))
        self.pixmap_mini3 = (QtGui.QPixmap(directory + "/" + list_files[(i+1) % len(list_files)]))
        self.pixmap_mini4 = (QtGui.QPixmap(directory + "/" + list_files[(i+2) % len(list_files)]))
        self.pixmap_mini5 = (QtGui.QPixmap(directory + "/" + list_files[(i+3) % len(list_files)]))
        self.set_mini_pixmap()

    def set_mini_pixmap(self):
        #функция установки изображений в превью
        if len(self.list_files) >= 5:
            self.ui2.mini_image_1.setPixmap(self.pixmap_mini1)
        if len(self.list_files) >= 3:    
            self.ui2.mini_image_2.setPixmap(self.pixmap_mini2)
        self.ui2.mini_image_3.setPixmap(self.pixmap_mini3)
        if len(self.list_files) >= 2:
            self.ui2.mini_image_4.setPixmap(self.pixmap_mini4)
        if len(self.list_files) >= 4:
            self.ui2.mini_image_5.setPixmap(self.pixmap_mini5)

    def info_clicked(self):
        if hasattr(self,'info_window'): #проверка что такое же окно ещё не запущено
            self.info_window.close()
        image_path = self.directory + "/" + self.list_files[self.number_main_im]
        self.info_window = info(image_path, self)
        self.info_window.setGeometry(QtWidgets.QStyle.alignedRect(QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter, self.info_window.size(), self.geometry()))
        self.info_window.show()

    def map_clicked(self):
        image_path = self.directory + "/" + self.list_files[self.number_main_im]
        self.image_path = image_path
        #image = Image.open(self.image_path)
        image_name = image_path[image_path.rfind("/")+1:] #имя
        # возращет Exif теги
        f = open(image_path, 'rb')
        tags = exifread.process_file(f)
        lat = 0
        lon = 0 
        if "GPS GPSLatitude" in tags and "GPS GPSLongitude" in tags:
            gps = str(tags["GPS GPSLatitude"])[1:len(str(tags["GPS GPSLatitude"]))-1].split(',')
            for i in range(len(gps)):
                gps[i] = gps[i].strip()
                if i == 2:
                    gps[i] = float(gps[i].split('/')[0])/float(gps[i].split('/')[1])
                else:
                    gps[i] = float(gps[i])
            lat = (gps[2]/60 + gps[1])/60 + gps[0]
            
            gps = str(tags["GPS GPSLongitude"])[1:len(str(tags["GPS GPSLongitude"]))-1].split(',')
            for i in range(len(gps)):
                gps[i] = gps[i].strip()
                if i == 2:
                    gps[i] = float(gps[i].split('/')[0])/float(gps[i].split('/')[1])
                else:
                    gps[i] = float(gps[i])
            lon = (gps[2]/60 + gps[1])/60 + gps[0]
        #print(lat,lon)
            self.myApp = MyApp([[lat,lon, image_name]], self)
            self.myApp.show()

    def allmap_clicked(self):
        coords=[]
        
        for images in self.list_files:
            image_path = self.directory + "/" + images
            self.image_path = image_path
            #image = Image.open(self.image_path)
            image_name = image_path[image_path.rfind("/")+1:] #имя
            # возвращет Exif теги
            f = open(image_path, 'rb')
            tags = exifread.process_file(f)
            lat = 0
            lon = 0 

            if "GPS GPSLatitude" in tags and "GPS GPSLongitude" in tags:
                gps = str(tags["GPS GPSLatitude"])[1:len(str(tags["GPS GPSLatitude"]))-1].split(',')
                for i in range(len(gps)):
                    gps[i] = gps[i].strip()
                    if i == 2:
                        gps[i] = float(gps[i].split('/')[0])/float(gps[i].split('/')[1])
                    else:
                        gps[i] = float(gps[i])
                lat = (gps[2]/60 + gps[1])/60 + gps[0]
            
                gps = str(tags["GPS GPSLongitude"])[1:len(str(tags["GPS GPSLongitude"]))-1].split(',')
                for i in range(len(gps)):
                    gps[i] = gps[i].strip()
                    if i == 2:
                        gps[i] = float(gps[i].split('/')[0])/float(gps[i].split('/')[1])
                    else:
                        gps[i] = float(gps[i])
                lon = (gps[2]/60 + gps[1])/60 + gps[0]
                #print(lat,lon)
                coords.append([lat,lon, image_name])
        self.myApp = MyApp(coords, self)
        self.myApp.show()


    def count_clicked(self,):
        folder = os.path.dirname(os.path.abspath(__file__)) + "/results/"
        if not os.path.isdir(folder):
            os.mkdir(folder)

        image_path = self.directory + "/" + self.list_files[self.number_main_im]
        self.image_path = image_path
        #image = Image.open(self.image_path)
        image_name = image_path[image_path.rfind("/")+1:] #имя

        f = open(image_path, 'rb')

        #вызов нейросети
        #получение количества моржей и сохранение новой фотографии 
        count = 123

        tags = exifread.process_file(f)

        lat = -1
        lon = -1
        date,time = -1,-1

        if "GPS GPSLatitude" in tags and "GPS GPSLongitude" in tags:
            gps = str(tags["GPS GPSLatitude"])[1:len(str(tags["GPS GPSLatitude"]))-1].split(',')
            for i in range(len(gps)):
                gps[i] = gps[i].strip()
                if i == 2:
                    gps[i] = float(gps[i].split('/')[0])/float(gps[i].split('/')[1])
                else:
                    gps[i] = float(gps[i])
            lat = (gps[2]/60 + gps[1])/60 + gps[0]
        
            gps = str(tags["GPS GPSLongitude"])[1:len(str(tags["GPS GPSLongitude"]))-1].split(',')
            for i in range(len(gps)):
                gps[i] = gps[i].strip()
                if i == 2:
                    gps[i] = float(gps[i].split('/')[0])/float(gps[i].split('/')[1])
                else:
                    gps[i] = float(gps[i])
            lon = (gps[2]/60 + gps[1])/60 + gps[0]

        dataTime = ['01.01.1000','00:00:00']
        if "Image DateTime" in tags:
            dataTime = str(tags["Image DateTime"]).split(' ')
            dataTime[0]=dataTime[0].replace(':','.')
        
        file = open(folder+'results.txt','a+')
        tmp = image_name + ";" + str(dataTime[0]) + ";" + str(dataTime[1]) + ";" + str(lat) + ";" + str(lon) + ";" + str(count) + "\n" 
        file.write(tmp)
        file.close()
        self.ui2.label.setText("Всего: " + str(count));



    def allcount_clicked(self):
        folder = os.path.dirname(os.path.abspath(__file__)) + "/results/"
        if not os.path.isdir(folder):
            os.mkdir(folder)

        for images in self.list_files:
            image_path = self.directory + "/" + images


            self.image_path = image_path
            #image = Image.open(self.image_path)
            image_name = image_path[image_path.rfind("/")+1:] #имя

            f = open(image_path, 'rb')

            #вызов нейросети
            #получение количества моржей и сохранение новой фотографии 
            count = 123

            tags = exifread.process_file(f)

            lat = -1
            lon = -1
            date,time = -1,-1

            if "GPS GPSLatitude" in tags and "GPS GPSLongitude" in tags:
                gps = str(tags["GPS GPSLatitude"])[1:len(str(tags["GPS GPSLatitude"]))-1].split(',')
                for i in range(len(gps)):
                    gps[i] = gps[i].strip()
                    if i == 2:
                        gps[i] = float(gps[i].split('/')[0])/float(gps[i].split('/')[1])
                    else:
                        gps[i] = float(gps[i])
                lat = (gps[2]/60 + gps[1])/60 + gps[0]
            
                gps = str(tags["GPS GPSLongitude"])[1:len(str(tags["GPS GPSLongitude"]))-1].split(',')
                for i in range(len(gps)):
                    gps[i] = gps[i].strip()
                    if i == 2:
                        gps[i] = float(gps[i].split('/')[0])/float(gps[i].split('/')[1])
                    else:
                        gps[i] = float(gps[i])
                lon = (gps[2]/60 + gps[1])/60 + gps[0]

            dataTime = ['01.01.1000','00:00:00']
            if "Image DateTime" in tags:
                dataTime = str(tags["Image DateTime"]).split(' ')
                dataTime[0]=dataTime[0].replace(':','.')
        
            file = open(folder+'results.txt','a+')
            tmp = image_name + ";" + str(dataTime[0]) + ";" + str(dataTime[1]) + ";" + str(lat) + ";" + str(lon) + ";" + str(count) + "\n" 
            file.write(tmp)
            file.close()

    def result_clicked(self):
        curr_path = QtCore.QDir.currentPath() #+ "/images"
        main_image_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Выбрать папку с результатами", curr_path ,"*.bmp *.png *.gif *.tiff *.jpg *.jpeg *.JPG")
        if main_image_path:
            window = wollieresult(main_image_path, self)
            window.setGeometry(QtWidgets.QStyle.alignedRect(QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter, window.size(), self.geometry()))
            window.show()



class wollieresult(QtWidgets.QWidget):
    def __init__(self, main_image_path, parent = wollie):
        super().__init__(parent, QtCore.Qt.Window)
        self.ui2 = Ui_Results()
        self.ui2.setupUi(self)
        self.ui2.main_image.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.pixmap = QPixmap(main_image_path) #оригинальная версия главной картинки, нужна для сброса и обновления
        self.image_scale = QImage(main_image_path) #версия картинки с увеличением
        self.image = QImage( main_image_path) #оригинальная картинка
        self.pixmap_zoom = QPixmap(self.image) #для отрисовки увеличенной картинки 
        self.ui2.main_image.setAlignment(Qt.AlignCenter)
        self.ui2.main_image.installEventFilter(self)
        self.setWindowModality(2) #начальное окно станет неактивным, пока запущена галерея

        # просмотр файлов каталоге и добавление превью в виджет
        self.directory = main_image_path[:main_image_path.rfind("/")] #дирректория, в которой открыли картинку
        main_image_name = main_image_path[main_image_path.rfind("/")+1:]
    
        self.list_files = listdir(self.directory) #все файлы в папке
        #удаление не картинок из списка
        self.list_files=[x for x in self.list_files if any([x.endswith(y) for y in ('bmp', 'png', 'gif', 'tiff', 'jpg', 'jpeg', 'JPG')])]

        self.number_main_im = self.list_files.index(main_image_name)
        self.number_mini_im_1 = (self.number_main_im - 2) % len(self.list_files) #нужен для реализиции стрелок превью

        #насройка превью
        if len(self.list_files) >= 5:
            self.pixmap_mini1 = (QtGui.QPixmap(self.directory + "/" + self.list_files[self.number_main_im-2]))
            self.ui2.mini_image_1.setScaledContents(True)
        if len(self.list_files) >= 3:
            self.pixmap_mini2 = (QtGui.QPixmap(self.directory + "/" + self.list_files[self.number_main_im-1]))
            self.ui2.mini_image_2.setScaledContents(True)
        self.pixmap_mini3 = (QtGui.QPixmap(self.directory + "/" + self.list_files[self.number_main_im]))
        self.ui2.mini_image_3.setScaledContents(True)
        if len(self.list_files) >= 2:
            self.pixmap_mini4 = (QtGui.QPixmap(self.directory + "/" + self.list_files[(self.number_main_im+1) % len(self.list_files)]))
            self.ui2.mini_image_4.setScaledContents(True)
        if len(self.list_files) >= 4:
            self.pixmap_mini5 = (QtGui.QPixmap(self.directory + "/" + self.list_files[(self.number_main_im+2) % len(self.list_files)]))
            self.ui2.mini_image_5.setScaledContents(True)
        
        self.set_mini_pixmap()

        #кнопки
        self.ui2.main_right_arrow.clicked.connect(self.main_right_arrow_clicked)
        self.ui2.main_left_arrow.clicked.connect(self.main_left_arrow_clicked)
        self.ui2.mini_right_arrow.clicked.connect(self.mini_right_arrow_clicked)
        self.ui2.mini_left_arrow.clicked.connect(self.mini_left_arrow_clicked)
        self.ui2.info_button.clicked.connect(self.info_clicked)
        self.ui2.map_button.clicked.connect(self.map_clicked)
        self.ui2.all_button.clicked.connect(self.allmap_clicked)
        self.ui2.excel_button.clicked.connect(self.excel_clicked)

        self.zoom = 1 #текущий зум     
        self.position = [0, 0] #левый верхний угол картинки

        self.Events()


    def update_zoom(self):
        #для перерисовки изображения с зумом
        if not self.image_scale.isNull():
            x, y = self.position
            x = x if (x <= self.image_scale.width() - self.ui2.main_image.width()) \
                else (self.image_scale.width() - self.ui2.main_image.width())
            y = y if (y <= self.image_scale.height() - self.ui2.main_image.height()) \
                else (self.image_scale.height() - self.ui2.main_image.height())
            x = x if (x >= 0) else 0
            y = y if (y >= 0) else 0
            self.position = (x, y)

            self.pixmap_zoom = QPixmap(self.ui2.main_image.size())
            self.pixmap_zoom.fill(QtCore.Qt.white) 
            # рисование pixmap с зумом
            painter = QPainter()
            painter.begin(self.pixmap_zoom)
            painter.drawImage(QtCore.QPoint(0, 0), self.image_scale,
                    QtCore.QRect(int(self.position[0]), int(self.position[1]), int(self.ui2.main_image.width()),\
                    int(self.ui2.main_image.height())) )
            painter.end()
            self.ui2.main_image.setPixmap(self.pixmap_zoom)
        else:
            pass

    def Events(self):
        # События мыши
        self.ui2.main_image.mousePressEvent = self.mousePressAction
        self.ui2.main_image.mouseMoveEvent = self.mouseMoveAction
        self.ui2.main_image.mouseReleaseEvent = self.mouseReleaseAction
        self.ui2.plus_zoom.clicked.connect(self.zoom_plus)
        self.ui2.min_zoom.clicked.connect(self.zoom_minus)
        self.ui2.reset_button.clicked.connect(self.reset_zoom)
        self.ui2.main_image.mouseDoubleClickEvent = self.mouse_zoom

    def mousePressAction(self, QMouseEvent):        
        x, y = QMouseEvent.pos().x(), QMouseEvent.pos().y()
        self.pressed = QMouseEvent.pos() # координаты мыши
        self.old = self.position         

    def mouseMoveAction(self, QMouseEvent):
        if self.zoom > 1:
            self.pixmap_zoom = QPixmap(self.ui2.main_image.size())
            self.pixmap_zoom.fill(QtCore.Qt.white)   
            x, y = QMouseEvent.pos().x(), QMouseEvent.pos().y()
            if self.pressed:
                dx, dy = x - self.pressed.x(), y - self.pressed.y() # вычисление перемещения картинки с зумом
                self.position = self.old[0] - dx, self.old[1] - dy 
                self.update_zoom()

    def mouseReleaseAction(self, QMouseEvent):
        self.pressed = None

    def mouse_zoom(self, QMouseEvent):
        self.zoom += 1
        if self.zoom == 2:
            x, y = QMouseEvent.pos().x(),QMouseEvent.pos().y()
            self.position = (x, y)
        else:
            x, y = self.position
            x += QMouseEvent.pos().x()
            y += QMouseEvent.pos().y()
            self.position = (x, y)
        self.image_scale = self.image.scaled(self.ui2.main_image.width() * self.zoom, self.ui2.main_image.height() * self.zoom, QtCore.Qt.KeepAspectRatio)
        self.update_zoom()

    def zoom_plus(self):    
        self.zoom += 1
        x, y = self.position
        x += self.ui2.main_image.width()/2
        y += self.ui2.main_image.height()/2
        self.position = (x, y)
        self.image_scale = self.image.scaled(self.ui2.main_image.width() * self.zoom, self.ui2.main_image.height() * self.zoom, QtCore.Qt.KeepAspectRatio)
        self.update_zoom()

    def zoom_minus(self):
        if self.zoom > 1:
            self.zoom -= 1
            x, y = self.position
            x -= self.ui2.main_image.width()/2
            y -= self.ui2.main_image.height()/2
            self.position = (x, y)
            if self.zoom == 1:
                self.position = [0,0]
                self.ui2.main_image.setPixmap(self.pixmap.scaled( \
                self.ui2.main_image.width(), self.ui2.main_image.height(), QtCore.Qt.KeepAspectRatio))
                self.image_scale = self.ui2.main_image
            else:
                self.image_scale = self.image.scaled(self.ui2.main_image.width() * self.zoom, \
                    self.ui2.main_image.height() * self.zoom, QtCore.Qt.KeepAspectRatio)
                self.update_zoom()

    def reset_zoom(self):
        self.zoom = 1
        self.position = [0, 0]
        self.ui2.main_image.setPixmap(self.pixmap.scaled( 
                self.ui2.main_image.width(), self.ui2.main_image.height(), QtCore.Qt.KeepAspectRatio))

    def keyPressEvent(self, eventQKeyEvent):
        key = eventQKeyEvent.key() #проверка, какая кнопка нажата
        #W = 87 - вверх; A = 65 - влево; S = 83 - вниз; D = 68 - вправо
        self.old = self.position
        if self.zoom > 1:
            dx, dy = self.ui2.main_image.width()/2, self.ui2.main_image.height()/2
            if key == 87 or key == 1062:
                self.position = self.old[0], self.old[1] - dy
            elif key == 83 or key == 1067:
                self.position = self.old[0], self.old[1] + dy
            elif key == 65 or key == 1060:
                self.position = self.old[0] - dx, self.old[1]
            elif key == 68 or key == 1042:
                self.position = self.old[0] + dx, self.old[1] 
            self.update_zoom()

    def eventFilter(self, source, event): 
        #функция для перирисовки изображения при смене размера виджета с сохранением пропорций
        if (event.type() == QtCore.QEvent.Resize):
            self.zoom = 1
            if (source is self.ui2.main_image):
                self.ui2.main_image.setPixmap(self.pixmap.scaled( 
                    self.ui2.main_image.width(), self.ui2.main_image.height(), QtCore.Qt.KeepAspectRatio))
        return super(wollieresult, self).eventFilter(source, event)

    def main_right_arrow_clicked(self):
        self.zoom = 1
        self.position = [0, 0]
        self.number_main_im += 1 #перенос номера главного изображения
        self.number_main_im %= len(self.list_files)
        self.number_mini_im_1 = (self.number_main_im - 2) % len(self.list_files) #перенос номера первого изображения превью
        number_main_im, list_files, directory,list_files = self.number_main_im, self.list_files, self.directory, self.list_files

        self.pixmap = (QtGui.QPixmap(directory + "/" + list_files[number_main_im]))
        self.pixmap_zoom = self.pixmap
        self.image = QImage(self.directory + "/" + self.list_files[self.number_main_im])
        if len(list_files) >= 5:
            self.pixmap_mini1 = (QtGui.QPixmap(directory + "/" + list_files[number_main_im-2]))
        if len(list_files) >= 3:
            self.pixmap_mini2 = (QtGui.QPixmap(directory + "/" + list_files[number_main_im-1]))
        self.pixmap_mini3 = (QtGui.QPixmap(directory + "/" + list_files[number_main_im]))
        if len(list_files) >= 2:
            self.pixmap_mini4 = (QtGui.QPixmap(directory + "/" + list_files[(number_main_im+1) % len(list_files)]))
        if len(list_files) >= 4:
            self.pixmap_mini5 = (QtGui.QPixmap(directory + "/" + list_files[(number_main_im+2) % len(list_files)]))

        self.ui2.main_image.setPixmap(self.pixmap_zoom.scaled( 
                    self.ui2.main_image.size(), QtCore.Qt.KeepAspectRatio))
        self.image_scale = self.ui2.main_image
        self.set_mini_pixmap() 

        #закрывает окно с информацией при переключении картинки
        if hasattr(self,'info_window'): 
            self.info_window.close()       

    def main_left_arrow_clicked(self):
        self.zoom = 1
        self.position = [0, 0]
        self.number_main_im -= 1 #перенос номера главного изображения
        self.number_mini_im_1 = (self.number_main_im - 2) % len(self.list_files) #перенос номера первого изображения превью

        if self.number_main_im == -1:
            self.number_main_im = len(self.list_files)-1
        number_main_im, list_files, directory,list_files = self.number_main_im, self.list_files, self.directory, self.list_files

        self.pixmap = (QtGui.QPixmap(directory + "/" + list_files[number_main_im]))
        self.pixmap_zoom = self.pixmap
        self.image = QImage(self.directory + "/" + self.list_files[self.number_main_im])
        if len(self.list_files) >= 5:
            self.pixmap_mini1 = (QtGui.QPixmap(directory + "/" + list_files[number_main_im-2]))
        if len(self.list_files) >= 3:
            self.pixmap_mini2 = (QtGui.QPixmap(directory + "/" + list_files[number_main_im-1]))
        self.pixmap_mini3 = (QtGui.QPixmap(directory + "/" + list_files[number_main_im]))
        if len(self.list_files) >= 2:
            self.pixmap_mini4 = (QtGui.QPixmap(directory + "/" + list_files[(number_main_im+1) % len(list_files)]))
        if len(self.list_files) >= 4:
            self.pixmap_mini5 = (QtGui.QPixmap(directory + "/" + list_files[(number_main_im+2) % len(list_files)]))
        
        self.ui2.main_image.setPixmap(self.pixmap_zoom.scaled( 
            self.ui2.main_image.size(), QtCore.Qt.KeepAspectRatio))
        self.set_mini_pixmap()

        #закрывает окно с информацией при переключении картинки
        if hasattr(self,'info_window'):
            self.info_window.close()

    def mini_right_arrow_clicked(self):
        i, list_files, directory,list_files = self.number_mini_im_1, self.list_files, self.directory, self.list_files
        self.number_mini_im_1 = (self.number_mini_im_1 + 1) % len(list_files) #перенос номера первого изображения превью

        self.pixmap_mini1 = (QtGui.QPixmap(directory + "/" + list_files[(i+1) % len(list_files)]))
        self.pixmap_mini2 = (QtGui.QPixmap(directory + "/" + list_files[(i+2) % len(list_files)]))
        self.pixmap_mini3 = (QtGui.QPixmap(directory + "/" + list_files[(i+3) % len(list_files)]))
        self.pixmap_mini4 = (QtGui.QPixmap(directory + "/" + list_files[(i+4) % len(list_files)]))
        self.pixmap_mini5 = (QtGui.QPixmap(directory + "/" + list_files[(i+5) % len(list_files)]))
        self.set_mini_pixmap()
        
    def mini_left_arrow_clicked(self):
        i, list_files, directory,list_files = self.number_mini_im_1, self.list_files, self.directory, self.list_files
        self.number_mini_im_1 = (self.number_mini_im_1 - 1) % len(list_files) #перенос номера первого изображения превью

        self.pixmap_mini1 = (QtGui.QPixmap(directory + "/" + list_files[(i-1) % len(list_files)]))
        self.pixmap_mini2 = (QtGui.QPixmap(directory + "/" + list_files[(i) % len(list_files)]))
        self.pixmap_mini3 = (QtGui.QPixmap(directory + "/" + list_files[(i+1) % len(list_files)]))
        self.pixmap_mini4 = (QtGui.QPixmap(directory + "/" + list_files[(i+2) % len(list_files)]))
        self.pixmap_mini5 = (QtGui.QPixmap(directory + "/" + list_files[(i+3) % len(list_files)]))
        self.set_mini_pixmap()

    def set_mini_pixmap(self):
        #функция установки изображений в превью
        if len(self.list_files) >= 5:
            self.ui2.mini_image_1.setPixmap(self.pixmap_mini1)
        if len(self.list_files) >= 3:    
            self.ui2.mini_image_2.setPixmap(self.pixmap_mini2)
        self.ui2.mini_image_3.setPixmap(self.pixmap_mini3)
        if len(self.list_files) >= 2:
            self.ui2.mini_image_4.setPixmap(self.pixmap_mini4)
        if len(self.list_files) >= 4:
            self.ui2.mini_image_5.setPixmap(self.pixmap_mini5)

    def info_clicked(self):
        if hasattr(self,'info_window'): #проверка что такое же окно ещё не запущено
            self.info_window.close()
        image_path = self.directory + "/" + self.list_files[self.number_main_im]
        self.info_window = info(image_path, self)
        self.info_window.setGeometry(QtWidgets.QStyle.alignedRect(QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter, self.info_window.size(), self.geometry()))
        self.info_window.show()

    def map_clicked(self):
        image_path = self.directory + "/" + self.list_files[self.number_main_im]
        self.image_path = image_path
        #image = Image.open(self.image_path)
        image_name = image_path[image_path.rfind("/")+1:] #имя
        # возращет Exif теги
        f = open(image_path, 'rb')
        tags = exifread.process_file(f)
        lat = 0
        lon = 0 
        if "GPS GPSLatitude" in tags and "GPS GPSLongitude" in tags:
            gps = str(tags["GPS GPSLatitude"])[1:len(str(tags["GPS GPSLatitude"]))-1].split(',')
            for i in range(len(gps)):
                gps[i] = gps[i].strip()
                if i == 2:
                    gps[i] = float(gps[i].split('/')[0])/float(gps[i].split('/')[1])
                else:
                    gps[i] = float(gps[i])
            lat = (gps[2]/60 + gps[1])/60 + gps[0]
            
            gps = str(tags["GPS GPSLongitude"])[1:len(str(tags["GPS GPSLongitude"]))-1].split(',')
            for i in range(len(gps)):
                gps[i] = gps[i].strip()
                if i == 2:
                    gps[i] = float(gps[i].split('/')[0])/float(gps[i].split('/')[1])
                else:
                    gps[i] = float(gps[i])
            lon = (gps[2]/60 + gps[1])/60 + gps[0]
        #print(lat,lon)
            self.myApp = MyApp([[lat,lon, image_name]], self)
            self.myApp.show()

    def allmap_clicked(self):
        coords=[]
        
        for images in self.list_files:
            image_path = self.directory + "/" + images
            self.image_path = image_path
            #image = Image.open(self.image_path)
            image_name = image_path[image_path.rfind("/")+1:] #имя
            # возвращет Exif теги
            f = open(image_path, 'rb')
            tags = exifread.process_file(f)
            lat = 0
            lon = 0 

            if "GPS GPSLatitude" in tags and "GPS GPSLongitude" in tags:
                gps = str(tags["GPS GPSLatitude"])[1:len(str(tags["GPS GPSLatitude"]))-1].split(',')
                for i in range(len(gps)):
                    gps[i] = gps[i].strip()
                    if i == 2:
                        gps[i] = float(gps[i].split('/')[0])/float(gps[i].split('/')[1])
                    else:
                        gps[i] = float(gps[i])
                lat = (gps[2]/60 + gps[1])/60 + gps[0]
            
                gps = str(tags["GPS GPSLongitude"])[1:len(str(tags["GPS GPSLongitude"]))-1].split(',')
                for i in range(len(gps)):
                    gps[i] = gps[i].strip()
                    if i == 2:
                        gps[i] = float(gps[i].split('/')[0])/float(gps[i].split('/')[1])
                    else:
                        gps[i] = float(gps[i])
                lon = (gps[2]/60 + gps[1])/60 + gps[0]
                #print(lat,lon)
                coords.append([lat,lon, image_name])
        self.myApp = MyApp(coords, self)
        self.myApp.show()

    def excel_clicked(self):
        if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/results/results.txt"):
            file = open(os.path.dirname(os.path.abspath(__file__)) + "/results/results.txt", "r")

            lines = file.readlines()
            name, date, time, lat, lon, walrus = [],[],[],[],[],[]
            for line in lines:
                line = line.split(';')
                if line[0] in name:
                    walrus[line.index(line[0])] = line[5]
                else:
                    name.append(line[0])
                    date.append(line[1])
                    time.append(line[2])
                    lat.append(float(line[3]))
                    lon.append(float(line[4]))
                    walrus.append(int(line[5]))
        
            df = pd.DataFrame({"Фото": name,
                "Дата": date,
                "Время": time,
                "Широта": lat,
                "Долгота": lon,
                "Моржи": walrus})
            file.close()
            df.to_excel('results/walruses.xlsx')
        return


class MyApp(QtWidgets.QWidget):
    def __init__(self, coords, parent = wollie):
        super().__init__(parent, QtCore.Qt.Window)
        self.setWindowTitle('Map')
        self.window_width, self.window_height = 900, 900
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        coordinate = (69.457453, 58.513938)
        m = folium.Map(
            #Stamen” (Terrain, Toner, and Watercolor
            tiles='OpenStreetMap',
            zoom_start=13,
            location=coordinate
        )

        for coord in coords:
            folium.Marker([coord[0], coord[1]], popup=coord[2]).add_to(m)

        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


class info(QtWidgets.QWidget):
    def __init__(self, image_path, parent = wollie):
        super().__init__(parent, QtCore.Qt.Window)
        self.ui2 = Ui_Info()
        self.ui2.setupUi(self)
        self.image_path = image_path
        image = Image.open(self.image_path)
        image_name = image_path[image_path.rfind("/")+1:] #имя
        (width, height) = image.size #размер изображения
        bits = '-'
        if (image_name[image_name.rfind(".")+1:] == ('jpg' or 'jpeg')):
            bits = image.bits #Глубина цвета

        info_text = (f"Имя:  {image_name}\nПуть:  {image_path}\nРазрешение:  {width} x {height}\nШирина:  {width}\nВысота:  {height}")
        info_text += (f"\nГлубина цвета:  {bits}")

        # возращет Exif теги
        f = open(image_path, 'rb')
        info_text += "\nExif и TIFF:\n"
        tags = exifread.process_file(f)
        # добавить exif в вывод

        for tag in tags.keys():
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                info_text += ("%s:  %s\n" % (tag, tags[tag]))

        self.ui2.text.setText(info_text)
        
########################################################################
app = QtWidgets.QApplication([])
application = StartWindow()
application.show()
sys.exit(app.exec())