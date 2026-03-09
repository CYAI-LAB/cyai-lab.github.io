from flask import Flask, render_template_string, send_from_directory
import yaml

app = Flask(__name__)

with open("_data/members.yml", "r", encoding="utf-8") as f:
    members = yaml.safe_load(f)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Members Preview</title>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; background: #fafafa; }
  h1 { border-bottom: 2px solid #333; padding-bottom: 10px; }
  h2 { color: #333; margin-top: 40px; border-bottom: 1px solid #ccc; padding-bottom: 8px; }
  .member-grid { display: flex; flex-wrap: wrap; gap: 2rem; }
  .member-card { flex: 1 1 calc(33.333% - 2rem); max-width: calc(33.333% - 2rem); background: #fff; border-radius: 10px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
  .member-card img { width: 100px; height: 100px; object-fit: cover; border-radius: 50%; }
  .member-card h3 { margin: 10px 0 5px; }
  .member-card ul { padding-left: 20px; font-size: 0.9rem; }
  .professor-section { display: flex; gap: 20px; background: #fff; border-radius: 10px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
  .professor-section img { width: 120px; height: 120px; object-fit: cover; border-radius: 50%; }
  @media (max-width: 768px) { .member-card { flex: 1 1 100%; max-width: 100%; } }
</style>
</head>
<body>
<h1>Members</h1>

<h2>교수</h2>
{% for m in professors %}
<div class="professor-section">
  <div><img src="/assets/images/{{ m.image.split('/')[-1] }}" alt="{{ m.name }}"></div>
  <div>
    <strong style="font-size:1.2rem;">{{ m.name }}</strong><br>
    <em>{{ m.position }}</em><br>
    📧 {{ m.email_user }}@{{ m.email_domain }}<br>
    {% if m.homepage %}🏠 <a href="{{ m.homepage }}">홈페이지</a>{% endif %}
    {% if m.education %}
    <p><strong>Education:</strong></p>
    <ul>{% for e in m.education %}<li>{{ e }}</li>{% endfor %}</ul>
    {% endif %}
    {% if m.career %}
    <p><strong>Career:</strong></p>
    <ul>{% for c in m.career %}<li>{{ c }}</li>{% endfor %}</ul>
    {% endif %}
  </div>
</div>
{% endfor %}

<h2>학부연구생</h2>
<div class="member-grid">
{% for m in undergraduates %}
  <div class="member-card">
    <img src="/assets/images/{{ m.image.split('/')[-1] }}" alt="{{ m.name }}">
    <h3>{{ m.name }}</h3>
    <p><strong>{{ m.role }}</strong></p>
    <p>✉ {{ m.email_user }}@{{ m.email_domain }}</p>
    {% if m.interests %}
    <strong>Interests:</strong>
    <ul>{% for i in m.interests %}<li>{{ i }}</li>{% endfor %}</ul>
    {% endif %}
  </div>
{% endfor %}
</div>

<h2>Alumni</h2>
<div class="member-grid">
{% for m in alumni %}
  <div class="member-card">
    <img src="/assets/images/{{ m.image.split('/')[-1] }}" alt="{{ m.name }}">
    <h3>{{ m.name }}</h3>
    <p><strong>{{ m.role }}</strong></p>
    <p>✉ {{ m.email_user }}@{{ m.email_domain }}</p>
    {% if m.interests %}
    <strong>Interests:</strong>
    <ul>{% for i in m.interests %}<li>{{ i }}</li>{% endfor %}</ul>
    {% endif %}
  </div>
{% endfor %}
</div>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(
        TEMPLATE,
        professors=members.get("professors", []),
        undergraduates=members.get("undergraduates", []),
        alumni=members.get("alumni", []),
    )

@app.route("/assets/images/<path:filename>")
def serve_image(filename):
    return send_from_directory("assets/images", filename)

if __name__ == "__main__":
    print("Preview: http://localhost:5000")
    app.run(debug=True, port=5000)
