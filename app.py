from flask import Flask, render_template, send_from_directory
import os
import time

app = Flask(__name__)

# 主页 - 密码生成器
@app.route('/')
def index():
    return render_template('en_index.html')

# 时间戳工具
@app.route('/timestamp')
def timestamp():
    return render_template('timestamp.html')

# Base64工具
@app.route('/base64')
def base64():
    return render_template('base64.html')

# 自动生成 sitemap.xml（谷歌永久自动抓取，无需手动推送）
@app.route('/sitemap.xml')
def sitemap():
    domain = "https://tool-web-coral.vercel.app"
    urls = [
        "",
        "timestamp",
        "base64"
    ]
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
    for u in urls:
        loc = f"{domain}/{u}" if u else domain
        xml += f'''  <url>
    <loc>{loc}</loc>
    <lastmod>{time.strftime('%Y-%m-%d')}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
'''
    xml += '</urlset>'
    return xml, 200, {'Content-Type': 'application/xml'}

# robots.txt 引导谷歌抓取，提升收录速度
@app.route('/robots.txt')
def robots():
    txt = '''User-agent: *
Allow: /
Sitemap: https://tool-web-coral.vercel.app/sitemap.xml
'''
    return txt, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(debug=False)