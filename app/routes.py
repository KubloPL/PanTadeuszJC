from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template("index.html")

def create_route(i):
    def route():
        return render_template(f'k{i}.html')
    route.__name__ = f'k{i}_route'
    app.route(f'/k{i}.html')(route)


for i in range(1, 13):
    create_route(i)
