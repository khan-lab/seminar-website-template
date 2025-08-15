---
layout: page
title: Organizers
subtitle: The team behind the Seminar Series
permalink: /organizers/
---

<div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4 g-4">
  {% assign people = site.data.organizers %}
  {% for p in people %}
  <div class="col">
    <div class="card h-100 shadow-sm border-0">
      <div class="card-body d-flex flex-column">
        <img
          src="{{ p.photo | default: '/assets/img/placeholder-speaker.jpg' | relative_url }}"
          alt="{{ p.name }}"
          class="rounded-circle shadow-sm d-block mx-auto mb-3 organizer-avatar"
          style="width: 120px; height: 120px; object-fit: cover;"
          loading="lazy"
        >
        <h5 class="mb-1 text-center">{{ p.name }}</h5>
        {% if p.role %}<div class="small text-center mb-2"><strong> {{ p.role }} </strong> </div>{% endif %}
        {% if p.title %}<div class="text-muted small text-center">{{ p.title }}</div>{% endif %}
        {% if p.affiliation %}<div class="small text-center mb-2">{{ p.affiliation }}</div>{% endif %}
        
        <div class="mt-auto d-flex justify-content-center gap-2">
          {% if p.url %}
            <a class="btn btn-sm btn-outline-primary" href="{{ p.url }}" target="_blank" rel="noopener">
              Website
            </a>
          {% endif %}
          {% if p.orcid %}
            <a class="btn btn-sm btn-outline-secondary"
               href="https://orcid.org/{{ p.orcid | replace: 'https://orcid.org/', '' }}"
               target="_blank" rel="noopener">
               ORCID
            </a>
          {% endif %}
        </div>
      </div>
    </div>
  </div>
  {% endfor %}
</div>
