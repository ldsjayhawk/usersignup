from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/validate", methods=['POST'])
def display_validate_form():
    template = jinja_env.get_template('signup_form.html')
    return template.render(name='',email='')

def validate():
    user_name = request.form['user-name']
    user_password = request.form['user-password']
    verfy_password = request.form['verify-password']
    user_email = request.form['user-email']

    user_name_error = ""
    user_password_error = ""
    verify_password_error = ""
    user_email_error = ""

    if len(user_name) < 3 or len(user_name) > 20 or " " in user_name:
        user_name_error = 'Please enter a valid user name between 3 and 20 characters long.'

    if len(user_password) < 3 or len(user_password) > 20 or " " in user_password:
        user_password_error = 'Please enter a valid password between 3 and 20 characters long.'

    if verify_password != user_password:
        verify_password_error = 'Passwords do not match.'

    if user_name_error = "": and        
    if user_password_error = "": and
    if verify_password_error = "": and        
    if user_email_error = "":
        template = jinja_env.get_template('successful_signup.html')
        return template.render()
    else:
        template = jinja_env.get_template('signup_form.html')
        return template.render(name=user_name,email=user_email)
   
app.run()