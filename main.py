from flask import Flask
app = Flask(__name__)

def sum(a, b):
    return a + b

@app.route("/")
def hello():
    sum = sum(5, 2)
    return "Hello World!: %s" % sum

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)
