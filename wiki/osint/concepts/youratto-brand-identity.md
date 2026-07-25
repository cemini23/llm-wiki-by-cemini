---
title: youratto brand identity — folio stack + corner tricolor
type: concept
tags: [concept, atto, youratto, brand, logo, k194, draft]
keywords: [folio stack, italian flag corner, wordmark, macOS icon, UPL visual fence]
related:
  - sources/gemini-atto-brand-identity-2026-07-24.md
  - sources/gemini-atto-landing-conversion-2026-07-23.md
  - concepts/youratto-lean-conversion-page.md
  - concepts/atto-macos-gtm-gumroad.md
  - sources/gemini-atto-marketing-compliance-2026-07-23.md
  - concepts/atto-local-first-threat-model.md
maturity: draft
created: 2026-07-24
updated: 2026-07-24
---

## Relations

- @sources/gemini-atto-brand-identity-2026-07-24.md — Gemini DR SoT
- @sources/gemini-atto-landing-conversion-2026-07-23.md — lean hero uses this lockup
- @concepts/youratto-lean-conversion-page.md — landing lockup
- @concepts/atto-macos-gtm-gumroad.md — Gumroad / listing surfaces
- @sources/gemini-atto-marketing-compliance-2026-07-23.md — claim fence; visual must-nots
- @concepts/atto-local-first-threat-model.md — local-first / AttoVault honesty in metaphor

## Raw Concept

Operator locked **Variant C** (2026-07-24): folio stack with thick slate borders + **small Italian flag stamp in the top-right corner only**. Rejected A (terracotta corner) and B (cypress corner). Full-sheet tricolor fill also rejected. SoT: OSINT/atto — not SEO-wiki craft alone.

## Narrative

### Locked

| Decision | Choice |
|----------|--------|
| Architecture | Symbol + wordmark (not wordmark-only, not bare “A” alone) |
| Primary mark | Document / **folio stack** — 3 offset rounded planes, thick continuous slate outlines |
| Corner accent | Tiny **Italian flag** (G `#009246` · W `#FFFFFF` · R `#CE2B37`) top-right of top sheet only |
| Base palette | Vellum `#F5F2EB` · Slate ink `#1A1C20` |
| UI / CTA accent | Prefer slate + sparse tricolor; do not flood UI with flag colors |
| Backup if 16px fails | Abstract geometric **A** (drop corner flag at tiny sizes if muddy) |
| Metaphor | Organizer / `~/AttoVault` — not attorney, not Ancestry, not government portal |
| Wordmark type | High-contrast modern serif (Playfair-class) |
| UI type | Native / geometric sans (SF Pro for macOS) |

Canonical mock: `atto/briefs/assets/atto-folio-variant-c-flag-corner.png`  
Brief: `atto/briefs/2026-07-24_youratto-logo-dual-accent-ab.md` (lock addendum)

### Tricolor rule (claim fence)

- **Allowed:** corner stamp / micro-badge only (≤ ~15% of icon width).
- **Forbidden:** full-page flag fill · Repubblica Italiana emblem · passport burgundy mimicry · implying consulate / Prenot@Mi affiliation.

### Must-not (visual claim fence)

Gavels · scales · columns · eagle seals · DNA / sepia trees / fingerprints · glowing cloud graphs / “magic” sparkles · neon cyber palettes · baked-in rounded corners on the 1024 PNG.

### Next (production)

1. ~~Freelancer bezier~~ → **shipped in-house** `apps/site/assets/brand/atto-mark.svg` + 1024 PNG (2026-07-24)
2. ~~Export sizes~~ — favicon / apple-touch / Discord 512 / Gumroad cover / Tauri icons done
3. ~~Wire lean site + Discord~~ — Pages live; Discord guild icon updated
4. **Operator:** upload `gumroad-cover-1280x720.png` in Gumroad UI
5. Rebuild/notarize `.dmg` on next desktop release (icons already regenerated)

## Snippets

```css
:root {
  --atto-vellum: #F5F2EB;
  --atto-ink: #1A1C20;
  --atto-flag-green: #009246;
  --atto-flag-white: #FFFFFF;
  --atto-flag-red: #CE2B37;
}
```

## Dead Ends

- **Variant A** terracotta corner `#C25946` — rejected 2026-07-24  
- **Variant B** cypress corner `#4A6B53` — rejected 2026-07-24  
- Full-sheet green/white/red folio fill — rejected (kitsch / affiliation risk); corner-only wins  
- Vault/lock and family-tree territories scored out of primary (DR rubric)
