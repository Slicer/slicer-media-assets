## Slicer Icon Color Palettes

This file contains information about Slicer Icon Palettes.

1. **BASIC CORE PALETTE THEME/STATE COLOR SWAPS:** Used for basic stroke and flat fill icons.

2. **EXTENDED CORE PALETTE THEME/STATE COLOR SWAPS:** Fills Used for View Configuration Icons, CoreModuleIcons, and System Messages. 

3. **CUSTOM PALETTE (for module icon authors**) contains some curated colors for developers to use and extend for Module color-coding accent colors. Other stroke/fill colors may be added to extend this palette. Also recommended to use FILL colors that work for all themes so they can be used without need for swapping.

3. **SIMPLE PALETTE (newest addition**) Has a small color palette for dark and light themes and a global palette that requires no changes when changing themes.

** NOTE: Adding new custom colors for icons may require updates to the the following items:
        -SlicerCustomPalette.gpl,csv,tsv, or
	-SlicerSimplePalette.gpl,csv,tsv, and
        -This README file.

###  Where to find Slicer Icon Palettes:
Slicer Icon Palettes are provided in Gimp Palette format (.gpl)  https://developer.gimp.org/core/standards/gpl/  and in csv and tsv files. Files can be found here:

github: Slicer/slicer-media-assets/SlicerIcons/SlicerPalettes

 **1. Basic Palette**
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerBasicPalette.gpl
 **2. Extended Palette**
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerExtendedPalette.gpl
 **3. Custom Palette**
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerCustomPalette.gpl
 **4. SimplePalette**
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerSimplePalette.gpl

Combined palettes in csv and tsv are also available.
 **SlicerPalettes combined CSV file**
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerPalettesCSV.csv
 **SlicerPalettes combined TSV file**
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerPalettesCSV.tsv 

### How to use Palettes in Inkscape
The Gimp Palette format (.gpl) files can be imported into Inkscape. Copying the palettes into Inkscape's palettes directory (for instance: Inkscape/Contents/Resources/share/inkscape/palettes, tho this will vary with version and platform) will make them selectable from the palettes menu. 

###ToDo: add simple palette here.

### Color Palette Table

| Palette  | ColorName               | Light/Enabled | Dark/Enabled | Light/Disabled| Dark/Disabled |
| -------- | ---------               | ------------- | ------------ | ------------- | ------------- | 
| BASIC    | Background              | #ffffff       | #121212      | #ffffff       | #121212       |
| BASIC    | BasicStroke             | #000000       | #e5e5f6      | #b2b2b2       | #666666       |
| BASIC    | BasicFill               | #e5e5ff       | #99a2e3      | #e8e8ff       | #808080       |
| BASIC    | Accent1                 | #010101       | #010101      | #b2b2b2       | #707070       |
| BASIC    | Accent2                 | #b8b8ff       | #5b5b7d      | #cccccc       | #666666       |
| EXTENDED | PassThroughWhite        | #ffffff       | #ffffff      | #cccccc       | #666666       |
| EXTENDED | PassThroughBlack        | #010101       | #010101      | #cccccc       | #666666       |
| EXTENDED | SlicerDarkestBlue       | #5b5b7d       | #5b5b7d      | #cccccc       | #666666       |
| EXTENDED | SlicerDarkBlue          | #787bbb       | #787bbb      | #cccccc       | #666666       |
| EXTENDED | SlicerMediumBlue        | #9a9ad6       | #9a9ad6      | #cccccc       | #666666       |
| EXTENDED | SlicerCoolBlue          | #99a2e3       | #99a2e3      | #cccccc       | #666666       |
| EXTENDED | ThreeDViewerBlueLight   | #ededfe       | #ededfe      | #cccccc       | #666666       |
| EXTENDED | CompareViewerOrange     | #ededfe       | #ededfe      | #cccccc       | #666666       |
| EXTENDED | SliceViewerYellow       | #f7ce63       | #f7ce63      | #cccccc       | #666666       |
| EXTENDED | SliceViewerRed          | #d53f37       | #d53f37      | #cccccc       | #666666       |
| EXTENDED | SliceViewerGreen        | #8ed595       | #8ed595      | #cccccc       | #666666       |
| EXTENDED | SliceViewerLightGrey    | #e5e5e5       | #e5e5e5      | #cccccc       | #666666       |
| EXTENDED | SliceViewer Grey        | #bfbfbf       | #bfbfbf      | #cccccc       | #666666       |
| EXTENDED | PlotViewerBlue          | #00a1e8       | #00a1e8      | #cccccc       | #666666       |
| EXTENDED | PlotViewerRed           | #e82b1f       | #e82b1f      | #cccccc       | #666666       |
| EXTENDED | PlotViewerOrange        | #f28a24       | #f28a24      | #cccccc       | #666666       |
| EXTENDED | PlotViewerGreen         | #03b42d       | #03b42d      | #cccccc       | #666666       |
| EXTENDED | ErrorMessageRed         | #d53F37       | #d53f37      | #cccccc       | #666666       |
| EXTENDED | WarningMessageYellow    | #f7ce63       | #f7ce63      | #cccccc       | #666666       |
| EXTENDED | ConfirmMessageGreen     | #8ed595       | #8ed595      | #cccccc       | #666666       |
| EXTENDED | InformationMessageBlue  | #7396df       | #7396df      | #cccccc       | #666666       |
| EXTENDED | SegmentEditorModuleGreen| #a4c5ac       | #a4c5ac      | #cccccc       | #666666       |
| EXTENDED | MarkupsModuleRed        | #de4d4d       | #fd5959      | #cccccc       | #666666       |
| EXTENDED | GreyFiftyPercent        | #808080       | #808080      | #cccccc       | #666666       |
| EXTENDED | GreySixtyPercent        | #989898       | #989898      | #cccccc       | #666666       |
| EXTENDED | GreySeventyPercent      | #b2b2b2       | #b2b2b2      | #cccccc       | #666666       |
| CUSTOM   | DarkGreen               | #64b381       | #64b381      | #cccccc       | #666666       |
| CUSTOM   | MediumGreen             | #8cc497       | #8cc497      | #cccccc       | #666666       |
| CUSTOM   | LightGreen              | #badfc3       | #badfc3      | #cccccc       | #666666       |
| CUSTOM   | DarkCyan                | #6bacc2       | #6bacc2      | #cccccc       | #666666       |
| CUSTOM   | MediumCyan              | #8cb4c2       | #8cb4c2      | #cccccc       | #666666       |
| CUSTOM   | LightCyan               | #afced8       | #afced8      | #cccccc       | #666666       |
| CUSTOM   | GreyedRed               | #d75c58       | #d75c58      | #cccccc       | #666666       |
| CUSTOM   | Brown                   | #d5b59d       | #d5b59d      | #cccccc       | #666666       |
| CUSTOM   | DarkOrange              | #f1a16e       | #f1a16e      | #cccccc       | #666666       |
| CUSTOM   | WarmOrange              | #ffb763       | #ffb763      | #cccccc       | #666666       |
| CUSTOM   | Yellow                  | #f7e08f       | #f7e08f      | #cccccc       | #666666       |
| CUSTOM   | LightYellow             | #f7e3bba      | #f7ebba      | #cccccc       | #666666       |
