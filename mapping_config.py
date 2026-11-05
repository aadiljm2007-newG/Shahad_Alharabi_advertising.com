import os
from PIL import Image, ImageOps

IMG_DIR = r"C:\Users\asus\OneDrive\Desktop\Temp\images"

# Mapping for Canva pages
CANVA_MAP = {
    1: [
        {"file": "WhatsApp Image 2026-10-22 at 6.24.03 PM.jpeg", "box": (366, 461, 1554, 765)}, # Hero Stage
        {"logo": True, "box": (761, 58, 1147, 146)} # Logo placeholder
    ],
    2: [
        {"file": "WhatsApp Image 2026-10-22 at 6.24.04 PM.jpeg", "box": (72, 53, 453, 999)}, # Workshop
        {"file": "WhatsApp Image 2026-10-22 at 6.24.05 PM (1).jpeg", "box": (498, 53, 879, 999)} # Craftsmanship
    ],
    3: [
        {"file": "WhatsApp Image 2026-10-22 at 6.24.05 PM (2).jpeg", "box": (70, 248, 550, 936)}, # Vision
        {"file": "WhatsApp Image 2026-10-22 at 6.24.05 PM.jpeg", "box": (609, 248, 1086, 936)} # Mission
    ],
    4: [
        {"file": "WhatsApp Image 2026-10-23 at 9.15.40 AM.jpeg", "box": (89, 436, 642, 840)}, # Serb Luxury Boutique
        {"file": "WhatsApp Image 2026-10-23 at 9.15.39 AM (1).jpeg", "box": (683, 436, 1237, 840)}, # Nadco Retail Scene
        {"file": "WhatsApp Image 2026-10-23 at 9.15.36 AM (1).jpeg", "box": (1278, 436, 1832, 840)} # Diriyah POS Showcase
    ],
    5: [
        {"file": "WhatsApp Image 2026-10-23 at 9.15.48 AM (1).jpeg", "box": (93, 356, 640, 766)}, # Monument Pylon
        {"file": "WhatsApp Image 2026-10-23 at 9.15.39 AM.jpeg", "box": (686, 356, 1233, 766)}, # 3D Letters (Arena)
        {"file": "WhatsApp Image 2026-10-23 at 9.15.41 AM (2).jpeg", "box": (1279, 356, 1826, 766)} # Building Facade (Vapiano curved)
    ],
    6: [
        {"file": "WhatsApp Image 2026-10-22 at 6.24.06 PM (1).jpeg", "box": (797, 58, 1317, 488)}, # Summit Stage
        {"file": "WhatsApp Image 2026-10-22 at 6.24.22 PM.jpeg", "box": (1343, 58, 1863, 488)}, # Curved LED
        {"file": "WhatsApp Image 2026-10-22 at 6.24.00 PM (1).jpeg", "box": (797, 528, 1317, 950)}, # Kinetic Light / CPHI Stage
        {"file": "WhatsApp Image 2026-10-22 at 6.24.23 PM.jpeg", "box": (1343, 528, 1863, 950)} # Precision Build Stage
    ],
    7: [
        {"file": "WhatsApp Image 2026-10-22 at 6.24.00 PM (2).jpeg", "box": (70, 404, 650, 934)}, # CPHI Portal Booth
        {"file": "WhatsApp Image 2026-10-22 at 6.24.03 PM (1).jpeg", "box": (672, 404, 1252, 934)}, # Cityscape Pavilion
        {"file": "WhatsApp Image 2026-10-22 at 6.24.02 PM (1).jpeg", "box": (1274, 404, 1852, 934)} # CPHI Deals Hub Kiosk
    ],
    8: [
        {"file": "WhatsApp Image 2026-10-23 at 9.15.40 AM (1).jpeg", "box": (766, 260, 1095, 775)}, # CNC / Metalwork Crane
        {"file": "WhatsApp Image 2026-10-22 at 6.24.26 PM.jpeg", "box": (1141, 260, 1470, 775)}, # Laser / Truss Structure
        {"file": "WhatsApp Image 2026-10-23 at 9.15.36 AM.jpeg", "box": (1516, 260, 1845, 775)} # Cleanroom Workshop
    ],
    9: [
        {"file": "WhatsApp Image 2026-10-22 at 6.24.06 PM.jpeg", "box": (73, 360, 604, 956)}, # 24 Fintech
        {"file": "WhatsApp Image 2026-10-22 at 6.24.24 PM.jpeg", "box": (627, 360, 1184, 956)}, # Global Health
        {"file": "WhatsApp Image 2026-10-22 at 6.24.01 PM.jpeg", "box": (1207, 360, 1853, 649)}, # CPHI Theatre
        {"file": "WhatsApp Image 2026-10-23 at 9.15.42 AM.jpeg", "box": (1207, 670, 1853, 956)} # Retail Flagship
    ],
    10: [
        {"logo": True, "box": (768, 83, 1148, 405)} # Company Logo
    ]
}

# Mapping for Gamma pages (1280x720)
GAMMA_MAP = {
    1: [
        {"file": "WhatsApp Image 2026-10-22 at 6.24.03 PM.jpeg", "box": (565, 25, 980, 488)}, # Hero Stage
        {"file": "WhatsApp Image 2026-10-23 at 9.15.36 AM (1).jpeg", "box": (565, 510, 980, 965)} # Detail Gold
    ],
    2: [
        {"file": "WhatsApp Image 2026-10-22 at 6.24.04 PM.jpeg", "box": (538, 46, 755, 495)}, # Atelier
        {"file": "WhatsApp Image 2026-10-22 at 6.24.22 PM.jpeg", "box": (758, 46, 975, 495)}, # Curved LED
        {"file": "WhatsApp Image 2026-10-23 at 9.15.39 AM.jpeg", "box": (538, 508, 975, 954)} # Precision Metal
    ],
    3: [
        {"file": "WhatsApp Image 2026-10-22 at 6.24.05 PM (2).jpeg", "box": (360, 34, 640, 488)}, # Vision Skyline
        {"file": "WhatsApp Image 2026-10-22 at 6.24.05 PM.jpeg", "box": (360, 512, 640, 966)} # Mission Stage
    ],
    4: [
        {"file": "WhatsApp Image 2026-10-23 at 9.15.40 AM.jpeg", "box": (23, 372, 593, 684)}, # Window Theater
        {"file": "WhatsApp Image 2026-10-23 at 9.15.36 AM (1).jpeg", "box": (610, 372, 977, 684)}, # Cosmetic POS
        {"file": "WhatsApp Image 2026-10-23 at 9.15.42 AM.jpeg", "box": (23, 690, 404, 995)} # Interactive Pod
    ],
    5: [
        {"file": "WhatsApp Image 2026-10-23 at 9.15.48 AM (1).jpeg", "box": (580, 34, 980, 264)}, # Exterior Pylon
        {"file": "WhatsApp Image 2026-10-23 at 9.15.41 AM (2).jpeg", "box": (580, 285, 775, 519)}, # Facade Channel Letters
        {"file": "WhatsApp Image 2026-10-23 at 9.15.39 AM (1).jpeg", "box": (786, 285, 981, 519)} # Wayfinding
    ],
    6: [
        {"file": "WhatsApp Image 2026-10-22 at 6.24.06 PM.jpeg", "box": (531, 34, 755, 495)}, # 24 Fintech
        {"file": "WhatsApp Image 2026-10-22 at 6.24.00 PM (1).jpeg", "box": (758, 34, 981, 495)}, # Light Tunnel
        {"file": "WhatsApp Image 2026-10-22 at 6.24.06 PM (1).jpeg", "box": (531, 506, 755, 966)}, # Keynote Stage
        {"file": "WhatsApp Image 2026-10-22 at 6.24.23 PM.jpeg", "box": (758, 506, 981, 966)} # Interactive Summit
    ],
    7: [
        {"file": "WhatsApp Image 2026-10-22 at 6.24.03 PM (1).jpeg", "box": (483, 34, 981, 338)}, # Custom Pavilion
        {"file": "WhatsApp Image 2026-10-22 at 6.24.02 PM (1).jpeg", "box": (483, 348, 730, 653)}, # Discovery Kiosk
        {"file": "WhatsApp Image 2026-10-22 at 6.24.00 PM (2).jpeg", "box": (735, 348, 981, 653)} # Pop-up Pod
    ],
    8: [
        {"file": "WhatsApp Image 2026-10-23 at 9.15.40 AM (1).jpeg", "box": (369, 34, 570, 494)}, # Laser & CNC
        {"file": "WhatsApp Image 2026-10-22 at 6.24.26 PM.jpeg", "box": (575, 34, 776, 494)}, # Flatbed UV / Truss
        {"file": "WhatsApp Image 2026-10-23 at 9.15.36 AM.jpeg", "box": (780, 34, 981, 494)} # Cleanroom Assembly
    ],
    9: [
        {"file": "WhatsApp Image 2026-10-22 at 6.24.24 PM.jpeg", "box": (336, 34, 657, 495)}, # Global Health
        {"file": "WhatsApp Image 2026-10-22 at 6.24.01 PM.jpeg", "box": (661, 34, 981, 495)}, # CPHI Theatre
        {"file": "WhatsApp Image 2026-10-23 at 9.15.42 AM.jpeg", "box": (336, 506, 657, 966)}, # Luxury Storefront
        {"file": "WhatsApp Image 2026-10-22 at 6.24.35 PM.jpeg", "box": (661, 506, 981, 966)} # Fire Protection Summit
    ],
    10: [
        {"file": "WhatsApp Image 2026-10-22 at 6.24.00 PM.jpeg", "box": (433, 34, 981, 330)}, # Atelier Showroom
        {"file": "WhatsApp Image 2026-10-22 at 6.24.05 PM (1).jpeg", "box": (433, 350, 981, 647)}, # Design Studio
        {"logo": True, "box": (25, 925, 240, 955)} # Company Logo
    ]
}

print("Configuration dictionaries established!")
