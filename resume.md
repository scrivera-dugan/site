---
layout: default
title: Resume
description: Resume of Sarah Dugan, technical writer and documentation lead with over a decade in docs and eight years in AI.
---
{% assign r = site.data.resume %}
<div class="resume">
<h1><span class="print-only">Sarah C. Dugan</span><span class="screen-only">Resume</span></h1>
<p class="contact print-only">sarahcdugan@gmail.com · linkedin.com/in/scdugan · sarahdocs.com</p>

<p class="summary">{{ r.summary }}</p>

<nav class="jump" aria-label="Jump to a role">
{% for job in r.experience %}<a href="#{{ job.id }}">{{ job.company | split: "," | first }}</a>
{% endfor %}</nav>

<h2 class="resume-section">Experience</h2>
{% for job in r.experience %}
<section class="role" id="{{ job.id }}">
<div class="role-head">
<h3><a href="#{{ job.id }}">{{ job.title }}</a></h3>
<span class="dates">{{ job.start }} – {{ job.end }}</span>
</div>
<p class="where">{{ job.company }} · {{ job.location }}</p>
<ul>
{% for bullet in job.bullets %}<li>{{ bullet }}</li>
{% endfor %}</ul>
</section>
{% endfor %}

<h2 class="resume-section">Education</h2>
{% for school in r.education %}
<section class="role">
<div class="role-head">
<h3>{{ school.school }}</h3>
<span class="dates">{{ school.year }}</span>
</div>
<p class="where">{{ school.degree }}<br>{{ school.minor }}</p>
</section>
{% endfor %}

<div class="meta">
<button class="button" type="button" onclick="window.print()">Download PDF</button>
<span>Updated {{ r.updated | date: "%B %Y" }}</span>
</div>
</div>
