# from flask import Flask ## import the Flask class 
# from os import environ ## import environ dictionary from os to get environment variables from Cloud9

# app = Flask(__name__) ## create instance of Flask class, pip install --upgrade pip

# @app.route('/')
# @app.route('/hello')

# ## create a fn that returns hello world
# def say_hi():
#   return 'Hello World!'

# ## when your app runs, tell it to listen for host IP & port
# if __name__ == "__main__":
#   app.run(host=environ['IP'],
#       port=int(environ['PORT'])
#   )

from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
  return "Hello World!"
 
if __name__ == "__main__":
  app.run()