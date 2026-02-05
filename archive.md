---
layout: default
title: Archive
---

<ul>
  {% assign sorted_posts = site.posts | sort: 'title' %}
  {% for post in sorted_posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
