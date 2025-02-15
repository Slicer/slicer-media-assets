## Slicer Icon Color Palette

This file contains information about the Slicer Icon Palette.

 **SLICER SIMPLE PALETTE:** Has a set of 11 "SWAP" colors that switch between dark and light themes and a limited set of "GLOBAL" colors that are used across themes -- no changes required. Additional global or swap colors can be added by module authors, and should be chosen:
 
* to have good appearance in both themes, and
* to NOT duplicate colors already in the palette.

 **USING THIS PALETTE FOR DARK AND LIGHT THEMES:** Note that ***GLOBAL*** colors will remain the same when the theme is changed between Light and Dark. ***SWAP*** colors come in Light/Dark Theme pairs. These colors are switched in each icon when the theme changes.

<img width="734" alt="SlicerSimplePalette-01-15-25" src="https://github.com/user-attachments/assets/9388fb44-a932-40cb-ab83-4b4593453b77" />

** NOTE: Adding new custom colors for icons may require updates to the the following items:

* SlicerSimplePalette.gpl,csv,tsv files, 
* This README file,
# The image of the color palette table above (which can be generated from the csv or tsv files).

###  Where to find Slicer Icon Palettes:
Slicer Icon Palette are provided in Gimp Palette format (.gpl)  https://developer.gimp.org/core/standards/gpl/  and in csv and tsv files. The palette directory and file can be found here:

* github: Slicer/slicer-media-assets/SlicerIcons/SlicerPalettes
* Simple Palette: ../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerSimplePalette.gpl

Combined palettes in csv and tsv are also available.

 * csv: ../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerPalettesCSV.csv
 
 * tsv: ../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerPalettesCSV.tsv 

### How to use Palettes in Inkscape
The Gimp Palette format (.gpl) files can be imported into Inkscape. Copying the palettes into Inkscape's palettes directory  (for instance: Inkscape/Contents/Resources/share/inkscape/palettes, though this location will vary with version and platform) will make them selectable from the palettes menu. 



