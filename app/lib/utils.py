from io import BytesIO
from flask import send_file

def serve_pil_image(pil_img, size=1000):
    img_io = BytesIO()
    final_img = pil_img
    width = pil_img.width;
    if(width != size):
        final_img = pil_img.resize((size, size))
    final_img.save(img_io, 'PNG', quality=100)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')