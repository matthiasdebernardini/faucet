import os
import random

from flask_qrcode import QRcode
from flask import Flask, render_template, request
from lightning import LightningRpc

rpc = LightningRpc(os.environ['RPC_SOCKET'])
app = Flask(__name__)
QRcode(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    invoice = None
    pay_result = None

    if request.method == 'POST':
        # create invoice
        if 'amount' in request.form:
            amount = request.form['amount']
            invoice = rpc.invoice(amount, str(random.random()), 'test')['bolt11']
        # pay invoice
        if 'invoice' in request.form:
            pay_result = rpc.pay(request.form['invoice'])
            pay_result = json.dumps(pay_result, sort_keys=True, indent=4, separators=(',', ': ')
             
    return render_template('index.html', name='justin', 
        invoice=invoice, pay_result=pay_result)
