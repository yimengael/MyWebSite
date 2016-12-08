from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# our index route will handle rendering our form
# Define a route for the default URL, which loads the form
@app.route('/')
def showIndex():
    return render_template("index.html")
    # return "Welcome!"

@app.route('/login')
def showLogin():
    return render_template("signInAndUp.html")


@app.route('/contact')
def showContact():
    return render_template("contactUs.html")


@app.route('/aboutme')
def showAboutMe():
    return render_template("aboutMe.html")


@app.route('/registerCustomer')
def showRegisterCustomer():
    return render_template("registerCustomer.html")


@app.route('/registerProject')
def showRegisterProject():
    return render_template("registerProject.html")


@app.route('/dashboardCustomer')
def showDashboardCustomer():
    return render_template("dashboardCustomer.html")


@app.route('/dashboardCustProject')
def showDashboardProject():
    return render_template("dashboardProject.html")


@app.route('/resume')
def showResume():
    return render_template("resume.html")



# Run the application
if __name__ == '__main__':
  app.run(
        host="0.0.0.0",
        port=int("5000"),
        debug=True
  )
