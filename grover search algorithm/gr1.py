my_list = [1, 3, 5, 2, 4, 9, 5, 8, 0, 7, 6]
def the_oracle(my_input):
    winner = 7
    if my_input is winner:
        response = True
    else:
        response = False
    return response

for index, trial_number in enumerate(my_list):
    if the_oracle(trial_number) is True:
        print('Winner found at index %i'%index)
        print('%i calls to the Oracle used'%(index+1))