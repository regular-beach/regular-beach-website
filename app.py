from flask import Flask, render_template, request
from waitress import serve
from flask import Flask, url_for
import os

app = Flask(__name__)
app.debug = False

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=projects)



@app.route('/project/<project_name>')
def project(project_name):
    # Find the project by name in your `projects` list
    project = next((p for p in projects if p["name"] == project_name), None)
    if project is None:
        return "Project not found", 404
    
    # Render the specific template for this project within the `projects` subdirectory
    try:
        return render_template(f'projects/{project_name}.html', project=project)
    except Exception as e:
        # Handle missing or misnamed templates
        return f"Error loading project template: {e}", 404



@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route('/about')
def about():
    return render_template('about.html')


projects = [
    {
        "name": "letterprints",
        "date": "'23 - present",
        "medium": "lino-cut",
        "artist": "reg-beach",
        "description": "Regular Beach experimental type project no.1."
    },
    {
        "name": "photofeature1",
        "date": "november '24",
        "medium": "35mm",
        "artist": "reg-beach",
        "description": "12 imgs from 2 rolls of 35mm."
    },
    {
        "name": "photofeature2",
        "date": "november '24",
        "medium": "iphone",
        "artist": "july guzman",
        "description": "informing artistic practice."
    }
    
    # Add more projects as needed
]


#if __name__ == '__main__':
 #app.run(host='0.0.0.0') 
  
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)


    