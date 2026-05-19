# Sayswitch Docs Recovery

This folder is a recovered static copy of the public Sayswitch documentation site that was previously hosted at:

- `https://sayswitch-documentation.vercel.app/`

## What This Contains

- The extracted HTML pages for the docs site
- The original exported `_next/static` CSS and JS assets
- A local `assets/img/say-switchlogo.png` copy so the site does not depend on the old deployment for the header logo
- A small cleanup script that strips old runtime-only dependencies and normalizes the export for static hosting

## Important Constraint

This is a recovered static site, not the original Nextra/Next.js source repository. You can update the docs immediately by editing the relevant `index.html` files, but if you want the old authoring experience back you would need a later migration into a fresh Nextra or Next.js docs repo.

## Local Preview

From this folder:

```bash
python3 -m http.server 4173
```

Then open:

- `http://localhost:4173/`

## Deploy To Vercel

From this folder:

```bash
npx vercel
```

For production:

```bash
npx vercel --prod
```

If you want to connect it to a specific team/project:

```bash
npx vercel link --yes --project sayswitch-documentation --scope Sayswitch
```

## Optional Cleanup Re-run

If you replace the extracted HTML with a fresh pull from the public site, re-run:

```bash
python3 scripts/normalize_export.py
```
