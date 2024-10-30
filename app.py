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
    return render_template('projects.html')


@app.route('/project/<project>')
def project(project):
    return render_template(f'{project}.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.context_processor
def inject_projects():
    path = "templates/projects"
    projects = []
    for root, d_names, f_names in os.walk(path):
        for f in f_names:
            # Filter for HTML files only
            if f.endswith('.html'):
                project_name = f.split('.')[0]  # Remove the file extension
                projects.append(project_name)
    return dict(projects=projects)


#if __name__ == '__main__':
 #app.run(host='0.0.0.0') 
  
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)


    