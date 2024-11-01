# import pickle

with open('pi_million_digits(1).txt') as file:
    pi = file.read()
pi = pi.rstrip()
pi = pi.replace('\n','')
pi = pi.replace(' ','')


tyil = '040709'
print(tyil in pi)

# pi = float(pi)
#
# with open('amaliyot/pi_float.dat','wb') as file:
#     pickle.dump(pi,file)