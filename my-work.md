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
    <h3>Vertex AI Grounding</h3>
    <p>Complete documentation set for grounding prompt responses using Gemini, demonstrating how to enhance LLM outputs with factual grounding.</p>
    <a href="https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview" target="_blank">View docs →</a>
  </div>
  
  <div class="carousel-item">
    <h3>Gemini Embeddings</h3>
    <p>Comprehensive documentation covering embeddings fundamentals and implementation, telling the complete AI/ML embeddings story.</p>
    <a href="https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings" target="_blank">View docs →</a>
  </div>

  <div class="carousel-item">
    <h3>Vector Search</h3>
    <p>Full documentation set for Google Cloud's Vector Search product, enabling similarity search at scale.</p>
    <a href="https://cloud.google.com/vertex-ai/docs/vector-search/overview" target="_blank">View docs →</a>
  </div>
  
  <div class="carousel-item">
    <h3>Vertex AI Model Registry Launch</h3>
    <p>Launch announcement blog post introducing Google Cloud's centralized model management system.</p>
    <a href="https://cloud.google.com/blog/products/ai-machine-learning/vertex-ai-model-registry" target="_blank">Read post →</a>
  </div>

  <div class="carousel-item">
    <h3>MLOps with BigQuery ML & Vertex AI</h3>
    <p>Developer-focused blog demonstrating practical MLOps workflows across Google Cloud's ML platform.</p>
    <a href="https://cloud.google.com/blog/topics/developers-practitioners/mlops-bigquery-ml-vertex-ai-model-registry" target="_blank">Read post →</a>
  </div>

  <div class="carousel-item">
    <h3>Why I'm Excited About Model Registry</h3>
    <p>Personal perspective on the value of centralized model management for ML teams, published on Medium.</p>
    <a href="https://medium.com/google-cloud/three-reasons-why-im-excited-about-google-cloud-vertex-ai-model-registry-c088e6bbbf3b" target="_blank">Read post →</a>
  </div>
  
  <div class="carousel-item">
    <h3>Stellic Learning Center</h3>
    <p>Architected and built a complete documentation portal from scratch, migrating 500+ pages to GitBook with AI-powered search.</p>
    <a href="https://learn.stellic.com/" target="_blank">Visit site →</a>
  </div>
</div>
<p style="margin-top: 2rem;">Want to see more? <a href="mailto:sarahcdugan@gmail.com">Get in touch</a> and I can share additional writing samples.</p>
