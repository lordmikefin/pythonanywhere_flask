from flask import Flask
#app = Flask(__name__)
app = Flask("TEST")

@app.route('/')
def home():
    # etc etc, flask app code
	return 'Test string :)'

if __name__ == '__main__':
    app.run()
