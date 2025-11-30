---
layout: default
title: My Work
---
<style>
.carousel {
  display: flex;
  overflow-x: scroll;
  scroll-snap-type: x mandatory;
  gap: 1rem;
  padding: 1rem 0;
  margin: 2rem 0;
}
.carousel::-webkit-scrollbar {
  height: 8px;
}
.carousel::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 10px;
}
.carousel::-webkit-scrollbar-thumb {
  background: var(--color-accent);
  border-radius: 10px;
}
.carousel-item {
  min-width: 300px;
  scroll-snap-align: start;
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
.carousel-item h3 {
  margin-top: 0;
  color: var(--color-text-primary);
}
.carousel-item p {
  color: var(--color-text-secondary);
  font-size: 0.95rem;
}
.carousel-item a {
  color: var(--color-accent);
  text-decoration: none;
  font-weight: 600;
}
.carousel-item a:hover {
  text-decoration: underline;
}
</style>
<h1>My Work</h1>
<p>Here's a selection of projects that showcase my approach to technical content.</p>
<div class="carousel">
  <div class="carousel-item">
    <h3>Google Gemini Documentation</h3>
    <p>Led the documentation strategy for Google's flagship LLM, creating developer guides, API references, and code samples for millions of users.</p>
    <a href="#">View samples →</a>
  </div>
  
  <div class="carousel-item">
    <h3>Stellic Learning Center</h3>
    <p>Architected and built a complete documentation portal from scratch, migrating 500+ pages to GitBook with AI-powered search.</p>
    <a href="https://learn.stellic.com/" target="_blank">Visit site →</a>
  </div>
  
  <div class="carousel-item">
    <h3>PaLM 2 Launch Content</h3>
    <p>Created launch documentation and hand-crafted API reference for Google's PaLM 2 model release.</p>
    <a href="#">View samples →</a>
  </div>
  
  <div class="carousel-item">
    <h3>AWS Training Content</h3>
    <p>Edited 30+ technical courses across Game Tech, Security, and IoT, contributing to a satisfaction score increase from 4.0 to 4.8.</p>
    <a href="#">Learn more →</a>
  </div>
  
  <div class="carousel-item">
    <h3>Vertex AI Model Registry</h3>
    <p>Developed comprehensive documentation for Google Cloud's ML model management system.</p>
    <a href="#">View samples →</a>
  </div>

  <div class="carousel-item">
    <h3>IBM Big Data Analytics</h3>
    <p>Early career foundation in technical writing, learning to navigate large-scale documentation systems and cross-functional collaboration in an enterprise environment.</p>
    <a href="#">Learn more →</a>
  </div>
</div>
<p style="margin-top: 2rem;">Want to see more? <a href="mailto:sarahcdugan@gmail.com">Get in touch</a> and I can share specific writing samples.</p>
