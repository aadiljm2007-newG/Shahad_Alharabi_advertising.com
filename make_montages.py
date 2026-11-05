from PIL import Image
import os

img_dir = r"C:\Users\asus\OneDrive\Desktop\Temp\images"
files = sorted([f for f in os.listdir(img_dir) if f.lower().endswith(('.jpeg', '.jpg', '.png'))])

out_dir = r"C:\Users\asus\OneDrive\Desktop\Temp\img_montage"
os.makedirs(out_dir, exist_ok=True)

# Create 4 montage sheets of 16 images each (4x4)
thumb_w, thumb_h = 400, 300
cols, rows = 4, 4

for sheet_idx in range(4):
    montage = Image.new('RGB', (cols * thumb_w, rows * thumb_h), (20, 20, 20))
    start_i = sheet_idx * 16
    end_i = min(start_i + 16, len(files))
    
    for i in range(start_i, end_i):
        slot = i - start_i
        r = slot // cols
        c = slot % cols
        p = os.path.join(img_dir, files[i])
        with Image.open(p) as img:
            img = img.convert('RGB')
            img.thumbnail((thumb_w - 10, thumb_h - 10))
            # paste in center of slot
            x = c * thumb_w + (thumb_w - img.width) // 2
            y = r * thumb_h + (thumb_h - img.height) // 2
            montage.paste(img, (x, y))
            
    montage.save(os.path.join(out_dir, f"sheet_{sheet_idx+1}.jpg"), quality=85)

print("Montages created successfully!")
