from flask import Flask, render_template
import json
import urllib2

app = Flask(__name__)

@app.route("/")
def home():
    u_resp = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=am0ATrYMJQfY8wXWMl4Jfv2OBJGZtFyaeQN5Qy8l")
    json_string = u_resp.read()
    json_dict = json.loads(json_string)
    return render_template(dict=json_dict)

if (__name__ == "__main__"):
    app.debug = True
    app.run()


