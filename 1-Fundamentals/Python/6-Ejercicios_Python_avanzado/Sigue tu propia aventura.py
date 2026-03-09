# Sigue tu propia aventura

# # Despiertas en un bosque. Sólo ves una cabaña. Hace frío, la cabaña parece caliente, tiene luz, y la luz tiembla. 
# # ¿Hay un fuego encendido? Suena demasiado bien para no intentarlo.  
# # Andas hasta la puerta, la empujas y se abre. La puerta es pesada, pero puedes abrirla.
# # Dentro encuentras una hoguera. En el centro de la sala. Y nada más. No hay muebles, no hay chimenea. El diseño es extraño. Todo parece antinatural. Como diseñado por algo no humano.
# # Al fondo de la sala vacía, a través del humo de la hoguera, se aprecian dos puertas. Iguales, juntas, inertes. Algo te dice que tienes que elegir, pero tu cerebro te grita que no lo hagas.
# # Avanzas hacia las puertas, te paras justo entre ambas y las observas, como pidiendo alguna señal. Suena un rugido en la puerta por la que has entrado. La cas tiene prisa, tienes que elegir. Señal recibida.
# # Miras a la derecha, miras a la izquierda. Y eliges:

juego = input('Empieza la aventura: ')


while juego != 'exit':
    juego = input('Seguimos? ')
    print('''Despiertas en un bosque. Sólo ves una cabaña. Hace frío, la cabaña parece caliente, tiene luz, y la luz tiembla. 
¿Hay un fuego encendido? Suena demasiado bien para no intentarlo.  
Andas hasta la puerta, la empujas y se abre. La puerta es pesada, pero puedes abrirla.
Dentro encuentras una hoguera. En el centro de la sala. Y nada más. No hay muebles, 
no hay chimenea. El diseño es extraño. Todo parece antinatural. 
Como diseñado por algo no humano.
Al fondo de la sala vacía, a través del humo de la hoguera, se aprecian dos puertas. 
Iguales, juntas, inertes. Algo te dice que tienes que elegir, 
pero tu cerebro te grita que no lo hagas.
Avanzas hacia las puertas, te paras justo entre ambas y las observas, 
como pidiendo alguna señal. Suena un rugido en la puerta por la que has entrado. 
La casa tiene prisa, tienes que elegir. Señal recibida.
''')
    
    juego = (input('Miras a la derecha, miras a la izquierda. Y eliges:')).lower()
    if juego == 'izquerda' or juego == 'i':
        print('Decides abrir la puerta izquierda')
        print('Algo te incita a entrar')
        print('Después de tu primer paso, la puerta se cierra.')
        print('Aparece un tigre')
        print('Te come')
        print('¿Has perdido?')
        juego = (input('Vuelves atrás 1 minuto. Miras a la derecha, miras a la izquierda. Y eliges:')).lower()
    if juego == 'derecha' or juego == 'd':
        print('Decides abrir la puerta derecha')
        print('Necesitas entrar')
        print('Después de tu primer paso, la puerta se cierra.')
        print('Aparece un tigre')
        print('Parece majo, es tu amigo ahora. Enhorabuena, tienes un tigre. Os vais y vivís aventuras')

    
    

