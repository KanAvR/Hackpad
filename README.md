# Hackpad

Hackpad is a 9 key macropad with a rotary encoder, an OLED Display and uses KMK firmware.

This will be used as a macropad for common desktop shortcuts such as, switching desktops; To boost productivity.

## Features:
- Open case because it looks cool
- 128x32 OLED Display
- EC11 Rotary encoder.
- 1 SK6812 MINI-E LED. 
- 9 Keys

## CAD Model:
Made in Fusion.
It has just one 3d printed piece, with a cutout at the top to easily slide the macropad in and out. It also features 4 screw holes which will be used to screw the macropad into my desk.

<img src=assets/cad.png alt="Schematic" width="500"/>




## PCB
Made in KiCAD.
Schematic

<img src=assets/schematic.png alt="Schematic" width="300"/>

PCB

<img src=assets/pcb.png alt="Schematic" width="300"/>




## Firmware Overview
This hackpad uses KMK firmware. 

- the rotary encoder changes volume. 
- The 9 keys will bound to various hyprland shortcuts as and when required.
- The OLED will be used for showing volume status.

## BOM:

- 9x Cherry MX Switches
- 9x DSA Keycaps
- 9x Through-hole 1N4148 Diodes
- 1x 1 SK6812 MINI-E LED
- 1x 0.91" 128x32 OLED Display
- 1x EC11 Rotary Encoder
- 1x XIAO RP2040
- 1x Case
