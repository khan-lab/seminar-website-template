---
layout: page
title: "About"
permalink: /about/
---

# About {{ site.title | default: "Seminar Series Template" }}

{{ site.tagline | default: "A Jekyll + Bootstrap starter for academic seminars" }}

This is a reusable website template for running an academic **seminar series**.
It’s built with **Jekyll** and **Bootstrap**, and it lets you manage talks using a single data file
(`_data/speakers.yml`). The site automatically renders **upcoming speakers**, detailed **event pages**,
a searchable **archive**, and “**Add to Calendar**” actions.

---

## Goals

- Make it simple to publish a professional seminar website in minutes.
- Keep content **data-driven** (no manual pages to maintain).
- Support common workflows: registration, remote/hybrid meetings, junior-speaker slots, and 1:1 sign‑ups.
- Be easy to deploy on **GitHub Pages** (or any static host) and maintain with PRs.

---

## How it works

- **Single source of truth:** Add/update talks in `_data/speakers.yml`.
- **Auto-generated pages:** A python generator `scripts/generate_events_md.py` creates `events/<id>.md` for each talk.
- **Homepage:** Lists upcoming events with speaker photos and quick actions.
- **Archive:** Searchable, filterable (by year), and paginated list of past talks.
- **Event details:** Title, speaker & affiliation, date/time, venue, abstract, bio, optional junior speaker,
  registration, and calendar buttons.

---

## Modules (optional)

- **Event format** — In‑person, Remote, or Hybrid. For remote/hybrid, show join link, meeting ID/passcode,
  and extra instructions.
- **Register button** — Renders when a `registration:` URL exists.
- **Add to Calendar** — Google and universal `.ics` download.
- **Meet the Speaker** — Show a Doodle/Calendly (or any URL) for 1:1 bookings.
- **Junior Speaker** — Compact card for a trainee spotlight below _Meet the Speaker_.

Configure these per talk inside `_data/speakers.yml`.

---

## Theming & SEO

- **Bootswatch** theming via `_config.yml`:
  ```yaml
  bootswatch:
    enabled_switcher: false # set true to show a Theme dropdown in the navbar
    theme: "" # "" or "default" = plain Bootstrap; or a Bootswatch theme name
    version: "5.3.7"
  ```
- **SEO**: The `{% raw %}{% seo %}{% endraw %}` tag (via `jekyll-seo-tag`) is wired in the `<head>` include.
  Set site metadata in `_config.yml` (`title`, `tagline`, `description`, `url`, `baseurl`).

---

## Organizers (demo)

List your team in `_data/organizers.yml`:

```yaml
- name: "Lead Organizer"
  title: "Assistant Professor"
  affiliation: "Your University, City"
  intro: "Initiates and oversees the seminar series; coordinates speakers and partnerships."
  photo: "/assets/img/organizers/lead.jpg"
  url: "https://example.edu/~lead"
```

The `/organizers/` page renders responsive cards from this data.

---

## Contributing & license

Issues and PRs are welcome to improve the template (docs, modules, accessibility, etc.).  
Code is released under the **MIT License**. Please keep credits and consider sharing enhancements back.

---

## Contact

If you've questions, suggestions, or need help, please reach out to the team at [https://khanlab.bio](https://khanlab.bio) or email us at **{{ site.email | default: 'aziz.khan@mbzuai.ac.ae' }}**.
