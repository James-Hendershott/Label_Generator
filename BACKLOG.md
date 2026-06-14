# Backlog

## Enhancements

- [ ] Server-side label generation (Pillow/ReportLab) — currently all rendering is client-side canvas
- [ ] API endpoint to generate labels on-demand (programmatic access)
- [ ] Database for tracking inventory / label print history
- [ ] Integration with "Where's My App" inventory system

## Improvements

- [ ] Extract inline CSS/JS from HTML templates into separate static files
- [ ] Dark/light theme toggle
- [ ] Responsive mobile layout improvements
- [ ] Quick Add support for wood screws and self-tapping screws (currently only metric)
- [ ] SVG export for Dual/Triple/Quad wood and self-tapping label layouts
- [ ] Color code reference page update to include wood screw gauge system
- [x] Gauge size reference table in sidebar (nominal shank Ø in/mm per # gauge) — v0.4.1

## Bugs

- (none known)

## Done (reference)

- [x] Flask application structure (app factory pattern)
- [x] Interactive label maker with multi-filter interface
- [x] Color code reference chart (M2-M6)
- [x] Canvas label rendering at 40×16mm / 300 DPI
- [x] Print sheets (US Letter)
- [x] PNG download for individual labels
- [x] SVG export for individual labels (native vector) — v0.3.0
- [x] Custom label creation (Single/Dual/Triple/Quad layouts)
- [x] localStorage persistence for custom labels
- [x] Wood screw labels (#6–#12, Flat/Wafer/Pan/Pocket heads, Torx/Phillips/Robertson drives) — v0.4.0
- [x] Self-tapping screw labels (Hex Washer Head) — v0.4.0
- [x] SVG export for wood and self-tapping labels — v0.4.0
