from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/private")
def private():
#test for user being looged in
#so redirect to login url
  return redirect (url_for('login'))

@app.route('/login')
def login():
  return "Now we would get username & password"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
