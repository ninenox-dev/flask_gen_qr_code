from flask import Flask, render_template, request
import qrcode
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.form.get("data")
    img = qrcode.make(data)
    img.save("static/qrcode.png")
    return render_template("generate.html")

if __name__ == "__main__":
    # app.run(debug=True)
    serve(app, host='0.0.0.0', port=5556)
