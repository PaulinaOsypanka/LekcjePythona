wzrost = float(input('Hej ile masz metrów wzrostu? '))
waga = float(input('a ile ważysz? (plis nie kłam lol) '))

wzrost2 = wzrost * wzrost
BMI = waga / wzrost2
Bmi2 = round(BMI, 2)
print('Twoje BMI (w zaokrągleniu) to', Bmi2)