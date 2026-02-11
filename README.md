<!-- ───────────────────────────────────────────── -->
<!--                A S T R O S T E V E O          -->
<!-- ───────────────────────────────────────────── -->

<h1 align="center">AstroSteveo</h1>
<p align="center">
  <strong>Software Engineer</strong> • AI Workflow Architect • Amateur Astrophysicist<br/>
  <em>"Research first. Test first. Evidence before claims."</em>
</p>

<p align="center">
  <img alt="Languages" src="https://img.shields.io/badge/Languages-Python | TypeScript | Rust | C++ | C%23 | Go | Java | GDScript-6f42c1?style=for-the-badge"/>
  <img alt="Focus" src="https://img.shields.io/badge/Focus-AI%20Workflows%20%2F%20Space%20Sims%20%2F%20Astronomy-8A2BE2?style=for-the-badge"/>
  <img alt="Vibe" src="https://img.shields.io/badge/Vibe-Discipline%20>%20Demos-ff6f3c?style=for-the-badge"/>
</p>

---

### What I'm Building

**Disciplined AI-assisted development.** Most AI coding agents suffer from context exhaustion, stale knowledge, and no verification. I build workflows that force research before design, tests before code, and evidence before claims. No shortcuts. When I hit a bug in the tools I use, I fix it upstream — like patching [tweakcc](https://github.com/Piebald-AI/tweakcc)'s session memory feature gate for Claude Code 2.1.38+.

**Space games with physics that feel right.** Thrust-based physics, hybrid sandbox gameplay loop, focused around a PvE experience. The universe's best pilots against the most dangerous threat in deep space. Currently in pre-production across Unity and Godot — prototyping mechanics and documenting lore.

**Astronomy tools for stargazers.** Real-time sky data, observation logging, meteor showers, ISS passes. From CLI to progressive web app. Happily hosted on [Vercel](https://vercel.app) and [Railway](https://railway.com).

> "If you're not occasionally computing twilight times for fun, are you even relaxing?"

---

### Flagship: `astrosky`

A full-stack astronomy application — CLI, API, and progressive web app. Your window to the cosmos.

**What it does:**
- Real-time visibility: planets, moon phase, ISS passes, meteor showers, 110 deep sky objects
- Observing conditions scoring based on weather, cloud cover, moon brightness
- One-tap observation logging with equipment tracking and Messier Marathon progress
- Anonymous sync across devices, works offline

**The stack:**
- **CLI:** Python + Skyfield + Click (`pip install astrosky` or `uvx astrosky`)
- **API:** FastAPI, deployed on Railway
- **Web:** React + Vite + Tailwind, deployed on Vercel (PWA with offline support)

**Current status:** Production. Live at [astrosky-beryl.vercel.app](https://astrosky-beryl.vercel.app). 103 Python tests. 206 frontend tests.

```bash
# Try it now
uvx astrosky tonight --lat 40.7128 --lon -74.0060
```

---

### Flagship: `blog-site`

A personal blog about building software with AI — the disciplined way. No hype, no ads, no tracking.

**What it covers:**
- AI & LLMs — what actually works, what doesn't, and why most "AI tutorials" miss the point
- Developer tools — workflows, automation, and building tools that make other tools better
- The craft — how to build things well, learned from doing it wrong first

**Posts:**
- [I Finally Contributed to Open Source (And It Terrified Me)](https://blog-site-astrosteveo.vercel.app/blog/first-oss-contribution) — overcoming the fear
- [My Claude Code Workflow: From Ad-Hoc Tasks to Structured Development](https://blog-site-astrosteveo.vercel.app/blog/my-claude-code-workflow)
- [The Best Claude Code Plugin is a Text File](https://blog-site-astrosteveo.vercel.app/blog/claude-md-guide) — a guide to CLAUDE.md

**The stack:** Astro, MDX, Pagefind for search. Deployed on Vercel.

**Current status:** Live at [blog-site-astrosteveo.vercel.app](https://blog-site-astrosteveo.vercel.app).

---

### Open Source Contributions

- **[tweakcc](https://github.com/Piebald-AI/tweakcc)** — Contributor. Patch customization tool for Claude Code. Fixed session memory feature gate for CC 2.1.38+ ([PR #509](https://github.com/Piebald-AI/tweakcc/pull/509))

---

### Operating Principles

- Research first. Training data is stale. Verify everything.
- Tests before code. No exceptions unless explicitly requested.
- Evidence before claims. "Should work" is not acceptable.
- The AI keeps making the same mistake? The process is wrong.
- Tools should amplify, not interrupt. Workflows beat willpower.
- Astrophysics is relaxing. Fight me.

---

### The Stack

```
AI Tooling:       Claude Code, tweakcc, custom workflow plugins
Game Dev:         Unity (C#), Godot (GDScript), pre-production
Astronomy:        Python, Skyfield, FastAPI, React, Tailwind, Vercel/Railway
Infrastructure:   Windows 11 / Linux, tmux always
```

---

### Flavor Bits

| | |
|---|---|
| **Motto** | "Worlds aren't hosted. They're cultivated." |
| **Superpower** | Turning fuzzy intent into verified, tested systems. |
| **Current Rabbit Hole** | Open source contributions and game dev prototyping. |
| **Late Night Hobby** | Checking what's visible in tonight's sky. |
| **Hot Take** | Most "AI coding tools" skip research, skip tests, and call it productivity. |

---

### Collaboration

Interested in:
- AI workflows that enforce discipline, not just suggest it
- Space sims, orbital mechanics, and game dev
- Astronomy tools and real-time celestial calculations
- Open source tools that make developer workflows better

Open an issue or start a discussion. I don't bite. The code might.

---

<p align="center"><sub>README = living document. Updated when reality changes.</sub></p>
