from flask import Flask, redirect
#app = Flask(__name__)
app = Flask("TEST")

@app.route('/')
def home():
    # etc etc, flask app code
	return 'Test string :)'
	
@app.route('/redirect_test')
def redirect_test():
	return redirect('https://fi.linkedin.com/in/lordmikefin')

@app.route('/linkedn')
def linkedn():
	return '<script type="text/javascript" src="https://platform.linkedin.com/badges/js/profile.js" async defer></script><div class="LI-profile-badge"  data-version="v1" data-size="large" data-locale="en_US" data-type="horizontal" data-theme="light" data-vanity="lordmikefin"><a class="LI-simple-link" href="https://fi.linkedin.com/in/lordmikefin?trk=profile-badge">Mikko Niemelä</a></div>'

if __name__ == '__main__':
    app.run()
