import math

weight_choice = input("Use Pounds or Grams?: (P/G)").upper()
p_weight = float(input("Enter total weight of Pennies (grams): "))
n_weight = float(input("Enter total weight of Nickels (grams): "))
d_weight = float(input("Enter total weight of Dimes (grams): "))
q_weight = float(input("Enter total weight of Quarters (grams): "))

def coin_estimator(p_weight, n_weight, d_weight, q_weight, weight_choice):
    pen_roll = 50
    nic_roll = 40
    dime_roll = 50
    quar_roll = 40
    N_const = 5.00
    P_const = 2.50
    D_const = 2.268
    Q_const = 5.670
    if weight_choice == 'P':
        
    penny_roll_total = math.floor((p_weight / P_const) / pen_roll)
    nickel_roll_total = math.floor((n_weight / N_const) / nic_roll)
    dime_roll_total = math.floor((d_weight / D_const) / dime_roll)
    quarter_roll_total = math.floor((q_weight / Q_const) / quar_roll)
    print(f'You need {penny_roll_total} penny rolls')
    print(f'You need {nickel_roll_total} nickel rolls')
    print(f'You need {dime_roll_total} dime rolls')
    print(f'You need {quarter_roll_total} quarter rolls')

    

coin_estimator(p_weight, n_weight, d_weight, q_weight)
