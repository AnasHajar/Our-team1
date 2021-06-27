from flask import Flask, render_template,request,session, url_for,redirect
from flask_mail import Mail, Message
from waitress import serve
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



@app.errorhandler(404)
def err_404(error):
   return render_template( '404.html' ), 404



# email configeration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'anashajr67@gmail.com'
app.config['MAIL_PASSWORD'] = 'zzdxafrrjeycocrx'
 
mail = Mail(app)

# for handle email (contact_us)
@app.route('/handle_email',methods=['GET','POST'])
def handle_email():
    nam = request.form['name']
    email = request.form['email']
    subject= request.form['subject']
    msg=Message(f"Message {email}",recipients=['anashajr67@gmail.com'],sender=email)
    msg.body= f''' {nam} said {subject} '''
    mail.send(msg)
    return render_template('index.html')


if __name__ == '__main__':
    # Debug Mode
    #app.run(debug=True)
    # production mode 
    p= os.environ.get('PORT')
    p='5000' if p == None else p
    serve(app,host='0.0.0.0', port=p)


    
