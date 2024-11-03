def al_rebre_numero(rebutNumero):
    if rebutNumero < numero:
        basic.show_icon(IconNames.HAPPY)
    elif rebutNumero == numero:
        basic.show_icon(IconNames.ASLEEP)
    else:
        basic.show_icon(IconNames.SAD)
radio.on_received_number(al_rebre_numero)

def al_polsar_boto_a():
    radio.send_string("Hola")
input.on_button_pressed(Button.A, al_polsar_boto_a)

def al_polsar_boto_ab():
    global numero_enviar
    numero_enviar = randint(1, 6)
    radio.send_number(numero_enviar)
input.on_button_pressed(Button.AB, al_polsar_boto_ab)

def al_rebre_text(rebutText):
    basic.show_string(rebutText)
radio.on_received_string(al_rebre_text)

def al_polsar_boto_b():
    global numero
    numero = (numero + 1) % 7
    basic.show_number(numero)
input.on_button_pressed(Button.B, al_polsar_boto_b)

numero_enviar = 0
numero = 0
radio.set_group(10)
