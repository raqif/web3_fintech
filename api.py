# api.py
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField
from wtforms.validators import InputRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

class InvoiceForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email address')])
    currency = SelectField('Select Currency', choices=[], validators=[InputRequired()])
    amount = DecimalField('Invoice Amount', validators=[InputRequired()])

    def set_currency_choices(self, currency_choices):
        self.currency.choices = currency_choices

class Invoice:
    next_invoice_number = 1
    invoices = []

    def __init__(self, invoice_id, username, email, total_amount, line_items, currency_type):
        self.invoice_id = Invoice.next_invoice_number
        Invoice.next_invoice_number += 1
        self.invoice_id = invoice_id
        self.username = username
        self.email = email
        self.total_amount = total_amount
        self.line_items = line_items
        self.currency_type = currency_type
        Invoice.invoices.append(self)

def get_currency_choices():
    # list of currency options
    return [('ETH', 'ETH'), ('BTC', 'BTC'), ('USDT', 'USDT'), ('USDC', 'USDC')]

def get_minimum_amount(currency_type):
    # setting deafult minimum amount for each currency
    currency_minimum_amounts = {'ETH': 0.1, 'BTC': 0.001, 'USDT': 0.01, 'USDC': 0.01}
    return currency_minimum_amounts.get(currency_type, 0.01)

def get_decimal_places(currency_type):
    # seting deafault decimal places for each currency
    currency_decimal_places = {'ETH': 1, 'BTC': 8, 'USDT': 2, 'USDC': 2}
    return currency_decimal_places.get(currency_type, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InvoiceForm()

    # set currency choices
    currency_choices = get_currency_choices()
    form.set_currency_choices(currency_choices)

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        currency_type = form.currency.data
        amount = form.amount.data

        # adjust amount based on the decimal places for the selected currency
        decimal_places = get_decimal_places(currency_type)
        adjusted_amount = round(amount, decimal_places)

        # simulate backend call to add an invoice
        simulate_backend_add_invoice(username, email, adjusted_amount, currency_type)

    # list all invoices
    invoices = get_all_invoices()

    return render_template('index.html', form=form, invoices=invoices)

def simulate_backend_add_invoice(username, email, amount, currency_type):
    invoice_id = len(Invoice.invoices) + 1 
    line_items = ["Item1"]
    invoice = Invoice(invoice_id=invoice_id, username=username, email=email, total_amount=amount, line_items=line_items, currency_type=currency_type)
    print(f"Simulated backend: Added Invoice - ID: {invoice.invoice_id}, Username: {invoice.username}, Email: {invoice.email}, Total Amount: {invoice.total_amount}, Currency: {invoice.currency_type}, Items: {line_items}")

def get_all_invoices():
    # get all invoices from the backend
    return Invoice.invoices

if __name__ == '__main__':
    app.run(port=5000, debug=True)
