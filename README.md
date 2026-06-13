# Label_Generator

A Flask web app that generates printable screw and fastener labels for toolbox organizers. I built this because I needed it.

## What it does

- Interactive label maker for metric screws (M2 through M6)
- Each label shows: M-size indicator bars, size x length, drive type, head type, material, and a profile drawing
- Color code reference chart for quick identification
- Custom label creation with localStorage persistence
- Print-ready output at 300 DPI, formatted for US Letter paper

## Tech

- **Backend:** Python, Flask, app factory pattern
- **Frontend:** HTML, CSS, JavaScript, Canvas API

## Why this exists

I have a toolbox with metric screws sorted into compartments. I needed labels that would tell me at a glance what is in each slot — not just "M4 x 10" but the drive type, head type, and material too. Nothing I found online did exactly what I wanted, so I made this.

## Honesty

AI helped with the Canvas rendering code — drawing the profile illustrations and getting the 300 DPI print layout right. The concept, the design system, and the label format are mine. This solves a real problem I had. I use the output.
