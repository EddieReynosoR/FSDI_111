from flask import Flask, render_template # from flask module import Flask class

app = Flask(__name__) # Instantiate the Flask class into the app variable [object]

# @app.get("/") # decorator that allows us to map routes to "view functions"
# def index(): # Flask calls these "view functions"
#     return "<h1>Hello World</h1>" # return statement

@app.get("/")
def index():
    return render_template('index.html')


@app.get("/about")
def About():
    return render_template('about.html')

@app.get("/objects")
def objects():
    return render_template('objects.html')