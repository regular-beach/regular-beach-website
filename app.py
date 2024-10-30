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
def projects_list():
    projects = ['photofeature1', 'letter prints']  # List of your project names
    return render_template('projects.html', projects=projects)



@app.route('/projects/<project>')
def project(project):
    try:
        return render_template(f'{project}.html')
    except Exception as e:
        print(f"Error rendering template: {e}")  # Log the error
        return "Internal Server Error", 500  # Return a 500 error response


#@app.route('/project/photofeature1')
#def photofeature1():
    #return render_template('photofeature1.html')

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
  
#if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=8000)


    