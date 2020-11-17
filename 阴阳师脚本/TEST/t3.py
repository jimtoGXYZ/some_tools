from PIL import ImageGrab

tmp_image = ImageGrab.grab(bbox=(100, 200, 200, 300))
tmp_image.save("../TEST/test.png", "PNG")
