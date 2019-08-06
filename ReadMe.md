# Remote python signer for tezos (alphanet):
1. Create operation in file **transaction.json**.
2. Run script **request_helpers.sh**, save result into file **operation.hex**.
3. Paste your private key into **sign.py** file (replace '<private_key>') 
4. Run python script **sign.py**.
5. Concatenate **operation.hex** and result of **sign.py** (*"operation.hex + sign.py_result"* ).
6. Paste it concatenation into **transaction_binary_signed.json**
7. Run script **request_inject.sh**.