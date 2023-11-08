# User class
class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

# Invoice class
class Invoice:
    # do incremental invoice number
    next_invoice_number = 1

    def __init__(self, total_amount, line_items):
        # set unique invoice number
        self.invoice_id = Invoice.next_invoice_number
        Invoice.next_invoice_number += 1

        self.total_amount = total_amount
        self.line_items = line_items

# CryptocurrencyHandler class
class CryptocurrencyHandler:
    def handle_payment(self, user, invoice, currency_type):
        if currency_type == "ETH":
            self.handle_ethereum_payment(user, invoice)
        elif currency_type == "BTC":
            self.handle_bitcoin_payment(user, invoice)
        elif currency_type == "USDT":
            self.handle_usdt_payment(user, invoice)
        elif currency_type == "USDC":
            self.handle_usdc_payment(user, invoice)

    def handle_ethereum_payment(self, user, invoice):
        print(f"Simulating Ethereum payment for user {user.username}, invoice {invoice.invoice_id}.")

    def handle_bitcoin_payment(self, user, invoice):
        print(f"Simulating Bitcoin payment for user {user.username}, invoice {invoice.invoice_id}.")

    def handle_usdt_payment(self, user, invoice):
        print(f"Simulating USDT payment for user {user.username}, invoice {invoice.invoice_id}.")

    def handle_usdc_payment(self, user, invoice):
        print(f"Simulating USDC payment for user {user.username}, invoice {invoice.invoice_id}.")

# Example Usage
if __name__ == "__main__":
    user = User(user_id=1, username="raqif", email="raqifmahat@gmail.com")
    crypto_handler = CryptocurrencyHandler()

    while True:
        input_currency = input("please select either ETH, BTC, USDT, USDC (type 'exit' to exit):\n")
        input_currency = input_currency.upper()
        
        invoice = Invoice(total_amount=1.5, line_items=["Item1"])

        if input_currency == 'EXIT':
            break  # Exit the loop if the user inputs 'exit'
        
        if input_currency in ["ETH", "BTC", "USDT", "USDC"]:
            crypto_handler.handle_payment(user, invoice, currency_type=input_currency)
        else:
            print("Invalid input. Please enter a valid currency or type 'exit' to exit.")
