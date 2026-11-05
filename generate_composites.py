import os
from PIL import Image, ImageOps
from mapping_config import CANVA_MAP, GAMMA_MAP

IMG_DIR = r"C:\Users\asus\OneDrive\Desktop\Temp\images"
LOGO_PATH = r"C:\Users\asus\OneDrive\Desktop\Temp\company logo.png"

def fit_image_into_box(img, target_w, target_h):
    # Center crop / fit nicely maintaining aspect ratio
    return ImageOps.fit(img, (target_w, target_h), method=Image.Resampling.LANCZOS)

def build_composite_pages(pages_dir, out_dir, mapping, is_gamma=False):
    os.makedirs(out_dir, exist_ok=True)
    logo_img = Image.open(LOGO_PATH).convert('RGBA')
    
    for page_num in range(1, 11):
        page_bg_path = os.path.join(pages_dir, f"page_{page_num}.png")
        if not os.path.exists(page_bg_path):
            print(f"Warning: {page_bg_path} missing")
            continue
            
        page_im = Image.open(page_bg_path).convert('RGBA')
        items = mapping.get(page_num, [])
        
        for item in items:
            box = item['box']
            x1, y1, x2, y2 = box
            w = x2 - x1
            h = y2 - y1
            
            if item.get('logo'):
                # Resize logo fitting nicely within box with padding
                pad = 10
                fitted_logo = ImageOps.contain(logo_img, (w - 2*pad, h - 2*pad), method=Image.Resampling.LANCZOS)
                paste_x = x1 + (w - fitted_logo.width) // 2
                paste_y = y1 + (h - fitted_logo.height) // 2
                page_im.paste(fitted_logo, (paste_x, paste_y), fitted_logo)
            else:
                img_path = os.path.join(IMG_DIR, item['file'])
                if not os.path.exists(img_path):
                    print(f"Warning: image {img_path} not found")
                    continue
                with Image.open(img_path) as src_im:
                    src_im = src_im.convert('RGBA')
                    fitted = fit_image_into_box(src_im, w, h)
                    page_im.paste(fitted, (x1, y1))
                    
        out_page_path = os.path.join(out_dir, f"page_{page_num}.png")
        # Save as RGB JPEG/PNG for highest quality
        page_im.convert('RGB').save(out_page_path, quality=95)
        print(f"Rendered composite {out_page_path}")

print("Building Canva edited pages...")
build_composite_pages(
    r"C:\Users\asus\OneDrive\Desktop\Temp\canva_pages",
    r"C:\Users\asus\OneDrive\Desktop\Temp\canva_edited_pages",
    CANVA_MAP,
    is_gamma=False
)

print("Building Gamma edited pages...")
build_composite_pages(
    r"C:\Users\asus\OneDrive\Desktop\Temp\gamma_pages",
    r"C:\Users\asus\OneDrive\Desktop\Temp\gamma_edited_pages",
    GAMMA_MAP,
    is_gamma=True
)

print("All composite pages successfully generated!")
