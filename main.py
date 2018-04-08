'''
    Matt Briggs, Web Python
    April 8, 2018
'''
import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('donations'))

@app.route('/donations/')
def donations():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/donations/<name>')
def donor(name):
    try:
        donated = { "name": name, "sum" : 0}
        record = Donor.select().where(Donor.name == name).get()
        na = int(record.id)
        query = Donation.select().where(Donation.donor == na)
        s = []
        for q in query:
            s.append(q.value)
        donated["sum"] = str(sum(s))
        return render_template('donor.jinja2', donated=donated)
    except:
        return render_template('error.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='localhost', port=port)
