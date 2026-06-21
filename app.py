from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route("/")
def home():
    data = {
        "status": "Running",
        "environment": "Production",
        "container": "Docker",
        "orchestration": "Kubernetes",
        "cicd": "Jenkins",
        "version": "v1.0",
        "hostname": socket.gethostname()
    }
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
