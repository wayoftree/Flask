from flask import Flask

## Create a simple flask application
app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "Hello, Azure Web Apps!"

if __name__=="__main__":
    app.run(debug=True)