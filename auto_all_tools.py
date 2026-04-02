import os
os.makedirs("templates", exist_ok=True)

pages = [
("en_index","Password Generator","Strong Password"),
("timestamp","Timestamp Converter","Unix Time Stamp"),
("base64","Base64 Encoder Decoder","Encode Decode Text")
]

for fname,title,desc in pages:
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title} | Free Online Tool</title>
<meta name="description" content="{desc} free online utility no register.">
</head>
<body><h1>{title}</h1></body>
</html>'''
    with open(f"templates/{fname}.html","w",encoding="utf-8") as f:
        f.write(html)
print("✅ 页面批量生成完成")