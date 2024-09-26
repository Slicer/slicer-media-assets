# Slicer Segment Editor Module Icons

Below is a current snapshot of icons for Slicer's Segment Editor Module. Please add comments.

To create NEW icons to add to this set, please follow [this simple workflow NOT YET LINKED]. The workflow will refer icon designers to Slicer's [Icon Design Guildelines] and Slicer's [Color Palette] to ensure new icons are visually compatible with Slicer's icons and that they work well in both Dark and Light Themes.

## Icon set symbolics 

* **Segmentation colors:** "SegmentationEditorGreen" fill color, "SegmentationAndLabelGridGreen" grid color

* **Segmentation:** an outlined 2D polygon with filled voxels and grid 
  
* **Segmentation vignette:** a part of segmentation shown as polygon filled with "SegmentationEditorGreen". Outline only along edge of segmentation, but not where it is cropped from view in the vignette.

* **Direct Action** "SegmentationAndLabelOutlineGreen" is used to indicate direct action like draw, paint, erase, seed, etc.

* **Seed created by Direct Action** Clicking in a particular location to create a seed or select a (local) region within an image for processing is shown as a small "SegmentationAndLabelOutlineGreen" shape (rounded square or circle) that marks the location clicked, surrounded by an outer "shell" with "SegmentationEditorGreen" fill. This symbol is used in icons for "FastMarching", "GrowFromSeed" and "LocalThreshold".
 
* **Image|view|slice:** theme-stroke-outlined 2D plane with (if resolution permits) axis & 4 quadrants OR 4 voxels


## Full Icon set for SegmentEditor Module Dark and Light Themes:

Light & Dark Theme 

24x24 px res

<img src="https://github.com/user-attachments/assets/866bf52c-1da4-4f4a-84e3-0b39f41fdeea" width="400">

48x48 px res

<img src="https://github.com/user-attachments/assets/01f70361-7846-48ce-8896-28f605bb4a19" width="600">

## Specific Colors included Palette

Slicer Segmentation and Label Grid Green (LightTheme):
* HEX #738C79FF
* RGB 115 140 121

Slicer Segmentation and Label Grid Green (DarkTheme):
* HEX #56695BFF
* RGB 86 105 91

Slicer Segmentation and Label Outline Green (also used to highlight seg direct action like paint/draw/erase in tools):
* HEX #27b94cff
* RGB 39 185 76 

## Current Slice Viewer Mockups with new icons

Top level icons for Display, Navigation, Basic UI ops

<img src="https://github.com/user-attachments/assets/1fe985f2-d208-4dc2-9d6c-8ea40949fbd4" width="600">

Icons for basic tools to create & edit segments

<img src="https://github.com/user-attachments/assets/6e6a85a3-8048-4e70-b5c7-1d91d8f8c08f" width="600">

Icons for advanced tools for adjusting & processing segments:

<img src="https://github.com/user-attachments/assets/aa6dc9ab-6459-4439-9af4-529ab2fbe524" width="600">

Icons for segment editor extra effects

<img src="https://github.com/user-attachments/assets/925020c0-d946-489e-ba33-d18609d4b4a2" width="600">

TODO: discuss comments/suggestions.

