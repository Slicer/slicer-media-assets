---
title: Slice Viewer Icons Design Guidelines

---

# Slice Viewer Icons

Icon set symbolics:

* **Source (volumes):** orthographic cube

* **Image|view|slice:** plane with axis & 4 quadrants OR 4 voxels

* **Action/processing:** green object (specifics below)

* **Plane with bar across top:** slice|image viewer

## Contents of this page include:

* refactored module icons to be consistent with above symbology
* new colors for use in Slice Viewers.
* new view configuration icon (if lightbox moved from Slice Viewer to view configuration menu)
* full Slice Viewer icon set
* grouped icons along with descriptions
* slice viewer mockups with new icons.


## Refactored Volumes and Models Module Icons
**Volumes Module Icon**
Modified to reflect 3D rather than 2D representation.

**Models Module Icon**
Also, **two versions** of Models Module Icon are checked into github, one simple with no fill, and the other with fill color consistent with segmentation model symbology. The team can choose which is preferred for use.

![Screenshot 2024-08-21 at 4.15.53 PM](https://hackmd.io/_uploads/Sy7IoTQsR.png =400x)


## New Colors
Slice Viewer Action Green:

* HSL 135 70 40 
* HEX #1FAD42FF
* RGB 31 173 66

Slicer Segmentation and Label Grid Green:

* HSL 135 10 50
* HEX #738C79FF
* RGB 115 140 121

Slicer Segmentation and Label Outline Green:
* HSL 135 82 44 
* HEX #14CC42FF
* RGB 20 204 66 

All three new colors are global colors, perceived well and kept unchanged in switches between both Dark and Light Themes.


## Lightbox View Configuration icons
We discussed in developer mtg moving lightbox out slice viewer. Created viewer config icons for lightbox view in R|Y|G viewers, in case this functionality is added to Viewer Configuration Icons, where it seems appropriate to include. These are checked into github.

![Screenshot 2024-08-19 at 5.13.06 AM](https://hackmd.io/_uploads/Sk-EpKlo0.png =200x)

![Screenshot 2024-08-19 at 5.25.29 AM](https://hackmd.io/_uploads/S1Kiy9gjC.png =225x)

## Full Icon set for Slice Viewers
Light Theme
![Screenshot 2024-08-23 at 1.23.56 PM](https://hackmd.io/_uploads/rJzaBBLiC.png =800x)


Dark Theme
![Screenshot 2024-08-23 at 1.20.55 PM](https://hackmd.io/_uploads/rJkYSSUsA.png =880x)


It's a lot of green when viewed in this array, but it plays pretty well in the actual mockup of the Slice Viewer (see below). 


## Grouped descriptions of icons

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

## Slice Viewer Mockups 
Light Theme
![Screenshot 2024-08-23 at 1.55.30 PM](https://hackmd.io/_uploads/SJWNTB8jC.png)


Dark Theme
![Screenshot 2024-08-23 at 1.51.18 PM](https://hackmd.io/_uploads/Sy-N3rLoR.png)

---

**TODO:**
*0. ~~change all light theme seg fills to 80% opacity for better visual contrast in dark mode*~~
*1. ~~create Dark Theme versions*~~
*2. ~~update slice viewer mockups dark/light*~~
*3. once colors approved, move them into palette files.*




