
# 3D Slicer Icon Design Guidelines

Below is a brief design specification for 3D Slicer Icons in Dark and Light Themes. A simple workflow is provided for developers creating new icons from scratch, or incorporating Google Fonts Material Symbols Icons.

Links to additional useful information and resources are as follows:
* Slicer's Palette: <A href="../SlicerPalettes/SlicerSimplePalette.gpl"> GPL format</A>, <A href="../SlicerPalettes/SlicerSimplePalette.csv"> CSV format</A>, <A href="../SlicerPalettes/SlicerSimplePalette.tsv"> TSV format</A>.
* Slicer's Templates: [24dp Icon Template], [48dp Icon Template] and [Icon documentation Template]
* <A href="https://fonts.google.com/icons"> Google Fonts Material Symbols Icons</A>

## Developing new Slicer icons using Material Symbols Icons

Icons downloaded from Google Fonts Material Symbols Icons may be used as-is or as starting point for a new icon design. If basing a new design on one of the Material Symbols Icons, please parameterize your selected icon for download as follows:

* Style = Sharp
* Fill = 0
* Grade 0,
* Weight 200,
* Optical Size = 48
* Select parameterized icon and from the dialog box select
  * SVG download
  * Color = #000000
  * Size = 24
  * Downlad SVG

## Designing with a Material Symbols Icon using the Slicer Icon template.

Depending on your resolution preference for designing the icon, open either Slicer's 24dp template or Slicer's 48dp template in the design software of your choice. Then import the svg into that template. If using the 48dp template, scale the entire icon by 200%. Note: as part of a font library, each icon is described by a set of closed and filled curves. Designing with the icons configured above, respecting the drawable area noted on the templates, and using Slicer's palette to create both Light and Dark themed versions will help to keep new icons visually compatible with Slicer's existing application icons.

Editing these curves can be tricky, so if you're not going to use the icon exactly as-is, you may want to use it as a temporary guide for creating your own version using simple vector elements. If so, please also see the New Icon Design Recommendations below.

## Visual appearance guidelines

The project subscribes to the <A href="https://m3.material.io/styles/icons/designing-icons" Material-IO design principles</A>. Because of the number of icons in the Slicer application interface and the complexity of some of the concepts that Slicer's icons represent, the design guidelines allow the use of multiple colors in a limited palette, and the use of icon element fill where the developer feels it is necessary. A spare set of recommendations follow. Respecting these will keep new icons consistent with the appearance of existing set of Slicer Application Icons.

###1. Icon metrics

* SIZE 24x24dp: Slicer's icons are based on a 24x24dp minimum pixel-perfect size. A content-free perimeter of 2dp should be respected; content should be designed to fit within the 20x20dp space enclosed by the padding. If necessary, visual elements (like the tip of an arrow) can sneak into the padding. No content should extend entirely to the edge, or into the trim (beyond the edge). The 24dpIconTemplate includes a frame that marks off the padding. This frame object should be deleted before saving the final Icon's design.
*
* SIZE 48x48dp Template: A 48dpIconTemplate is also provided, and developers who prefer to work in this space should take care to ensure that all element metrics scale properly down to pixel-perfect 24x24dp resolution. For instance, stroke widths of 1dp in 24x24dp icon should be 2dp in a 48x48dp icon.
  
* CORNERS:
  
* STROKE:
  
* PERSPECTIVE:
  
* COMPLICATED SHAPES: If an icon requires complex details, subtle metric adjustments can be made to improve legibility. Material.io refers to these adjustments as optical corrections. Any optical correction should use the geometric forms on which all other icons are based, without skewing or distorting those shapes.





## Notes on configuring SVG-Edit for icon design.

One simple web tool for easy vector image design is <A href="https://svgedit.netlify.app/editor/index.html"> SVG-Edit</A>. SVG-edit is a fast, web-based, JavaScript-driven SVG drawing editor with basic functionality that works in any modern browser. It can be easily configured and used to create new, or modify existing icons for Slicer. 

## Notes on configuring INKSCAPE for icon design.

### 1. IMPORT SLICER'S PALETTE

**Before opening Inkscape**, it's useful to import Slicer's SlicerSimplePalette. This is accomplished by copying SlicerSimplePalette.gpl (in GIMP Palette Format) into Inkscapes palettes directory. Different versions of Inkscape locate the palettes subdir differently. For Inkscape 1.3, it can be found using this path under the Inkscape install: Inkscape(root)/Contents/Resources/share/inkscape/palettes/. Different Versions and different platform installs may be slightly different. Inkscape discovers Slicer's palette on startup, and it can be selected using the palette selector button at the bottom right of Inkscape's menu:

<img src="https://github.com/user-attachments/assets/a8bf9222-2fe5-4d08-8442-f5f545186a23" width="200">

### 2. SET SOME USEFUL INKSCAPE SETTINGS PREFERENCES

**Before opening or importing an existing SVG file**, It's useful to configure some basic Inkscape Settings. Below are tips for setting interaction and document properties, and creating grids to guide “pixel-perfect” design. The preferences menu is available under Inkscape->Settings. Preferences that are particlarly useful are:

* Inkscape->Preferences->Imported Images: make sure SVG import mode is set to “include”.
* Inkscape->Preferences->Imported Images: if required, here is where you set default import/export resolutions.
* Inkscape->Preferences->Interface->Grids: set the grid units to px; and set up a grid you like here.
* Inkscape->Preferences->Interface->Color Selector: choose the types of color selectors you'd like to have access to.
* Inkscape->Preferences->Behavior->Steps: set arrow key translation & rotation metrics.

### 3. SET INKSCAPE DOCUMENT PROPERTIES

Once you open an SVG file, confirm that your Document Properties are good to go:

* In File->Document properties, under the Display Tab, set resolution and units:
* ----WORK IN PROGRESS----
Set up your page format to be “Custom”, 
Set your Page units to be pixels 
Set your Display units to be pixels 
Set the Document width & height to match whether you are using Slicer's 24dp template or Slicer's 48dp template. (depends on lowest resolution for Slicer and what multiples of it we need) [For example, choose 24 for Material Symbol Icons if 24x24dp is chosen].
Choose 1.0 for Scale (“pixels per user unit”)
Open the Viewbox settings and choose X=Y=0.0; width & height [24] to create a display viewport that includes the whole document.

In File->Document properties, under the Grids Tab, set up grids to delineate sets of pixels that will scale down to a single pixel when the icon is resized to its lowest resolution. For Material Symbols Icons at opsz 24:  
Create grid1 with lines spaced by 1px and origin X,Y = 0,0; then
Create grid2 with lines spaced by 1px, and origin X,Y = 0.5px. This puts grid2 marks in the center of each pixel. Render the grid2 with dots for readability.
For each grid, check enable, visible, and enable snap to visible grid.

To reduce off-grid errors and for convenience, set arrow key increments for translation and rotation:
In Inkscape->Preferences->Behavior->Steps, set “arrow keys move by” to be half a grid space 0.5px.
In Inkscape->Preferences->Behavior->Steps, also set “rotation snaps” to be 15 degrees.

In File->Document properties, under the Color Tab, set up the correct color profile:
Inkscape’s default color profile is sRGB (Inkscape’s default)
Inkscape’s color profile functionality is brittle, so if you haven’t ever changed it, for print or whatever, just leave it alone.



<!--- list all symbolic patterns that NEW icons in this set should adhere to -->

## Icon set symbolics

* ** visual element 1

* ** visual element 2

* ** ...

* ** visual element N
  
<!--- Optional: provide screen shot of icons included in this set.-->

## Full Icon set for Slice Viewers Dark and Light Themes:

Light & Dark Theme 



<!--- if relevant, provide current table of Dark Theme versions of svg image data -->

|Icon SVG |Name |
|-----|--------|
| link to A.svg | A |
| link to B.svg | B |
| ... | ... |
| link to N.Svg | N |


<!--- if appropriate, include any special colors used in image data that NEW icons in this set should use -->

<!--- note whether they have been included in SlicerSimplePalette, and if they are SWAP|GLOBAL. -->

## Specific Colors included in SlicerSimplePalette

ColorName1 (SWAP / LightTheme):
* HEX #000000

ColorName1 (SWAP / DarkTheme):
* HEX #ffffff

ColorName2 (GLOBAL / Both themes):
* HEX #123456



