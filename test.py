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

@app.route("/aboutus.html")
@app.route("/aboutus")
def about_us():
    return render_template('aboutus.html')


@app.route("/contactus.html")
@app.route("/contactus.html")
def contact_us():
    return render_template('contactus.html')





@app.route("/csscourse.html")
@app.route("/csscourse.html")
def csscourse():
    return render_template('csscourse.html')

    

@app.route("/htmlcoures.html")
@app.route("/htmlcoures.html")
def htmlcoures():
    return render_template('htmlcoures.html')


# @app.route("/javacourse.html")
@app.route("/javacourse.html")
def javacourse():
    return render_template('javacourse.html')




@app.route("/javascriptcourse.html")
@app.route("/javascriptcourse.html")
def javascriptcourse():
    return render_template('javascriptcourse.html')



@app.route("/loginpage.html")
@app.route("/loginpage.html")
def loginpage():
    return render_template('loginpage.html')

    


@app.route("/phpcourse.html")
@app.route("/phpcourse.html")
def phpcourse():
    return render_template('phpcourse.html')




@app.route("/rigesster.html")
@app.route("/rigesster.html")
def rigesster():
    return render_template('rigesster.html')




@app.route("/test.html")
@app.route("/test.html")
def test():
    return render_template('test.html')


@app.route("/users.html")
@app.route("/users.html")
def users():
    return render_template('users.html')



if __name__ == '__main__':
    # Debug Mode
    app.run(debug=True)
    # production mode 
    #p= os.environ.get('PORT')
    #p='5000' if p == None else p
    #serve(app,host='0.0.0.0', port=p)