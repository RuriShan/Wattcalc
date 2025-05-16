from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

def watt(Tensão, Corrente):
    Watt = Tensão * Corrente
    return Watt

def ampere(Potencia, Tensão):
    Ampere = Potencia / Tensão
    return Ampere

def volt(Corrente, Ohm):
    Volt = Corrente * Ohm
    return Volt

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method =='POST':
        try:
            Potencia = float(request.form['potencia'])
        except:
            Potencia = 0

        try:
            Tensão = float(request.form['tensao'])
        except:
            Tensão = 0
        
        try:
            Corrente = float(request.form['corrente'])
        except:
            Corrente = 0
        
        try:
            Ohm = float(request.form['Ohm'])
        except:
            Ohm = 0

        a = watt(Tensão, Corrente)

        try:
            b = float(ampere(Potencia, Tensão))
        except:
            b = 0

        c = volt(Corrente, Ohm)
        return render_template('main.html', a=a, b=b, c=c)
    else:
        a = 0
        b = 0
        c = 0
        return render_template('main.html', a=a, b=b, c=c)