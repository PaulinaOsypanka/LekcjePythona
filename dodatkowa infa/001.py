import time

input('Hej! Zobacz ten fajny film. (kliknij \'enter\' aby kontynuować)')
wiek = input('Ten film nie jest odpowiedni dla wszystkich użytkowników. Ile masz lat? ')

if int(wiek) > 7 or int(wiek) == 7:
    input('Film jest odpowiedni dla ciebie. Przejdź dalej klikając \'enter\'')
    print('loading.')
    time.sleep(0.01)
    print('loading..')
    time.sleep(0.01)
    print('loading...')
    print('Failed to load, please try again.')
else:
    czekaj = 7 - int(wiek)    
    print('Aby obejrzeć ten film, musisz zaczekać ', int(czekaj), 'lat/a')
