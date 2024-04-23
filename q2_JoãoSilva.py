
# passo 1: Create Transaction
create_transaction = lambda: print("Create Transaction")

# passo 2a: Fund Transfer - Receive Cash
receive_cash = lambda: print("Receive Cash")
provide_bank_details = lambda: print("Provide Bank Deposit Details")
fund_transfer = lambda: receive_cash() or provide_bank_details()

# passo 2b: Credit - Request Credit Account Details
request_credit_details = lambda: print("Request Credit Account Details")
request_bank_payment = lambda: print("Request Payment from Bank")
credit = lambda: request_credit_details() or request_bank_payment()

# passo 3: Print Payment Receipt if Cash was received
print_receipt = lambda: print("Print Payment Receipt")

# passo 4: Complete Transaction
complete_transaction = lambda: print("Complete Transaction")

# passo 5: Confirma pagamento
confirm_payment = lambda: print("Confirm Payment Approval from Bank")

# passo 6: Close Transaction
close_transaction = lambda: print("Close Transaction")

# passo 7: Cancel Transaction 
cancel_transaction = lambda: print("Cancel Transaction")

# Funções dos pagamentos
def payment_flow_cash():
    create_transaction()
    fund_transfer()
    print_receipt()
    complete_transaction()
    close_transaction()

def payment_flow_credit():
    create_transaction()
    credit()
    confirm_payment()
    complete_transaction()
    close_transaction()

def stress_test():
    pass  

def test_payment_flow_cash():
    pass 

def test_payment_flow_credit():
    pass  


def main():
    payment_flow_cash()
    payment_flow_credit()
    # Simular stress
    stress_test()

main()


