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

{% for tag in site.tags %}
  {% assign tag_name = tag | first %}
  {% assign tag_name_pretty = tag_name | replace: "_", " " | capitalize %}
  <div class="tag-list">
    <div id="#{{ tag_name | slugize }}"></div>
    <p class="post-list-heading line-bottom"> {{ tag_name }}: </p>
    <a name="{{ tag_name | slugize }}"></a>
    <ul class="post-list post-list-narrow">
     {% for post in site.tags[tag_name] %}
     <li>
       {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
       <b>
         <a href="{{ post.url | relative_url }}">
           {{ post.title | escape }}
         </a>
       </b> - <i>{{ post.date | date: date_format }}</i>
     </li>
     {% endfor %}
    </ul>
  </div>
{% endfor %}
</div>
