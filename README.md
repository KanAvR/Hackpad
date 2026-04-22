# Hackpad
<img src=assets/render.png width="500"/>
Hackpad is a 9 key macropad with a rotary encoder, an OLED Display and uses KMK firmware.

This will be used as a macropad for common desktop shortcuts such as, switching desktops; To boost productivity.

## Features:
- Open case because it looks cool
- 128x32 OLED Display
- EC11 Rotary encoder.
- 1 SK6812 MINI-E LED. 
- 9 Keys

## CAD Model:
Made in Blender.
The model is made of two seprate parts that will be screwed togeather to make the case.


<img src=assets/cad.png width="500"/>



## PCB
Made in KiCAD.
Schematic

<img src=assets/schematic.png alt="Schematic" width="300"/>

PCB

<img src=assets/pcb.png alt="Schematic" width="500"/>




## Firmware Overview
This hackpad uses KMK firmware.
 
- The rotary encoder changes volume. Turning it clockwise increases the volume by 5% and turning it counter-clockwise decreases it by 5%. Pressing it toggles mute.
- The 9 keys will be bound to various hyprland shortcuts as and when required. Right now key 1-6 switch to workspaces 1-6, key 7 kills the focused window, key 8 toggles fullscreen, and key 9 takes a screenshot.
- The OLED will be used for showing volume status. It shows a bar that fills up as the volume increases and shows MUTE when muted.
- The SK6812MINI LED glows blue normally and turns red when muted.

## BOM:

- 9x Cherry MX Switches
- 9x DSA Keycaps
- 9x Through-hole 1N4148 Diodes
- 1x 1 SK6812 MINI-E LED
- 1x 0.91" 128x32 OLED Display
- 1x EC11 Rotary Encoder
- 1x XIAO RP2040
- 1x Case
