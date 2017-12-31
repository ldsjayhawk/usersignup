@app.route("/signup", methods=['POST'])
def signup():
    user_name = request.form['user-name']
    template = jinja_env.get_template('successful_signup.html')
    return template.render(name=user_name)


 if user_email != " " and if "@" in user_email or "." in user_email
        verify_password_error = ''
        template = jinja_env.get_template('signup_form.html')
        return template.render()
    else:
        template = jinja_env.get_template('successful_signup.html')
        return template.render()


    @app.route('/')
def form_display():
    template = jinja_env.get_template('signup_form.html') 
    return template.render()

@app.route("/signup", methods=['POST'])
def signup():
    user_name = request.form['user-name']
    template = jinja_env.get_template('successful_signup.html')
    return template.render(name=user_name)