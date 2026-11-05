import os, urllib.parse

img_dir = r'C:\Users\asus\OneDrive\Desktop\Temp\images'
files = sorted([f for f in os.listdir(img_dir) if f.lower().endswith(('.jpeg', '.jpg', '.png'))])

html = '''<!DOCTYPE html><html><head><style>
body { background: #111; color: #fff; font-family: sans-serif; }
.grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; padding: 20px; }
.card { background: #222; padding: 10px; border-radius: 8px; text-align: center; }
img { max-width: 100%; height: 180px; object-fit: cover; border-radius: 4px; }
p { font-size: 11px; margin-top: 8px; word-break: break-all; color: #ccc; }
span { font-weight: bold; color: #d4af37; font-size: 14px; }
</style></head><body><h1>All 64 Images</h1><div class="grid">'''

for idx, f in enumerate(files):
    quoted = urllib.parse.quote(f)
    html += f'<div class="card"><span>#{idx}</span><br><img src="images/{quoted}"><p>{f}</p></div>'

html += '</div></body></html>'

with open(r'C:\Users\asus\OneDrive\Desktop\Temp\preview_images.html', 'w', encoding='utf-8') as out:
    out.write(html)
print('HTML created successfully!')
