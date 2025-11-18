# app.py
from flask import Flask, request, redirect, url_for, send_from_directory
import os, subprocess, shlex, html

# Correct project paths
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(PROJECT_ROOT, "data", "alumni.txt")
FRONTEND_DIR = os.path.join(PROJECT_ROOT, "frontend")

# FIX → static_folder should be folder name, NOT full path
app = Flask(__name__, static_folder="frontend", template_folder="frontend")

# ------------ HOME PAGE ------------
@app.route("/add")
@app.route("/frontend")
@app.route("/frontend/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")

# Serve all HTML files inside frontend/
@app.route("/frontend/<path:filename>")
def frontend_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)

# ------------ ADD ALUMNI ------------
@app.route("/add", methods=["POST"])
def add_alumni():
    name = request.form.get("name", "").strip()
    year = request.form.get("year", "").strip()
    course = request.form.get("course", "").strip()
    email = request.form.get("email", "").strip()

    if not name or not email:
        return "Name & Email required", 400

    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"{name},{year},{course},{email}\n")

    return f"""
    <!doctype html>
    <html><head><meta charset="utf-8"><title>Added</title></head>
    <body style="font-family:Arial;text-align:center;padding:30px;background:#eef;">
      <h2>Alumni Added Successfully</h2>
      <p><b>Name:</b> {html.escape(name)}<br>
         <b>Year:</b> {html.escape(year)}<br>
         <b>Course:</b> {html.escape(course)}<br>
         <b>Email:</b> {html.escape(email)}</p>
      <p><a href="http://localhost:5000/frontend/index.html">Home</a> | <a href="http://localhost:5000/frontend/view.html">View All</a></p>
    </body></html>
    """

# ------------ VIEW ALL ------------
@app.route("/view")
def view_all():
    rows = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                while len(parts) < 4: parts.append("")
                rows.append([html.escape(x) for x in parts[:4]])

    table = "<table border='1' cellpadding='8' style='margin:auto;background:white'><tr><th>Name</th><th>Year</th><th>Course</th><th>Email</th></tr>"
    for r in rows:
        table += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    table += "</table>"

    return f"""
    <!doctype html>
    <html><head><meta charset="utf-8"><title>All Alumni</title></head>
    <body style="font-family:Arial;text-align:center;padding:20px;">
      <h2>All Alumni</h2>
      {table}
      <p><a href="/frontend/index.html">Home</a></p>
    </body></html>
    """

# ------------ SEARCH ------------
@app.route("/search")
def search():
    name = request.args.get("name", "").strip()
    if not name:
        return redirect("/frontend/search_alumni.html")

    found = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if name.lower() in parts[0].lower():
                    while len(parts) < 4: parts.append("")
                    found.append(parts[:4])

    if not found:
        body = f"<p>No alumni found with name: <b>{html.escape(name)}</b></p>"
    else:
        body = "<br><br>".join(
            f"Name: {html.escape(r[0])} | Year: {html.escape(r[1])} | Course: {html.escape(r[2])} | Email: {html.escape(r[3])}"
            for r in found
        )
        body = f"<p>{body}</p>"

    return f"""
    <!doctype html>
    <html><head><meta charset="utf-8"><title>Search</title></head>
    <body style="font-family:Arial;text-align:center;padding:20px;">
       <h2>Search Results</h2>
       {body}
       <p><a href="/frontend/index.html">Home</a></p>
    </body></html>
    """

# ------------ RUN SERVER ------------
if __name__ == "__main__":
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    open(DATA_FILE, "a").close()
    app.run(host="0.0.0.0", port=5000, debug=True)