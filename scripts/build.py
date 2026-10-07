#!/usr/bin/env python3
"""Build the GitHub profile and static portfolio from reviewed public copy."""
import html
import json
from pathlib import Path
from string import Template

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "content/portfolio.json").read_text())
esc = html.escape


def card(project, index):
    tags = "".join(f'<li>{esc(tag)}</li>' for tag in project["tags"])
    url = project["public_repo"]
    action = (f'<a class="project-link" href="{esc(url)}">Explore repository <span aria-hidden="true">↗</span></a>'
              if url else '<span class="private-note">In development · source remains private</span>')
    return f'''<article class="project" id="{esc(project['id'])}">
      <div class="project-top"><span class="project-number">0{index}</span><span class="project-status">{esc(project['status'])}</span></div>
      <p class="eyebrow">{esc(project['category'])}</p>
      <h3>{esc(project['name'])}</h3>
      <p class="project-description">{esc(project['description'])}</p>
      <ul class="tags" aria-label="Technologies and focus">{tags}</ul>
      {action}
    </article>'''


def readme_project(project):
    title = project["name"]
    if project["public_repo"]:
        title = f'[{title}]({project["public_repo"]})'
    tags = " · ".join(project["tags"]) or "Private project"
    return f'### {title}\n\n{project["description"]}\n\n**{tags}**\n'


site = Template((ROOT / "templates/index.html").read_text()).substitute(
    name=esc(data["name"]), role=esc(data["role"]), intro=esc(data["intro"]),
    approach=esc(data["approach"]), website=esc(data["website"]),
    portfolio_url=esc(data["portfolio_url"]), email=esc(data["email"]),
    cards="\n".join(card(p, i) for i, p in enumerate(data["projects"], 1)),
)
(ROOT / "site/index.html").write_text(site)
readme = Template((ROOT / "templates/README.md").read_text()).substitute(
    name=data["name"], intro=data["intro"], approach=data["approach"],
    website=data["website"], portfolio_url=data["portfolio_url"], email=data["email"],
    projects="\n".join(readme_project(p) for p in data["projects"]),
)
(ROOT / "README.md").write_text(readme)
print("Built README.md and site/index.html from reviewed portfolio content.")
