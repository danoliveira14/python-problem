a_pagar = int(input())
pago_por_mes = int(input())

restante = 1
parcelar = a_pagar / pago_por_mes
dps = a_pagar - pago_por_mes

if a_pagar < pago_por_mes:
    zero = 0
    print('pagamento:', restante)
    print('antes = ', a_pagar)
    print('depois =', zero)
    print("-" * 5)
else:
    while parcelar != 0:
        print('pagamento:', restante)
        print('antes = ', a_pagar)
        print('depois =', dps)
        print("-" * 5)
        parcelar -= 1
        a_pagar -= pago_por_mes
        restante += 1
        dps -= pago_por_mes
