from crypt import methods
from urllib import response
from flask import Flask, request, send_file
from flask_cors import CORS
import qrcode
from io import BytesIO


app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generator():
    buffer = BytesIO()
    data = request.form.get('data')

    img = qrcode.make(data)
    img.save(buffer) 
    buffer.seek(0)

    response = send_file(buffer, mimetype='image/png')
    return response

if __name__ == '__main__':
    app.run()


