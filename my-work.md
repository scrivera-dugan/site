---
layout: default
title: Portfolio
description: Documentation, systems, and writing by Sarah Dugan, mostly for machine learning products.
---
{% assign work = site.data.work %}

<header class="page-head">
<h1>Docs, systems, and tools I've built.</h1>
<p>Mostly machine learning, mostly for developers.</p>
</header>

<section class="block" aria-labelledby="docs-h">
<h2 class="label" id="docs-h">Documentation</h2>
<ul class="entries">
{% for item in work.docs %}{% include work-entry.html item=item %}{% endfor %}
</ul>
</section>

<section class="block" aria-labelledby="writing-h">
<h2 class="label" id="writing-h">Writing</h2>
<ul class="entries">
{% for item in work.writing %}
<li class="entry">
    <p class="meta"><span>{{ item.where }}</span></p>
    <div class="body">
        <h3><a href="{{ item.url }}" rel="noopener">{{ item.title }}<span class="ext" aria-hidden="true"> ↗</span></a></h3>
        <p>{{ item.summary }}</p>
    </div>
</li>
{% endfor %}
</ul>
</section>

<p class="closing">Want more samples? <a href="mailto:sarahcdugan@gmail.com">Get in touch</a> and I'll share additional writing.</p>
