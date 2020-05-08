dog_cal = 140
bun_cal = 120
mus_cal = 20
ket_cal = 80
onion_cal = 40


print ("\tHDog\tBun\tKet\tMus\tOni\tTotal")
count = 1
for HDog in [0, 1]:
    for Bun in [0, 1]:
        for Ket in [0, 1]:
            for Mus in [0, 1]:
                for Oni in [0, 1]:
                    total_cal = HDog * dog_cal + Bun * bun_cal + Mus * mus_cal + Ket * ket_cal + Oni * onion_cal
                    print ("#", count, "\t", HDog, "\t", Bun, "\t", Ket, "\t", Mus, "\t", Oni, "\t", total_cal)
                    count = count + 1 