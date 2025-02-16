from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

contact = '/contact.html'
endpoints = ('index.html', 'works.html', 'about.html', 'about.html', 'contact.html')


@app.route('/<string:page_name>')
def my_home(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('./database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('./database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            'did not saved to database'
    else:
        return 'something went wrong. Try again'
