# Zeki Inspector — Asset Batch 01

This batch replaces the incorrect logo and icon files with exports derived from
the exact final mascot artwork supplied by the user.

## Source of truth

`assets/logo/logo-mark-source.png`

No generated substitute, earlier logo, or alternate mascot is used.

## Asset groups

- `assets/logo/`: transparent primary logo master and common display sizes.
- `assets/app-icon/`: warm-cream rounded-square app icons, favicon PNGs and ICO.
- `assets/extension-icon/`: transparent Chrome/Edge extension icon sizes.

## Size matrix

| Asset | Sizes |
|---|---|
| Logo mark | source 1254, 1024, 512, 256, 128, 64 |
| App icon | 1024, 512, 256, 128, 64, 32, 16 |
| Extension icon | 256, 128, 64, 48, 32, 16 |
| Favicon | 16, 32, 48 PNG + multi-size ICO |

## Important format note

`logo-mark.svg` is an SVG document with the exact PNG embedded. It is useful
as an SVG asset in web tooling, but its mascot remains raster artwork. A true
editable path-level vector would require a separate manual vector-redraw pass
and would not preserve the exact painterly texture pixel-for-pixel.
