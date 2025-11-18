# Digital_Alumni_Management
A lightweight web-based Alumni Management System built using HTML, CSS, Flask, and C++. Supports adding, viewing, and searching alumni with fast file-based storage and a C++ search engine. Simple, portable, and ideal for academic DSA projects.
Digital Alumni Management System

A lightweight and user-friendly web-based Alumni Management System built using HTML, CSS, Flask (Python), and C++. It allows colleges or institutions to easily add, view, and search alumni records using simple file-based storage. This project is ideal for academic submissions, DSA concepts, and demonstrating backend–frontend integration with file handling.

Features

Add Alumni – Stores Name, Year, Course, Email

View Alumni – Displays all records in a structured HTML table

Search Alumni – Fast name-based search using a C++ search engine

Events Page – Static page for alumni announcements

File Handling – All records stored in alumni.txt

Flask Backend – Handles routing, submissions, and responses


Tech Stack

Frontend: HTML, CSS
Backend: Python Flask
Search Engine: C++
Storage: Text File (alumni.txt)

Folder Structure

Digital_Alumni_Management/
│-- app.py
│-- data/
│   └── alumni.txt
│-- frontend/
│   ├── index.html
│   ├── add_alumni.html
│   ├── search_alumni.html
│   ├── view_alumni.html
│   └── events.html
│-- cpp/
│   ├── search_tool.cpp
│   └── search_tool

How to Run

1. Install Flask
pip install flask


2. Run the server
python3 app.py


3. Open in browser
http://localhost:5000/



Compile Search Tool (Optional)

g++ cpp/search_tool.cpp -o cpp/search_tool

Future Enhancements

Admin login

Database integration

Export data to CSV/PDF

Improved UI design
