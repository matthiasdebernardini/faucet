import os

from flask import Flask
from lightning import LightningRpc

rpc = LightningRpc(os.environ["RPC_SOCKET"])
app = Flask(__name__)

@app.route("/")
def getinfo():
    return str(rpc.getinfo())
