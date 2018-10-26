from flask import Flask
#the argumnet is important This is needed so that Flask knows where to look for templates, static files, and so on
app = Flask(__name__)

#use the route() decorator to tell Flask what URL should trigger our function.
@app.route("/<name>")
def hello(name):
    return f"Hello {name}"

#to make the server Externally Visible run flask run --host=0.0.0.0, This tells your operating system to listen on all public IPs

#converter to specify the type of the argument like <converter:variable_name>.
#string, int, float, path, uuid
@app.route("/age/<int:years>") 
def dob(years):
    return f"You are {years + 100} old :)"

#URL Building to a specific function using url_for()
#Inside templates you also have access to the request, session and g [1] objects as well as the get_flashed_messages() function

