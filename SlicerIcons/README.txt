/*-------------------------------------------------------------------------------------------------*/
/*-------------------------------------------------------*/
/*
/*      Notes for Creating Slicer Icons for display 
/*      in two STATES: Enabled and Disabled, and
/* 	for two THEMES: Light and Dark
/*      Last update: 28 March 2024
/*-------------------------------------------------------*/
/*-------------------------------------------------------------------------------------------------*/
		ICON TEMPLATE
A template icon is provided with demarcations for symbol area, soft margin and hard margin.
Two versions are provided, pending choice of rendering method for color swapping:

../slicer-media-assets/SlicerIcons/SlicerSVG/LayeredStyles/IconTemplate/SlicerIconTemplate.svg
../slicer-media-assets/SlicerIcons/SlicerSVG/SwapStyles/IconTemplate/SlicerIconTemplate.svg

All icons were designed using Inkscape 1.3 (0e150ed, 2023-07-21). 

THEMES are Light and Dark
STATES are Enabled and Disabled (Hover and Press states are communicated with an icon button's outline).


                COLOR PALETTES
/*-------------------------------------------------------------------------------------------------*/

		BASIC PALETTE THEME/STATE COLOR SWAPS:
		Used for basic line and flat fill icons.
/*-------------------------------------------------------------------------------------------------*/

		EXTENDED PALETTE THEME/STATE COLOR SWAPS:
		Fills Used for View Configuration Icons, ModuleIcons, and System Messages.
		Colors are SAME for Light/Dark Theme
/*-------------------------------------------------------------------------------------------------*/

		CUSTOM PALETTE contains some curated colors for developers to use for
		Module color-coding FILL colors. Other fills may be added to extend the palette.
		Recommended to use only Basic Palette Stroke / Accent colors for strokes for consistency.
		Use FILL colors that work for all themes so they can be used without need for swapping.
		    ** NOTE: Adding new custom colors for icons may require updates to the the following items:
 	            -Custom Color Handling logic,
		    -SlicerCustomPalette.gpl,
		    -This README file.

/*-------------------------------------------------------------------------------------------------*/

   DIRECTORIES, IMPORTANT FILES AND WHERE TO FIND THEM:
 
There is a Basic Palette File  and a Custom Palette File (see below)
Palette files are in GIMP (.gpl) format, and can be imported into Inkscape by copying them to the
application's Resources/share/inkscape/palettes directory (location depending on your installation).

Directories DarkSlicerDrafts and LightSlicerDrafts are ICONSandboxes -- these will be removed, 
   but keep for now, but finished work moves from there to SlicerSVG
SlicerPalettes contains GIMP format palettes that can be imported into inkscape and
   csv version of palettes.
SlicerSVG contains LightThemeIcons and DarkThemeIcons which are versions of drafts chosen for use.
   keep for now, but eventually remove.
   Subdir LayeredStyles includes layered versions of icons, work in progress.
   Subdir SwapStyles includes Light Theme Enabled icons that can be converted to other
      Themes/States using color swapping logic described below,

  1. Basic Palette
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerBasicPalette.gpl
  2. Extended Palette
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerExtendedPalette.gpl
  3. Custom Palette
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerCustomPalette.gpl
  4. SlicerPalettes combined CSV file
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerPaalettesCSV.csv
  5. SlicerPalettes combined TSV file
../slicer-media-assets/SlicerIcons/SlicerPalettes/SlicerPaalettesCSV.tsv  

  SWAPPING COLORS FOR THEMES/STATES: SWAPSTYLES icons can be used as-are here:
  are located in /slicer/media-assets/SlicerIcons/SlicerSVG/SwapStyles

  COMBINED VERSIONS FOR THEMES/STATES: LAYEREDSTYLES icons
  are located in /slicer-media-assets/SlicerIcons/SlicerSVG/LayeredStyles

  
/*-------------------------------------------------------------------------------------------------*/

   COLOR HANDLING FOR THEME & STATE CHANGES (2 approaches)

   -SWAP STYLES
   -LAYERED STYLES
   
   OVERVIEW of SWAP STYLES approach
   To CHANGE COLORS FOR THEME/STATE in the SWAPSTYLES approach:
   * Requires no text editing of Icon SVG's XML
   * Keeps Icon SVG compact,
   * but requires more complicated swapping logic.

   OVERVIEW of LAYERED STYLES approach
   * Requires some text editing of Icon SVG's XML
   * Requires icon designer to create icon layer for each theme/state
   * larger SVG files 
   * simpler swapping logic.
  /*------------------------------------------------------------*/
  

  DETAILS OF EACH:
  /*------------------------------------------------------------*/
            LAYEREDSTYLES
  /*------------------------------------------------------------*/

Slightly more design work, less programatic color swapping.
EACH THEMES/STATE is contained in a separate layer in a single SVG file.
Two edits to SVG's XML are required: 
   -The group id for each layer should be changed to id=THEMENAMESTATENAMELayer.
   -The visibility attribute must be added to each group just after the id:
       -visibility="visible" for LightThemeEnabledLayer as a default.
       -visibility="hidden" for LightThemeDisabledLayer, DarkThemeEnabledLayer, DarkThemeDisbledLayer.
       
   THEME/STATE CHANGING LOGIC:
   
Each icon is created in 4 layers, one for each Theme/state combination.
By default, only the LightThemeEnabled lyer is visible, and the other three layers are NOT visible.
This is specified in the layers panel in Inkscape, where each layer's visibility icon can be configured.
In the saved SVG's xml, this change is given by the display attribute of each layer's inline style as either:
style="display:inline" or style="display:none". Having only one layer visible makes each icon easier to preview in any SVG viewer.

Two ways to modify Layered SVG for theme/state switches:

1: When theme or state changes, the SVG's xml can be modified so that ONLY the appropriate
THEME/STATE layer's style is changed to style="display:inline". 

2: To update each icon to a new THEME/STATE, read the original SVG's XML,
Find the desired THEME/STATE layer, and make sure it's visible.

  TIPS FOR CREATING NEW ICONS IN THEME/STYLE LAYERS using inkscape or other software

    1. Each layer of an Icon's design must be contained in a single XML 'group' <g /g>.
    Each SVG file contains four such groups as layers, each NAMED and STYLED (using palettes)
    for a THEME/STATE permutation.
    The four layers should be overlapping for smooth transitions between states or themes.
    The light theme enabled layer should be set as visible, and all others not.
    There should be NO grouped elements within each layer to keep parsing simple.

    2. IF the icon has been created in Inkscape, each can be created in a layer,
    and layers should be named as below, to make subsequent editing the SVG'S XML easier:
       LightThemeEnabledLayer
       LightThemeDisabledLayer
       DarkThemeEnabledLayer
       DarkThemeDisabledLayer
    Inkscape conveniently represents layers as groups in an exported SVG's XML.
    In the SVG's XML, each group will have an inkscape:label attribute with a value that
    matches a named layer in the Icon's SVG's file. 

    3. If NOT using Inkscape to design, the Icon's SVG's XML may need to be edited to isolate each
    layer inside its own THEME/STATE group <g /g>.

    4. As noted, the Icon SVG's XML MUST BE EDITED TO SET THE ID inside each
    THEME/STATE layer/group appropriately, to reflect its theme and state using one of these
    attribute value pairs that will be searched for by color swapping logic.
       id="LightThemeEnabledLayer"
       id="LightThemeDisabledLayer"
       id="DarkThemeEnabledLayer"
       id="DarkThemeDisabledLayer"


/*--------------------------------------------------------------*/

            SWAPSTYLES PSEUDOCODE
	    
To swap colors to render a Light Theme icon in it's Dark theme and disabled states in both themes,
read original svg xml and search for graphic elements with inline stroke & fill attributes.
OVERRIDE these inline styles by appending appropriate colors for fill and stroke
at the END of the style definition, overriding original values. Send modified
SVG to SvgRenderer.

ANY THEME/STATE -> Light/Enabled:
     Render the original LIGHT THEME SVG as-is;

ANY THEME/STATE -> Light/Disabled
  For each graphic element in original LIGHT THEME SVG (paths, rects, etc):
  {
  1. If its inline "stroke" style attribute that does NOT have a value of stroke:none,
     APPEND a stroke color with value=(corresponding Light/Diabled color) at the END
     of the style specification, e.g. style="....;stroke:#B2B2B2;" to override.
     
  2. If its inline "fill" style attribute does NOT have a value of fill:none,
        /* capture cases where icon uses a filled curve instead of stroke */
     	IF its inline "fill" style attribute has a value of #000000:
	     APPEND new fill color with value=(STROKE Light/Disabled color) at the END
	     of the style specification, e.g. style="....;fill:#B2B2B2;" to override.
	ELSE
             APPEND new fill color with value=(corresponding FILL Light/Disabled color) at the END
	     of the style specification, e.g. style="....;fill:#E8E8FF;" to override.
  }

ANY THEME/STATE -> Dark/Disabled:
  For each graphic element in original LIGHT THEME SVG:
  {
  1. If its inline "stroke" style attribute that does NOT have a value of stroke:none,
     APPEND a stroke color with DarkThemeDisabledBasicStroke color at the END
     of the style specification, e.g. style="....;stroke:#666666;" to override.
     
  2. If its inline "fill" style attribute does NOT have a vaue of fill:none,
        /* capture cases where icon uses a filled curve instead of stroke */
     	IF its inline "fill" style attribute has a value of #000000:
	     APPEND new fill color with value=(STROKE Dark/Disabled color) at the END
	     of the style specification, e.g. style="....;fill:#666666;" to override.
	ELSE
	     APPEND a fill color with value=(corresponding FILL Dark/Disabled color) at the END
	     of the style specification, e.g. style="...;fill:#808080;" to override.
  }
     
ANY THEME/STATE -> Dark/Enabled:

  For each graphic element in original LIGHT THEME SVG:
  1. If CUSTOM/EXTENDED COLOR HANDLING (see below) returns false
  {
     1A. If element's inline style contains a "stroke" attribute that does NOT
     have a value of stroke:none, and:
          -IF original stroke is LightTHemeEnabledAccent1, APPEND a stroke color with DarkThemeEnabledAccent1.
	  -ELSE IF original stroke is LightThemeEnabledAccent2, APPEND a stroke color of DarkThemeEnabledAccent2.
          -ELSE APPEND stroke color of  DarkThemeEnabledBasicStroke
     at the END of the style specification, e.g. style="...;stroke:#E5E5F6;" to override.
     
     1B. If element's inline style contains a "fill"  attribute that does NOT
     have a value of fill:none, and:
          -IF original stroke is LightTHemeEnabledAccent1, APPEND a fill color with DarkThemeEnabledAccent1.
	  -ELSE IF original stroke is LightThemeEnabledAccent2, APPEND a fill color of DarkThemeEnabledAccent2.
          -ELSE APPEND fill color of  DarkThemeEnabledBasicFill
     at the END of the style specification, e.g. style="...;fill:#99A2E3;" to override.
  }

CUSTOM/EXTENDED COLOR HANDLING. (handles accent colors that may be used by view configuration
   or individual module icons.)

  If a graphic element's inline style contains a stroke or fill attribute matching a value in
  Slicer's custom or extended color palette (above):
     1. Use that same color for Dark Theme. Return TRUE.
  ELSE Return FALSE.

/*-------------------------------------------------------------------------------------------------*/


  
  
