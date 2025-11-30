from flask import Flask, render_template, request
from waitress import serve
from flask import Flask, url_for
import os

app = Flask(__name__)
app.debug = False

@app.route('/')
@app.route('/new')
def new():
    return render_template('new.html')


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

@app.route('/shop1')
def shop1():
    return render_template('shop1.html')

@app.route('/shop2')
def shop2():
    return render_template('shop2.html')


projects = [
    {
        "name": "RTees",
        "date": "July '25",
        "medium": "shirt",
    },
     
      {
        "name": "ProtologoTees",
        "date": "May '25",
        "medium": "shirt",
    },
  
    {
        "name": "Inventory",
        "date": "May '25",
        "medium": "zine",
        "artist": "Hendrix Park",
       "description": "archiving Inventory by Hendrix Park. Made for Chain Mail at Pretty Gritty sf."
    },

    {
        "name": "tshirtsforthevisualarts",
        "date": "May '25",
        "medium": "zine",
       "description": "archiving t shirts for the visual arts #1."
    },

        {
        "name": "photofeature2",
        "date": "March '25",
        "medium": "digital photography",
        "artist": "Seth Eddy",
       "description": " Artist's selection of over a dozen b/w images - thank you seth."
    },
   
    {
        "name": "letterprints",
        "date": "'23 - present",
        "medium": "lino-cut",
        "description": "Regular Beach experimental type project no.1."
    },


    
    # Add more projects as needed
]


#if __name__ == '__main__':
# app.run(host='0.0.0.0') 
  
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)


    