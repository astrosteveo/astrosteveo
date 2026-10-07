# Maintaining this portfolio

The root README is the GitHub profile. `site/` is the GitHub Pages portfolio.
Both share reviewed copy in `content/portfolio.json` and templates in `templates/`.

## Edit and preview

1. Update `content/portfolio.json` for project descriptions or contact details.
2. Update the templates for layout changes and `site/style.css` for styling.
3. Run `python3 scripts/build.py` and `python3 scripts/validate.py`.
4. Preview with `python3 -m http.server 8080 --directory site`.
5. Commit the source and generated README and HTML together.

The Portfolio workflow validates the generated files on pull requests. Pushes to
`main` also deploy only `site/` to GitHub Pages. No dependencies or secrets are
needed to build the portfolio.

## Public content policy

Use public project documentation or an explicitly approved description. Do not
copy implementation details, infrastructure, issue histories, benchmarks,
screenshots, paths, or credentials from private projects. Void Sector receives
only its approved high-level description and no repository or old demo link.
Check repository visibility anonymously before adding any source link.

The profile and site use original vector artwork rather than project captures.
There are no analytics, visitor counters, or external JavaScript dependencies.
The optional orbital animation respects reduced-motion settings.

Public sources for the project copy:

- [mdview README](https://github.com/astrosteveo/mdview#readme)
- [Claude Plugins README](https://github.com/astrosteveo/claude-plugins#readme)
- [gdh README](https://github.com/astrosteveo/gdh#readme)

GitHub setup references:

- [Profile README requirements](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)
- [GitHub Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

## Profile finishing touches

Pin the three public project repositories with **Customize your pins** on your
GitHub profile. GitHub's public API does not currently expose a repository-pin
mutation. Keep the account website field pointing to the portfolio if desired;
the README and portfolio both retain the separate writing website.

The custom social image is `site/social.png` (1200 × 630); use it as the
repository social preview under **Settings → General → Social preview**.
The page already references it for Open Graph and social cards.
