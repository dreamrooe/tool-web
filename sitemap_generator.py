import os
os.makedirs("static", exist_ok=True)
# 你的Vercel域名，已自动填好
domain = "https://tool-web-coral.vercel.app/"
urls = ["/", "/timestamp", "/base64"]

xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
for url in urls:
    xml += f'''  <url>
    <loc>{domain}{url.lstrip('/')}</loc>
    <lastmod>{os.path.getmtime(f'templates/{url.split("/")[-1]}.html') if url != '/' else os.path.getmtime('templates/en_index.html')}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
'''
xml += '</urlset>'

with open("static/sitemap.xml", "w", encoding="utf-8") as f:
    f.write(xml)
print("✅ sitemap.xml 生成成功！")
print(f"站点地图地址：{domain}sitemap.xml")