# skill-pack

A curated bundle of agent skills for GitHub Copilot, VS Code agent mode, and Claude Code.

## Installation

### GitHub Copilot / VS Code agent mode

```bash
# Install a skill from this repository with GitHub CLI
# Replace <owner> with sk-surya or your fork owner on GitHub
gh skill install <owner>/skill-pack <skill-name>
```

Manual install also works: copy any `skills/<skill-name>/` directory from this repository into either `.github/skills/<skill-name>/` for a single repository or `~/.copilot/skills/<skill-name>/` for personal use. The skill directories in this repo follow Copilot's `SKILL.md` naming, folder naming, and YAML frontmatter conventions so they can be copied as-is.

### Claude Code

```bash
# Install all skills
# Replace <owner> with sk-surya or your fork owner on GitHub
claude skills install --from github:<owner>/skill-pack

# Or install individual skills
claude skills install --from github:<owner>/skill-pack/skills/<skill-name>
```

## Skills

### Working with AI

| Skill | Description |
|-------|-------------|
| [prompt-engineer](skills/prompt-engineer) | Expert prompt engineering using the "Genius Intern Framework" |
| [think-first](skills/think-first) | "Think First, AI Second" — stay sharp while working with AI |
| [skill-creator](skills/skill-creator) | Create skills that extend Claude's capabilities |
| [taste](skills/taste) | Domain-grounded judgment for creation — make output feel authored, not generated |

### Dev workflow

| Skill | Description |
|-------|-------------|
| [tdd](skills/tdd) | Test-driven development with vertical slices and tracer bullets (by [mattpocock](https://github.com/mattpocock/skills)) |
| [qa](skills/qa) | Full QA on all session changes using Codex as a second pair of eyes |
| [agentic-review](skills/agentic-review) | Multi-agent code review — security, perf, architecture in parallel |
| [iterate](skills/iterate) | Spin up N agents on isolated worktrees, compare approaches, pick winner |
| [orchestrating-swarms](skills/orchestrating-swarms) | Multi-agent orchestration with teams, tasks, and message-passing |
| [mcp-builder](skills/mcp-builder) | Build high-quality MCP servers in Python or TypeScript |
| [visual-explainer](skills/visual-explainer) | Generate self-contained HTML pages that visually explain systems and code |
| [napkin](skills/napkin) | Per-repo napkin file as a continuously curated runbook (by [blader](https://github.com/blader/napkin)) |

### Product & strategy

| Skill | Description |
|-------|-------------|
| [b2b-expert-advisor](skills/b2b-expert-advisor) | B2B startup strategy advisor grounded in Lenny Rachitsky's 7-part series and April Dunford's positioning framework |
| [plan-ceo-review](skills/plan-ceo-review) | Founder/CEO plan review — rethink the problem, find the 10-star product (from [Garry Tan's gstack](https://github.com/garrytan/gstack)) |
| [shaping](skills/shaping) | Collaboratively shape solutions — iterate on requirements and solution options before building |
| [doc-coauthoring](skills/doc-coauthoring) | Structured 3-stage workflow for co-authoring documentation, specs, and proposals |

### Design

| Skill | Description |
|-------|-------------|
| [design-swarm](skills/design-swarm) | Orchestrate a team of 10 design agents for holistic UI audit, ideation, and implementation |
| [frontend-design](skills/frontend-design) | Create distinctive, production-grade frontend interfaces that avoid generic AI aesthetics |

### Learning & growth

| Skill | Description |
|-------|-------------|
| [master](skills/master) | Turn reference docs into active mastery — retrieval practice, case binding, and scenario simulation |
| [storytelling-influence](skills/storytelling-influence) | Coach on storytelling, communication, and influence — 45 practitioner-tested techniques |
| [upskilling-coach](skills/upskilling-coach) | Systematic coaching for skill acquisition — habit design, practice plans, plateau-breaking |

## Resources

Standalone reference materials that any skill (or you) can use directly. Not locked to a specific skill.

### Communication & leadership

Practitioner-sourced material on influence, stakeholder management, team leadership, and executive communication — from Lenny Rachitsky's newsletter and podcast archive.

```
resources/communication-leadership/
├── lenny-communication-leadership-reference.md   # Consolidated reference (45 techniques)
├── newsletters/                                   # 9 original newsletter articles
│   ├── a-pms-guide-to-influence.md
│   ├── getting-buy-in.md
│   ├── managing-up.md
│   └── ...
└── podcasts/                                      # 11 podcast transcripts
    ├── claire-hughes-johnson.md
    ├── julie-zhuo.md
    ├── wes-kao.md
    └── ...
```

Use with the `master` skill (`/master learn communication`) for structured learning, or read directly.

## Recommended tools

Not skills, but essential tools for building with AI.

| Tool | What it does | Install |
|------|-------------|---------|
| [Agentation MCP](https://github.com/benjitaylor/agentation) | Visual feedback toolbar + MCP server for AI-assisted design critique | `npx add-mcp "npx -y agentation-mcp server"` |
| [DialKit](https://github.com/joshpuckett/dialkit) | Floating control panel for React — sliders, toggles, spring editors for live-tuning UI | `npm install dialkit motion` |
| [Tirith](https://github.com/sheeki03/tirith) | Terminal security — intercepts homograph attacks, ANSI injection, and pipe-to-shell attacks | See [repo](https://github.com/sheeki03/tirith) |
| [ACIP](https://github.com/Dicklesworthstone/acip) | Advanced Cognitive Inoculation Prompt — hardened system prompt security | See [repo](https://github.com/Dicklesworthstone/acip) |

## Contributing

PRs welcome. Each skill should be a self-contained directory under `skills/` with a `SKILL.md` file, a lowercase hyphenated directory name, and frontmatter that follows GitHub Copilot agent skill conventions.

## License

MIT
