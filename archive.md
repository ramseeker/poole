---
layout: default
title: Archive
---
{% assign sortedPosts = site.posts | sort: 'title' %}


  <ul>
	  {% for post in site.posts %}
	    {% unless post.next %}
	      <h3>{{ post.date | date: '%Y %b' }}</h3>
	    {% else %}
	      {% capture year %}{{ post.date | date: '%Y %b' }}{% endcapture %}
	      {% capture nyear %}{{ post.next.date | date: '%Y %b' }}{% endcapture %}
	      {% if year != nyear %}
	        <h3>{{ post.date | date: '%Y %b' }}</h3>
	      {% endif %}
	    {% endunless %}

	    <li>{{ post.date | date: '%B %d, %Y' }}
<a href="{{ post.url }}">{{ post.title }}</a></li>
	  {% endfor %}
	</ul>

    
