# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## Project Overview

Label Generator is a Flask web app for creating and managing fastener labels for toolbox organizers. It serves self-contained HTML tools: a label maker with filter/select/print/export functionality, and a color code reference chart.

**Tech Stack**: Python, Flask  
**Origin**: Migrated from standalone HTML files on Unraid server

## Running the Application

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
python run.py
```

App runs on `http://localhost:5000`.

There are no tests, linting, or build steps configured. No CI/CD pipeline exists.

## Architecture

### Routes

| Route | Template | Purpose |
|-------|----------|---------|
| `/` | `index.html` | Landing page with links to both tools |
| `/labels` | `label_maker.html` | Interactive label maker |
| `/color-code` | `color_code.html` | M2-M6 color code reference chart |

Flask app factory is in `app/__init__.py`, routes in `app/routes.py` (Blueprint named `main`). Entry point is `run.py`.

### Key Design Decisions

- **HTML files are self-contained**: `label_maker.html` and `color_code.html` include all CSS/JS inline. Flask serves them unchanged — no Jinja templating is used. When modifying these files, test that inline JS/CSS still works since there's no build step.
- **No database**: Labels are generated client-side using Canvas API; SVGs are generated client-side as strings.
- **Custom labels use localStorage**: Saved under `customLabels` key, reloaded on init.
- **static/output/ is gitignored**: Generated label PNGs go here but aren't tracked.
- **Google Fonts loaded via CDN**: Outfit + JetBrains Mono.

### Label Dimensions

**Physical:** 40mm × 16mm  
**Canvas:** 472 × 189px (300 DPI equivalent)  
**Print sheet:** US Letter (8.5×11") at 300 DPI = 2550×3300px

### Label Categories

#### Metric Machine Screws (cat: `'screw'`)

| Field | Values |
|-------|--------|
| `size` | M2, M2.5, M3, M4, M5, M6 |
| `length` | integer mm (varies by size) |
| `head` | CAP, BTN, CSK, RCSK |
| `drive` | PH (Phillips), HX (Hex socket) |
| `material` | Black, Stainless |

Identity bars: count = M-size rank (M2=1 … M6=6), black color.

#### Hardware (cat: `'nut'` / `'washer'`)

Same `size` and `material` as screws; no head/drive/length.

#### Wood Screws (cat: `'wood'`)

| Field | Values |
|-------|--------|
| `gauge` | #6, #8, #9, #10, #12 |
| `length` | imperial string: `'3/4"'` through `'4"'` |
| `head` | FLAT (countersunk), WAFER (low dome), PAN (domed), PKT (pocket flat) |
| `drive` | TX15, TX20, TX25 (Torx), PH (Phillips), SQ (Robertson square) |
| `material` | Zinc (filled), Stainless (outline) |

Identity bars: brown (`#A0522D`), count = gauge rank (#6=1 … #12=5).

#### Self-Tapping Screws (cat: `'tapping'`)

| Field | Values |
|-------|--------|
| `gauge` | #6, #8, #10, #12 |
| `length` | imperial string: `'1/2"'` through `'2"'` |
| `head` | HWH (Hex Washer Head) — always |
| `material` | Zinc (filled), Stainless (outline) |

Identity bars: steel blue (`#2B6CB0`), count = gauge rank (#6=1 … #12=4).

#### Multi-bin layouts (cat: `'dual'` / `'triple'` / `'quad'`)

Contain nested configs (`left`/`right`, `topLeft`/`topRight`/`bottom`, etc.). Each sub-config is any single-label category.

### Drawing Architecture

All rendering happens client-side via two parallel systems:

**Canvas (display + PNG export)**  
- `drawLabel(canvas, cfg)` — dispatch function; routes to specialized drawers
- `drawWoodLabel`, `drawTappingLabel` — full single-label renderers for new types
- `drawTopDown` / `drawSideProfile` — metric screw icons
- `drawWoodTopDown` / `drawWoodSideProfile` — wood screw icons (4 head shapes)
- `drawHexWasherTopDown` / `drawHexWasherSide` — self-tapping icons
- `drawTorxDrive` — 6-lobe star (6 overlapping circles + center fill)
- `drawWoodDriveTopDown` — dispatches PH/SQ/Torx drive icons
- `drawNutTopDown` / `drawNutSide` / `drawWasherTopDown` / `drawWasherSide` — hardware icons

**SVG (vector export)**  
Parallel set of `svg*` functions producing SVG string markup:
- `buildSVG(cfg)` — top-level dispatcher
- `svgSingleHalf` — metric screw/nut/washer labels
- `svgWoodHalf` — wood screw and self-tapping labels
- `svgTopDown` / `svgSideProfile` — metric screw icons
- `svgWoodTopDown` / `svgWoodSideProfile` — wood screw icons
- `svgHexWasherTopDown` / `svgHexWasherSide` — self-tapping icons
- `svgTorxDrive` / `svgWoodDriveTopDown` — drive icons
- `svgNut*` / `svgWasher*` — hardware icons

### Filter State

```javascript
let filters = {
  // Metric
  cat, size, head, drive, mat, len,
  // Wood
  woodGauge, woodHead, woodDrive, woodMat, woodLen,
  // Self-tapping
  stGauge, stMat, stLen
}
```

Wood and self-tap filter UI panels are hidden by default; toggling the category chip shows them.

### preview_label.py

Standalone Pillow script for prototyping metric label layout as PNG. Requires `Pillow` (not in `requirements.txt`). Output: `label_preview.png`.

## Project Tracking

- `BACKLOG.md` — planned features and known bugs
- `CHANGELOG.md` — version history (current: **0.4.0**), follows Keep a Changelog format
