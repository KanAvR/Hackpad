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
| Name | Purpose | Qty | Price | Link | Distributor |
|------|---------|-----|-------------|------|-------------|
| 0.91 inch blue OLED display module | Volume display (I already have this) | 1 | $0.00 | [Link](https://robocraze.com/products/0-91-inch-blue-oled-display-module) | Robo Craze |
| SK6812 MINI E RGB LED 3228 SMD Individually Addressable Full Color DC 5V (Pack of 100) | Mute status indicator (I already have this) | 1 | $0.00 | [Link](https://www.amazon.in/100PCS-Similar-WS2812B-Individually-Addressable/dp/B0DMNBBM9V) | Amazon |
| 1N4148 Fast Switching Diodes, 100V 300mA, Pack of 100, DO 35 Glass Zener Diodes for Electronic Projects | Preventing Ghosting (quantity is 1 because it comes in packs of 100, I will use 9) (I already have this) | 1 | $0.00 | [Link](https://www.amazon.in/100-Pieces-1N4148-Switching-High-Speed/dp/B079KJ91JZ) | Amazon |
| CentIoT EC11 10K Rotary Encoder Digital Potentiometer Coding Volume Control with switch 5 Pin 15mm Half handle (2PCS) | Volume knob (I already have this) | 1 | $0.00 | [Link](https://www.amazon.in/CentIoT-Encoder-Digital-Potentiometer-Control/dp/B0888RWNM1) | Amazon |
| Seeed Studio XIAO RP2040 Development Board | Connecting the hackpad to my computer (I already have this) | 1 | $0.00 | [Link](https://robocraze.com/products/seeed-studio-xiao-rp2040-development-board) | Robo Craze |
| Cherry MX Switches | Mechanical key switches (got from an old keyboard that stopped working) | 9 | $0.00 | N/A | N/A |
| DSA Keycaps | Keycaps for switches (got from an old keyboard that stopped working) | 9 | $0.00 | N/A | N/A |
