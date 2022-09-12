### Instructions

```
git clone https://github.com/fedimint/faucet.git
cd faucet
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export RPC_SOCKET=/path/to/lightning-rpc
export CONNECT_INFO=$(mint_client_cli <workdir> connect-info)
flask --app faucet.py run --host=0.0.0.0
```
