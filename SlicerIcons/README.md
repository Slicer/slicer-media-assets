
## Contents Overview
This directory is a sandbox for Slicer icon design.
Current designs are limited-color stroke and flat fill.

### DIRECTORIES, IMPORTANT FILES AND WHERE TO FIND THEM:

### Icon Design Guidelines
Once technical requirements are solidified, design guidelines for icons that meet them will be provided in 

./SlicerIconDesignGuidelines



---


### Icon Templates
Icon templates will be provided for Inkscape and svg-edit desktop and web apps. Currently, multiple versions are provided, pending choice of rendering approach for theme changes:

./SlicerSVG/LayeredStyles/IconTemplate/SlicerIconTemplate.svg

./SlicerSVG/SeparateStyles/LightThemeIcons/IconTemplate/SlicerIconTemplate.svg

./SlicerSVG/SeparateStyles/DarkThemeIcons/IconTemplate/SlicerIconTemplate.svg

./SlicerSVG/QStyles/IconTemplate/SlicerIconTemplate.svg

All icons were designed using Inkscape 1.3 (0e150ed, 2023-07-21). 



---

### Icon Color Palettes
Basic, Extended, and Custom palette files are in 

./SlicerPalettes


---

### Icon Sandbox Directories
./SlicerSVG contains separate versions of icons for use in different approaches to switching themes within Slicer. These versions are in flux. Briefly:

./SlicerSVG/SeparateStyles includes Light Theme Enabled icons AND Dark Theme icons that can be used with QIconFromTheme and Qt's existing framework for changing icons upon theme switch. For now, likely low performance, and easiest for icon authors.
 
./SlicerSVG/Qstyles includes Light Theme icons only, intended for use with CSS classes, QSS or some other way to style icons.

./SlicerSVG/LayeredStyles includes Multi-theme/state icon files comprised of grouped Light-enabled, Light-disabled, dark-enabled, dark-disabled versions of the icon. 


