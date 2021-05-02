from flask import Flask, render_template
app = Flask(__name__)


IMAGE_FOLDER = "./static/images"
app.config["IMAGE_FOLDER"] = IMAGE_FOLDER

app.config.from_object(__name__)

@app.route('/')
def hello():
    name = "Umamusu search!!!!"
    return render_template("app.html", title="UMAMUSU", name=name)

@app.route('/good')
def good():
    name = "Good"
    return name

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
