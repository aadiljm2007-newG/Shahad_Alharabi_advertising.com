from PIL import Image, ImageDraw
import numpy as np

# Coordinates for all Canva pages (1920x1080)
# Page 1:
# Hero: (366, 461, 1554, 765)
# Logo top: (761, 58, 1147, 146)

# Page 2:
# Box 1 (Workshop): (72, 53, 453, 999)
# Box 2 (Craftsmanship): (498, 53, 879, 999)

# Page 3:
# Box 1 (Vision): (70, 248, 550, 936)
# Box 2 (Mission): (609, 248, 1086, 936)

# Page 4:
# Box 1 (Boutique): (89, 436, 642, 840)
# Box 2 (Retail Scene): (683, 436, 1237, 840)
# Box 3 (POS Showcase): (1278, 436, 1832, 840)

# Page 5:
# Box 1 (Monument Pylons): (93, 356, 640, 766)
# Box 2 (3D Letters): (686, 356, 1233, 766)
# Box 3 (Facades): (1279, 356, 1826, 766)

# Page 6:
# Box 1 (Summit Stages): (797, 58, 1317, 488)
# Box 2 (Curved LED): (1343, 58, 1863, 488)
# Box 3 (Kinetic Light): (797, 528, 1317, 950)
# Box 4 (Precision Build): (1343, 528, 1863, 950)

# Page 7:
# Box 1 (Booth): (70, 404, 650, 934)
# Box 2 (Pavilion): (672, 404, 1252, 934)
# Box 3 (Kiosk): (1274, 404, 1852, 934)

# Page 8:
# Box 1 (CNC Cutting): (766, 260, 1095, 775)
# Box 2 (Laser Routing): (1141, 260, 1470, 775)
# Box 3 (UV Printing): (1516, 260, 1845, 775)

# Page 9:
# Box 1 (Fintech): (73, 360, 604, 956)
# Box 2 (Global Health): (627, 360, 1184, 956)
# Box 3 (Innovation): (1207, 360, 1853, 649)
# Box 4 (Retail Flagship): (1207, 670, 1853, 956)

# Page 10:
# Logo placeholder: (768, 83, 1148, 405)

print("Canva coordinates defined!")
