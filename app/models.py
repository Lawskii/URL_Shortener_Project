import sqlite3

DB_NAME = 'urls.db'


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE NOT NULL,
            long_url TEXT NOT NULL,
            clicks INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()


def save_url(short_code, long_url):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO urls (short_code, long_url) VALUES (?, ?)",
              (short_code, long_url))
    conn.commit()
    conn.close()


def url_exists(short_code):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT 1 FROM urls WHERE short_code = ?", (short_code,))
    exists = c.fetchone() is not None
    conn.close()
    return exists
def get_long_url(short_code):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

def increment_click(short_code):
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?", (short_code,))
    conn.commit()
    conn.close()
