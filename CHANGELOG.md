# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.4.1] - 2026-06-13

### Added

- **Gauge size reference table** in the Wood Screw sidebar filter panel — collapsible table showing nominal shank diameter (inches and mm) for #6/8/9/10/12; includes the sizing formula (D = 0.060 + N×0.013") and a note that the same scale applies to Self-Tap gauges

## [0.4.0] - 2026-06-13

### Added

- **Wood screws** — new label category for #6/8/9/10/12 gauge, imperial lengths (3/4"–4")
  - Head types: Flat (countersunk), Wafer, Pan, Pocket
  - Drive types: Torx T15/T20/T25, Phillips, Robertson Square
  - Brown identity bars (count = gauge rank: #6=1 bar … #12=5 bars)
  - Unique side profiles per head: V-countersink (Flat), low bezier dome (Wafer), domed pan (Pan), flat rectangular (Pocket)
  - Coarse thread lines extending beyond shank, sharp gimlet point
- **Self-tapping screws** — Hex Washer Head category for #6/8/10/12 gauge, imperial lengths (1/2"–2")
  - Blue identity bars, hex-on-washer-flange side profile, pointed tip
- **Drive icons**: Torx 6-lobe star, Robertson square recess, Phillips cross (in addition to existing Hex socket)
- **SVG export for all new types** — `svgWoodHalf`, `svgWoodTopDown`, `svgWoodSideProfile`, `svgHexWasherTopDown`, `svgHexWasherSide` added; `buildSVG` dispatches to wood/tapping paths
- **Sidebar filter sections** — Wood and Self-Tap category chips; dedicated filter panels (gauge, head, drive, material, imperial length) shown/hidden per category toggle

## [0.3.0] - 2026-04-17

### Added

- SVG export for metric screw labels — native vector output (no canvas rasterization)
- `downloadSelectedSVG()` button in sidebar
- SVG rendering mirrors canvas geometry exactly: circles, paths, lines, text elements
- Physical output size: 40mm × 16mm
- Supports all label layouts: Single, Dual, Triple, Quad
- Intended workflow: select labels → Download SVGs → import into Fusion 360 / Bambu Studio / laser software

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
