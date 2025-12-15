<!-- ───────────────────────────────────────────── -->
<!--                A S T R O S T E V E O          -->
<!-- ───────────────────────────────────────────── -->

<h1 align="center">AstroSteveo</h1>
<p align="center">
  <strong>Software Engineer</strong> • AI Agent Tinkerer • Amateur Astrophysicist<br/>
  <em>"The best tools disappear into the workflow."</em>
</p>

<p align="center">
  <img alt="Languages" src="https://img.shields.io/badge/Languages-Rust | TypeScript | Shell-6f42c1?style=for-the-badge"/>
  <img alt="Focus" src="https://img.shields.io/badge/Focus-AI%20Agents%20%2F%20Game%20Dev-8A2BE2?style=for-the-badge"/>
  <img alt="Vibe" src="https://img.shields.io/badge/Vibe-Workflows%20>%20Willpower-ff6f3c?style=for-the-badge"/>
</p>

---

### What I'm Building

**AI that actually works in production codebases.** Most AI coding tools choke on real projects—context exhaustion, slop accumulation, mental misalignment. I'm not interested in demos that work on todo apps. I'm building workflows that survive contact with legacy code.

**Games with physics that feel right.** Space sims where ships move like ships, not sprites. Real orbital mechanics, real inertia, real satisfaction. The kind of game where you can feel the mass of your vessel when you try to stop.

**Scripts that answer questions.** How many light-seconds from Earth to Mars right now? What's the delta-v budget to get there? Sometimes you just need to do the math at 2am because the universe won't stop being interesting.

> "If you're not occasionally computing orbital mechanics for fun, are you even relaxing?"

---

### Flagship: `claude-code-plugins`

A collection of Claude Code plugins, headlined by **epic** — a structured workflow for AI-assisted development that I built because I got tired of babysitting context windows.

```
/epic:explore → /epic:plan → /epic:implement → /epic:validate → /epic:commit
```

**The problem:** AI fills its context window with grep calls before writing any code, then ships slop that needs rework. You spend more time fixing AI output than you saved by using AI.

**The solution:** Deliberate phases with artifact documentation. Research agents run in the background. Plans get reviewed before code gets written. Context stays at 40-60% utilization. The AI earns trust incrementally.

**The result:** AI that handles brownfield codebases, complex multi-file problems, and passes expert review. Code that doesn't make you wince.

```bash
claude plugin marketplace add astrosteveo/claude-code-plugins
claude plugin install epic@astrosteveo-plugins
```

---

### Also in Orbit: `void-sector`

A space game built with Bevy (Rust). Click-to-move flight, approach commands, orbital mechanics. Client/server architecture with replicon networking. Combat, economy, and progression systems in various stages of completion.

**The goal:** "Physics poetry" — ships that float like they have mass in a universe that has rules. No arcade nonsense. No "space is just water with stars." Actual Newtonian vibes.

**Current status:** The ships fly. The ships shoot. The economy... exists. It's getting there.

---

### Operating Principles

- Tools should amplify, not interrupt.
- Workflows beat willpower. Systems beat motivation.
- If the AI keeps making the same mistake, the process is wrong — not the AI.
- Document the why; the what is in the code.
- The best abstraction is the one you delete later.
- Astrophysics is relaxing. Fight me.

---

### The Stack

```
AI Tooling:       Claude Code plugins, agent workflows, context management
Game Dev:         Rust, Bevy, ECS patterns, networked multiplayer
Scripts:          Whatever gets the answer fastest (usually Python, sometimes regret)
Infrastructure:   Arch Linux, Nix when it makes sense, tmux always
```

---

### Flavor Bits

| | |
|---|---|
| **Motto** | "Worlds aren't hosted. They're cultivated." |
| **Superpower** | Turning fuzzy intent into running systems before the coffee gets cold. |
| **Current Rabbit Hole** | Making AI assistants useful beyond the demo. |
| **Late Night Hobby** | Calculating how long it takes light to reach places. |
| **Hot Take** | Most "AI coding tools" are just autocomplete with better marketing. |

---

### Collaboration

Interested in:
- AI agent patterns that actually scale beyond toy examples
- Context management strategies for LLM-assisted development
- Space sims, orbital mechanics, and n-body problems
- Anything where the math is satisfying and the abstractions are honest

Open an issue or start a discussion. I don't bite. The code might.

---

<p align="center"><sub>README = living document. Updated when reality changes.</sub></p>
