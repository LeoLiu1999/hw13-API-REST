from flask import Flask, render_template
import json
import urllib2

u_resp = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=am0ATrYMJQfY8wXWMl4Jfv2OBJGZtFyaeQN5Qy8l")
json_string = u_resp.read()
json_dict = json.loads(json_string)
print json_dict

u_resp2 = urllib2.urlopen("http://api.nytimes.com/svc/topstories/v2/technology.json?api-key=33106c01bb1a4ca9a76239620531eb30")
json_string2 = u_resp2.read()
json_dict2 = json.loads(json_string2)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("temp.html", dict=json_dict, dict2=json_dict2)

if (__name__ == "__main__"):
    app.debug = True
    app.run()


