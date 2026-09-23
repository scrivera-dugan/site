---
layout: default
title: Home
---
{% assign work = site.data.work %}
{% assign feed = site.data.substack %}
{% assign r = site.data.resume %}

<section class="block" id="work" aria-labelledby="work-h">
{% include section-head.html id="work-h" label="Selected" title="work" %}

<p class="section-intro">A note on what&rsquo;s here: much of my strongest work lives behind NDAs and internal docs, so this is a partial, public-facing slice &mdash; including early testing on Gemini (back when it was Bard) at Google, across a range of tech-writing tools and stacks. For now these are just links. I&rsquo;ll build them into proper case studies down the line.</p>

{% if work.featured %}
<article class="work-card work-card--lead">
    <div class="body">
        <h3><a href="{{ work.featured.url }}" rel="noopener">{{ work.featured.title }}<span class="ext" aria-hidden="true"> &#8599;</span></a></h3>
        <p class="org">{{ work.featured.org }} &middot; {{ work.featured.kind }}</p>
        <p>{{ work.featured.summary }}</p>
        {% if work.featured.meta %}<p class="card-meta">{{ work.featured.meta }}</p>{% endif %}
    </div>
</article>
{% endif %}

<div class="work-grid">
{% for item in work.docs %}
<article class="work-card">
    <div class="body">
        <h3><a href="{{ item.url }}" rel="noopener">{{ item.title }}<span class="ext" aria-hidden="true"> &#8599;</span></a></h3>
        <p class="org">{{ item.org }} &middot; {{ item.kind }}</p>
        <p>{{ item.summary }}</p>
        {% if item.gated %}<p class="card-gated">Access-gated &mdash; links to stellic.com</p>{% endif %}
    </div>
</article>
{% endfor %}
</div>
{% if work.writing and work.writing.size > 0 %}
<h3 class="sub-label">Writing elsewhere</h3>
<ul class="index-list">
{% for item in work.writing %}
    <li><a class="index-row" href="{{ item.url }}" rel="noopener">
        <span class="what">{{ item.title }}</span>
        <span class="where">{{ item.where }}</span>
        <span class="when">&#8599;</span>
    </a></li>
{% endfor %}
</ul>
{% endif %}
</section>

<section class="block newsletter" id="substack" aria-labelledby="news-h">
{% include section-head.html id="news-h" label="Write this" title="down" %}
<div class="boxed">
<span class="eyebrow">Newsletter</span>
<p>My newsletter on Substack, about information, language, and myth. It's free and it shows up occasionally.</p>
{% if feed.posts and feed.posts.size > 0 %}
<ul class="index-list">
    {% for post in feed.posts limit: 3 %}
    <li><a class="index-row" href="{{ post.link }}" rel="noopener">
        <span class="what">{{ post.title }}</span>
        <span class="where">Substack</span>
        <span class="when">{{ post.date | date: "%b %-d, %Y" }}</span>
    </a></li>
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
</div>
</section>

<section class="block resume" id="resume" aria-labelledby="resume-h">
{% include section-head.html id="resume-h" label="Where I've" title="been" %}
<h1 class="print-only">Sarah C. Dugan</h1>
<p class="contact print-only">sarahcdugan@gmail.com · linkedin.com/in/scdugan · sarahdocs.com</p>
<p class="summary">{{ r.summary }}</p>

<h3 class="sub-label">Experience</h3>
<ul class="index-list">
{% for job in r.experience %}
    <li id="{{ job.id }}">
        <span class="index-row">
            <span class="what">{{ job.title }}</span>
            <span class="where"><span class="co">{{ job.company }}</span>{% if job.industry %}<span class="industry">{{ job.industry }}</span>{% endif %}{% if job.location %}<span class="loc">{{ job.location }}</span>{% endif %}</span>
            <span class="when">{{ job.start }}{% if job.end %} &ndash; {{ job.end }}{% endif %}</span>
        </span>
        {%- comment -%}
        The bullets stay in the markup but are hidden on screen: the section
        is a glance, while the printed PDF is still a full resume.
        {%- endcomment -%}
        {% if job.bullets %}<ul class="role-detail print-only">
        {% for bullet in job.bullets %}<li>{{ bullet }}</li>
        {% endfor %}</ul>{% endif %}
    </li>
{% endfor %}
</ul>

<h3 class="sub-label">Education</h3>
<ul class="index-list">
{% for school in r.education %}
    <li>
        <span class="index-row">
            <span class="what">{{ school.degree }}</span>
            <span class="where">{{ school.school }}</span>
            <span class="when">{{ school.year }}</span>
            {% if school.minor %}<span class="note">{{ school.minor }}</span>{% endif %}
        </span>
    </li>
{% endfor %}
</ul>
</section>

<section class="block" id="about" aria-labelledby="about-h">
{% include section-head.html id="about-h" label="A little" title="about me" %}

<div class="prose-columns">
<p><img class="initial" src="{{ '/images/initial-s.jpg' | relative_url }}" alt="" aria-hidden="true"><span class="visually-hidden">S</span>arah grew up reading, writing, and watching all the movies she could get her hands on. As the middle child of five, she spent years working at her parents' bed and breakfast, where she met countless fascinating guests and made an equal number of beds.</p>

<p>It was actually one of those guests who first suggested technical writing to Sarah when she was in high school and connected her with an internship at IBM, and the rest is history. A Boston native, Sarah is a New Englander at heart and is grateful for how it shaped her.</p>

<h3>Today</h3>

<p>Sarah lives in Minneapolis and has become an academic nomad&mdash;she and her husband (a cognitive neuroscience professor) have moved four times since 2020. Living with someone who studies attention, memory, and learning has given her a front-row seat to understanding how the brain actually processes information. She's always connecting those insights back to her work: how do people absorb new concepts? What makes technical explanations stick?</p>

<h3>Interests</h3>

<p>When she's not working, you'll find her puttering, thrifting, crafting, and daydreaming story ideas.</p>
</div>

<p class="credit">Initial S from Varro, <em>De re rustica</em>, <a href="https://digital.bodleian.ox.ac.uk/objects/e2c7b068-4180-48a9-95a9-d0fa21109bdb/">MS. Lat. class. d. 2</a>, fol. 1r. Image: Bodleian Libraries, University of Oxford. <a href="https://creativecommons.org/licenses/by-nc/4.0/">CC BY-NC 4.0</a>.</p>
</section>
