from random import randint, choice
from time import sleep, time
from colorama import Fore, Back, init
init(autoreset=True)

#--- estructura de juego hasta la línea 80
#version
print(Fore.GREEN + Back.BLACK + "Canuto's Trivia version 4.1")
print(Fore.CYAN + "∆ " * 35 + Fore.RESET)

## LISTAS
A = [1, 2, 3, 4, 5, 6]
num_preguntas = [1, 2, 3, 4, 5, "BONUS"]  #estas para el historial de juego
puntajes = []

textos = [
    "Pregunta 1:", "Pregunta 2:", "Pregunta 3:", "Pregunta 4:","Pregunta 5:","¡BONUS!"
]  
preguntas = [
    '¿Quién es el autor de "Don Quijote de la Mancha"?',
    "¿Cuál es el río más largo del mundo?",
    "¿Dónde se originaron los juegos olímpicos?",
    "¿Cuándo acabó la II Guerra Mundial?",
    "¿Quién es el padre del psicoanálisis?",
    "¿Cuál de los siguientes números es HEXADECIMAL?"
]

letras = ["a)", "b)", "c)", "d)"]  #defino las letras y las alternativas en listas diferentes para que pueda seleccionarlas independientemente
alternativas = [["Miguel de Cervantes Saavedra", "Inca Garcilaso de la Vega", "Ricardo Palma", "Adolfo Béquer"], ["Nilo", "Amazonas", "Éufrates", "Misisipi"],["Roma", "Arabia", "China", "Grecia"],["1935", "1945", "1928", "1937"],["Isaac Netwon", "Iván Pávlov", "Sigmund Freud","Wilhelm Wundt"], ["145.789", "12FF01G", "01010101", "10BC13F"]]  ##

##  variables
puntaje = 10  #puntaje inicial
t = 0  #define el num de pregunta
iniciar_trivia = True

#modos de juego
normal = False  #valor del 'normal'
contra = False  #valor del 'contrarreloj'
myf = False  #valor del modo "mala y fuera"
cron = False  #valo del 'cronómetro'
intentos = int(1)  #num de intentos   ##

W = Fore.WHITE + Back.BLACK
R = Fore.RESET + Back.RESET  #los defino porque usaré esta configuración seguido


#---FUNCIONES:
#para instrucciones. (solo las usaré una vez -por ahora-, pero es mucho texto y prefiero aislarlo del cuerpo)
def instrucciones():
  print(
      Fore.LIGHTBLUE_EX +
      '''\n\nDeberás responder las siguientes preguntas escribiendo la letra de la alternativa que consideres correcta y luego presionando 'Enter' para enviarla. Dependiendo de si la letra es la correcta o no, recibirás una cantidad aleatoria de puntos, que pueden ser negativos o positivos. 
      
      Además, en algunas preguntas podrías obtener puntos 'extras' si eliges la letra oculta. ¡Deberás probar! ¿Entendido?\n''')

  ok = input(Fore.YELLOW + "(Responde entendido)   ").lower()
  while ok not in ("entendido"):
      ok = input("Quiero que estés seguro. Responde de nuevo:   ").lower()

  print("¡Está bien!\n")


#para la ejecucion automática y aleatoria de las preguntas
def preg(k):
    global t
    print("\n\n", textos[0][t] + "\n-->" + Fore.YELLOW + textos[1][k - 1] + "\n")
    sleep(2)
    for i in range(0, 4):
      print(letras[i], alternativas[k - 1][i])
      sleep(.7)
    t = t + 1


#para las respuestas de cada pregunta
def respuesta():
    r = input("\n-->" + W + " Tu respuesta: " + R).lower()
    while r not in ("a", "b", "c", "d"):
      r = input(Fore.GREEN + "--> Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ").lower()
    return r
#---

#INTRO
print(Fore.CYAN+'''\n\n--> Soy Mr. Canuto'''+Fore.RESET+'''
        __
     o-''|\_____/)
      \_/|_)     )
         \  __  /
         (_/ (_/  
        ''')

input(Fore.YELLOW+'(Di "Hola Mr. Canuto")'+Fore.RESET+'   ')

print('''\n           ,-.___,-.
--> ¡Hola, \_/_ _\_/
     hola!   )O_O(
            { (_) }
             `-^-'   ''')
    
sleep(0.5)
nombre = Fore.CYAN+ input(Fore.CYAN+"Dime, ¿cómo te llamas? ")

print(Fore.RESET+'''\n--> Bien
  ███▓▒░░''',nombre,'''░░▒▓███  \n''')

# texto de bienvenida
print('''
 --> ╔═══╗ ♪   ¡Bienvenid@
     ║███║  ♫  a mi trivia
     ║(●)  ♫   sobre
     ╚═══╝ ♪♪  Cultura General!
    ''')
sleep(1.5) 
print('''Ahora pondré a prueba tus conocimientos :D.''')
print("--> ¿Está bien?\n")
a_ = input(Fore.YELLOW+"(Responde sí o no)  ").lower()

if a_ in ("si", "sí"):
  print("¡Correcto!")
else:
  print('''¡Ehh! ¿Y esos ánimos?
  Bueno...''')
sleep(1.5)

#BUCLE DE JUEGO
while iniciar_trivia == True:
  print("\n\nEste es tu intento n°",intentos," ahora mismo tienes 10 puntos.\n\n")
  sleep(1)
  print("¿Deseas comenzar o primero leer las instrucciones?\n")
  sleep(1)

  print("1) Deseo comenzar")
  sleep(0.5)
  answer = input("2) Deseo leer las instrucciones   ")
    
  if answer == "1":
    print("")
  elif answer == "2":
    instrucciones()
  else:
    b_ = input("\nSi eliges 1 el juego comenzará inmediatamente, si eliges 2, mostraré las instrucciones.   ")
    while b_ not in ("1","2"):
      b_ = input(Fore.GREEN+"Escribe 1 o 2 para continuar: ")
    if b_ == "2":
      instrucciones()
  
  print("Existen 4 modos de juegos.")
  sleep(.7)
  print(Fore.YELLOW+"1)  Normal:"+Fore.RESET+" 5 preguntas, tiempo ilimitado.")
  sleep(1.3)
  print(Fore.LIGHTGREEN_EX+"2)  Contrarreloj:"+Fore.RESET+" Tendrás 5 minutos para responder la mayor cantidad de preguntas posibles.")
  sleep(1.3)
  print(Fore.LIGHTBLUE_EX+"3)  Incorrecta y fuera:"+Fore.RESET+" Logra la mayor cantidad de preguntas correctas. Tiempo ilimitado, el juego acabará cuando cometas un error.")
  sleep(1.3)
  print(Fore.LIGHTMAGENTA_EX+"4)  Cronómetro:"+Fore.RESET+" Te daré 5 preguntas, trata de reponderlas en el menor tiempo posible")
  
  modo = input("¿Con cuál quieres comenzar?   ")
  str_m = modo.isnumeric()

  while str_m == False:
    modo = input("Ingresa un número. ")
    str_m = modo.isnumeric()
  
  while modo not in ("1","2","3","4"):
    modo = input("Elige un número válido: ")

  print("¡Comencemos...!") 
  sleep(2)
    
  print("Cargando trivia...")
  sleep(0.7)
  print(" 10% █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  sleep(0.7) 
  print(" 30% ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  sleep(.7)
  print(" 50% █████▒▒▒▒▒▒▒▒▒▒")
  sleep(.7)
  print(" 70% ███████▒▒▒▒▒▒")
  sleep(.7)
  print(" 90% █████████▒▒")
  sleep(.7)
  print("100% ██████████")
  sleep(0.5) 

  #COMIENZO DE MODOS DE JUEGO
  if modo == "1":
    normal=True
    print('''Estás jugando en el modo:'''+Fore.YELLOW+'''"Normal"''')

    while normal == True:
      pass
      normal = False
    print("")

  elif modo == "2":
    contra=True
    print('''Estás jugando en el modo:'''+Fore.YELLOW+'''"Contrarreloj"''')

    while contra == True:
      pass
      contra = False
    print("")
    
  elif modo == "3":
    myf=True
    print('''Estás jugando en el modo:'''+Fore.YELLOW+'''"Incorrecta y fuera"''')

    while myf == True:
      pass
      myf = False
    print("")

  elif modo == "4":
    cron=True
    print('''Estás jugando en el modo:'''+Fore.YELLOW+'''"Cronómetro"''')

    while cron == True:
      pass
      cron = False
    print("")
  #FIN DE MODOS DE JUEGO
  

  #Posibilidad de ver el historial de juego
  historial = input(Fore.YELLOW+'''\n¿Deseas ver tu Historial de juego'''+Fore.RESET+'''Escribe 'H' para mostrar el historial de esta partida: ''').lower()
  if historial == "h" :
    print(Fore.BLACK + Back.WHITE+'''Historial de juego:'''+R+'''\n''') 
    for number in range(0, 6):
      print(Fore.CYAN+"El puntaje de la pregunta", num_preguntas[number], "es", puntajes[number])
    print("Puntaje total: ",puntaje)
  sleep(1.3)

  #Posibilidad de jugar de nuevo
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'R' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != ("r"): 
    iniciar_trivia = False 
  else:
    intentos +=1 

#DESPEDIDA
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
                        '''+Fore.YELLOW+'''Alcanzaste''', puntaje,'''puntos.
                        ''')
     
print(Fore.CYAN+"∆ "*35)