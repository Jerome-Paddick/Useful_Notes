FLASK
===

### CVAPI 

`source VirtualEnvs/cvapi/bin/activate`


### GENERAL

Flask Templates
"Ginger" Framework

All Flask apps create an "Application Instance" -> an object to which all requests are sent for handling using WSGI (Web Server Gateway Interface) protocol

WSGI -> server/gateway side, and application/framework side, WSGI middle-ware
	WSGI middleware python callable that is converted into a generator

Generator -> Function that behaves like an iterator (can be iterated upon)

Only requirement for Flask class creator is name of module or package, for most instances it is pythons __name__ variable, used to determine root path of the application
 -> flask = app(__name__)

---

### ROUTES AND VIEWS 

client request -> web server -> Flask application Instance -> handled and passed to handler function
FAI Response -> client

FAI keeps a mapping of URLs to python functions, mostly through `@app.route("/")` decorator
decorator adjust the behaviour of a function
decorator can register functions as handlers for an event

    @app.route("/")
    def index():
        return "<h1> HEllo <h1>"

the `@app.route` decorator registers the index() function as the handler for the root url, the return of the function is the response

index() -> VIEW Function

variables can be used in the route decorator -> 

    @app.route("/<name>")
    def index(name):
        return "<h1> Hello %s <h1>" %name

Types
eg. `@app.route("/<int:id>")`  will only match URLs with int
int, float, path (string with slashes)

---

### SERVER-STARTUP

FAI instance has a run method to launch server

    if __name__ == "__main__":
        app.run(debug=True)

the `__name__ == "__main__"` syntax ensures code only runs when code is called directly (instead of eg. file import)

server loops and acts as a listener for requests
debug -> activated debugger and reloader

---
### REQUEST-RESPONSE CYCLE 

FIA recieves request -> makes objects available for handlers
request object -> encapsulates request object HTTP request from client

Instead of passing these objects to every possible handler as arguments
Flask CONTEXTS can make an object GLOBALLY available to a THREAD without making it available to other threads

    from flask import request
    @app.route("/")
    def index():
        user_agent = request.headers.get("User-Agent")  # 
        return "<p>Your Browser is %s<p>" % user_agent

`request` is used as if it was a global variable, which is impossible as a multithreaded server is running multiple requests simultaneously.

A thread is the smallest sequence of instructions that can be managed independantly 
--> multithreaded servers start a pool of threads and select a thread from the pool for each incoming request

CONTEXTS -> 2 contexts 
1. Apllication Context:  
	`current_app` -> 	Application Instance  
	`g` -> 		object that the application uses for temporary storage  
	
2. Request Context: 
	`request` ->	HTTP request object sent by client  
	`session` -> 	user session dictionary
			can be used to store values that are "remembered" between requests

Flask activates (or pushes) the application and request contexts before dispatching a request and then removes them when the request is handled

When application context is pushed:
-> `current_app` & `g` made available to thread

when request context is pushed:
-> `request` & `session` made available to thread

---
### PUSHING A CONTEXT:

    from hello import app
    from flask import current_app

calling current_app.name  at this point will fail as it outside app instance

    app_ctx = app.app_context()
    app_ctx.push()
    current_app.name
    >> "Hello"

---
### REQUEST DISPATCHING

App recieves a request uses URL to find the VIEW function to service it  
--> URL map built using `app.route` decorators (or `app.add_url_rule()`)

INSPECT URL MAP ->  

    from hello import app
    app.url_map

---

### REQUEST HOOKS

Code can be executed before of after each request is processed  
-> Database Connection  
-> Authentication

REQUEST HOOKS are implemented as decorators
1. `before_first_request`		before first request handled
2. `before_request`		before each request handled
3. `after_request`		after each request if no exception occured
4. `teardown_request`		after each request even if exception occured

Common to share data between request hook function and view function is to use `g` 
application context variable  
->  `before_request` loads loggin-in user data and stores it in `g.user`  
->  view function loads user data from `g.user`

---
### RESPONSES

Flask expects view return value to be response to request, but will accept multiple responses

1. return text -> str
2. status code -> int
3. headers     -> dictionary 

only return text required, default status code is 200

    @app.route("/")
    def index():
        return "<h1>BAD<h1>", 400

Instead of returning tuple of response, can return OBJECT
-> `make_response()`
ingests 1,2 or 3 arguments like above and returns a response object which can be further configured

    from flask import make_response
    @app.route("/")
    def index():
        response = make_response("<h1>this doc has a cookie<h1>")
        response.set_cookie("answer", "42")
        return response

Other responses
1. REDIRECT
2. ABORT

REDIRECT includes a browser url, typically indicated with a 302 status code

    from flask import redirect
    @app.route("/")
    def index():
        return redirect("http://www.example.com")

ABORT used for error handling, typically 404

    from flask import abort
    @app.route("/user/<id>")
    def get_user(id):
        user = load_user(id)
        if not user:
            abort(404)
        return "<h1>Hello %s<h1>" % user.name

---
### FLASK EXTENSIONS

extensions are imported using flask.ext namespace
from flask.ext.script import [extension]

these are usually initialised by passing an application instance as an argument to the class

`manager = Manager(app)
if __name_ == "__main__":
	manager.run()`

---
### COMMAND LINE OPTIONS

    RUN
    python app.py
    python app.py runserver
    flask run
    
    HELP
    flask run --help

    default listener for connections on localhost
    adding --host can be used to listen for connections on public network interface
    python runserver --host 0.0.0.0
    
    web server now accessable in network http://a.b.c.d:5000
    where a.b.c.d is external IP address of computer running server

