
# 3D Slicer Icon Design Guidelines and Resources

This document desribes design guidelines for 3D Slicer Icons in Dark and Light Themes. Helpful resources and a few simple workflows are provided for developers adding Material Symbols Icons to Slicer, creating new icons by adapting Material Symbols Icon designs or directly from scratch.

Links to useful information and resources are as follows:
* Slicer's Palette: <A href="../SlicerPalettes/SlicerSimplePalette.gpl"> GPL format</A>, <A href="../SlicerPalettes/SlicerSimplePalette.csv"> CSV format</A>, <A href="../SlicerPalettes/SlicerSimplePalette.tsv"> TSV format</A>.
* Slicer's Templates: [24x24SlicerIconTemplate], [48x48SlicerIconTemplate] and [Icon documentation Template]
* <A href="https://fonts.google.com/icons"> Google Fonts Material Symbols Icons</A>

---
## Developing Slicer icons from Material Symbols Icons

### Configuring and Downloading
Icons downloaded from Google Fonts Material Symbols Icons may be used as-is or as starting point for a new icon design. In either case, please parameterize your selected icon as follows before downloading:

* Style = Sharp
* Fill = 0
* Grade 0,
* Weight 200,
* Optical Size = 24 (1dp = 1pixel)
* Select parameterized icon and from the dialog box select
  * SVG download
  * Color = #000000 (for Light Theme) AND
  * Color = #E5E5F6 (for Dark Theme)
  * Size = 24 
  * Downlad SVG
  * Rename in a Slicer-compatible way.
 
### Using Material Symbol Icon As-Is or Modifying for Slicer
If using the icon as-is, you're done! Keeping in mind that users may encounter this icon in other software they use, it's good practice to only use this icon to represent the concept it was intended for. To represent a different concept, modify the icon in some distinct way to represent your concept.

### **To modify an existing icon or develop a new one**, very simple svg document templates for Slicer Icons are provided for use with Inkscape or other vector editing applications, and are linked at the top of this document. These templates come with Document Properties set up already, and the padding marked around the icon document's perimeter to guide design. If you choose not to work with a template,remember to respect the 2dpi padding around the perimeter of the icon you are designing and respect the visual design guidelines listed in this document. Some helpful tips are provided below to ensure compatible icon specifications and to support various common workflows.

### Surprises when importing icons generated in a vector editing software **different** than the one you prefere to use.

It's a known issue that some products ignore the scale of SVG files and standard DPI of 96. Wwhen importing or exporting SVG files across different vector editing applications, you'll find the scale of a document may appear different than expected. Do not be surprised if you notice the need to resize a set of imported svg elements in the software you are using. Just take care to resize for pixel-perfect rendering of the icon.

### Basing a Slicer icon on a Material Symbols Icon.

Note: as part of a font library, each Materials Symbols icon is described by a set of closed and filled curves. Designing with the icons configured as above, respecting the drawable area noted on the templates, and using Slicer's palette to create both Light and Dark themed versions will help to keep new icons visually compatible with Slicer's existing application icons. Editing these closed curves can be tricky to do well, so if you're not going to use the icon exactly as-is, you may want to create your own version using it as a guide. If so, please see the Workflow Tips and the Visual Design Recommendations below.

### Using one of Slicer's 24x24 px template with a Material Symbols Icon.

Open Slicer's 24x24IconTemplate template (in which 1dp = 1 pixel) in the design software of your choice (specific advice will be given for Inkscape V1.3). Then import the svg into that template.  The template includes a frame that indicates padding, the content-free 2dp perimeter; content should be designed to fit within the 20x20dp space enclosed by the padding. If necessary, visual elements (like the tip of an arrow) can sneak into the padding. No content should extend entirely to the edge, or into the trim (beyond the edge).

To create a LightTheme version of your icon, select all visual elements and set their fill color to Slicer's Default Light Theme Stroke #000000. To create a DarkTheme version of your icon, select all visual elements and set their fill color to Slicer's Default DarkTheme Stroke #E5E5F6. Finally, when you are finished with your design, the padding should be deleted before saving the new icon SVG.

---
## Basing a new icon on an existing Slicer Icon.
Slicer SVG icons may be saved as a 24x24 pixel icon, or as a 48x48 pixel icon. When you open this file in your vector editing software, you may need to proportionately resize it to conform to your desired working resolution. 

---
### Creating Slicer Icons from Scratch using a template

If using Inkscape, helpful tips for configuring Inkscape and importing Slicer's SimpleColorPalette are below.

If using SVG-Edit, some helpful tips for setting Document Properties and Editor Preferences are given, but it's mostly self-explanatory.

---
## Visual appearance guidelines

Slicer's most basic application UI icons are derived from Material Symbols Icons. To realistically accommodate the large and diverse community of 3D Slicer contributors without an onboard icon designer, we recommend referring to the <A href="https://m3.material.io/styles/icons/designing-icons" Material-IO design principles</A> as a touchstone and inspiration, but don't require rigid adherance.  

At a minimum, respecting the following 10 recommendations will help keep new designs consistent with the appearance of existing set of Slicer Application Icons:

1. Design icons on a transparent background.
   
2. At 24x24 pixel resolution, stroke width should be 1 dp = 1 px. This will insure pixel-perfect rendering at resolution multiples of 24x24.

3. Use simple stroked elements without fill where possible.

4. If filled elements are required, use limited color, preferrably from Slicer's palette, consistent across your UI and compatible with Slicer's application UI.

5. Use face-forward icons where possible and orthographic perspective with 45 deg angles where required.

6. Avoid gradients and other 3D effects.
   
7. Respect the stroke, fills and backgrounds colors specified in Slicer's palette for both Dark and Light Themes. 
   
8. Padding of 2dp is recommended around the icon perimeter. Slicer templates indicate the 2dp padding for guidance.
   
9. Preview the Dark and Light Theme versions of your icon on Dark and Light Theme backgrounds and at multiple resolutions to insure they look good.

10. Delete padding object (if using template) and all hidden or unused visible elements before finalizing your work.

---
## Tips for designing in Inkscape V1.3: 

* SIZE 24x24px: Slicer's 24x24IconTemplate can be used if desired. Slicer's icons are based on a 24x24dp minimum pixel-perfect size. At this resolution 1dp=1pixel, so stroke width should be 1px.

* SIZE 48x48px: A 48x48IconTemplate is also provided, and developers who prefer to work in this space should take care to ensure that all element metrics scale properly down to pixel-perfect 24x24dp resolution. For instance, stroke widths of 1px in 24x24 pixel icon should be 2px in a 48x48 pixel icon.

### 1. IMPORT SLICER'S PALETTE

**Before opening Inkscape**, it's useful to import Slicer's SlicerSimplePalette. This is accomplished by copying SlicerSimplePalette.gpl (in GIMP Palette Format) into Inkscapes palettes directory. Different versions of Inkscape locate the palettes subdir differently. For Inkscape 1.3, it can be found using this path under the Inkscape install: Inkscape(root)/Contents/Resources/share/inkscape/palettes/. Different Versions and different platform installs may be slightly different. Inkscape discovers Slicer's palette on startup, and it can be selected using the palette selector button at the bottom right of Inkscape's menu:

<img src="https://github.com/user-attachments/assets/a8bf9222-2fe5-4d08-8442-f5f545186a23" width="200">

### 2. SET USEFUL INKSCAPE PREFERENCES:

**Before opening or importing an existing SVG file**, It's useful to configure some basic Inkscape Settings. Below are tips for setting basic units, workspace dimensions, interaction and document properties, and creating grids to guide “pixel-perfect” design. The Inkscape Preferences menu is available under Inkscape->Settings. Preferences that are particlarly useful -- some that avoid irritating problems and some that you'll probably revisit often as you work -- are included below:

* Inkscape->Preferences->Imported Images: make sure SVG import mode is set to “include”.
* Inkscape->Preferences->Imported Images: make sure that import and export resolution is the standard 96 dpi.
* Inkscape->Preferences->Imported Images: select 'Ask about linking and scaling when importing'.
* Inkscape->Preferences->Interface->Grids: set the grid units to px; and set Origin X and Y = 0.0, Spacing X and Y = 1.0, and a grid line every 1 px.
* Inkscape->Preferences->Interface->Color Selector: choose the types of color selectors you'd like to have access to.
* Inkscape->Preferences->Behavior->Steps: set/re-set arrow key translation & rotation metrics to match the kind of big or small nudges you need.

### 3. SET INKSCAPE DOCUMENT PROPERTIES

If you're using one of Slicer's templates, the following Document Properties should already be set. If you are starting from scratch, the Document Properties menu is available under File->Document Properties. Some useful properties are:

**In the Document Properties->Display Tab:**

* set resolution to 24x24 and units to pixels:
* make sure Scale = 1.0
* make sure Viewbox is configured with X=0, Y=0, width=24, height=24

**In the Document Properties->Grids Tab:**

  * Create a rectangular grid
  * Check Enabled, Visible, and Snap to visible.
  * Make sure grid units are set to pixels.
  * If not specified in Inkscape Preferences already, set Origin X and Y = 0.0, Spacing X and Y = 1.0, and select a grid line every 1 unit.

---
* ----WORK IN PROGRESS----


