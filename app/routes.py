import os
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import RequestForm, PayForm

from flask_qrcode import QRcode
from flask import Flask, render_template, request
from lightning import LightningRpc
from lightning.lightning import RpcError

from json2html import *

rpc = LightningRpc(os.environ['RPC_SOCKET'])
# fedi_connect = os.environ['CONNECT_INFO']


@app.route('/pay', methods=['GET', 'POST'])
def pay():
    form = PayForm()
    if form.validate_on_submit():
        try:
            result = rpc.pay(form.invoice.data)
            pay_result = json2html.convert(json=result)
        except RpcError as e:
            print(e.error["message"], e)
            flash('{}'.format(
                e.error["message"]))
            return redirect('/index')
        flash('Invoice {}'.format(
            form.invoice.data))
        return redirect('/index')
    return render_template('pay.html', title='Pay Invoice', form=form)


@app.route('/')
def landing():
    return url_for('index')


@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/request', methods=['GET', 'POST'])
def request():
    form = RequestForm()
    if form.validate_on_submit():
        flash('Amount {}'.format(
            form.amount.data))
        return redirect('/index')
    return render_template('request.html', title='Request', form=form)
