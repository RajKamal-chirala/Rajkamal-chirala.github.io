from flask import Flask, render_template
import base64, os

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('home.jinja2')

@app.route("/resume/", methods=['GET'])
def resume():
    return render_template('resume.jinja2', title='Resume')

@app.route("/projects/")
def projects():
    return render_template('projects.jinja2')


if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)


