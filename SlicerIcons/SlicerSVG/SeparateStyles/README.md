## Separate versions of Light Theme and Dark Theme icons.

### SLICER

**LightThemeIcons/** directory contains icons for display on a white Slicer background (#ffffff). 

**DarkThemeIcons/** directory contains corresponding icons for display on a dark slicer background (#121212).

Slicer core icons use the **basic**, **extended** and **custom** palettes. For individuals contributing additional icons, it is recommended they be:

*     simple as possible, 
*     adhere to the basic palette and "link to: design guidelines"
*     use / extend custom palette minimally to add module "acccent" color.
*     rely on inline styles only where possible.


#### Pros/Cons of using separate svgs for themes.
**Cons:**
* whether this kind of switching will be slow with so many icons.
* application bloat from keeping multiple themed svgs for each icon 

**Pros:**
* seems like Qt has framework for doing this. 
* It's also possible that users will not switch between themes often enough for this to negatively impact user usability/experience.
* Makes using color to help distinguish related icons easier (monochromatic icons tend to start looking self-similar).

## Options for theme switching in Qt
**Other theme switching options** are being explored for changing icon svg colors in a more performative way. Below are NOTES for: **A.** Using existing Qt framework for switching light/dark icons when a theme change is requested; **B.** editing light and dark theme svgs to insert style classes and put them on appropriate graphic elements, store both in memory as QByteArray for later switching; **C.** Using with QVariantList -- or Qt Advanced Stylesheets; and **D.** Using light theme icons to **derive** a dark theme versions at startup, and **storing both** in memory for switching.


## A. Using light and dark svgs within existing Qt framework:

A1. USE SPECIFIC DIRECTORY STRUCTURE. Create Custom Icon library (using Freedesktop Icon Theme specification)

Icons and themes are organized in and searched for in **specific directories**. By default, apps look for themed icons in $HOME/.icons, but a "custom theme" and its directory can be specified and should override. 

Create and name directory for custom icons whose subdirectory structure looks like this:
   
<img width="254" alt="directoryStructureExample" src="https://github.com/Slicer/slicer-media-assets/assets/142107139/dfac027f-f9da-4e1c-baa5-d53d9e2ce291">

A2. CREATE THEME INDEX FILES. Index files for the light and dark themes (above, light.theme and dark.theme) define various aspects of the theme.

For example, a "dark" theme index definition file:

> [Icon Theme]
> Name=dark
> Comment=dark theme icons

> 
> PanelDefault=22
> PanelSizes=22
> 
> Directories=svg,png
> 
> [svg]
> Size=48
> Context=Applications
> MinSize=16
> MaxSize=128
> Type=Scalable

    
A3.SPECIFY ALL ICONS AND INDEX.THEME FILES IN APPLICATION RESOURCE FILE. For example:

> <RCC>
>     <qresource prefix="/">
>         <file>icons/dark/index.theme</file>
>         <file>icons/light/index.theme</file>
>         <file>icons/light/svg/check.svg</file>
>         <file>icons/light/png/check.png</file>
>         <file>icons/light/png/cancel.png</file>
>         <file>icons/dark/png/check.png</file>
>         <file>icons/dark/png/cancel.png</file>
>         <file>icons/dark/svg/check.svg</file>
>     </qresource>
> </RCC>


A4.  SOME STUFF TO SET UP FOR EACH ICON: 

> ...
> QIcon.setThemeSearchPaths -- path to custom icons
> QIcon.setThemeName ("light") or ("dark")
> QIcon.fromTheme (QIcon selectColorIcon QIcon::fromTheme(QIcon::ThemeIcon SlicerSelectColorIcon))
> QIcon.addFile(SlicerSelectColor.svg...)
> 

A5. OBVSERVE FOR THEME CHANGE EVENT. 

Changing theme should trigger a QEvent::StyleChange event;To toggle theme for icon, each icon should observe for a QEvent::StyleChange event.
 
Its callback function should include:
 QIcon::setthemeName ("dark") or ("light") in response.
 Does the icon need to be redisplayed? 

    bool darkMode = false;
    if ( darkMode )
    {
	...
        QIcon::setThemeName("dark");
    }
    else
    {
	...
        QIcon::setThemeName("light");
    }
    customIcon.show();

## B. Editing light and dark versions of svg to specify internal css classes or variables and apply them to appropriate graphic elements. 

These classes are based on Slicer's palettes would be:
* copied into the DEFS section of any created svg file.
* applied to the default light theme icon's graphic elements.
* then used to programatically derive a dark (or disabled state) icon by editing the defs to replace light theme colors with corresponding dark theme colors from Slicer palettes.

REQUIRES MINIMAL EDITING OF ANY CREATED SVG.  Example of class definitions and application to graphic elements: 

```
<svg height="100" width="100">
    <defs 
             # replace the light stroke color with dark stroke color from palettes below...
            .STROKE_BasicStroke {
                # BasicStroke Light Theme
                stroke: #000000
                #BasicStroke Dark Theme
                #stroke: #E2E2EF;
            }
            .FILL_BasicFill {
                # BasicFill Light Theme
                fill: #E5E5FF;
                #BasicFill Dark Theme
                #fill: #99A2E3;
            }
            .STROKE_BasicAccent1 {
                # BasicAccent1 Stroke Light Theme
                stroke: #010101;
                # BasicAccent1 Stroke Dark Theme
                #stroke: #010101;
            }
             .FILL_BasicAccent1 {
                # BasicAccent1 Fill Light Theme
                fill: #010101;
                # BasicAccent1 Fill Dark Theme
                #fill: #010101;
            }
            .FILL_ExtendedPlotViewerGreen {
                #PlotViewerGreen Fill Light Theme
                fill: #03b42d;
                #PlotViewerGreen Fill Dark Theme
                fill: #03b42d;
            }
            ....and so on...
    </defs>

    <circle cx="50" cy="50" r="40" class="STROKE_BasicStroke" fill="None"/>
    --or--
    circle cx="50" cy="50" r="40" class="FILL_BasicAccent1" stroke="None" />
</svg>
```
## C. QVariantList or Qt Advanced Stylesheets?
1. A QVariant object can hold a value of many different types, such as int, double, QString, and more. The QVariantList can be useful when working with heterogeneous data and allows for storing different types of data in one container. Could be used for keeping themed icon QByteArrays (dark/light/other) created at startup; then index/redisplay on theme/state change.

2. Advanced stylesheets for Qt? https://marketplace.qt.io/products/qt-advanced-stylesheets

## D. Using color changing logic to derive dark theme version from light theme.

If retrieving separate files from disk on theme change is not performative:

Color swapping logic to generate Dark Theme FROM Light Theme icons is described below. This approach would replace colors in a the XML-parsed version of a Light Theme's SVG with corresponding palette colors for the Dark Theme (and also corresponding disabled states if desired). Versions of the parsed XML trees can be stored as QbyteArrays and sent to svg renderer. [**Challenge:** would be cumbersome to cover all possible specifications of style in SVG...]
    
To swap colors to render a Light Theme icon in it's Dark theme and disabled states in both themes:
At application startup:

1. Parse original (light theme) svg xml using something like python lxml.etree.
1. Use etree.deepcopy to create a version for editing into a dark theme version.
1. Use logic below to create dark theme XML tree.
1. Translate Light and Dark XML trees into easily displayable form (like QByteArrays...LightIconBytes DarkIconBytes)
1. Redisplay with SvgRenderer when theme is changed.
1. Same approach can also be used for light/disabled and dark/disabled theme/states.


**Challenges:** SVG format is quite variable in how styles are specified internal to the svg. Further, some very compact icon libaries have  styles stripped out and rely on external styling or default rendering (black) if none are specified. So there are lots of cases to look for to understand and recreate an author's intent.

**An icon testing utility will be essential** for icon authors to test their icon in light and dark mode using this logic should be available to avoid surprises.

**NOTES on Logic to try:**
Assume a requirement for icons is to use simple internal style specification. No CSS selectors and no css classes. Within a copy of the original LightTree (from parsed xml), search for where style specification is found:

* inline 
* presentation atts
* internal css within a style element
* other

Given the priority order of the style cascade, treat each of the graphic elements specified (rect circle, ellipse, line, marker, path, polygon, polyline, rect, symbol, ...) so that an **overriding** inline style definition specifies new fill and stroke colors. 

Save changed document as DarkTree. Save both Light and Dark Trees as QByteArrays to be sent to QSvgRenderer when necessary:

> xmlstr = ElementTree.tostring(lightTree, encoding='utf8')

This produces a bytestring, which in Python 3 is the bytes type. [Might need other encoding for Python <3]

Send modified SVG to SvgRenderer.

#### Go from Light/Enabled to Dark/Enabled Pseudocode
```
For each graphic element in original LIGHT THEME SVG:
   1. If CUSTOM/EXTENDED COLOR HANDLING (see below) returns false
   {
      #--- replacing inline fill/stroke attribute values
      #--- or presentation attributes, 
      #--- or creating inline attr=vals if no internal style is defined.
      
      #--- INLINE STROKES
      If element's inline style contains a "stroke" attribute that does NOT have a value of "None"
      {
         IF original stroke is LightEnabledAccent1, 
             change stroke to DarkEnabledAccent1.
 	      ELSE IF original stroke is LightEnabledAccent2
 	          change stroke to DarkEnabledAccent2.
           -ELSE  
             change stroke to DarkEnabledBasicStroke
      }
      
      #--- INLINE FILLS
      If element's inline style contains a "fill" attribute that does NOT have a value of "None"
      {
         IF original fill is LightEnabledAccent1, 
             change fill to DarkEnabledAccent1.
 	      ELSE IF original fill is LightEnabledAccent2
 	          change fill to DarkEnabledAccent2.
           -ELSE  
             change fill to DarkEnabledBasicFill
      }
      
      #--- PRESENTATION FILL/STROKE 
      If element has NO inline style, look for presentation attributes. parse and use regex for style definition within each graphic element to extract fill & stroke.
      {
         #---same logic as above; either update presentation attributes or add inline attrib/value pairs
      }

      #--- adding stroke if no internal style specified.
      If element has NO inline style and no presentatation attributes
      {
      for each graphic element, set stroke to DarkEnabledBasicStroke.
      }
    }    
```
