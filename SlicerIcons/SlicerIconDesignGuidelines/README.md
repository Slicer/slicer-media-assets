
# 3D Slicer Icon Design Guidelines, Resources and Workflow Tips for New Designs

This document desribes design guidelines for 3D Slicer Icons in Dark and Light Themes. Helpful resources and a few simple workflows are provided for developers adding Material Symbols Icons to Slicer, creating new icons by adapting Material Symbols Icon designs or directly from scratch.

Links to useful information and resources:
* Slicer's Palette can be found in:
  * GPL format: Slicer/slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerSimplePalette.gpl,
  * CSV format: Slicer/slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerSimplePalette.csv, and
  * TSV format: Slicer/slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerSimplePalette.tsv.
* Slicer's Templates for documenting icons, can be copied from the following and used in a new module directory:
  * Slicer/slicer-media-assets/SlicerIcons/SlicerTemplates/README.md"
    
---
## Visual appearance guidelines

Slicer's most basic application UI icons are derived from Material Symbols Icons. To realistically accommodate the large and diverse community of 3D Slicer contributors without an onboard icon designer, we consider the <A href="https://m3.material.io/styles/icons/designing-icons" Material-IO design principles</A> a touchstone and inspiration, **but don't require rigid adherance**.  

Following this simple set of **10 recommendations** will help keep new designs consistent with the appearance of existing set of Slicer Application Icons:

1. Design 3D Slicer icons as vector images on a transparent background. Reuse existing Slicer symbols for data and concepts, symbolic colors and other UI patterns where appropriate.
   
2. At 24x24 pixel resolution, stroke width should be 1 dp = 1 px. This will insure pixel-perfect rendering at resolution multiples of 24. Most of 3D Slicer's icons are designed at 200% scale, at 48x48 pixel resolution, with 1dp=2px.

3. Use simple stroked elements without fill where possible. Stroke caps and corners can be sharp or rounded with r = dp/2.

4. If filled elements are required, use limited color, preferrably from Slicer's SimpleColorPalette, consistently across your UI and compatibly with Slicer's application UI. Ensure the fill color works well in both Dark and Light themes.
   
5. Respect the stroke, fill and backgrounds colors as defined and named for use in Slicer's SimpleColorPalette for both Dark and Light Themes. 

6. Use face-forward icons where possible and orthographic perspective with 45 deg angles where required.

7. Avoid gradients, shadows and other 3D effects.
   
   
8. Padding of 2dp is recommended around the icon perimeter. 
   
9. Preview the Dark and Light Theme versions of your icon on Dark and Light Theme backgrounds and at multiple resolutions to ensure they look great.

10. Ensure all hidden or unused visible elements are removed from the SVG file before finalizing your work.


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
 
### Using Material Symbol Icon As-Is 
If using the icon as-is, you're done! Keeping in mind that users may encounter this icon in other software they use, it's good practice to only use this icon to represent the concept it was intended for. To represent a different concept, modify the icon in some distinct way to represent your concept.

### Basing a Slicer icon on a Material Symbols Icon.

Note: as part of a font library, each Materials Symbols icon is described by a set of closed and filled curves. Designing with the icons configured as above, respecting a 2dp padding around the perimeter of the icon, and using Slicer's palette to create both Light and Dark themed versions will help to keep new icons visually compatible with Slicer's existing application icons. Editing these closed curves can be tricky to do well, so if you're not going to use the icon exactly as-is, you may want to create your own version using it as a guide. 

### Some Workflow Tips for Creating New Icons

* If your vector editing software allows you to import Slicer's SimpleColorPalette, definitely do that and choose appropriate named colors for each Theme.
   * If your software doesn't permit loading custom palettes, you can refer to the README documentation in the SlicerPalettes directory for a table of colors and values.
   * If you're using Inkscape, you'll need to copy the palette .gpl file into the palettes directory which will vary according to your Inkscape version and your platform. The palette will be discovered on startup, and can be displayed using Inkscape's palette selector.

* If designing at resolution 24x24 px from a Material Symbols Icon, load or import the icon, parameterized and saved as above, into your vector editing software. Resize or reposition the vector elements as need. If something looks wrong, see further tips below.
  
* If designing a 48x48 Icon from a Material Symbols Icon, load or import the icon, parameterized and saved as above, into your vector editing software. Scale it by 200% and position on the document. If something looks wrong, see further tips below.

* If a Materials Symbols Icon loads or imports in a surprising way into your vector editing software, check the document properties to debug units (px); viewbox X, Y, Width and Height; and Scale. Some simple vector editing tools don't handle document ***imports*** well when the imported document has viewbox and scale parameters that differ from the document you're importing ***into***. so:
   * If you are starting by loading the 48x48SlicerIconTemplate.svg file, the document Width=Height=48px, Scale=1.0 (px per user unit), and Viewbox X=0, Y=0, Width=48, Height=48. If you find that the scale or position of the imported icon is way off, that's a sign that your software isn't handling the viewbox mapping well. You can still resize and reposition the imported content, within the template, and the resulting saved icon should be fine. Just make sure the resized vector elements are pixel-perfect.
   * If you are starting by loading a Materials Symbol Icon parameterized and saved as above, the document Width=Height=24, Scale=0.0250, and the Viewbox X=0, Y=-960, Width=960, Height=960. If you want to change this document to 48x48px resolution in keeping with 3D Slicer's other icons, change document width and height to 48px, and change Scale to 0.05. Note that the Viewbox will still have its original values, but that's just fine.

* If you're starting your own icon from scratch and not using a template or a Material Symbols Icon, that's fine too. For consistency in that case, please set your icon's document properties to match existing icons: units=px; Document Width=Height=48px; Viewbox X=Y=0, Width=Height=48 and Scale=1.0. Refer to the Design Guidelines above, and enjoy!

