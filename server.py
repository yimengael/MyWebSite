from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# our index route will handle rendering our form
# Define a route for the default URL, which loads the form
@app.route('/')
def main():
    return render_template("index.html")
    # return "Welcome!"





# Run the application
if __name__ == '__main__':
  app.run(
        host="0.0.0.0",
        port=int("8000"),
        debug=True
  )
