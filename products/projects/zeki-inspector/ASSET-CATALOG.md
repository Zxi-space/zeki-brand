# Zeki Inspector — Consolidated Brand Asset Catalog

Version: `1.0`  
Scope: Batch 01 Logo & Icons + Batch 02 Brand Lockups + Batch 03 Product Illustrations

## Source-of-truth rule

`assets/logo/logo-mark-source.png` is the approved mascot source supplied by
the user. `assets/logo/approved-mascot-source.png` is an exact duplicate kept
under an explicit name for easier discovery. Do not replace these with earlier
concepts, generated logo alternatives, preview-board crops, or test vectors.

## Asset structure

```text
zeki-brand/
└── products/
    └── zeki-inspector/
        ├── brand/
        ├── design-system/
        └── assets/
            ├── logo/              # Batch 01 — mascot logo master and sizes
            ├── app-icon/          # Batch 01 — app icons and favicon
            ├── extension-icon/    # Batch 01 — browser extension icons
            ├── brand-lockup/      # Batch 02 — horizontal and vertical lockups
            └── illustration/      # Batch 03 — five product illustrations
```

## Batch index

### Batch 01 — Logo & Icons
- Transparent mascot logo master and standard sizes.
- App icon exports and favicon.
- Browser extension icon exports.
- SVG wrapper is raster-backed and should not be described as editable path
  vector artwork.

### Batch 02 — Brand Lockups
- `assets/brand-lockup/logo-horizontal.png`
- `assets/brand-lockup/logo-vertical.png`
- Mascot-only and compact icon uses should use the approved Batch 01 mark.

### Batch 03 — Product Illustrations
- Empty state.
- Element selection success.
- AI Context workflow.
- Welcome / onboarding.
- Curious hint / guidance.

## Implementation notes

- Preserve transparent backgrounds.
- Preserve source aspect ratios; do not stretch.
- Prefer `object-fit: contain` for illustrations.
- Do not crop away the mascot, magnifying glass, or green focus-corner motif.
- Use the app icon only where a square tile is required.
- Use extension icon exports in the browser extension manifest.
- Use horizontal/vertical lockups for brand placements, not as tiny toolbar icons.
- For dark mode, place transparent artwork on the dark surface; do not recolor the
  approved mascot unless a separately approved monochrome variant is created.

## Validation

See `asset-manifest.json` for exact file paths, image dimensions, transparency
metadata, byte sizes, and SHA-256 hashes.
