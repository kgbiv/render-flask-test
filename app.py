from flask import Flask, jsonify

app = Flask(__name__)

# Hardcoded root domains and subdomains
root_domains = ["example.com", "openai.com"]
subdomains = {
    "example.com": ["www.example.com", "blog.example.com"],
    "openai.com": ["chat.openai.com", "api.openai.com"]
}

@app.route("/")
def home():
    return "Flask API on Render is running!"

@app.route("/domains")
def get_domains():
    return jsonify(root_domains)

@app.route("/subdomains/<domain>")
def get_subdomains(domain):
    return jsonify(subdomains.get(domain, []))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
