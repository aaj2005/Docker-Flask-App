from flask import Flask

app = Flask(__name__)

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> f897735 (something)
CORS(app)

import base64
from PIL import Image
from io import BytesIO

def webp_to_jpg(webp_base64_string, output_file_path='output.jpg'):
    # Remove the "data:image/webp;base64," prefix
    webp_base64_string = webp_base64_string.replace("data:image/webp;base64,", "")

    # Decode base64 string to binary data
    binary_data = base64.b64decode(webp_base64_string)

    # Open WebP image using Pillow
    with Image.open(BytesIO(binary_data)) as webp_image:
        # Save as JPG
        webp_image.convert('RGB').save(output_file_path, format='JPEG')

# Example usage


@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "GET":
        return "goodbye world"
	# print(test)
	# print(request.headers)
    data = request.json["imageData"]
    webp_to_jpg(data)
	# print(jpg_original)
	# img = cv2.imdecode(jpg_as_np, flags=1)
	# print(img)
	# cv2.imwrite('./images.webp', img)

    return {"1":"hello world"}


@app.route("/api/frame", methods=["POST","GET"])
def imageProcess():
    if request.method == "GET":
        return "hello world"
	# print(test)
	# print(request.headers)
    data = request.json["imageData"]
    webp_to_jpg(data)
	# print(jpg_original)
	# img = cv2.imdecode(jpg_as_np, flags=1)
	# print(img)
	# cv2.imwrite('./images.webp', img)

    return {"1":"hello world"}

if __name__ == "__main__":
    app.run(port=2223)
<<<<<<< HEAD
=======
=======
@app.route("/")
def hello():
	return "Hello world!"
>>>>>>> parent of c40facc (updated .py file)
>>>>>>> f897735 (something)
=======
@app.route("/")
def hello():
	return "Hello world!"
>>>>>>> a604540 (Revert "something")
