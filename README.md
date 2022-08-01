
### Instructions

```
git clone https://github.com/justinmoon/minimint_helper.git
cd minimint_helper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export RPC_SOCKET=/path/to/lightning-rpc
flask run --host=0.0.0.0
```

From your minimint directory:

```
CONNECT_INFO=$($FM_MINT_CLIENT connect-info)
qrencode -m 2 -o connect.png <<< $CONNECT_INFO
```

And copy `connect.png` to `minimint_helper/static/connect.png`

Note: perhaps we should add a `save_qr` command to `lib.sh` in addition to `print_qr` ...
