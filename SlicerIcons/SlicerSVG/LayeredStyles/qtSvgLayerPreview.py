import sys
import os.path
import xml.etree.ElementTree as ET
import copy
from PyQt5 import QtGui, QtSvg, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton

#---- globals

currentState = "Enabled"
currentTheme = "Light"
currentText = currentTheme + ", " + currentState
fileName = ""
workFileName = "./tmp.svg"
minnestSize = 12
minSize = 12
maxSize = 640
currentSize = maxSize

#---- Subclass QMainWindow 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layered Icon Preview")
        self.setGeometry(50, 50, 900, 800)
        self.UIcomponents()
        self.show()
        self.svgWidget = QtSvg.QSvgWidget(fileName, self)
        self.svgWidget.setStyleSheet('background-color:rgb(255,255,255)')
        self.svgWidget.setGeometry(50,50,640,640)
        self.svgWidget.show()

    def ParseSVG(self):
        global fileName
        global workFileName
        global currentTheme
        global currentState
        
        # Parse
        try:
            file = open(fileName, 'r')
        except IOError:
            print("File ", filenName, " can't be opened or does not exist...Exiting.")
            sys.exit()

        #---- Find namespaces
        namespaces = {node[0]: node[1] for _, node in ET.iterparse(fileName, events=['start-ns'])}
        # Register each one.
        for key, value in namespaces.items():
            ET.register_namespace(key, value)
            #print('registering namespace ' + key + ' ' + value + '\n')
    
        #---- Parse
        origDoc = ET.parse(fileName)
        file.close()
        origRoot = origDoc.getroot();
        workDoc = copy.deepcopy(origDoc)
        workRoot = workDoc.getroot();
        ET.indent(workDoc, space="\t", level=0)

        #---- Remove unused layers
        for layer in workRoot.findall('{http://www.w3.org/2000/svg}g'):
            s = str(layer.attrib)
            #print('and ' + currentTheme + '/' + currentState)
            #print('processing:' + s + '\n')
            if not( currentTheme in s and currentState in s):
                #print('REMOVING:' + s + '\n')
                workRoot.remove(layer)
                
        #---- make sure layer is visible
        for layer in workRoot.findall('{http://www.w3.org/2000/svg}g'):
            layer.set('style', 'display:inline')

        #---- write out layer until we figure out how to get ET contents into qsvgWidget.
        workDoc.write(workFileName, encoding="UTF-8")


    def UIcomponents(self):
        
        #---- creating a push button 
        LTbutton = QPushButton("Light theme", self) 
        LTbutton.setGeometry(700, 100, 150, 40) 
        LTbutton.clicked.connect(self.setLightTheme)
            
        DKbutton = QPushButton("Dark theme", self) 
        DKbutton.setGeometry(700, 150, 150, 40) 
        DKbutton.clicked.connect(self.setDarkTheme)
            
        ENbutton = QPushButton("Enabled state", self) 
        ENbutton.setGeometry(700, 300, 150, 40) 
        ENbutton.clicked.connect(self.setEnableState)
            
        DISbutton = QPushButton("Disabled state", self) 
        DISbutton.setGeometry(700, 350, 150, 40) 
        DISbutton.clicked.connect(self.setDisableState)

        PlusButton = QPushButton("+", self)
        PlusButton.setGeometry(725, 400, 50, 40)
        PlusButton.clicked.connect(self.increaseSize)

        MinusButton = QPushButton("-", self)
        MinusButton.setGeometry(775, 400, 50, 40)
        MinusButton.clicked.connect(self.decreaseSize)

        Quitbutton = QPushButton("Quit", self) 
        Quitbutton.setGeometry(700, 580, 150, 40) 
        Quitbutton.clicked.connect(self.quitStuff)
    

    #---- action methods

    
    def increaseSize(self):
        global maxSize
        global minSize
        global currentSize
        if currentSize == maxSize:
            return
        #----resize the icon
        if currentSize <= maxSize:
            currentSize = int(currentSize * 2)
        self.svgWidget.resize( currentSize, currentSize)
        self.svgWidget.setGeometry(50, 50, currentSize, currentSize)
        self.svgWidget.show()
            
    def decreaseSize(self):
        global maxSize
        global minSize
        global currentSize
        if currentSize == minSize:
            return
        #----resize the icon
        if currentSize >= minSize:
            currentSize = int(currentSize / 2)
        self.svgWidget.resize( currentSize, currentSize)
        self.svgWidget.setGeometry(50, 50, currentSize, currentSize)
        self.show()
                            
    def setLightTheme(self):
        global currentTheme
        currentTheme = "Light"
        global currentState
        global workFileName
        self.ParseSVG()
        self.svgWidget.setStyleSheet('background-color:rgb(255,255,255)')
        self.svgWidget.load(workFileName)
        self.svgWidget.update()
        print(currentTheme + ", " + currentState)
            
    def setDarkTheme(self):
        global currentTheme
        currentTheme = "Dark"
        global currentState
        self.svgWidget.setStyleSheet('background-color:rgb(50,50,50)')
        self.ParseSVG()
        self.svgWidget.load(workFileName)
        self.svgWidget.update()
        print(currentTheme + ", " + currentState)
            
    def setEnableState(self):
        global currentTheme
        global currentState
        currentState = "Enabled"
        self.ParseSVG()
        self.svgWidget.load(workFileName)
        self.svgWidget.update()
        print(currentTheme + ", " + currentState)

    def setDisableState(self):
        global currentTheme
        global currentState
        currentState = "Disabled"
        self.ParseSVG()        
        self.svgWidget.load(workFileName)
        self.svgWidget.update()
        print(currentTheme + ", " + currentState)

    def quitStuff(self):
        sys.exit()
        
#---- Main script: open file to parse into tree, open gui, preview each layer for bugs..

n = len(sys.argv)
if n==1:
    print ("Usage: " + sys.argv[0] + "svg filename")
    sys.exit()

fileName = sys.argv[1]
app = QApplication(sys.argv)
window = MainWindow()
window.show()

#event loop
app.exec()

sys.exit(app.exec_())

