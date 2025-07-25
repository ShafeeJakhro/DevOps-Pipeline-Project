from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is Shafee — Flask deployed with Jenkins to Kubernetes (EKS)!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
