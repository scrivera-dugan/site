---
layout: default
title: Home
---
{% assign feed = site.data.substack %}
<section class="hero">
    <h1 class="weave">Hi, I'm Sarah.</h1>
    <div class="intro">
        <p>I'm a technical and creative writer. I've written docs for over ten years and worked in AI for eight.</p>
        <p>I also write a newsletter, <em>{{ feed.title }}</em>, about information, language, myth, and whatever else catches my interest.</p>
    </div>
    <div class="home-links">
        <a href="mailto:sarahcdugan@gmail.com">Email</a>
        <a href="https://www.linkedin.com/in/scdugan/">LinkedIn</a>
        <a href="https://github.com/scrivera-dugan">GitHub</a>
        <a href="https://substack.com/@sarahdocs">Substack</a>
    </div>
</section>

<ul class="index" aria-label="Sections">
    <li><a href="{{ '/my-work.html' | relative_url }}"><span class="name">Portfolio</span><span class="desc">Docs, systems, and tools I've built</span></a></li>
    <li><a href="{{ '/resume.html' | relative_url }}"><span class="name">Resume</span><span class="desc">Ten years in docs, eight in AI</span></a></li>
    <li><a href="{{ '/friends&philosophy.html' | relative_url }}"><span class="name">Philosophy</span><span class="desc">How I think about the work</span></a></li>
    <li><a href="{{ '/about-me.html' | relative_url }}"><span class="name">About</span><span class="desc">The rest of me</span></a></li>
</ul>

<section class="feed" aria-labelledby="feed-title">
    <h2 id="feed-title">{{ feed.title }}</h2>
    <p class="sub">My newsletter on Substack.</p>
    {% if feed.posts and feed.posts.size > 0 %}
    <ul class="index">
        {% for post in feed.posts limit: 3 %}
        <li><a href="{{ post.link }}"><span class="name">{{ post.title }}</span><span class="desc">{{ post.date | date: "%b %-d, %Y" }}</span></a></li>
        {% endfor %}
    </ul>
    {% endif %}
    <a class="button" href="{{ feed.link }}">Subscribe on Substack</a>
</section>
