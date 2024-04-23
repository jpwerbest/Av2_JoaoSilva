# Inicializa o processo de pagamento, imprimindo a ação.
create_transaction = lambda: print("Create Transaction")

# Função que simula o recebimento de dinheiro, imprimindo a ação.
receive_cash = lambda: print("Receive Cash")

# Função que simula a impressão do recibo de pagamento, imprimindo a ação.
print_payment_receipt = lambda: print("Print Payment Receipt")

# Função que simula o retorno do recibo de pagamento, imprimindo a ação.
return_payment_receipt = lambda: print("Return Payment Receipt")

# Função que simula a conclusão da transação, imprimindo a ação.
complete_transaction = lambda: print("Complete Transaction")

# Função que simula a transferência de fundos, imprimindo a ação.
fund_transfer = lambda: print("Fund Transfer")

# Função que simula o fornecimento de detalhes do depósito bancário, imprimindo a ação.
provide_bank_deposit_details = lambda: print("Provide Bank Deposit Details")

# Função que simula o pedido de pagamento ao banco, imprimindo a ação.
request_payment_bank = lambda: print("Request Payment from Bank")

# Função que simula a confirmação da aprovação do pagamento pelo banco, imprimindo a ação.
confirm_payment_approval = lambda: print("Confirm Payment Approval from Bank")

# Função que simula o fechamento da transação, imprimindo a ação.
close_transaction = lambda: print("Close Transaction")

# Função que simula o pedido de detalhes da conta de crédito, imprimindo a ação.
request_credit_account_details = lambda: print("Request Credit Account Details")

# Função que simula o cancelamento da transação, imprimindo a ação.
cancel_transaction = lambda: print("Cancel Transaction")

# Uma expressão lambda para determinar o fluxo com base em uma condição, que nesse caso é estática,
# mas poderia ser dinâmica dependendo da implementação desejada.
payment_flow = lambda condition: (fund_transfer(), provide_bank_deposit_details(), confirm_payment_approval(), close_transaction()) \
    if condition == 'fund_transfer' else (receive_cash(), print_payment_receipt(), return_payment_receipt(), complete_transaction())

# Outra expressão lambda para a decisão de crédito.
credit_decision = lambda is_approved: (request_credit_account_details(), request_payment_bank()) if is_approved else (cancel_transaction(),)

# O processo principal de pagamento encapsulado em uma função `def`.
def payment_process():
    create_transaction()  # Inicia o processo de pagamento.

    # Aqui poderia haver uma lógica para determinar qual fluxo seguir.
    # Por simplicidade, vamos assumir um valor fixo.
    payment_type = 'fund_transfer'  # Pode ser 'fund_transfer' ou 'cash'.
    payment_flow(payment_type)  # Executa o fluxo de pagamento com base no tipo.

    # Assumindo uma aprovação de crédito estática, mas isso seria dinâmico na realidade.
    is_credit_approved = True
    credit_decision(is_credit_approved)  # Executa a decisão de crédito.

# Chamando a função principal para iniciar o processo.
payment_process()
