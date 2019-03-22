import inputs
import turtle as t
t.setup(700,700)
t.shape("turtle")
t.color("red")
while True:
    events = inputs.get_gamepad()
    for event in events:
        if event.code == 'BTN_SOUTH' and event.state == 1:
             print('Equis!')
             t.forward(50)
        if event.code == 'BTN_NORTH' and event.state == 1:
             print('Triangulo!')
             t.backward(50)
        if event.code == 'BTN_WEST' and event.state == 1:
             print('Cuadrado!')
             t.left(90)
        if event.code == 'BTN_EAST' and event.state == 1:
             print('Circulo!')
             t.left(-90)
        if event.code == 'BTN_TR' and event.state == 1:
             print('Triger Derecho Superior!')
             t.penup()
        if event.code == 'BTN_THUMBR' and event.state == 1:
             print('Centro Analogico Derecho!')
        if event.code == 'BTN_TL' and event.state == 1:
             print('Triger Izquierdo Superior!')
             t.pendown()
        if event.code == 'BTN_THUMBL' and event.state == 1:
             print('Centro Analogico Izquierdo!')
        if event.code == 'BTN_START' and event.state == 1:
             print('Select!')
        if event.code == 'BTN_SELECT' and event.state == 1:
             print('Start!')
        if event.code == 'ABS_HAT0X' and event.state == 1:
             print('D Right!')
        if event.code == 'ABS_HAT0Y' and event.state == 1:
             print('D Down!')
        if event.code == 'ABS_HAT0X' and event.state == -1:
             print('D Left!')
        if event.code == 'ABS_HAT0Y' and event.state == -1:
             print('D Up!')
        if event.code == 'ABS_Z' and event.state > 10:
             print('Analogico Posterior izquierdo ' + str(event.state))
        if event.code == 'ABS_RZ' and event.state > 10:
             print('Analogico Posterior derecha ' + str(event.state))
        if event.code == 'ABS_Y' and event.state > 150:
             print('Analogico Principal Baja ' + str(event.state))
        if event.code == 'ABS_Y' and event.state < 50:
             print('Analogico Principal Sube ' + str(event.state))
        if event.code == 'ABS_X' and event.state > 200:
             print('Analogico Principal Derecha ' + str(event.state))
        if event.code == 'ABS_X' and event.state < 50:
             print('Analogico Principal Izquierda ' + str(event.state))
        if event.code == 'ABS_RY' and event.state > 200:
             print('Analogico Secundario Baja ' + str(event.state))
        if event.code == 'ABS_RY' and event.state < 50:
             print('Analogico Secundario Sube ' + str(event.state))
        if event.code == 'ABS_RX' and event.state > 200:
             print('Analogico Secundario Derecha ' + str(event.state))
        if event.code == 'ABS_RX' and event.state < 50:
             print('Analogico Secundario Izquierda ' + str(event.state))