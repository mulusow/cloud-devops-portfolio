from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/api/hello")
def hello():
    return jsonify(message="Hello from cloud-devops-portfolio")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
