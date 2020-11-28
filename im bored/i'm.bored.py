tel={}

tel['Paula']='518 543 519'
tel['Jaś']='696 969 696'
tel['Jakiś_random']='518 543 518'

print(tel)

print(tel.keys())

print(tel.values())


for i in tel.keys():
    print(i + '=' + tel[i])