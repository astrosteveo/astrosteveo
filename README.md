<!-- ───────────────────────────────────────────── -->
<!--                A S T R O S T E V E O          -->
<!-- ───────────────────────────────────────────── -->

<h1 align="center">AstroSteveo</h1>
<p align="center">
  <strong>Software Engineer</strong> • AI Workflow Architect • Amateur Astrophysicist<br/>
  <em>"Research first. Test first. Evidence before claims."</em>
</p>

<p align="center">
  <img alt="Languages" src="https://img.shields.io/badge/Languages-Rust | TypeScript | Python-6f42c1?style=for-the-badge"/>
  <img alt="Focus" src="https://img.shields.io/badge/Focus-AI%20Workflows%20%2F%20Space%20Sims%20%2F%20Astronomy-8A2BE2?style=for-the-badge"/>
  <img alt="Vibe" src="https://img.shields.io/badge/Vibe-Discipline%20>%20Demos-ff6f3c?style=for-the-badge"/>
</p>

---

### What I'm Building

**Disciplined AI-assisted development.** Most AI coding agents (Claude Code, Codex, are designed to be unopinionated  — context exhaustion, stale knowledge, no verification. I build workflows that force research before design, tests before code, and evidence before claims. No shortcuts. All powered by a [Engram](https://github.com/astrosteveo/engram).

**Space games with physics that feel right.** Thrust-based physics, hybrid sandpark gameplay loop, focused around a PvE experience--it's the worlds best pilots in the Universe against the worlds most dangerous threat ever identified in the far reaches of Deep Space. Do you take the next contract, or do you pass it to focus on other things higher up your proiority tree? Your actions carry weight -- that contract you ignored could result in death, espionage, or you just might save your own life by turning a blind eye. Which will you choose?

**Astronomy tools for stargazers.** Real-time sky data, observation logging, meteor showers, ISS passes. From CLI to progressive web app. Are you curious of the skies tonight will be clear enough to spot celestial objects, and speceifically, which of these will be the easiest to spot. Happily hosted on [Vercel](https://vercel.app) and [Railway](https://railway.com).

> "If you're not occasionally computing twilight times for fun, are you even relaxing?"

---

### Flagship: `void-sector`

A space sandbox MMO built with Bevy 0.17 (Rust). Eve Online's depth meets WoW's accessibility — but PvE-first.

**The vision:** A living galaxy where every item is crafted, not spawned. NPC factions with territorial ambitions. Environmental hazards. Hostile space fauna. Bio-ships grown from harvested creatures. The void is alive and hungry.

**The implementation:**
- Eve Online-style flight physics (exponential acceleration curves, verified by tests)
- Navigation commands: Approach, Orbit, Keep at Range, Align, Warp
- Click-to-target with lock timers and QWEASD hotkey system
- 64-bit coordinates via `big_space` for massive universe support
- 36+ passing tests verifying physics formulas

**Current status:** Pre-production. Flight prototype complete. Click-to-target system in progress. The ships fly exactly like Eve ships should.

```
void-sector/
├── crates/void_core/    # Shared physics & commands
├── crates/void_client/  # Bevy client application
├── GDD.md               # 1,661-line game design document
└── .harness/            # Structured development workflow
```

---

### Flagship: `astrosky`

A full-stack astronomy application — CLI, API, and progressive web app. Your window to the cosmos.

**What it does:**
- Real-time visibility: planets, moon phase, ISS passes, meteor showers, deep sky objects
- Observing conditions scoring based on weather, cloud cover, moon brightness
- Observation logging with equipment tracking and Messier Marathon progress
- Achievements, weekly challenges, and a gamified progression system
- Smart "What should I observe tonight?" recommendations (Premium)

**The stack:**
- **CLI:** Python + Skyfield + Click (`pip install astrosky`)
- **API:** FastAPI, deployed on Railway
- **Web:** React 19 + Vite + Tailwind, deployed on Vercel (PWA with offline support)

**Current status:** Production. Live at [astrosky-beryl.vercel.app](https://astrosky-beryl.vercel.app). 95+ tests. 59 React components. Premium tier with subscription infrastructure.

```bash
# CLI
pip install astrosky
astrosky tonight --location "Austin, TX"

# Or without installing
uvx astrosky tonight
```

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
AI Tooling:       Claude Code plugins, SUPERHARNESS workflow, context management
Game Dev:         Rust, Bevy 0.17, ECS patterns, big_space coordinates
Astronomy:        Python, Skyfield, FastAPI, React, Tailwind, Vercel/Railway
Infrastructure:   Arch Linux, tmux always, Nix when it makes sense
```

---

### Flavor Bits

| | |
|---|---|
| **Motto** | "Worlds aren't hosted. They're cultivated." |
| **Superpower** | Turning fuzzy intent into verified, tested systems. |
| **Current Rabbit Hole** | Bio-horror space ships grown from alien creatures. |
| **Late Night Hobby** | Checking what's visible in tonight's sky. |
| **Hot Take** | Most "AI coding tools" skip research, skip tests, and call it productivity. |

---

### Collaboration

Interested in:
- AI workflows that enforce discipline, not just suggest it
- Space sims, orbital mechanics, and Eve Online flight physics
- Astronomy tools and real-time celestial calculations
- Anything where the math is satisfying and the tests prove it works

Open an issue or start a discussion. I don't bite. The code might.

---

<p align="center"><sub>README = living document. Updated when reality changes.</sub></p>
