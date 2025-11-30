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
.carousel-item a:hov
