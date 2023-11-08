# web3_fintech
invoices for customers and accept cryptocurrency

## setup, run and testing

1. clone the repository.
2. create env: `conda create --name web3` and activate: `conda activate web3`
3. install requirements: `pip3 install -r requirements.txt`
4. run the API flask server: `python3 app.py`
5. open web browser and navigate to http://localhost:5000.

## usage

1. enter username and email.
2. select a currency from the dropdown list.
3. default invoice amount for the selected currency will be displayed in the Invoice Amount field.
4. click the "Simulate Payment" button to simulate the creation of an invoice.
5. list of invoice created will be displayed as well.

## expectations

1. Security Measures:
- include end-to-end encryption for user data and transactions.
- use HTTPS to secure communication.
- implement secure key management for cryptocurrency wallets.
- consider 2-factor authentication for user accounts.

2. Strategies for Scaling Up:
- load balancing to distribute traffic.
- caching for frequently accessed data.