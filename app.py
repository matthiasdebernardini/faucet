"""
Generate invoice on one daemon and pay it on the other
"""
import os
from lightning import LightningRpc

l = LightningRpc(os.environ["RPC_SOCKET"])

info = l.getinfo()
print(info)
