import random  
from time import sleep
from colorama import Fore, Back, Style, init
init(autoreset = True)

#  variables
puntaje = 10
a = int(random.randint(5,21))
iniciar_trivia = True
intentos = int(0)

preguntas = [1,2,3,4,5,"BONUS"]
puntajes = []
W = Fore.WHITE+ Back.BLACK 
R = Fore.RESET+Back.RESET

#colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

print(Fore.GREEN+Back.BLACK+ "Canuto's Trivia version 1.2.4")
print(Fore.CYAN+"∆ "*35 +Fore.RESET)

#Funciones:
def comenzar():
  print("¡Comencemos...!") 
  sleep(2)
    
  print("Cargando trivia...")
  sleep(0.7)
  print("10% █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  sleep(0.7) 
  print("30% ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  sleep(.7)
  print("50% █████▒▒▒▒▒▒▒▒▒▒")
  sleep(.7)
  print("70% ███████▒▒▒▒▒▒")
  sleep(.7)
  print("90% █████████▒▒")
  sleep(.7)
  print("99.9% █████████▒")
  sleep(2)
  print("100% ██████████")
  sleep(0.5)

def instrucciones():
  print(GREEN+'''\n\nDeberás responder las siguientes preguntas escribiendo la letra de la alternativa que consideres correcta y luego presionando 'Enter' para enviarla. 
  Dependiendo de si la letra es la correcta o no, recibirás una cantidad aleatoria de puntos, que pueden ser negativos o positivos. 
  
  Además, en algunas preguntas podrías obtener puntos 'extras' si eliges la letra oculta. (PISTA: En la pregunta 3 la letra es el equivalente a 10 en el sistema de numeración romano. Y en la pregunta 5, la letra que indica 100 en este mismo sistema).
  ¿Entendido?\n''')
  ok = input(YELLOW+"(Responde entendido)   "+RESET).lower()
  
  while ok not in ("entendido"):
    ok = input("Quiero que estés seguro. Responde de nuevo:   ").lower()

  else:
    print("¡Está bien!\n")
    comenzar()

def contra():
  pass

def incorrecta():
  pass

def cronom():
  pass

def conc():
  pass


#bienvenida
print(CYAN+'''\n\n--> Soy Mr. Canuto'''+RESET+ '''
        __
     o-''|\_____/)
      \_/|_)     )
         \  __  /
         (_/ (_/  
        ''')

input(YELLOW+ Style.NORMAL+'(Di "Hola Mr. Canuto")   '+RESET)

print('''\n           ,-.___,-.
--> ¡Hola, \_/_ _\_/
     hola!   )O_O(
            { (_) }
             `-^-'   ''')
    
sleep(0.5)
nombre = CYAN+ input(CYAN+'''
    Dime, ¿cómo te llamas? '''+RESET)+RESET

while iniciar_trivia == True:
  intentos += 1

  print('''\n--> Bien
  ███▓▒░░''',nombre,'''░░▒▓███  
''')

  # texto de bienvenida
  print('''
--> ╔═══╗ ♪  ¡Bienvenid@
    ║███║  ♫  a mi trivia
    ║(●)  ♫   sobre
    ╚═══╝ ♪♪  Cultura General!
    ''')
  sleep(1.5) 
  print('''Ahora pondré a prueba tus conocimientos :D.''')
  print("--> ¿Está bien?\n")
  a_ = input(YELLOW+"(Responde sí o no)  "+RESET).lower()

  if a_ in ("si", "sí"):
    print("¡Correcto! Este es tu intento n°",intentos,"y tienes 10 puntos.\n\n")
    sleep(1)
  
  else:
    print("¡Ehh! ¿Y esos ánimos?")
    sleep(1.5)
    print("Bueno, este es tu intento n°",intentos," ahora mismo tienes 10 puntos.\n\n")
    sleep(1)
  
  print("Existen 4 modos de juegos.")
  sleep(.7)
  print(YELLOW+"1)  Contrareloj:"+RESET+" Tendrás 5 minutos para responder la mayor cantidad de preguntas posibles.")
  sleep(1.3)
  print(Fore.LIGHTGREEN_EX+"2)  Incorrecta y fuera:"+RESET+" Logra la mayor cantidad de preguntas correctas. Tiempo ilimitado, el juego acabará cuando cometas un error.")
  sleep(1.3)
  print(Fore.LIGHTBLUE_EX+"3)  Cronómetro:"+RESET+" Te daré 10 preguntas, trata de reponderlas en el menor tiempo posible.")
  sleep(1.3)
  print(Fore.LIGHTMAGENTA_EX+"4)  Pura concentración:"+RESET+" 10 preguntas, pero muchas distracciones (en construcción)")
  
  modo = input("¿Con cuál quieres comenzar?   ")

  while(not modo.isdigit()):
    modo=input("Ingresa un número: ")
  
  while modo not in ("1","2","3","4"):
    modo=input("Ingresa un número válido: ")
   
  if modo == "1":
    contra()
  elif modo == "2":
    incorrecta()
  elif modo == "3":
    cronom()
  elif modo == "4":
    conc()
  

  print("¿Deseas comenzar o primero leer las instrucciones?\n")
  sleep(1)

  print("1) Deseo comenzar")
  sleep(0.5)
  r = input("2) Deseo leer las instrucciones   ")

  if r == "1":
    print("")
    comenzar()
  elif r == "2":
    instrucciones()
  else:
    b_ = input("\nSi eliges 1 el juego comenzará inmediatamente, si eliges 2, mostraré las instrucciones.   ")
    while b_ not in ("1","2"):
      b_ = input(GREEN+"Escribe 1 o 2 para continuar: "+RESET)
    
    if b_ == "1":
      comenzar()
    elif b_ == "2":
      instrucciones()
    
  print(''' --------------

--> Pregunta 1:
'''
   ,nombre,YELLOW+ '''¿quién es el autor de "Don Quijote de la Mancha"?\n''')
  sleep(2)
  print("a) Miguel de Cervantes Saavedra")
  sleep(0.5)
  print("b) Inca Garcilaso de la Vega")
  sleep(0.5)
  print("c) Ricardo Palma")
  sleep(0.5)
  print("d) Adolfo Bécquer")
  sleep(0.5)
  r_1 = input("\n-->"+W+" Tu respuesta: "+R).lower()

  while r_1 not in ("a", "b", "c", "d"):
    r_1 = input(GREEN+"--> Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ").lower()

  if r_1 == "a":
    puntaje += 10
    puntajes.append(10)
    print("¡Geniaal! Ganaste 10 puntos", nombre)
  else:
    puntaje -= a
    puntajes.append(-a)
    print("¡Incorrecto! Has perdido",a,"puntos",nombre)



  print('''\n  --------------

--> Pregunta 2: 
  '''+YELLOW+'''¿Cuál es el río más largo del mundo?\n''')
  sleep(2)
  print("a) Nilo")
  sleep(0.5)
  print("b) Amazonas")
  sleep(0.5)
  print("c) Eúfrates")
  sleep(0.5)
  print("d) Misisipi")
  sleep(0.5)
  r_2 = input("\n-->"+W+" Tu respuesta: "+R).lower()

  while r_2 not in ("a", "b", "c", "d", "x"):
    r_2 = input(GREEN+"--> Debes responder a, b c o d. Ingresa nuevamente tu respuesta: ").lower()

  if r_2 == "b":
    puntaje +=a
    puntajes.append(a)
    print("¡ Muy bien",nombre,"! Ganaste",a,"puntos")
  elif r_2 == "a":
    puntaje -= a
    puntajes.append(-a)
    print("Ehhh, incorrecto. Sé que puede causar confusión, pero la respuesta es la b. Has perdido",a,"puntos",nombre)
  elif r_2 == "x":
    puntaje *=2
    puntajes.append("Desconocido xd")
    print("¿Hola? Wiii. Esto es divertido. Ahora tienes",puntaje, nombre,)
  else:
    puntaje -=a
    puntajes.append(-a)
    print("¡Incorrecto! La respuesta correcta es la b. Has perdido",a,"puntos",nombre)

  uno = input("\n\n--> ¿Te gustaron los Juegos Panamericanos y Parapanamericanos del año pasado? (Responde sí o no).  ").lower()

  if uno in ("sí","si"):
    print('''¡Qué bien!
    
    En ese caso''')
  elif uno in ("no"):
    print('''¿En serio? ¡Una lástima! Bueno...
    
    En cualquier caso...''')
  else:
    print('''¿Disculpa? Creo que no entendí. Bueno...
    
    En cualquier caso...''')






  print('''\n --------------

--> Pregunta 3:'''+YELLOW+'''
    ¿Dónde se originaron los juegos olímpicos?\n''')
  sleep(2)
  print("a) Roma")
  sleep(0.5)
  print("b) Arabia")
  sleep(0.5)
  print("c) China")
  sleep(0.5)
  print("d) Grecia")
  sleep(0.5)
  r_3 = input("\n-->"+W+"Tu respuesta: "+R).lower()

  while r_3 not in ("a", "b", "c", "d", "no lo se"):
    r_3 = input(GREEN+"--> Debes responder a, b c o d. Ingresa nuevamente tu respuesta: ").lower()

  if r_3 == "d":
    a = random.randint(0,21)
    puntaje += a
    puntajes.append(a)
    print("¡Muy bien! Ganaste", a, "puntos", nombre)
    
  elif r_3 == "no lo se":
    
    print("Oye, si no sabes la respuesta correcta intenta con cualquier clave. No seas tímid@. La respuesta correcta es la d: Grecia\n")
  else:
    puntaje +=a
    print("¡Incorrecto! La respuesta correcta es la d. Has perdido",a,"puntos",nombre) 
    
  print("Se llaman así porque se celebraban en la ciudad de Olimpia. ¿Lo sabías?")


  print('''\n  --------------

--> Pregunta 4: '''+YELLOW+'''
    ¿Cuándo acabó la II Guerra Mundial?\n''')
  sleep(2)
  print("a) 1935")
  sleep(0.5)
  print("b) 1945")
  sleep(0.5)
  print("c) 1928")
  sleep(0.5)
  print("d) 1937")
  sleep(0.5)
  r_4 = input("\n-->"+W+" Tu respuesta: "+R).lower()

  while r_4 not in ("a", "b", "c", "d", "l"):
    r_4 = input(GREEN+"--> Debes responder a, b c o d. Ingresa nuevamente tu respuesta: ").lower()

  if r_4 == "b":
    puntaje +=a
    puntajes.append(a)
    print("¡Muy bien! Ganaste", a, "puntos", nombre)
  elif r_4 == "l":
    d = random.randint(0,5001)
    puntaje += d
    puntajes.append(d, "Era un 'extra' uwu")
    print("¡GENIAAL! Ganaste", d, "puntos", nombre)
    print("Ahora tienes",puntaje,"puntos")
  else:
    puntaje -= a
    puntajes.append(-a)
    print("¡Incorrecto! Has perdido", a, "puntos", nombre,". La respuesta correcta es la b.")




  print('''\n  --------------

  --> Pregunta 5: '''+YELLOW+'''
    ¿Quién es el padre del psicoanálisis?\n''')
  sleep(2)
  print("a) Isaac Netwon")
  sleep(0.5)
  print("b) Iván Pavlov")
  sleep(0.5)
  print("c) Sigmund Freud")
  sleep(0.5)
  print("d) Wilhelm Wundt")
  sleep(0.5)
  r_5 = input("\n-->"+W+" Tu respuesta: "+R).lower()

  while r_5 not in ("a", "b", "c", "d"):
    r_5 = input(GREEN+"--> Debes responder a, b c o d. Ingresa nuevamente tu respuesta: ").lower()

  if r_5 == "c":
    puntajes.append(puntaje)
    puntaje *=2
    print("¡ Muy bien",nombre,"! Tu puntaje ha sido duplicado. Ahora tienes ",puntaje,"puntos.")
    sleep(1)
  elif r_5 == "a":
    puntaje /=2
    puntajes.append(-puntaje)
    print("Ehhh, ¡totalmente incorrecto! La respuesta es la c. Isaac Netwon es el Padre de la Física Moderna, ¡deberías saberlo! Pierdes"+YELLOW+" la mitad "+RESET+"de tus puntos.")
    sleep(2)
  elif r_5 == "b":
    puntaje += 1
    puntajes.append(1)
    print("¡Incorrecto! La respuesta correcta es la c. Iván Pavlov es un psicoanalista pero no el padre de esta. Solo ganas"+YELLOW+ " 1 "+RESET+ "punto.")
    sleep(2)
  else:
    puntaje -= 15
    puntajes.append(-15)
    print("¡Incorrecto! La respuesta correcta es la c. Wilhelm Wundt es el Padre de la Psicología; no del Psicoanálisis. Pierdes "+YELLOW+ "15 "+RESET+ "puntos",nombre,".")
    sleep(2)

  # Pregunta con operadores matemáticos:
  print(CYAN+"\n--> ¡BONUS! ¿Cuál de los siguientes números es HEXADECIMAL?")
  sleep(2)
  print("a) 145.789")
  sleep(0.5)
  print("b) 12FF01G")
  sleep(0.5)
  print("c) 01010101")
  sleep(0.5)
  print("d) 10BC13F")
  sleep(0.5)
  bonus = input("\n"+W+"Tu respuesta: "+R).lower()

  while bonus not in ("a", "b", "c", "d"):
    bonus = input(GREEN+"Debes responder a, b c o d. Ingresa nuevamente tu respuesta: ").lower()
  
  if bonus == "a":
    print("¡Totalmente incorrecto!", nombre, "Este es un número DECIMAL... ¡Deberías saberlo! Pierdes "+YELLOW+"la mitad"+YELLOW+" de tu puntaje")
    puntaje /= 2
    puntajes.append(-puntaje)

  elif bonus == "b":
    print("¡Incorrecto!", nombre, "Te confundiste por una letra... Los números hexadecimales llegan hasta la F, la G no corresponde. Te damos"+YELLOW+" + 5"+RESET+" puntos por casi acertar")
    puntaje += 5
    puntajes.append(5)
  elif bonus == "c":
    print("¡Incorrecto!", nombre, "¡este es número binario! Lo siento, pierdes"+YELLOW+" 5"+RESET+" puntos.")
    puntaje -= 5
    puntajes.append(-5)
  else:
    print("¡Correcto!", nombre, "Este es el único número hexadecimal de la lista, ¡ganaste puntos "+YELLOW+"x 2!!"+RESET)
    puntajes.append(puntaje)
    puntaje = puntaje * 2


  sleep(2)
  print('''
          __^__                                      __^__
        ( ___ )------------------------------------( ___ )
         | / |                                      | \ |
         | / |        '''+YELLOW+'''    ¡Felicidades!'''+RESET+'''            | \ |
         | / |      ¡Terminaste esta trivia!        | \ |
         |___|                                      |___|
        (_____)------------------------------------(_____) 
  ''')
  s = input(YELLOW+'''\n¿Deseas ver tu Historial de juego?'''+RESET+''' 
     Escribe s para mostrar el historial de esta partida: ''')
  if s == "s" :
    print(Fore.BLACK + Back.WHITE+Style.BRIGHT+'''Historial de juego:'''+R+'''\n''')
       
    for number in range(0, 6):
      print(CYAN+"El puntaje de la pregunta", preguntas[number], "es", puntajes[number])
       
    print("Puntaje total: ",puntaje)

  sleep(1.3)
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'R' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != ("r"): 
     print('''\n
                    __
                  .'  '.
              _.-'/  |  \
  ,        _.-"  ,|  /  0 `-.
  |\    .-"       `--""-.__.'=====================-,
  \ '-'`        .___.--._)=========================|
    \            .'      |                         |
      |     /,_.-'       |    ¡GRACIAS,''',nombre,'''    |
  _ /   _.'(             |        POR JUGAR         |
  /  ,-' \  \            |        MI TRIVIA!        |
  \  \    `-'            |                          |
  `-'                   '--------------------------'
                        '''+YELLOW+'''Alcanzaste''', puntaje,'''puntos.
                        '''+RESET)
     
     print(CYAN+"∆ "*35 +RESET)
     iniciar_trivia = False  

        


      