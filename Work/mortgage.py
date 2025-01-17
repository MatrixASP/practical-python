# mortgage.py
#
# Exercise 1.7


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0.0
paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
while principal > 0:
    # keep counter for month
    month = month + 1
    # check if month is ranged for additional payments
    if (month >= extra_payment_start_month and month <= extra_payment_end_month):
        paid = payment + extra_payment
    else:
        paid = payment
    
    # reduce principal and calc payments made to date
    principal = principal * (1 + rate / 12) - (paid)
    total_paid = total_paid + paid
    #month - total paid - pricipal
    print('{0} {1} {2}'.format(month, round(total_paid, 4), principal))

    if (paid > principal):
        paid = principal
        principal = 0
        total_paid = total_paid + paid
        month += 1
        print('{0} {1} {2}'.format(month, round(total_paid, 4), principal))
        break
        

print('Total paid', round(total_paid, 4))
print(month)
print('Total paid: {} in {} months'.format( total_paid, month))

