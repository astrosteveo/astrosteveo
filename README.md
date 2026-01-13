<!-- ───────────────────────────────────────────── -->
<!--                A S T R O S T E V E O          -->
<!-- ───────────────────────────────────────────── -->

<h1 align="center">AstroSteveo</h1>
<p align="center">
  <strong>Software Engineer</strong> • AI Workflow Architect • Amateur Astrophysicist<br/>
  <em>"Research first. Test first. Evidence before claims."</em>
</p>

<p align="center">
  <img alt="Languages" src="https://img.shields.io/badge/Languages-Python | TypeScript | Rust-6f42c1?style=for-the-badge"/>
  <img alt="Focus" src="https://img.shields.io/badge/Focus-AI%20Workflows%20%2F%20Space%20Sims%20%2F%20Astronomy-8A2BE2?style=for-the-badge"/>
  <img alt="Vibe" src="https://img.shields.io/badge/Vibe-Discipline%20>%20Demos-ff6f3c?style=for-the-badge"/>
</p>

---

### What I'm Building

**Disciplined AI-assisted development.** Most AI coding agents suffer from context exhaustion, stale knowledge, and no verification. I build workflows that force research before design, tests before code, and evidence before claims. No shortcuts. Powered by [Engram](https://github.com/astrosteveo/engram) — semantic memory that lets Claude Code pick up where you left off.

**Space games with physics that feel right.** Thrust-based physics, hybrid sandbox gameplay loop, focused around a PvE experience. The universe's best pilots against the most dangerous threat in deep space. Currently deep in worldbuilding — documenting the lore of substrate mining incidents and corporate cover-ups.

**Astronomy tools for stargazers.** Real-time sky data, observation logging, meteor showers, ISS passes. From CLI to progressive web app. Happily hosted on [Vercel](https://vercel.app) and [Railway](https://railway.com).

> "If you're not occasionally computing twilight times for fun, are you even relaxing?"

---

### Flagship: `engram`

Semantic memory for Claude Code. Persistent context across sessions.

**The problem:** You're deep in a multi-day feature. Context fills up. You `/new`. Now Claude has no idea what was happening.

**The solution:** Engram watches Claude Code's conversation logs, indexes them into a project-local vector database, and exposes MCP tools that let Claude query past context.

```bash
pip install engram
cd your-project && engram init
# Restart Claude Code — memory tools available
```

When you `/new` mid-task, just say `resume`. Claude instantly sees what you were working on.

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

### Flagship: `void-sector-lore`

The worldbuilding foundation for Void Sector — a lore wiki documenting substrate mining incidents, corporate cover-ups, and the disappearances the United Mining Guild doesn't want you to know about.

**Features:**
- 14 interconnected documents (recovered logs, leaked communications, suppressed reports)
- Terminal immersion system with progressive corruption tracking
- Ambient horror effects that degrade as you read deeper

**Current status:** Live at [astrosteveo.github.io/void-sector-lore](https://astrosteveo.github.io/void-sector-lore/). The game is pre-production, but the universe is alive.

> *"19 incidents. 18 months. 0 investigations."*

---

### Claude Code Tools

Beyond the main projects, I build tools that make Claude Code better:

- **[claude-usage-statusline](https://github.com/astrosteveo/claude-usage-statusline)** — Real-time usage limits in your status bar
- **[marketplace](https://github.com/astrosteveo/marketplace)** — Personal plugin marketplace for Claude Code workflows

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
AI Tooling:       Claude Code, Engram for memory, custom workflow plugins
Game Dev:         Rust, Bevy, ECS patterns (pre-production)
Astronomy:        Python, Skyfield, FastAPI, React, Tailwind, Vercel/Railway
Infrastructure:   Arch Linux, tmux always, Nix when it makes sense
```

---

### Flavor Bits

| | |
|---|---|
| **Motto** | "Worlds aren't hosted. They're cultivated." |
| **Superpower** | Turning fuzzy intent into verified, tested systems. |
| **Current Rabbit Hole** | Substrate mining lore and progressive terminal corruption. |
| **Late Night Hobby** | Checking what's visible in tonight's sky. |
| **Hot Take** | Most "AI coding tools" skip research, skip tests, and call it productivity. |

---

### Collaboration

Interested in:
- AI workflows that enforce discipline, not just suggest it
- Space sims, orbital mechanics, and immersive worldbuilding
- Astronomy tools and real-time celestial calculations
- Anything where the math is satisfying and the tests prove it works

Open an issue or start a discussion. I don't bite. The code might.

---

<p align="center"><sub>README = living document. Updated when reality changes.</sub></p>
