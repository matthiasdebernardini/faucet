import os
import random

from flask_qrcode import QRcode
from flask import Flask, render_template, request
from lightning import LightningRpc

rpc = LightningRpc(os.environ['RPC_SOCKET'])
app = Flask(__name__)
QRcode(app)

@app.route('/getinfo')
def getinfo():
    return str(rpc.getinfo())

@app.route('/', methods=['GET', 'POST'])
def index():
    invoice = None
    pay_result = None

    # set invoice if that was requested
    if request.method == 'POST':
        amount = request.form['amount']
        print(request.form)
        invoice = rpc.invoice(amount, str(random.random()), 'test')

    return render_template('index.html', name='justin', invoice=invoice)
