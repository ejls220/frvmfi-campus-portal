from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("map.html")   # MAIN PAGE

# allow access to any file inside the project
@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("", path)

if __name__ == "__main__":
    app.run()