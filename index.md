---
layout: default
title: Home
---
{% assign work = site.data.work %}
{% assign feed = site.data.substack %}
{% assign r = site.data.resume %}

<section class="block" id="work" aria-labelledby="work-h">
<h2 class="label section-label" id="work-h"><svg class="leaf-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M12 21c0-7 4-11 9-13-2 8-4 13-9 13Z"/><path d="M12 21c0-7-4-11-9-13 2 8 4 13 9 13Z"/><path d="M12 21V9"/></svg>Selected work</h2>
<div class="work-grid">
{% for item in work.docs %}
<article class="work-card">
    <div class="img-placeholder">Image placeholder</div>
    <div class="body">
        <h3><a href="{{ item.url }}" rel="noopener">{{ item.title }}<span class="ext" aria-hidden="true"> ↗</span></a></h3>
        <p class="org">{{ item.org }} · {{ item.kind }}</p>
        <p>{{ item.summary }}</p>
    </div>
</article>
{% endfor %}
</div>
{% if work.writing and work.writing.size > 0 %}
<h3 class="sub-label">Writing</h3>
{% include writing-list.html items=work.writing %}
{% endif %}
</section>

<section class="block newsletter" id="substack" aria-labelledby="news-h">
<h2 class="label section-label" id="news-h"><svg class="leaf-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M12 21c0-7 4-11 9-13-2 8-4 13-9 13Z"/><path d="M12 21c0-7-4-11-9-13 2 8 4 13 9 13Z"/><path d="M12 21V9"/></svg>{{ feed.title }}</h2>
<p>My newsletter on Substack, about information, language, and myth. It's free and it shows up occasionally.</p>
{% if feed.posts and feed.posts.size > 0 %}
<ul class="writing">
    {% for post in feed.posts limit: 3 %}
    <li><a href="{{ post.link }}"><span class="where">{{ post.date | date: "%b %-d, %Y" }}</span><span class="title">{{ post.title }}</span></a></li>
    {% endfor %}
</ul>
{% endif %}
<form class="subscribe" action="{{ feed.link }}subscribe" method="get" target="_blank">
    <label for="sub-email">Email address</label>
    <div class="row">
        <input id="sub-email" name="email" type="email" autocomplete="email" placeholder="you@example.com" required>
        <button class="button" type="submit">Subscribe</button>
    </div>
    <p class="hint">Opens Substack to confirm.</p>
</form>
</section>

<section class="block resume" id="resume" aria-labelledby="resume-h">
<h2 class="label section-label" id="resume-h"><svg class="leaf-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M12 21c0-7 4-11 9-13-2 8-4 13-9 13Z"/><path d="M12 21c0-7-4-11-9-13 2 8 4 13 9 13Z"/><path d="M12 21V9"/></svg>Résumé</h2>
<h1 class="print-only">Sarah C. Dugan</h1>
<p class="contact print-only">sarahcdugan@gmail.com · linkedin.com/in/scdugan · sarahdocs.com</p>
<p class="summary">{{ r.summary }}</p>

<nav class="jump" aria-label="Jump to a role">
{% for job in r.experience %}<a href="#{{ job.id }}">{{ job.company | split: "," | first }}</a>
{% endfor %}</nav>

<h3 class="resume-section">Experience</h3>
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

<h3 class="resume-section">Education</h3>
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
</section>

<section class="block" id="about" aria-labelledby="about-h">
<h2 class="label section-label" id="about-h"><svg class="leaf-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M12 21c0-7 4-11 9-13-2 8-4 13-9 13Z"/><path d="M12 21c0-7-4-11-9-13 2 8 4 13 9 13Z"/><path d="M12 21V9"/></svg>About</h2>
<div class="about-placeholder">About text coming soon.</div>
</section>
