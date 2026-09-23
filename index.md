---
layout: default
title: Home
---
{% assign work = site.data.work %}
{% assign feed = site.data.substack %}
{% assign featured = work.docs | where: "featured", true %}

<section class="lede" aria-label="About me">
<p>I write documentation for complex products, mostly machine learning platforms, for the developers who build on them. At Google I documented Gemini and PaLM 2 on Vertex AI. Before that I built the <a href="https://learn.stellic.com/" rel="noopener">Stellic Learning Center</a> from nothing, information architecture and all.</p>
<p>I care about what makes an explanation stick. Living with a cognitive neuroscientist gives me a front-row seat to how people actually learn.</p>
<p class="quiet">Off the clock I'm thrifting, crafting, or daydreaming about stories I haven't written yet.</p>
</section>

<section class="block" aria-labelledby="work-h">
<h2 class="label" id="work-h">Selected work</h2>
<ul class="entries">
{% for item in featured %}{% include work-entry.html item=item %}{% endfor %}
</ul>
<a class="more" href="{{ '/my-work.html' | relative_url }}">Full portfolio →</a>
</section>

<section class="block" aria-labelledby="writing-h">
<h2 class="label" id="writing-h">Writing</h2>
{% include writing-list.html items=work.writing %}
</section>

<section class="block newsletter" aria-labelledby="news-h">
<h2 class="label" id="news-h">Newsletter</h2>
<p><em>{{ feed.title }}</em> is where I write about information, language, and myth. It's free and it shows up occasionally.</p>
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
