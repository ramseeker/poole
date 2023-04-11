---
layout: default
title: Archive
---

This is all the stuff I have so far...

{% assign sortedPosts = site.posts | sort: 'title' %}


  <ul>
{% for post in sortedPosts %}
 <li> <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
  </ul>
