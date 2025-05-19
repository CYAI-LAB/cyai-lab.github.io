---
layout: splash
title: "Members"
permalink: /members/
author_profile: false
classes: wide
---

<style>
.member-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
}
.member-card {
  flex: 1 1 calc(50% - 2rem); /* 2열: 50% - 여백 */
  max-width: calc(50% - 2rem);
}
@media (min-width: 960px) {
  .member-card {
    flex: 1 1 calc(33.333% - 2rem); /* 3열 for desktop */
    max-width: calc(33.333% - 2rem);
  }
}
</style>

## 교수

<div class="row">
  {% for member in site.data.members.professors %}
  <div class="col-12">
    <div class="row">
      <div class="col-3">
        <img src="{{ member.image }}" alt="{{ member.name }}" style="width: 100px; height: 100px; object-fit: cover; border-radius: 50%;">
      </div>
      <div class="col-9">
        <p><strong style="font-size: 1.2rem;">{{ member.name }}</strong><br>
        <em>{{ member.position }}</em></p>

        {% if member.short_bio %}
        <p style="font-size: 0.95rem;">{{ member.short_bio }}</p>
        {% endif %}

        <p style="font-size: 0.9rem;">
          📧 <a class="email" data-user="{{ member.email_user }}" data-domain="{{ member.email_domain }}"></a><br>
          {% if member.homepage and member.homepage != "" %}
          🏠 <a href="{{ member.homepage }}" target="_blank">홈페이지</a>
          {% endif %}
        </p>
        {% if member.education %}
        <strong style="font-size: 0.95rem;">Education:</strong>
        <ul style="font-size: 0.9rem;">
          {% for edu in member.education %}
            <li>{{ edu }}</li>
          {% endfor %}
        </ul>
        {% endif %}

        {% if member.career %}
        <strong style="font-size: 0.95rem;">Career:</strong>
        <ul style="font-size: 0.9rem;">
          {% for job in member.career %}
            <li>{{ job }}</li>
          {% endfor %}
        </ul>
        {% endif %}
      </div>
    </div>
    <hr>
  </div>
  {% endfor %}
</div>

<!-- ## 박사과정 -->

<!-- <div class="member-grid">
  {% for member in site.data.members.phd_students %}
  <div class="member-card">
    {% if member.image %}
    <img src="{{ member.image }}" alt="{{ member.name }}" style="width: 100px; height: 100px; object-fit: cover; border-radius: 50%;">
    {% endif %}
    <h3>{{ member.name }}</h3>
    <p><strong>{{ member.role }}</strong></p>
    <p>✉ {{ member.email }}</p>
    {% if member.homepage %}
    <p>🌐 <a href="{{ member.homepage }}" target="_blank">Homepage</a></p>
    {% endif %}
    {% if member.interests %}
    <strong>Interests:</strong>
    <ul>
      {% for interest in member.interests %}
      <li>{{ interest }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  </div>
  {% endfor %}
</div> -->

<!-- ## 석사과정 -->

<!-- <div class="member-grid">
  {% for member in site.data.members.phd_students %}
  <div class="member-card">
    {% if member.image %}
    <img src="{{ member.image }}" alt="{{ member.name }}" style="width: 100px; height: 100px; object-fit: cover; border-radius: 50%;">
    {% endif %}
    <h3>{{ member.name }}</h3>
    <p><strong>{{ member.role }}</strong></p>
    <p>✉ {{ member.email }}</p>
    {% if member.homepage %}
    <p>🌐 <a href="{{ member.homepage }}" target="_blank">Homepage</a></p>
    {% endif %}
    {% if member.interests %}
    <strong>Interests:</strong>
    <ul>
      {% for interest in member.interests %}
      <li>{{ interest }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  </div>
  {% endfor %}
</div> -->

## 학부연구생

<div class="member-grid">
  {% for member in site.data.members.undergraduates %}
  <div class="member-card">
    {% if member.image %}
    <img src="{{ member.image }}" alt="{{ member.name }}" style="width: 100px; height: 100px; object-fit: cover; border-radius: 50%;">
    {% endif %}
    <h3>{{ member.name }}</h3>
    <p><strong>{{ member.role }}</strong></p>
    <p>✉ <a class="email" data-user="{{ member.email_user }}" data-domain="{{ member.email_domain }}"></a></p>
    {% if member.homepage %}
    <p>🌐 <a href="{{ member.homepage }}" target="_blank">Homepage</a></p>
    {% endif %}
    {% if member.interests %}
    <strong>Interests:</strong>
    <ul>
      {% for interest in member.interests %}
      <li>{{ interest }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  </div>
  {% endfor %}
</div>