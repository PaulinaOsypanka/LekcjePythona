who = input('Who are you? I\'m ')
if who == 'Paulina Osypanka':
    print('Oh, okay.')
    print('*Music stops*')
    print('Wait a minute.. ')
    exit()
else:
    print('Ok, thanks.')

where = input('Where do u live? I live in ')
when = input('Która godzina? ')

if when == 'Pora na lunch':
    print(':D')

info={}
info['WHO'] = who
info['ERWEH'] = where
info['HWEN'] = when

def info_show(info):
    print(info['WHO'], 'u live in...')
    print(info['ERWEH'], '^0^')
    print('So... It\'s',info['HWEN'], 'o\'clock',)
    print('Srsly? I dont neeed to know what time is it ;-;')


info_show(info)

print('THE END')