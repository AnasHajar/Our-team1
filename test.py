from flask import Flask, render_template,request,session, url_for,redirect
import secrets 
import os
secrets.token_hex(16)


app = Flask(__name__)
app.secret_key = 'fbd1_efad885bf@35e1d5ea08424xenel221'

@app.route("/")
@app.route("/index.html")
@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/about_us.html")
@app.route("/about_us")
def about_us():

    return render_template('about_us.html')

if __name__ == '__main__':
    # Debug Mode
    app.run(debug=True)
    # production mode 
    #p= os.environ.get('PORT')
    #p='5000' if p == None else p
    #serve(app,host='0.0.0.0', port=p)