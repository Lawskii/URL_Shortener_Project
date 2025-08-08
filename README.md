#  Flask URL Shortener

This is a simple, elegant URL shortener built with **Flask**, designed as an internship project. It allows users to shorten long URLs and get a unique short link that redirects to the original page.

> Clean UI •  Functional Backend • Built in Python + Flask

---

##  Features

-  Shortens long URLs into neat, unique short links
-  Redirects users from short URL to original
-  Copy to clipboard button (UX win)
-  Sleek and modern UI
-  Smart system to avoid duplicate entries in DB

---

##  How It Works

1. Paste your long URL in the form
2. Flask checks if it already exists in the DB
3. If not, it generates a short unique string
4. Stores the mapping in an SQLite database
5. Redirects users when the short URL is visited

---

##  Tech Stack

| Layer        | Technology     |
|--------------|----------------|
| Backend      | Python, Flask  |
| Frontend     | HTML, CSS, JavaScript |
| Database     | SQLite         |

---


