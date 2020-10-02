from flask import Flask
from flask_mail import Mail,Message
from flask import request,render_template,redirect
app = Flask(__name__)


#### FLASK MAIL CONFIGURATION ######
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USERNAME'] = 'darsh.modi1111@gmail.com'
app.config['MAIL_PASSWORD'] = 'vnswpyprvlyuwesz'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
##########################################

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sendmail',methods=['POST'])
def sendmail():
    try:
        sub = request.form.get('subject')
        email_to = request.form.get('email')
        Body_data = request.form.get('body')
        
        msg = Message(
            sub,
            sender= 'darsh.modi1111@gmail.com',
            recipients=[email_to],
            body=Body_data,
        )
        
        mail.send(msg)
        return "Mail sent .."
    except Exception as e : 
        print("Error is :", str(e))
if __name__ == "__main__":
    app.run(debug=True)