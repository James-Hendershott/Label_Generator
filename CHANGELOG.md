# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.2.0] - 2026-02-12

### Added

- Custom label creation via Quick Add — type any length value, not just predefined sizes
- Custom labels persist to localStorage and reload on future visits
- Black material labels now render with solid filled icons (white details); Stainless keeps outline style

### Changed

- Redesigned label layout:
  - Full-width size bars spanning the entire top of the label (taller)
  - "M3 x 50" format (size × length, no "mm") at 62px bold
  - "HEX CAP" line (drive + head abbreviation) at 32px bold
  - "Socket: Hex" and "Head: Cap Head" detail lines at 22px
  - Material at 22px bold
  - Text zone widened to 52%, drawings compressed on right
- Print sheets now use US Letter (8.5×11") instead of A4
- Quick Add length field changed from dropdown to number input with datalist suggestions
- Hardware labels (nuts/washers) updated with larger text to match new layout
- Updated color code guide label system notes to reflect new format

## [0.1.0] - 2026-02-11

### Added

- Initial project structure with Flask web server
- Screw Label Maker (interactive label browser, filter, print sheets)
- Color Code System reference page (M2-M6 matrix)
- Index page with links to both tools
- Project documentation (BACKLOG.md, CHANGELOG.md, CLAUDE.md)

### Notes

- Migrated from standalone HTML files on Unraid server
- All original HTML functionality preserved unchanged
- HTML files are self-contained with inline CSS/JS; Flask serves them as-is
