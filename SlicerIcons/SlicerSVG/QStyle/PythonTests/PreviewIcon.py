import sys
import os

import lxml.etree as ET
import xpath
import copy

import cssutils

import csv
from collections import defaultdict

from PyQt5 import QtGui, QtSvg, QtWidgets
from PyQt5.QtCore import Qt, QPointF, QPoint, QRectF
from PyQt5 import QtGui, QtSvg, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton



#-------------------------------------------------------------------------------
# some globals for command line.
paletteFileName = "./palette.csv"
svgFileName = ""
currentTheme = "l"
currentState = "e"
currentTree = "le"

# global Theme/State Trees parsed from SVG at startup.
# These would be saved for each icon and used to refactor svg stroke/fill colors.
#
# LightTheme/EnabledState
global LEtree
# LightTheme/DisabledState
global LDtree
# DarkTheme/EnabledState
global DEtree
# DarkTheme/DisbledState
global DDtree
# Color Palette Dictionary
global colorDict


    #-------------------------------------------------------------------------------
    #--- SVG ESSENTIALS:
    #--- ---------------------------------
    #--- SVG elements can be styled in many different ways
    #---   1. using external CSS styles (in an external style sheet).
    #---   2. using internal <style> elements
    #---        e.g.  <style> circle { fill: green  } </style>
    #---              <circle cx="5" cy="5" r="4" />
    #---        Style elements can be located in a variety of places, under <svg>, <defs>, 
    #---        and <g> tags, and inside graphical elements.
    #---   3. using custom styles included in <defs> or <style> sections.
    #---        e.g. <style id="style1">
    #---                    .blue-fill {
    #---                    fill : blue;
    #---                    }
    #---              </style>
    #---              then: >circle class="blue-fill", cx="5" cy="5" r="4" />
    #---   4. using inline styles (in an element's style attribute), [Inkscape SVG]
    #---        e.g.  <rect style="fill: red; stroke: blue; stroke-width: 3" x="200" y="100" width="600" height="300"/>
    #---   5. using "shorthand" presentation attributes (no explicit <style> or style=)
    #---        e.g. <circle fill="deepPink" stroke="yellow" stroke-width="5" cx="50" cy="50" r="10"></circle>
    #---   6. using svg defaults: there may be NO style information inside the svg.
    #---        e.g. The default value of "fill" is black, if no fill color is specified.
    #---             The default value of "stroke" is none, if no stroke color is specified.
    #--- These specifications can be found in a number of places within an svg file.
    #--- So parsing logic will have to target all of these. (todo: what's missing?)
    #---
    #---
    #--- HOW STYLE OVERRIDES OCCUR:
    #--- ---------------------------------
    #--- The cascade governs how these styles are applied to elements:
    #--- Presentation attributes are low-level “author style sheets” and are overridden by ANY other style def.
    #--- External styles are overridden by internal styles in style blocks, and
    #--- internal style blocks are overridden by inline styles in a style attribute.
    #---
    #---
    #--- USE and LIMITATIONS OF THIS PARSING LOGIC:
    #--- ------------------------------------------
    #--- RECOGNIZED set of graphic elements:
    #--- <circle>, <g>, <line>, <ellipse>, <path>, <polygon>, <polyline>, <rect>
    #--- Element Attributes handled by theme/state changing logic:
    #--- stroke, fill
    #--- NOT HANDLED: inherit, <use>, currentColor, css variables, filters, markers,linear gradients, or filters.
    #--- NO eternal CSS or XSL files can be used for Slicer Icon SVGs
    #--- NO <use> specifications are handled.
    #--- Parsing assumes a <g> group contains only graphic elements and does not recurse into any child groups.
    #--- SVGS may not contain multiple SVG fragments. All elements included within same <svg ...</svg>
    #---
    #---
    #--- TESTS FOR ICON FITNESS FOR LOGIC:
    #--- ---------------------------------
    #--- To avoid parsing errors, the following tests should be made:
    #--- 1. test that any layers of graphic elements are flat.
    #--- 2. test that there is no reliance on <use>
    #--- 3. test that there is no reliance on external CSS.
    #--- 4. test that there is no reliance on css variables 
    #--- 5. test for filters, markers, gradients
    #---
    #---
    #--- FIND STYLES IN SVG FOR PARSING:
    #--- ---------------------------------
    #--- Looking for styles specified in the manners listed above:
    #--- 1. is not relevant since we're not using external CSS with Slicer SVGs.
    #--- 2. may be defined under svg root, or in <defs>,
    #--- 3. and may be found under a layer <g>, so need to look for it in all 3 places
    #---        e.g.  <svg height="100" width="100">          
    #---              <defs id="someDefs">
    #---              <style id="style1">
    #---                    .blue-fill {
    #---                        fill : blue;
    #---                    }
    #---                </style>
    #---            </defs>
    #---            <style id="style2">
    #---                .red-stroke {
    #---                    stroke : red;
    #---                    stroke-width : 
    #---                }
    #---            </style>
    #---            <circle cx="50" cy="50" r="40" class="blue-fill red-stroke" />
    #---        </svg>
    #--- 4. graphic elements as children of root: inline styles and
    #--- 5. presentation attr:
    #---            <rect fill="#FF0000" height="26" id="svg_2" stroke="#000000"/>
    #---            <rect style="display:inline;fill:#61a6be;fill-opacity:1;stroke:#17171d"/>
    #--- 6. graphic elements within a layer <g> which is a child of root: inline styles and
    #--- 7. presentation attr:
    #---           <g ... <rect fill="#FF0000" height="26" id="svg_2" stroke="#000000"/>... />
    #---           <g ... <rect style="display:inline;fill:#61a6be;fill-opacity:1;stroke:#17171d"/>... \>
    #--- 
    #---
    #--- ---------------------------------
    #--- TODO:
    #--- * Check whether svgs that specify presentation attributes can be overridden by Qstyles or QSS.
    #--- * Write tests
    #--- * Refactor logic for checking for:
    #---       -style blocks children of <defs>,
    #---       -custom style definitions of children of <defs>
    #---       -style blocks children of <svg> root
    #---       -inline styles of elements which are children of <svg> root
    #---       -presentation styles of elements which are children of <svg> root
    #---       -style blocks of groups <g> that are children of <svg> root
    #---       -inline styles of elements that are children of <g> 
    #---       -presentation styles of elements that are children of <g?
    #-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
def testIconFitnessForLogic():
    #--- Test for <use>
    #--- Test for reliance on external CSS 
    #--- Test that there are no grouped elements within a layer group.
    #--- Test that there is no reliance on <use>
    #--- Test that there is no reliance on css variables 
    #--- Test for filters, markers, gradients
    #--- Report any finds that could cause rendering problem for the icon.
    print('not implemented.')


#-------------------------------------------------------------------------------
def createColorDictionaryFromCSV():
    
    global colorDict
    global paletteFileName

    # Create Theme/State color dictionary from Slicer Palettes with columns:
    # Palette, ColorName, Light/Enabled, Dark/Enabled, Light/Enabled, Light/Disabled.
    try:
        file = open(paletteFileName, 'r')
    except IOError:
        print("File ", paletteFileName, " can't be opened or does not exist...Exiting.")
        sys.exit()

        reader = csv.DictReader(file)
        colorDict = [row for row in reader]
        print(colorDict)

        

#-------------------------------------------------------------------------------
def getCurrentColorFromDictionary(color):
    global currentTheme
    global currentState
    global colorDict

    print ("indexing on color" + color + '\n')
    if (currentTheme == 'l' or currentTheme == 'L'):
        if (currentState == 'e' or currentState == 'E'):

            # assuming LightEnabled is the default color in svg, just return it
            print ("light/enabled color" + color + '\n')
            newcolor = colorDict[2]['LightEnabled']
            return (newcolor)

        else:
            # find row where element [2] matches color and return element [3]
            newcolor = colorDict[3]['LightDisabled']
            return (newcolor)
    else:
        if (currentState == 'e' or currentState == 'E'):
            # find row where element [2] matches color and return element [4]
            newcolor = colorDict[3]['DarkEnabled']
            print ("light/enabled color" + newcolor + '\n')
            return (newcolor)
        else:
            # return Dark/Disabled
            # find row where element [2] matches color and return element [5]            
            newcolor = colorDict[3]['DarkDisabled']
            return (newcolor)


#-------------------------------------------------------------------------------
def skipElementTagCheck (tagname ):

    #--- what are all the things to check for...
    if ( 'def' in tagname ):
        print ("not processing\n")
        return False
    if ( 'title' in tagname ):
        print ("not processing\n")
        return False
    else:
        return True
    
        

#-------------------------------------------------------------------------------
def styleElementTagCheck (tagname ):

    #--- did we find a style element?
    if ( 'style' in tagname ):
        return True
    else:
        return False



#-------------------------------------------------------------------------------
def changeStyleInSVG (root, styles):
    print('not implemented.')


#-------------------------------------------------------------------------------
def changeStylesInDefs(root, styles):
    print('not implemented.')


#-------------------------------------------------------------------------------
def changeInlineStyles(root, styles):
    print('not implemented.')


#-------------------------------------------------------------------------------
def changePresentationAttributes(root, styles):
    print('not implemented.')

    

#-------------------------------------------------------------------------------
def  createThemeStateTrees (theme, state):
    global DEtree, DDtree, LEtree, LDtree
    #---    
    #--- find default strokes and fills
    #--- map them to other palettes
    #---

    if theme == 'D':
        if state == 'E':
            tree = DEtree
        else:
            tree = DDtree
    else:
        if state == 'E':
            tree = LEtree
        else:
            tree = LDtree
    ET.indent(tree, space="\t", level=0)

    #--- first look for <defs> and if it exists, look for style blocks
    defs = root.findall('{http://www.w3.org/2000/svg}defs')
    if !(defs == "None"):
        printf ("found defs\n")
        styles = root.findall('{http://www.w3.org/2000/defs}style')
        if !(styles == "None"):
            #--- find strokes and fills inside and replace colors.
            printf ("found styleblock in defs\n")
            changeStylesInDefs ( root, styles )

    #--- look for all of <svg>'s <style> element children
    kidsOfRoot = tree.tostring(root)
    styles = root.findall('{http://www.w3.org/2000/svg}style')
    if !(styles == "None"):            
        printf( "found styleblock under svg root")
        if !(styles == "None"):
            #--- find strokes and fills inside and replace colors.            
            changeStylesinSVG ( root, styles)
#--- CONTINUE HERE.                
    #--- give me all of <svg>'s children that have children.
    tree.xpath('/svg/*[count(child::*) != 0 ]')
    if (count > 0 ):
        svgElement = /root/child::*[child::svg]
        print ( svgElements)

    #--- give me all of <g>'s children that have children.
    tree.xpath('/g/*[count(child::*) != 0 ]')
    if ( count > 0):
        layerElements = /g/child::*[child::g]
        print ( layerElements)

    root = tree.getroot()

    #--- handle grouped or ungrouped svg elements 
    groups = root.findall('{http://www.w3.org/2000/svg}g')rr
    #------- Parse svg trees with no layers (groups of elements)
    if not groups:
        print ('.............NO LAYERS............\n')
        kids = root.getchildren()
        if not kids:
            print ('Found no elements to parse. Exiting.\n')
            sys.exit()
        else:
            #--- this is the place where css style blocks would be, so look for style tags
            if styleElementStyleCheck (kid.tag) == True:
            for kid in kids:
                if skipElementTagCheck (kid.tag) == False:
                    continue
                else:
                    print ("printing all element attributes: ")
                    print (kid.attrib)
                    if (kid.attrib == "style" ):
                        print ( kid.attrib.values )
                    print ("\n")
            #--- pull out inline style text
            #sheet = cssutils.parseStyle(kid.attrib.values)
            #print (sheet.cssText)
            # now process the string to change the stroke and fill colors.
            # extract value --
            # look for either stroke:#xxxxxx, or stroke="#xxxxxx"<space>
            # get new value from palette
            # substitute value into substring
            # substitute substring into string=
            # set new style using kid.set

    #------- Parse svg trees with layers (groups of elements)
    else:
        print ('.............LAYERED SVG............\n')
        for group in groups:
            print (group, '\n')
            kids = group.getchildren()
            if not kids:
                print ('no elements to parse. Exiting.\n')
                sys.exit()
            for kid in kids:
                found = 0
                if skipElementTagCheck (kid.tag) == False:
                    continue
                else:
                    #--- probe for stroke and fill colors in one of three style specifications:
                    #---
                    #--- 1. Look for style block within a <style> element
                    if (len(kid) > 0):
                        gkids = kid.getchildren()
                        element = .findall('{http://www.w3.org/2000/svg}style')                        
                        for gkid in gkids:
                            print ("printing all element attributes: ")
                            print (gkid.attrib)
                            if ('style' in gkid.attrib):
                                stystr = gkid.attrib['style']
                                print ( "Found a style element with attributes ", gkid.attrib.values, "\n" )
                                found = 1

                    #--- 2. Look for inline style inside a style attribute 
                    print ("printing all element attributes: ")
                    print (kid.attrib)
                    if ('style' in kid.attrib):
                        stystr = kid.attrib['style']
                        print ( "Found inline style in style attribute ", kid.attrib.values, "\n" )
                        found = 1
                    
                    #--- 3. Look for presentation attributes 

                    #--- 4. OR, no known style specification found.

                            
                    #---



                    print ( stystr)

                    if (not stystr):
                        print ("no style found.\n")
                        continue
                    else:
                        items=stystr.split(";")
                        print (len(items), items)
            
            #--- pull out inline style text
            #sheet = cssutils.parseStyle(kid.attrib.values)
            #print (sheet.cssText)
            # now process the string to change the stroke and fill colors.
            # do the same as up there ^
    sys.exit()


    # Access value
    origColor = element.get('value')
    print (origColor )
    # Change value if not none
    if (origColor != "None" or origColor != "none"):
        newColor = getCurrentColorFromDictionary (origColor)
        print (' ')
        print (newColor)
        element.set('value', 'newColor')
        print ('Changed stroke color from: ' + origColor + ' to: ' + newColor )

    #--- Find fills and replace their color
    root = tree.getroot();
    for element in root.findall('{http://www.w3.org/2000/svg}fill'):
        print (element)
        # Access value
        origColor = element.get('value')
        # Change value
        if (origColor != "None" or origColor != "none"):
            newColor = getCurrentColorFromDictionary (origColor)
            element.set('value', 'newColor')
            print ('Changed stroke color from: ' + origColor + ' to: ' + newColor )



#-------------------------------------------------------------------------------
#---- Subclass QMainWindow 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layered Icon Preview")
        self.setGeometry(50, 50, 900, 800)
        print ("calling parseFiles\n")
        self.ParseFiles()
        #self.UIcomponents()
        self.show()

    def ParseFiles(self):
        global svgFileName
        global paletteFileName
        global currentTheme
        global currentState
        global LEtree, LDtree, DEtree, DDtree
        
        #---- open svg and palette files
        try:
            file = open(paletteFileName, 'r')
        except IOError:
            print("File ", paletteFileName, " can't be opened or does not exist...Exiting.")
            sys.exit()
        try:
            file = open(svgFileName, 'r')
        except IOError:
            print("File ", svgFileName, " can't be opened or does not exist...Exiting.")
            sys.exit()

        #--- Create the color dictionary from palettes file
        #--- This contains hex colors for all themes/states.
        #--- Is used for swapping colors when themes/states change.
        print ("Creating color dictionary...\n")
        createColorDictionaryFromCSV()

        #---- Parse what we assume is Light/Enabled default SVG into LEtree
        print ("Parsing svg...\n")
        LEtree = ET.parse(svgFileName)
        file.close()

        #--- Copy the parsed Light/Enabled SVG into other Theme/State trees.
        print ("Creating theme/state trees...\n")
        LDtree = copy.deepcopy(LEtree)
        DEtree = copy.deepcopy(LEtree)
        DDtree = copy.deepcopy(LEtree)
        
        #--- Create Dark/Enabled tree, with color swap from Light/Enabled version
        createThemeStateTrees ('D', 'E')
        createThemeStateTrees ('L', 'D')
        createThemeStateTrees ('D', 'D')

        print ("BYE FOR NOW\n")
        sys.exit();
        
        svg = QSvgRenderer()
        svgBytes = PaintHelper.changeSvgFill(os.path.join(os.path.dirname(sys.modules[__name__].__file__), '../assets/icons/material/', icon), color)
        svg.load(svgBytes)
        painter.setOpacity(opacity)
        svg.render(painter, QRectF(x, y, size, size))
        painter.setOpacity(1)        


#-------------------------------------------------------------------------------
#----
#---- Main script:
#---- Open Palette CSV file and create dictionary.
#---- Open SVG file to parse into tree, create other theme/state trees
#---- Open gui, look at the Theme/State requested.
#----

n = len(sys.argv)
if n==1 or n!= 5:
    print ("Usage: " + sys.argv[0] + " svgfile" + " palettefile" + " theme (L|D)" + " state (E|D)\n")
    sys.exit()

svgFileName = sys.argv[1]
paletteFileName = sys.argv[2]
theme = sys.argv[3]
state = sys.argv[4]
app = QApplication(sys.argv)
createColorDictionaryFromCSV()
window = MainWindow()
window.show()

#event loop
app.exec()

sys.exit(app.exec_())

