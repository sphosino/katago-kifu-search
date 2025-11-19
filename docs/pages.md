---
  title: PAGES
---

<ul>
  {% for p in site.pages %}
    <li>{{ p.path }} - {{ p.url }} - {{ p.title }}</li>
  {% endfor %}
</ul>
