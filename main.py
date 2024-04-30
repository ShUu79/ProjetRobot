#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Création del'obet robot sous le nom ev3
ev3 = EV3Brick()

# Programme à exécuter

# numéro de l'exemple à exécuter
# à choisir parmi 1, 2, 3, 4, 5, 6.1, 6.2, 7, 8, 9.1, 9.2, 9.3 ou 10
numero = 1

if numero <= 0:
    pass

elif numero == 1:
    # Exemple 1
    # Création de l'écran
    ecran = ev3.screen
    # Afficher un texte au point (10,10) de l'écran
    ecran.draw_text(10, 10, "Hello World !")
    wait(1000)

elif numero == 2:
    # Exemple 2
    # le robot parle...
    ev3.speaker.say("Hello world !")
    # ... et que la Force soit avec vous !
    morceau = [(392, 350, 100), (392, 350, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100), (392, 700, 100), (587.32, 350, 100), (587.32, 350, 100), (587.32, 350, 100), (622.26, 250, 100), (466.2, 25, 100), (369.99, 350, 100), (311.1, 250, 100), (466.2, 25, 100), (392, 700, 100), (784, 350, 100), (392, 250, 100), (392, 25, 100), (784, 350, 100), (739.98, 250, 100), (698.46, 25, 100), (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200), (554.36, 350, 100), (523.25, 250, 100), (493.88, 25, 100), (466.16, 25, 100), (440, 25, 100), (466.16, 50, 400), (311.13, 25, 200), (369.99, 350, 100), (311.13, 250, 100), (392, 25, 100), (466.16, 350, 100), (392, 250, 100), (466.16, 25, 100), (587.32, 700, 100), (784, 350, 100), (392, 250, 100), (392, 25, 100), (784, 350, 100), (739.98, 250, 100), (698.46, 25, 100), (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200), (554.36, 350, 100), (523.25, 250, 100), (493.88, 25, 100), (466.16, 25, 100), (440, 25, 100), (466.16, 50, 400), (311.13, 25, 200), (392, 350, 100), (311.13, 250, 100), (466.16, 25, 100), (392.00, 300, 150), (311.13, 250, 100), (466.16, 25, 100), (392, 700,100)]
    for note in morceau:
        ev3.speaker.beep(note[0], note[1])
        wait(note[2])

elif numero == 3:
    # Exemple 3
    # On allume les leds en jaune
    ev3.light.on(Color.YELLOW)
    # Pause d'1 seconde
    wait(1000)
    # On allume les leds en rouge
    ev3.light.on(Color.RED)
    # Pause d'1 seconde
    wait(1000)
    # On éteint toutes les leds
    ev3.light.off()
    # Pause d'1 seconde
    wait(1000)

elif numero == 4:
    # Exemple 4
    # test d’appui
    for i in range(0, 100):
        if Button.LEFT in ev3.buttons.pressed():   # Appui sur le bouton [GAUCHE]
            print("Left is pressed")
        if Button.DOWN in ev3.buttons.pressed():   # Appui sur le bouton [BAS]
            print("Down is pressed")
        wait(100)

elif numero == 5:
    # Exemple 5
    # initialisation du capteur
    contact_sensor = TouchSensor(Port.S1)
    # test du capteur
    # Tant qu'il n'est pas enfoncé, on allume les leds en rouge
    while contact_sensor.pressed() is False:
        ev3.light.on(Color.RED)
        # Si il est enfoncé, on allume les leds en jaune
    if contact_sensor.pressed() == True:
        ev3.light.on(Color.YELLOW)
        wait(2000)
        # On éteint toutes les leds
        ev3.light.off()
        wait(1000)    

elif numero == 6.1:
    # Exemple 6.1
    # Création du capteur lumineux
    color_sensor = ColorSensor(Port.S3)
    # Tant que la couleur n'est pas blanche...
    while color_sensor.color() != Color.WHITE:
        if color_sensor.color() == Color.RED:
            ev3.light.on(Color.RED)
        if color_sensor.color() == Color.GREEN:
            ev3.light.on(Color.GREEN)
        if color_sensor.color() == Color.YELLOW:
            ev3.light.on(Color.YELLOW)
    # On éteint tout
    ev3.light.off()

elif numero == 6.2:
    # Exemple 6.2
    # Création du capteur lumineux
    color_sensor = ColorSensor(Port.S3)
    # Pendant 10 secondes on change la led selon la lumière
    for i in range(0, 10):
        if color_sensor.reflection() < 50:
            ev3.light.on(Color.RED)
        else:
            ev3.light.on(Color.YELLOW)
        wait(1000)
    # On éteint tout
    ev3.light.off()

elif numero == 7:
    # Exemple 7
    # Création du capteur ultrason et de l'écran
    us = UltrasonicSensor(Port.S2)
    ecran = ev3.screen
    # Pendant 10 secondes on lit et affiche la distance en cm
    for i in range(0, 10):
        distance = int(us.distance()) / 10
        affichage =  "%f cm" % distance
        ecran.print("Distance = ")
        ecran.print(affichage)
        wait(1000)
        ecran.clear()

elif numero == 8:
    # Exemple 8
    # Création du capteur gyroscopique et de l'écran
    gs = GyroSensor(Port.S4, Direction.CLOCKWISE)
    ecran = ev3.screen
    # Pendant 10 secondes on lit et affiche l’angle
    for i in range(0, 10):
        angle = gs.angle()
        ecran.draw_text(10, 10, "Angle = %d degres" % angle)
        wait(1000)
        ecran.clear()

elif numero == 9.1:
    # Exemple 9.1
    # Création des moteurs
    left_m = Motor(Port.A, Direction.CLOCKWISE)
    right_m = Motor(Port.C, Direction.CLOCKWISE)
    medium_m = Motor(Port.B, Direction.CLOCKWISE)
    # Les moteurs tournent pendant 2s à une vitesse de 500 deg/s dans le même sens (horaire)
    # le robot avance
    left_m.run(500)
    right_m.run(500) 
    wait(2000)
    left_m.stop()
    right_m.stop()
    # Les moteurs tournent pendant 2,8s à une vitesse de 500 deg/s dans des sens différents
    # le robot tourne sur lui-même
    left_m.run(-500)
    right_m.run(500) 
    wait(2800)
    left_m.stop()
    right_m.stop()
    # Les moteurs tournent pendant 2s à une vitesse de 500 deg/s dans le même sens (anti-horaire)
    # le robot recule
    left_m.run(-500)
    right_m.run(-500) 
    wait(2000)
    left_m.stop()
    right_m.stop()
    # Le troisème moteur abaisse et remonte la barre
    medium_m.run(-1000)
    wait(1000)
    medium_m.stop()
    medium_m.run(+1000)
    wait(1000)
    medium_m.stop()


elif numero == 9.2:
    # Exemple 9.2
    # Création des moteurs gauche et droit reliés aux ports A et C
    left_m = Motor(Port.A, Direction.CLOCKWISE)
    right_m = Motor(Port.C, Direction.CLOCKWISE)
    # Les moteurs tournent pendant 1s chacun leur tour
    left_m.run_time(500, 1000)
    right_m.run_time(500, 1000)
    wait(1000)
    # Les moteurs tournent pendant 1s simultanément
    left_m.run_time(500, 1000, wait = False)
    right_m.run_time(500, 1000, wait = False)
    wait(1000)

elif numero == 9.3:
    # Exemple 9.3
    # Initialisation des moteurs.
    left_motor = Motor(Port.A)
    right_motor = Motor(Port.C)
    # Initialisation du mode de pilotage.
    robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
    # Le robot avance et recule d'un mètre.
    robot.straight(1000)
    ev3.speaker.beep()
    robot.straight(-1000)
    ev3.speaker.beep()
    # Le robot fait un tour sur lui-même puis recommence dans l'autre sens.
    robot.turn(360)
    ev3.speaker.beep()
    robot.turn(-360)
    ev3.speaker.beep()

elif numero == 10:
    # Exemple 10
    continuer = True
    while continuer:
        # on écrit ici le code à exécuter
        # on fait clignoter les leds en jaune et en rouge
        for loop in range(1000):
            ev3.light.on(Color.YELLOW)
            if len(ev3.buttons.pressed()) != 0:
                continuer = False
        for loop in range(1000):
            ev3.light.on(Color.RED)
            if len(ev3.buttons.pressed()) != 0:
                continuer = False
    # on écrit ici l'action à exécuter en cas d'arrêt
    ev3.light.off()
    wait(1000)

else:
    pass