# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Label Generator is a Flask-based web app for creating and managing screw/fastener labels for tool box organizers. It serves two self-contained HTML tools: a label maker with filter/select/print functionality, and a color code reference chart for M2-M6 screws.

**Tech Stack**: Python, Flask
**Origin**: Migrated from standalone HTML files on Unraid server (`/mnt/user/ShottsBox/Projects/Tool_Box_Organizer/Labels/`)

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

- **HTML files are self-contained**: `label_maker.html` and `color_code.html` include all CSS/JS inline (each is thousands of lines). Flask serves them unchanged — no Jinja templating is used. When modifying these files, test that inline JS/CSS still works since there's no build step.
- **No database**: Labels are generated client-side in the browser using Canvas API.
- **Custom labels use localStorage**: Labels created with non-predefined size/length combos are saved to `localStorage` under the key `customLabels` and reloaded on init.
- **static/output/ is gitignored**: Generated label PNGs go here but aren't tracked.
- **Google Fonts loaded via CDN**: `label_maker.html` uses Outfit + JetBrains Mono; `color_code.html` uses DM Sans + JetBrains Mono.

### Label Layout (40x16mm @ 300 DPI = 472x189px)

- **Top bars**: Full-width bars spanning the label (count = M size: 1=M2, 2=M2.5, ... 6=M6)
- **Line 1**: `M3 x 50` — size x length (62px bold, no "mm")
- **Line 2**: `HEX CAP` — drive abbreviation + head abbreviation (32px bold)
- **Line 3**: `Socket: Hex` — full drive name (22px)
- **Line 4**: `Head: Cap Head` — full head name (22px)
- **Line 5**: `Black` — material (22px bold)
- **Right side**: Top-down and side profile drawings (52/48% split)
- **Material styling**: Black = solid filled icons with white details; Stainless = outline icons
- **Print**: US Letter (8.5x11") at 300 DPI

### preview_label.py

Standalone Pillow script for prototyping label layout as PNG. Requires `Pillow` (not in `requirements.txt` — install separately with `pip install Pillow`). Output goes to `label_preview.png` in project root.

## Project Tracking

- `BACKLOG.md` — planned features and known bugs
- `CHANGELOG.md` — version history (current: 0.2.0), follows Keep a Changelog format
