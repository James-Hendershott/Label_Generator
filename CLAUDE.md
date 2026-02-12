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

## Architecture

### File Structure
```
Label_Generator/
├── run.py                  # Flask entry point
├── app/
│   ├── __init__.py         # App factory (create_app)
│   └── routes.py           # Route definitions
├── templates/
│   ├── index.html          # Landing page with links to tools
│   ├── label_maker.html    # Screw label maker (self-contained HTML)
│   └── color_code.html     # Color code reference (self-contained HTML)
├── static/
│   └── output/             # Generated label output (gitignored)
└── assets/
    ├── screw_labels_all_pages.pdf
    └── sheet_preview.png
```

### Routes

| Route | Template | Purpose |
|-------|----------|---------|
| `/` | `index.html` | Landing page with links to both tools |
| `/labels` | `label_maker.html` | Interactive label maker |
| `/color-code` | `color_code.html` | M2-M6 color code reference chart |

### Key Design Decisions

- **HTML files are self-contained**: Both `label_maker.html` and `color_code.html` include all CSS/JS inline. Flask serves them unchanged — no Jinja templating needed.
- **No database yet**: Labels are generated client-side in the browser. Server-side generation is a backlog item.
- **static/output/ is gitignored**: Generated label PNGs go here but aren't tracked in version control.

## Development Notes

- The original HTML files came from Unraid at `/mnt/user/ShottsBox/Projects/Tool_Box_Organizer/Labels/`
- `individual_labels/` directory (~1700+ PNGs) is not included in the project — it's generated build output
- When modifying HTML files, test that inline JS/CSS still works since there's no build step
