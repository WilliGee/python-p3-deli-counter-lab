katz_deli = []
def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        alert = "The line is currently:"
        for i in range(len(katz_deli)):
            alert = alert + f' {i + 1}. {katz_deli[i]}'
        print(alert)

def take_a_number(katz_deli, new_customer):
    katz_deli.append(new_customer)
    print(f'Welcome, {new_customer}. You are number {len(katz_deli)} in line.')


take_a_number(katz_deli, 'Ada')

if not katz_deli:
        print("There is nobody waiting to be served!")
else:
    print(f'Currently serving {katz_deli[0]}.')
    del katz_deli[0]