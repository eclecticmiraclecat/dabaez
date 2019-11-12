# mortgage.py
#
# Find out how long to a pay off a mortgage

principal = 500_000
payment = 2684.11
rate = 0.05
total_paid = 0

# Extra payment info
extra_payment = 1_000
extra_payment_start_month = 1
extra_payment_end_month = 60
month = 0

out = open('schedule.txt', 'w')     # Open a file for writing
print(f"{'Month' :>5s} {'Interest' :>10s} {'Principal' :>10s} {'Remaining' :>10s}", file=out)
while principal > 0:
    month += 1
    if extra_payment_start_month <= month <= extra_payment_end_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    interest = principal*(rate/12)
    principal = principal + interest - total_payment
    total_paid += total_payment
    print(f'{month :>5d} {interest :>10.2f} {total_payment - interest :>10.2f} {principal :>10.2f}', file=out)

out.close()
print('Total paid:', total_paid)
