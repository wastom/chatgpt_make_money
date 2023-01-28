from flask import Flask, render_template, request, Response
# from flask import Flask, request, Response
from PIL import Image
import io

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/jpgtopng", methods=["GET"])
def jpgtopng():
    return render_template("jpgtopng.html")

@app.route("/pngtojpg", methods=["GET"])
def pngtojpg():
    return render_template("pngtojpg.html")

@app.route("/webptopng", methods=["GET"])
def webptopng():
    return render_template("webptopng.html")

@app.route("/bmptopng", methods=["GET"])
def bmptopng():
    return render_template("bmptopng.html")

@app.route("/pngtopdf", methods=["GET"])
def pngtopdf():
    return render_template("pngtopdf.html")


@app.route('/api/jpgtopng', methods=['POST'])
def jpg_to_png():
    image = request.files['image']
    image_data = Image.open(io.BytesIO(image.read()))
    if image_data.format != 'JPEG':
        return {'error': 'Invalid image format. Only JPEG is allowed.'}

    image_data = image_data.convert('RGB')
    image_data = image_data.save('converted.png')
    with open('converted.png', 'rb') as f:
        image_data = f.read()
    response = Response(image_data, content_type='image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='converted.png')
    return response


@app.route("/api/pngtojpg", methods=["POST"])
def png_to_jpg():
    image = request.files['image']
    image_data = Image.open(io.BytesIO(image.read()))
    if image_data.format != 'PNG':
        return {'error': 'Invalid image format. Only PNG is allowed.'}

    image_data = image_data.convert('RGB')
    image_data = image_data.save('converted.jpg')
    with open('converted.jpg', 'rb') as f:
        image_data = f.read()
    response = Response(image_data, content_type='image/jpg')
    response.headers.set('Content-Disposition', 'attachment', filename='converted.jpg')
    return response

@app.route("/api/webptopng", methods=["POST"])
def webp_to_png():
    image = request.files["image"]
    image = Image.open(image)
    pdf_buffer = io.BytesIO()
    image.save(pdf_buffer, 'PNG', resolution=100.0)
    pdf_buffer.seek(0)
    response = Response(pdf_buffer, content_type="application/png")
    response.headers["Content-Disposition"] = "attachment; filename=converted_file.png"
    # response = Response(jpg_image, content_type='image/jpeg', headers={'Content-Disposition': 'attachment; filename="converted.jpg"'})
    return response

@app.route("/api/bmptopng", methods=["POST"])
def bmp_to_png():
    image = request.files["image"]
    image = Image.open(image)
    pdf_buffer = io.BytesIO()
    image.save(pdf_buffer, 'PNG', resolution=100.0)
    pdf_buffer.seek(0)
    response = Response(pdf_buffer, content_type="application/png")
    response.headers["Content-Disposition"] = "attachment; filename=converted_file.png"
    # response = Response(jpg_image, content_type='image/jpeg', headers={'Content-Disposition': 'attachment; filename="converted.jpg"'})
    return response

@app.route("/api/pngtopdf", methods=["POST"])
def png_to_pdf():
    image = request.files["image"]
    image = Image.open(image)
    pdf_buffer = io.BytesIO()
    image.save(pdf_buffer, 'PDF', resolution=100.0)
    pdf_buffer.seek(0)
    response = Response(pdf_buffer, content_type="application/pdf")
    response.headers["Content-Disposition"] = "attachment; filename=converted_file.pdf"
    # response = Response(jpg_image, content_type='image/jpeg', headers={'Content-Disposition': 'attachment; filename="converted.jpg"'})
    return response

if __name__ == "__main__":
    app.run(debug=True)
