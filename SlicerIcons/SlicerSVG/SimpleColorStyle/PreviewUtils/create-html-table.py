# Run as: create-html-table.py L|D {Light or Dark Theme}
# The script requires 1 argument: the css file to use to style document. 

import sys
import os.path
import copy
import math

#---Gets a list of subdirectories in the given path."""
def getSubdirectories(path):
    subdirectories = []
    for entry in os.scandir(path):
        if entry.is_dir():
            subdirectories.append(entry.path)
    return subdirectories

n = len(sys.argv)
if n!=2:
    print ("Usage: " + sys.argv[0] +  "L|D {Light DarkTheme}" )
    sys.exit()

# Create the html document head and include css
theme = sys.argv[1]

#---globals
dirList = []
fileList = []
numfiles = 0

# stringify style classes based on theme choice
if theme=="L" or theme=="l":
    fileName= "./LightThemeIconsIndex.html"
    titleText = "Light Theme Slicer Icons"
    tableText = "table, th, td { background-color: white; color: black; border: None; padding: 10px; font-size: 12px;}\n"
    tooltipCellText = ".CellWithTooltip { position:relative; }\n"
    tooltipStyleText = ".CellTooltip { display: None; z-index: 100; position: absolute; border: None; font-size: 10pt; color: black; top: 60px; background-color:white; padding: 3px; }\n"
    cellWithTooltipText = ".CellWithTooltip:hover span.CellTooltip { display:block; }\n"
    cssStyleText = "<style>\n" + tableText + tooltipCellText + tooltipStyleText + cellWithTooltipText + "</style>\n"
    bodyStyleText = "<body style=\"margin-left: 200px; margin-top: 100px; font-family: sans-serif; align: left; color: black; background-color: white\">\n"
    headingText = "<h2 style= \"color:black;\"> Slicer Design Guidelines & Light Theme Icons Preview </h2>\n"
if theme=="D" or theme=="d":
    fileName = "./DarkThemeIconsIndex.html"
    titleText = "Dark Theme Slicer Icons"
    tableText = "table, th, td { background-color: #121212; color: #e5e5f6; border: None; padding: 10px; font-size: 12px;}\n"
    tooltipCellText = ".CellWithTooltip { position:relative; }\n"
    tooltipStyleText = ".CellTooltip { display: None; z-index: 100; position: absolute; border: None; font-size: 10pt; color: #e5e5f6; top: 60px; background-color:#121212; padding: 3px; }\n"
    cellWithTooltipText = ".CellWithTooltip:hover span.CellTooltip{ display:block; }\n"
    cssStyleText = "<style>\n" + tableText + tooltipCellText + tooltipStyleText + cellWithTooltipText + "</style>\n" 
    bodyStyleText = "<body style=\"margin-left: 200px; margin-top: 100px; font-family: sans-serif; align: left; color: #e5e5f6; background-color: #121212\"> "
    headingText = "<h2 style= \"color: #e5e5f6;\"> Slicer Design Guidelines & Dark Theme Icons Preview </h2>\n"
    
# IncludeDesign Guildlines
fileout = open(fileName, "w")
pStyle = "<p style=\"margin-bottom: 40px; margin-top: 40px; margin-left: 30px; width: 80%; font-size:10pt;\">\n"
designGuidelines = pStyle + "1. Design icons as vector images on a transparent background.\n</p>"
designGuidelines += pStyle + "2. At 24x24 pixel resolution, stroke width should be 1dp = 1px for pixel-perfect rendering at resolution multiples of 24.\n</p>"
designGuidelines += pStyle + "3. Use simple stroked elements without fill where possible.\n</p>"
designGuidelines += pStyle + "4. If filled elements are required, use limited color, consistently within your UI, compatibly with Slicer's application UI, and preferrably from Slicer's SimpleColorPalette.\n</p>"
designGuidelines += pStyle + "5. Use face-forward icons where possible and orthographic perspective with 45 degree angles where required.\n</p>"
designGuidelines += pStyle + "6. Avoid gradients and other 3D effects.\n</p>"
designGuidelines += pStyle + "7. Respect stroke, fill and background colors defined in Slicer's SimpleColorPalette for both Dark and Light Themes.\n</p>"
designGuidelines += pStyle + "8. Padding of 2dp is recommended around the icon perimeter.\n</p>"
designGuidelines += pStyle + "9. Preview the Dark and Light Theme versions of your icons on Dark and Light Theme backgrounds and at multiple resolutions.\n</p>"
designGuidelines += pStyle + "10. Remove all hidden or unused vector elements from the SVG file before finalizing work.\n</p>"

# write out document head and close file.
bulkText = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<title> " + titleText + " </title>\n" + cssStyleText + "</head>\n" + bodyStyleText + "<font face=\"verdana\">\n" + headingText + designGuidelines

fileout.writelines(bulkText)
fileout.close()

# now open in append mode for rest
fileout = open(fileName, "a") 

cwd=os.getcwd()
topPath=os.path.abspath(os.path.join(cwd, os.pardir))

if theme=="L" or theme=="l":
    topPath += "/LightThemeIcons"
    delimiter = "LightThemeIcons/"
if theme=="D" or theme=="d":
    topPath += "/DarkThemeIcons"
    delimiter = "DarkThemeIcons/"
    
subDirs = []
iconDirs = []
allIconDirs = []

# find top-level directories
iconDirs = getSubdirectories(topPath)
#DELETE
print (iconDirs)

numIconDirs = len(iconDirs)


# build list with directories and subdirectories in order.
i = 0 
while i < numIconDirs:

    # build list of icon directories and subdirectories.
    allIconDirs.append(iconDirs[i])

    #look for iconDirs with subdirectories
    subDirs = getSubdirectories (iconDirs[i])
    numSubDirs = len(subDirs)

    if numSubDirs > 0:
        j=0
        while j < numSubDirs:
            allIconDirs.append(subDirs[j])
            j+=1
    i+=1

# build text for table title -- use path after either "LightThemeIcons" or "DarkThemeIcons"
numTables = len(allIconDirs)
tableTitles = []
svgFiles = []
iconCaptions = []
i=0
while i < numTables:

    # construct title
    text = allIconDirs[i]
    title = text.split(delimiter, 1)[1]
    tableTitles.append(title)

    # construct list of svgs to render in table
    # and corresponding captions.
    for file in os.listdir(allIconDirs[i]):
        if file.endswith(".svg"):
            svgFiles.append (os.path.join(allIconDirs[i], file))
            iconCaptions.append (file)
    
    # if svg files are in dir, construct table and write out 
    numIcons = len(svgFiles)
    if numIcons > 0:
        # use 10 columns for readability
        cols = 10
        rows = 1
        if numIcons > 10:
            rows = math.trunc(numIcons/cols) + 1
            rows = rows + 1

        # create and write out top of table
        pStyle = "<p style=\"margin-bottom: 40px; margin-top: 40px; margin-left: 30px; width: 100%; font-size:10pt;\">\n"
        toptableText =  pStyle + "<table style=\"border: None; align: justify; cellpadding: 10; cellspacing: 0\n" + "<tr>\n" + "<th colspan = \"10\">" + title + "</th>\n" +  "</tr>\n"
        fileout.writelines(toptableText)

        # embed icons in each table cell and add style to present filename-tooltips
        row=0
        iconCount=0
        while row < rows:
            col=0
            cellText = "<tr>\n"
            while col < cols:
                if iconCount < numIcons:
                    with open (svgFiles[iconCount], "r") as file:
                        svgText=file.read()
                        cellText += "<td class=\"tData CellWithTooltip\"> " + svgText + "<span class=\"CellTooltip\">" + iconCaptions[iconCount] + "</span>\n </td>\n"
                iconCount+=1
                col+=1
            cellText += "</tr>\n"
            fileout.writelines(cellText)        
            row+=1

        #end the table declaration
        endTableText = "</table>\n" + "</p>\n" 
        fileout.writelines(endTableText)

    # Move on to next table
    svgFiles.clear()
    iconCaptions.clear()
    i+=1

# close the rest
bulkText = "</body>\n" + "</html>\n"
fileout.writelines(bulkText)
fileout.close()
