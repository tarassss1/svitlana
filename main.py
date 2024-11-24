from PIL import Image

image = Image.open("ccc.jpg")
image = image.convert("L")

# апрвавапвпв
# L - чорно-білий
# RGB 
# RGBA 
# CMYK 
# HSV 
# P 
colors = image.getcolors()
# кількість унікальних кольорів
print(len(colors)) 



# img_contours = image.filter(ImageFilter.CONTOUR)
# img_contours.show() 

# COUNTUR - 
# DETAIL - 
# EDGE_ENHANCE - 
# EDGE_ENHANCE_MORE - 
# EMBOSS - 
# FIND_EDGES 
# SHARPEN - 
# SMOOTH - 



# print(image.size) # розмір файлу
# print(image.format) # формат файлу
# print(image.mode) # колірний тип
# image2 = image.resize((100,100))
# image.show()
# image2.show()


# import os
# from PyQt5.QtWidgets import (
#    QApplication, QWidget,
#    QFileDialog, # Діалог відкриття файлів (і папок)
#    QLabel, QPushButton, QListWidget,
#    QHBoxLayout, QVBoxLayout
# )
 
# from PyQt5.QtCore import Qt # потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
# from PyQt5.QtGui import QPixmap # оптимізована для показу на екрані картинка
 
# from PIL import Image, ImageFilter
 
# app = QApplication([])
# win = QWidget()      
# win.resize(700, 500)
# win.setWindowTitle('Easy Editor')
# lb_image = QLabel("Картинка")
# btn_dir = QPushButton("Папка")
# lw_files = QListWidget()
 
# btn_bw = QPushButton("Ч/Б")
# btn2 = QPushButton("Контур")
 
# row = QHBoxLayout()          # Головна лінія
# col1 = QVBoxLayout()         # ділиться на два стовпці
# col2 = QVBoxLayout()
# col1.addWidget(btn_dir)      # в першому - кнопка вибору каталогу
# col1.addWidget(lw_files)     # і список файлов
# col2.addWidget(lb_image, 95) # в другому - картинка
# row_tools = QHBoxLayout()    # і ряд кнопок
# row_tools.addWidget(btn_bw)
# row_tools.addWidget(btn2)
# col2.addLayout(row_tools)
 
# row.addLayout(col1, 20)
# row.addLayout(col2, 80)
# win.setLayout(row)
 
# win.show()
 
# workdir = ''
 
# def filter(files, extensions):
#    result = []
#    for filename in files:
#        for ext in extensions:
#            if filename.endswith(ext):
#                result.append(filename)
#    return result
 
# def chooseWorkdir():
#    global workdir
#    workdir = QFileDialog.getExistingDirectory()
 
# def showFilenamesList():
#    extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
#    chooseWorkdir()
#    filenames = filter(os.listdir(workdir), extensions)
 
#    lw_files.clear()
#    for filename in filenames:
#        lw_files.addItem(filename)
 
# btn_dir.clicked.connect(showFilenamesList)
 
# class ImageProcessor():
#    def __init__(self):
#        self.image = None
#        self.dir = None
#        self.filename = None
#        self.save_dir = "Modified/"
 
#    def loadImage(self, dir, filename):
#        ''' під час завантаження запам'ятовуємо шлях та ім'я файлу '''
#        self.dir = dir
#        self.filename = filename
#        image_path = os.path.join(dir, filename)
#        self.image = Image.open(image_path)
 
#    def do_bw(self):
#        self.image = self.image.convert("L")
#        self.saveImage()
#        image_path = os.path.join(self.dir, self.save_dir, self.filename)
#        self.showImage(image_path)

    

#    def do_contur(self):
#        self.image = self.image.filter(ImageFilter.CONTOUR)
#        self.saveImage()
#        image_path = os.path.join(self.dir, self.save_dir, self.filename)
#        self.showImage(image_path)
 
#    def saveImage(self):
#        ''' зберігає копію файлу у підпапці '''
#        path = os.path.join(self.dir, self.save_dir)
#        if not(os.path.exists(path) or os.path.isdir(path)):
#            os.mkdir(path)
#        image_path = os.path.join(path, self.filename)
#        self.image.save(image_path)
 
#    def showImage(self, path):
#        lb_image.hide()
#        pixmapimage = QPixmap(path)
#        w, h = lb_image.width(), lb_image.height()
#        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
#        lb_image.setPixmap(pixmapimage)
#        lb_image.show()
 
# def showChosenImage():
#    if lw_files.currentRow() >= 0:
#        filename = lw_files.currentItem().text()
#        workimage.loadImage(workdir, filename)
#        image_path = os.path.join(workimage.dir, workimage.filename)
#        workimage.showImage(image_path)
 
# workimage = ImageProcessor() #поточне робоче зображення для роботи
# lw_files.currentRowChanged.connect(showChosenImage)
 
# btn_bw.clicked.connect(workimage.do_bw)
# btn2.clicked.connect(workimage.do_contur)
 
# app.exec()





