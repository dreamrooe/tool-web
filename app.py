from flask import Flask, render_template
import random
import string
import time
import base64

app = Flask(__name__)

def gen_pwd(length=16):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.sample(chars, length))

@app.route('/')
def index():
    return render_template("en_index.html",
        pwd12=gen_pwd(12),
        pwd16=gen_pwd(16),
        pwd24=gen_pwd(24))

@app.route('/timestamp')
def timestamp_page():
    return render_template("timestamp.html", now_ts=int(time.time()))

@app.route('/base64')
def base64_page():
    return render_template("base64.html")

@app.route('/sitemap.xml')
def sitemap():
    return app.send_static_file("sitemap.xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)