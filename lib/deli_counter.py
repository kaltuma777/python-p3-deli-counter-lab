katz_deli = []
deli_II = ['Mark','John','Faith','Tracy']
deli_III = ['Eleanor', 'Oliver', 'Aria', 'Leo', 'Isabella']

def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        lineup = ' '.join([f"{index + 1}. {value}" for index,value in enumerate(katz_deli)])
        print(f"The line is currently: {lineup}")

line(katz_deli)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {katz_deli.index(name) + 1} in line.")

take_a_number(deli_II, 'Matz')

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)

print(now_serving(deli_III))