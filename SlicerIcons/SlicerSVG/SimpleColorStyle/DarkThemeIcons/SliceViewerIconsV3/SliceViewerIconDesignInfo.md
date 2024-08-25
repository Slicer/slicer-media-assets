---
title: SliceViewerIconDesignInfo

---

# Slice Viewer Icons

Below is a current snapshot of icons for Slicer's Slice Viewers. 

To create NEW icons to add to this set, please follow [this simple workflow]. The workflow will refer icon designers to Slicer's [Icon Design Guildelines] and Slicer's [Color Palette] to ensure new icons are visually compatible with Slicer's icons and that they work well in both Dark and Light Themes.

Icon set symbolics:

* **Source (volumes):** orthographic cube

* **Image|view|slice:** plane with axis & 4 quadrants OR 4 voxels

* **Action/processing:** green/amber object color TBD

* **Plane with bar across top:** slice|image viewer

## Contents of this page include:

* **Refactored module icons** to be consistent with above symbology
* **New view configuration icon** (if lightbox moved from Slice Viewer to view configuration menu)
* **New palette colors** for use in Slice Viewers.
* **Versions V2 + V3 review** of full Slice Viewer icon sets
* **Slice viewer mockups** with new icons.
* **Icon descriptions** in groups (for V2 only)



## Refactored Volumes and Models Module Icons
**Volumes Module Icon**
Modified to reflect 3D rather than 2D representation.

**Models Module Icon**
Also, **two versions** of Models Module Icon are checked into github, one simple with no fill, and the other with fill color consistent with segmentation model symbology. The team can choose which is preferred for use.

![Screenshot 2024-08-21 at 4.15.53 PM](https://hackmd.io/_uploads/Sy7IoTQsR.png =400x)

## Lightbox View Configuration icons
We discussed in developer mtg moving lightbox out slice viewer. Created viewer config icons for lightbox view in R|Y|G viewers, in case this functionality is added to Viewer Configuration Icons, where it seems appropriate to include. These are checked into github.

![Screenshot 2024-08-19 at 5.13.06 AM](https://hackmd.io/_uploads/Sk-EpKlo0.png =200x)

![Screenshot 2024-08-19 at 5.25.29 AM](https://hackmd.io/_uploads/S1Kiy9gjC.png =225x)

## New Colors (Choose between ActionGreen and ActionAmber)
Slice Viewer Action Green:
* HEX #1FAD42FF
* RGB 31 173 66

SliceViewer Action Amber (LightTheme):
* RGB 237 136 0
* HEX #ED8800FF

SliceViewer Action Amber (DarkTheme):
* RGB 250 159 0
* HEX #FA9F00FF

Slicer Segmentation and Label Grid Green (LightTheme):
* HEX #738C79FF
* RGB 115 140 121

Slicer Segmentation and Label Grid Green (DarkTheme):
* HEX #56695BFF
* RGB 86 105 91

Slicer Segmentation and Label Outline Green:
* HEX #14CC42FF
* RGB 20 204 66 

## TODO: Final color decisions: 

Colors we have for important conceptual color-coding: Green is easily perceived in both Dark/Light themes. We can also use orange/amber (mixes of primarily green and red) and cyans (mixes of primarily green and blue) for important color codes, but these will likely want to be HSL-tuned a little for best effect on both dark and light background. That means more stroke-fill color swapping when switching themes. 

**Lock in a color** for 'segmenation' (green, cyan). This color will be used heavily in the slice viewers and segment editor module, so pick a color you will like to see a lot of.

**Lock in a color** for 'action' (green, amber). This color will be used application-wide in slicer, including in editor.

Update palette with Color Choice.**


## Full Icon set for Slice Viewers (both options V2 & V3)
Light Theme V2

![Screenshot 2024-08-23 at 1.23.56 PM](https://hackmd.io/_uploads/rJzaBBLiC.png =800x)


Dark Theme V2
![Screenshot 2024-08-23 at 1.20.55 PM](https://hackmd.io/_uploads/rJkYSSUsA.png =800x)

Light Theme V3
![Screenshot 2024-08-25 at 9.48.39 AM](https://hackmd.io/_uploads/HkvLInuoA.png =800x)



Dark Theme V3
![Screenshot 2024-08-25 at 9.43.04 AM](https://hackmd.io/_uploads/HJO4B3uoR.png =800x)


## Slice Viewer Mockups 
Light Theme V2
![Screenshot 2024-08-23 at 1.55.30 PM](https://hackmd.io/_uploads/SJWNTB8jC.png =800x)


Dark Theme V2
![Screenshot 2024-08-23 at 1.51.18 PM](https://hackmd.io/_uploads/Sy-N3rLoR.png)

Light Theme V3
![Screenshot 2024-08-25 at 11.52.44 AM](https://hackmd.io/_uploads/ByCEvAujC.png =800x)

Dark Theme V3
![Screenshot 2024-08-25 at 12.08.16 PM](https://hackmd.io/_uploads/SJwBPCusC.png =800x)

---

### Color-coding consideration:
V2 presents a lot of green, and green is double-coded to mean BOTH Segmentation and Action on an image/slice/view here. The saturated green is distinct enough from segmentation green, but making this distinction clearer would be best for interpretation (and teaching). V3 makes -PRESENTATION OF- and -ACTION ON- a view/object much more distinct at a glance. 

## Grouped descriptions of icons (only V2 shown)

**Slice Viewer R|Y|G Toolbars**

Pin|Unpin, Viewer R|G|Y Label, Reset Field of View, Max|Minimize View.

![Screenshot 2024-08-23 at 1.32.29 PM](https://hackmd.io/_uploads/BkN0wSUj0.png =300x)

Font chosen is Gill Sans, but do choose what you like.

---

**Main Toolbar Viewer & View UI**

Hide|Show UI, Link|Unlink, Visible|Invisible, Axial|Sagittal|Coronal, Lightbox, Hide|Show Reformat Widget, Blend Mode, Slice Spacing, Rotate to Volume Plane, Orientation Markers, Ruler Display, Thick Slab Recon. Compare the current UI with proposed mockup below.

[Again, trying out Axi/Sag/Cor icons - for discussion. I think these are pretty clear about slice plane orientation while being view-direction-agnostic.]

![Screenshot 2024-08-19 at 7.53.23 AM](https://hackmd.io/_uploads/SkL1Xhei0.png)





---

**Foreground and Background Layers**

Foreground Layer Label, InterpolationON|InterpolationOFF

![Screenshot 2024-08-19 at 8.07.04 AM](https://hackmd.io/_uploads/H1vYSnxiC.png =300x)


Background Layer Label, InterpolationON|InterpolationOff

![Screenshot 2024-08-19 at 8.09.02 AM](https://hackmd.io/_uploads/SkIeU3xiC.png =300x)



**Label Map Layers**
Icons convey strictly 2D construct.

Label Layer Label, Visible|Invisible, Label Display Options: Fill|Outline|Fill+Outline

![Screenshot 2024-08-19 at 5.10.35 PM](https://hackmd.io/_uploads/BJGeHVWi0.png =300x)


**Segmentation Layers**
Icons convey dyadic 2D/3D construct.

Segmentation Layer Label, Visible|Invisible, Segmentation Display Options: Fill|Outline|Fill+Outline, Each Segment Visibility (discussed excluding this element in meeting.)

![Screenshot 2024-08-19 at 8.11.52 PM](https://hackmd.io/_uploads/rypUJDWi0.png =350x)







