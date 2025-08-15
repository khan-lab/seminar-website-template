# Seminar Website Template (Jekyll + Bootstrap)

[![Use this template](https://img.shields.io/badge/Use_this_template-2ea44f?logo=github)](https://github.com/khan-lab/seminar-series-template/generate)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#license)

A ready-to-use template for academic **seminar series** websites. Built with **Jekyll** and **Bootstrap**, it includes upcoming speakers on the home page, a searchable **archive**, **Add-to-Calendar** buttons (Google, universal `.ics`), optional **Meet the Speaker** and **Junior Speaker** sections, circular speaker photos, **Bootswatch** theming, and a **Docker** dev environment.

**Repo:** https://github.com/khan-lab/seminar-series-template/  
**Live demo:** https://khan-lab.github.io/seminar-series-template/

---

## Features

<ul class="list-unstyled lh-lg my-3">
  <li><i class="fa-solid fa-database me-2" style="color:#6f42c1;"></i>Data-driven events from <code>_data/speakers.yml</code> (single source of truth)</li>
  <li><i class="fa-brands fa-python me-2" style="color:#3776AB;"></i>Python generator auto-creates <code>events/&lt;id&gt;.md</code> (runs via <code>start.sh</code>)</li>
  <li><i class="fa-solid fa-file-lines me-2" style="color:#0d6efd;"></i>Rich event pages: title, date/time, venue, abstract, speaker bio + photo</li>
  <li><i class="fa-solid fa-calendar-check me-2" style="color:#20c997;"></i><strong>Meet the Speaker</strong> module (Doodle/Calendly link + description)</li>
  <li><i class="fa-solid fa-user-graduate me-2" style="color:#fd7e14;"></i><strong>Junior Speaker</strong> module (name, affiliation, blurb, optional photo/url)</li>
  <li><i class="fa-solid fa-ticket me-2" style="color:#198754;"></i>Register button (shows when <code>registration</code>/<code>rsvp</code> is provided)</li>
  <li><i class="fa-solid fa-calendar-plus me-2" style="color:#0d6efd;"></i>Add-to-Calendar buttons (Google, Outlook Web, universal <code>.ics</code>)</li>
  <li><i class="fa-solid fa-globe me-2" style="color:#0dcaf0;"></i>Event formats: in-person / remote / hybrid with join link &amp; passcode</li>
  <li><i class="fa-solid fa-table me-2" style="color:#6c757d;"></i>Archive table with live search, dynamic year filter, and pagination (10/page)</li>
  <li><i class="fa-solid fa-users me-2" style="color:#0dcaf0;"></i>Organizers page powered by <code>_data/organizers.yml</code></li>
  <li><i class="fa-solid fa-palette me-2" style="color:#d63384;"></i>Bootswatch theming via <code>_config.yml</code> + optional navbar theme switcher</li>
  <li><i class="fa-solid fa-chart-line me-2" style="color:#198754;"></i>SEO via <code>{% raw %}{% seo %}{% endraw %}</code> and simple analytics include</li>
  <li><i class="fa-solid fa-wand-magic-sparkles me-2" style="color:#ffc107;"></i>Sticky footer, compact buttons, circular speaker avatars</li>
  <li><i class="fa-brands fa-docker me-2" style="color:#2496ED;"></i>Docker dev environment (<code>docker compose up --build</code>) for effency and more ...</li>
</ul>

---

## Quick start

### 1) Create your site from this template

- Click **Use this template** (button above) → create your repository.

### 2) Edit your seminar data

- Open `_data/speakers.yml`
- Add/edit entries (see **Data schema** below)

### 3) Run locally (Docker, recommended)

```bash
docker compose up --build     # serves http://localhost:4000
```

This uses a robust setup where Ruby gems are stored in a Docker volume and won’t be masked by your bind mount.

### 4) Deploy to GitHub Pages

1. Push to `main`
2. In your repo: **Settings → Pages**
   - **Build and deployment → Source:** GitHub Actions _(recommended)_ or **Deploy from branch**
3. Your site will appear at  
   `https://khan-lab.github.io/seminar-series-template/`

---

## Data schema (`_data/speakers.yml`)

```yaml
- id: my-unique-id
  title: "Talk title"
  abstract: "Summary…"
  date: 2025-10-23 16:30:00 +04:00
  duration_min: 60
  venue: "Auditorium A"
  format: "hybrid" # in_person | remote | hybrid (optional)
  remote: # optional; used for remote/hybrid
    platform: "Zoom"
    url: "https://example.zoom.us/j/123"
    meeting_id: "123 456 789"
    passcode: "ILM2025"
    instructions: "SSO required."
  registration: "https://example.com/register" # optional
  meet_url: "https://doodle.com/…" # optional (Meet the Speaker)
  meet_desc: "Sign up for 1:1s." # optional
  speaker:
    name: "Full Name"
    affiliation: "Department / University"
    photo: "/assets/img/speaker.jpg" # or a full URL
    bio: "Short bio…"
  junior: # optional
    name: "Junior Name"
    affiliation: "Affiliation"
    blurb: "One-sentence blurb."
    photo: "/assets/img/junior.jpg" # optional
    url: "https://example.com/profile" # optional
```

- **`id`** must be unique; if missing, the generator will slugify the title and assign it (and optionally write back).
- Use a **consistent timezone** (set default in `_config.yml → ilm.timezone`).

---

## Organizers data (`_data/organizers.yml`)

You can list the seminar series organizers in `_data/organizers.yml` to create a dedicated page.

```yaml
- name: "Organizer Name"
  title: "Position / Role"
  affiliation: "Department / University"
  role: "Organizer role"
  photo: "/assets/img/organizer.jpg" # or a full URL
  url: "https://example.com/profile" # optional
  orcid: "0000-0001-2345-6789" # optional
```

## Bootswatch configuration (and optional switcher)

`_config.yml`:

```yaml
bootswatch:
  enabled_switcher: true # or false to hide the selector entirely
  theme: "" # "" or "default" -> plain Bootstrap; or set a Bootswatch name e.g. "flatly"
  version: "5.3.7" # used for both Bootstrap and Bootswatch CDN links
```

- The **head include** loads the correct CSS based on the config (and saved choice if the switcher is enabled).
- Add `{% raw %}{% include theme_switcher.html %}{% endraw %}` inside your navbar to show the dropdown when enabled.

---

## Local development

```bash
docker compose up --build
# open http://localhost:4000
```

- Gems are installed to a named volume so they persist across runs.
- `start.sh`: ensures gems, runs the event generator, then builds & serves with live reload.

---

## Contributing

Issues and PRs are always welcome!

---
