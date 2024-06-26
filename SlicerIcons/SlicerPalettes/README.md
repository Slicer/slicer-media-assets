## Slicer Icon Color Palettes

This file contains information about Slicer Icon Palettes.

1. **SLICER SIMPLE PALETTE (newest addition**) Has a set of only 4 colors that switch between dark and light themes and a limited set of "global" colors that are used across themes -- no changes required. Additional global colors can be added by module authors, and should be chosen to have good appearance in any theme.
   ![image](https://github.com/Slicer/slicer-media-assets/assets/142107139/8d458c3e-ff43-4a73-81eb-a3a85dcfb460)
2. **SLICER BASIC CORE PALETTE THEME/STATE COLOR SWAPS:** Used for basic stroke and flat fill icons.

3. **SLICER EXTENDED CORE PALETTE THEME/STATE COLOR SWAPS:** Fills Used for View Configuration Icons, CoreModuleIcons, and System Messages. 

4. **SLICER CUSTOM PALETTE (for module icon authors**) contains some curated colors for developers to use and extend for Module color-coding accent colors. Other stroke/fill colors may be added to extend this palette. Also recommended to use FILL colors that work for all themes so they can be used without need for swapping.


** NOTE: Adding new custom colors for icons may require updates to the the following items:
        -SlicerCustomPalette.gpl,csv,tsv, or
	-SlicerSimplePalette.gpl,csv,tsv, and
        -This README file.

###  Where to find Slicer Icon Palettes:
Slicer Icon Palettes are provided in Gimp Palette format (.gpl)  https://developer.gimp.org/core/standards/gpl/  and in csv and tsv files. Files can be found here:

github: Slicer/slicer-media-assets/SlicerIcons/SlicerPalettes

 **1. Simple Palette**
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerSimplePalette.gpl
 **2. Basic Palette**
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerBasicPalette.gpl
 **3. Extended Palette**
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerExtendedPalette.gpl
 **4. Custom Palette**
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerCustomPalette.gpl


Combined palettes in csv and tsv are also available.
 **SlicerPalettes combined CSV file**
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerPalettesCSV.csv
 **SlicerPalettes combined TSV file**
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerPalettesCSV.tsv 

### How to use Palettes in Inkscape
The Gimp Palette format (.gpl) files can be imported into Inkscape. Copying the palettes into Inkscape's palettes directory (for instance: Inkscape/Contents/Resources/share/inkscape/palettes, tho this will vary with version and platform) will make them selectable from the palettes menu. 



