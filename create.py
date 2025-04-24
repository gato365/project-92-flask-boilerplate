from PIL import Image

# Create a 16x16 black square
favicon = Image.new("RGB", (16, 16), (0, 0, 0))
favicon.save("favicon.ico", format="ICO")