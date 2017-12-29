from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def form_display():
    template = jinja_env.get_template('signup_form.html') 
    return template.render()

@app.route("/validate", methods=['POST'])
def validate():
    user_name = request.form['user-name']
    user_password = request.form['user-password']
    verfy_password = request.form['verify-password']
    user_email = request.form['user-email']

    template = jinja_env.get_template('validate_signup.html')
    return template.render(name=user_name,email=user_email)
    
@app.route("/signup", methods=['POST'])
def signup():
    user_name = request.form['user-name']
    template = jinja_env.get_template('successful_signup.html')
    return template.render(name=user_name)


app.run()