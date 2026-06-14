# Label_Generator

A Flask web app that generates printable fastener labels for toolbox organizers. I built this because I needed it.

## What it does

**Metric machine screws (M2–M6)**
- Filter by size, head type (CAP/BTN/CSK/RCSK), drive (Phillips, Hex socket), material (Black/Stainless), length
- Color-coded identity bars (1–6 bars match M2–M6)
- Each label: size × length, drive + head abbreviation, full names, material, top-down and side-profile drawings

**Wood screws (#6–#12 gauge, imperial lengths)**
- Head types: Flat (countersunk), Wafer, Pan, Pocket
- Drive types: Torx T15/T20/T25, Phillips, Robertson Square
- Brown identity bars (count = gauge rank)
- Coarse thread side profile, sharp wood-screw point

**Self-tapping screws (#6–#12 gauge)**
- Hex Washer Head with socket/nut-driver interface
- Blue identity bars, hex-on-flange side profile

**Color code reference chart** — M2–M6 quick-reference page

**Output formats**
- Print sheets — US Letter, 300 DPI, cut-to-size sticker paper
- PNG download — individual labels
- SVG export — native vector for 3D printing, laser engraving, CAD import (40×16mm physical size)

**Custom labels** — any non-standard combination via Quick Add, persisted to localStorage

## Tech

- **Backend:** Python, Flask, app factory pattern
- **Frontend:** HTML, CSS, JavaScript, Canvas API + SVG generation

## Why this exists

I have toolbox bins sorted by fastener type. I needed labels that show at a glance what's in each slot — not just "M4 x 10" but also the drive, head, and material. Nothing I found did exactly what I wanted, so I made this. It now covers my wood screw and self-tapping bins too.

## Honesty

AI helped with the Canvas rendering code and SVG path generation — drawing the profile illustrations, Torx star geometry, and getting the 300 DPI print layout right. The concept, label system design, and hardware taxonomy are mine. This solves a real problem I have. I use the output.
