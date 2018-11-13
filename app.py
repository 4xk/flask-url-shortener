from flask import Flask, redirect, request
import json
app = Flask(__name__)

@app.route("/")
def index():
	return "Index page!"
@app.route("/<path:path>")
def redir(path):
	with open("sites.json") as f:
		data = json.loads(f.read())
		site = data[path]
		if not site.startswith('https') or not site.startswith('http'):
			site = 'http://' + site
		return redirect(site)
@app.route("/api/v1/create/<string:code>")
def create(code):
	url = request.headers['url']
	with open("sites.json", "r+") as f:
		data = f.read()
		f.seek(0)
		json_data = json.loads(data)
		keys = json_data.keys()
		if code in keys:
			f.write(json.dumps(json_data))
			return "Url already exists!"
		else:
			json_data[code] = url
			f.write(json.dumps(json_data))
			return f"Created code {code} with url {url}!"
		f.write(json.dumps(json_data))
	return code

app.run()
