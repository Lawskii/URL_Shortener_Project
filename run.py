from flask import Flask, render_template, request
import random
import string

from app.models import init_db, save_url, url_exists

# default will look for 'templates/' in the same folder as run.py
app = Flask(__name__)

# Initialize DB when app starts
init_db()


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form.get('long_url')
    if not long_url:
        return "Error: No URL provided", 400

    # Generate a unique short code
    short_code = generate_short_code()
    while url_exists(short_code):
        short_code = generate_short_code()

    # Save short_code and long_url to database
    save_url(short_code, long_url)

    # Build full short URL
    short_url = request.host_url + short_code

    # Render sleek success page
    return render_template('shortened.html', short_url=short_url)
from flask import redirect
from app.models import get_long_url, increment_click

@app.route('/<short_code>')
def redirect_to_url(short_code):
    long_url = get_long_url(short_code)
    if long_url:
        increment_click(short_code)
        return redirect(long_url)
    else:
        return "Short URL not found", 404


if __name__ == '__main__':
    app.run(debug=True)
