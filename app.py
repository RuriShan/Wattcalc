from flask import Flask, render_template, request, url_for, redirect
from calc import watt
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    a = watt()
    return render_template('main.html', a=a)