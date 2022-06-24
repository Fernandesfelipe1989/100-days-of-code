import smtplib

from decouple import config
from email.mime.text import MIMEText
from flask import Flask, render_template, request


from post import Post

app = Flask(__name__)
post = Post()


def make_message(name, email, phone, subject, content):
    message = MIMEText(f"Name: {name.title()}\nEmail:{email}\nPhone: {phone}\nMessage: {content}")
    message["Subject"] = subject
    message["From"] = email
    message["To"] = receiver
    return message


def send_email(email, message):
    with smtplib.SMTP(host=host, port=port) as server:
        server.login(user=user, password=password)
        server.sendmail(
            from_addr=email,
            to_addrs=receiver,
            msg=message.as_string(),
        )


@app.route('/about')
def about():
    context = dict(city='Sorocaba')
    return render_template("about.html", **context)


@app.route('/contact',  methods=['GET', "POST"])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        text = request.form['message']
        message = make_message(name=name, email=email, phone=phone, subject="Contact", content=text)
        send_email(email=email, message=message)
    context = dict(city='Sorocaba')
    return render_template("contact.html", **context)


@app.route("/post/<int:id>")
def get_post(id):
    context = dict(city='Sorocaba', post=post.get_post(id=id))
    return render_template('post.html', **context)


@app.route('/')
def home():
    post_data = post.get_posts()
    context = dict(city='Sorocaba', all_post=post_data)
    return render_template("index.html", **context)


if __name__ == "__main__":
    host = config("EMAIL_HOST", default='smtp.mailtrap.io')
    port = config("EMAIL_PORT", default=2525)
    user = config("EMAIL_HOST_USER", default="")
    password = config("EMAIL_HOST_PASSWORD", default="")
    receiver = config("EMAIl_RECEIVER", default="test@gmail.com")

    app.run(debug=True)
