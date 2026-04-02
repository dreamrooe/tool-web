import os
os.makedirs("static", exist_ok=True)
# 后面换成你自己的Vercel域名
domain = "https://xxx.vercel.app"
urls = ["/","/timestamp","/base64"]

xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
for u in urls:
    xml += f"<url><loc>{domain}{u}</loc></url>\n"
xml += "</urlset>"

with open("static/sitemap.xml","w",encoding="utf-8") as f:
    f.write(xml)
print("✅ sitemap.xml 生成成功")