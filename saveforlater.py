@app.route("/signup", methods=['POST'])
def signup():
    user_name = request.form['user-name']
    template = jinja_env.get_template('successful_signup.html')
    return template.render(name=user_name)