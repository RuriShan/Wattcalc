from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

def watt(Tensão, Corrente):
    V = Tensão
    A = Corrente

    Watt = V * A
    return Watt

def ampere(Tensão, Potencia):
    Ampere = Tensão / Potencia
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
            b = ampere(Tensão, Potencia)
        except:
            b = 0
        c = volt(Corrente, Ohm)
        return render_template('main.html', a=a, b=b, c=c)
    else:
        a = 0
        b = 0
        c = 0
        return render_template('main.html', a=a, b=b, c=c)