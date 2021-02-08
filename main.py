#light
#while True:
#    print(input.light_level())
#    if (input.light_level()) > 0:
#        light.clear()
#    else:
#        light.clear()

print(input.light_level() + 35.6)

while True: 
    if input.light_level()+ 35.6 > 400:
       music.power_up.play_until_done()
    else:
        music.stop_all_sounds()