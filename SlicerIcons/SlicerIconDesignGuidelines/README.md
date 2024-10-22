
# 3D Slicer Icon Design Guidelines and Resources

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

1. Design icons as vector images on a transparent background.
   
2. At 24x24 pixel resolution, stroke width should be 1 dp = 1 px. This will insure pixel-perfect rendering at resolution multiples of 24.

3. Use simple stroked elements without fill where possible.

4. If filled elements are required, use limited color, preferrably from Slicer's palette, consistent across your UI and compatible with Slicer's application UI, and ensure the fill color works well in both Dark and Light themes.

5. Use face-forward icons where possible and orthographic perspective with 45 deg angles where required.

6. Avoid gradients and other 3D effects.
   
7. Respect the stroke, fill and backgrounds **colors** defined in Slicer's palette for both Dark and Light Themes. 
   
8. Padding of 2dp is recommended around the icon perimeter. 
   
9. Preview the Dark and Light Theme versions of your icon on Dark and Light Theme backgrounds and at multiple resolutions to insure they look great.

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

If so, some helpful Workflow Tips are linked below:

## Links to Workflow Tips:

