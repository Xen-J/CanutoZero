from random  import randint, shuffle, choice
from time import sleep, time
from colorama import Fore, Back, Style, init
init(autoreset = True)

#version
print(Fore.GREEN+Back.BLACK+ "Canuto's Trivia version 3.1.2")
print(Fore.CYAN+"∆ "*35 +Fore.RESET)

#LISTAS
preguntas = [1,2,3,4,5,"BONUS"]
A =[1,2,3,4,5,6]
puntajes = []
textos=[["Pregunta 1:","Pregunta 2:","Pregunta 3:", "Pregunta 4:", "Pregunta 5:","¡BONUS!"], ['¿Quién es el autor de "Don Quijote de la Mancha"?',"¿Cuál es el río más largo del mundo?","¿Dónde se originaron los juegos olímpicos?","¿Cuándo acabó la II Guerra Mundial?", "¿Quién es el padre del psicoanálisis?","¿Cuál de los siguientes números es HEXADECIMAL?"]]
letras = ["a)","b)","c)","d)"]
alternativas =[["Miguel de Cervantes Saavedra","Inca Garcilaso de la Vega", "Ricardo Palma","Adolfo Béquer"], ["Nilo", "Amazonas","Éufrates","Misisipi"], ["Roma","Arabia","China","Grecia"],["1935","1945","1928","1937"],["Isaac Netwon","Iván Pávlov","Sigmund Freud","Wilhelm Wundt"],["145.789", "12FF01G", "01010101", "10BC13F"]]

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


#---FUNCIONES:
#para las respuestas de cada pregunta
def respuesta():
  r = input("\n-->"+W+" Tu respuesta: "+R).lower()
  while r not in ("a","b","c","d"):
    r = input(GREEN+"--> Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ").lower()
  return r

#para la ejecucion automática y aleatoria de las preguntas
def preg(k):
  global t
  print("\n\n",textos[0][t]+"\n-->"+YELLOW+textos[1][k-1]+"\n")
  sleep(2)
  for i in range(0,4):
    print(letras[i], alternativas[k-1][i])
    sleep(.7)
  t=t+1
#para instrucciones
def instrucciones():
  print(Fore.LIGHTBLUE_EX+'''\n\nDeberás responder las siguientes preguntas escribiendo la letra de la alternativa que consideres correcta y luego presionando 'Enter' para enviarla. 
  Dependiendo de si la letra es la correcta o no, recibirás una cantidad aleatoria de puntos, que pueden ser negativos o positivos. 
  
  Además, en algunas preguntas podrías obtener puntos 'extras' si eliges la letra oculta. ¡Deberás probar!
  ¿Entendido?\n''')
  
  ok = input(YELLOW+"(Responde entendido)   "+RESET).lower()
  while ok not in ("entendido"):
    ok = input("Quiero que estés seguro. Responde de nuevo:   ").lower()
  
  print("¡Está bien!\n")

#para el final 1 del modo 2: 
def f_12():
  print("¡Bien hecho!")
  print("¡Has respondido todo a tiempo!")
#para el final 1 del modo 3
def f_13():
  print("¡Bien hecho!")
  print("¡Has completado esta trivia satisfactoriamente! Wow, 6 respuestas correctas seguidas, ¡impresionante!")
#--- FUNCIONES

#  variables
puntaje = 10
t =0
iniciar_trivia = True

normal= False
contra=False
myf = False #valor del modo "mala y fuera"
cron=False
intentos = int(0)

#INTRO
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
  ███▓▒░░''',nombre,'''░░▒▓███  \n''')

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
  
  print("\n\n¿Deseas comenzar o primero leer las instrucciones?\n")
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
      b_ = input(GREEN+"Escribe 1 o 2 para continuar: "+RESET)
    if b_ == "2":
      instrucciones()
  
  print("Existen 4 modos de juegos.")
  sleep(.7)
  print(YELLOW+"1)  Normal:"+RESET+" 5 preguntas, tiempo ilimitado.")
  sleep(1.3)
  print(Fore.LIGHTGREEN_EX+"2)  Contrarreloj:"+RESET+" Tendrás 5 minutos para responder la mayor cantidad de preguntas posibles.")
  sleep(1.3)
  print(Fore.LIGHTBLUE_EX+"3)  Incorrecta y fuera:"+RESET+" Logra la mayor cantidad de preguntas correctas. Tiempo ilimitado, el juego acabará cuando cometas un error.")
  sleep(1.3)
  print(Fore.LIGHTMAGENTA_EX+"4)  Cronómetro:"+RESET+" Te daré 5 preguntas, trata de reponderlas en el menor tiempo posible")
  
  modo = input("¿Con cuál quieres comenzar?   ")
  str_m = modo.isnumeric()

  while str_m == False:
    str_m = input("Ingresa un número. ")
  
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

  if modo =="1":
    normal=True
  elif modo=="2":
    contra=True
  elif modo=="3":
    myf=True
  elif modo=="4":
    cron=True

  def p_1():
    a=randint(0,21)
    global r, puntaje,modo
    if r == "a":
      puntaje += 10
      puntajes.append(10)
      print("¡Geniaal! Ganaste 10 puntos", nombre)
    elif modo=="3":
      if r!="a":
        myf == False
    else:
      puntaje -= a
      puntajes.append(-a)
      print("¡Incorrecto! Has perdido",a,"puntos",nombre)
  def p_2():
    a=randint(0,21)
    global r, puntaje, modo
    if r == "b":
      puntaje +=a
      puntajes.append(a)
      print("¡ Muy bien",nombre,"! Ganaste",a,"puntos")
    elif r == "a":
      puntaje -= a
      puntajes.append(-a)
      print("Ehhh, incorrecto. Sé que puede causar confusión, pero la respuesta es la b. Has perdido",a,"puntos",nombre)
    elif r == "x":
      puntaje *=2
      puntajes.append("Desconocido xd")
      print("¿Hola? Wiii. Esto es divertido. Ahora tienes",puntaje, nombre,)
    elif modo=="3":
      if r!="b":
        myf == False
    else:
      puntaje -=a
      puntajes.append(-a)
      print("¡Incorrecto! La respuesta correcta es la b. Has perdido",a,"puntos",nombre)
  def p_3():
    randint(0,21)
    global r, puntaje,modo
    if r == "d":
      puntaje += a
      puntajes.append(a)
      print("¡Muy bien! Ganaste", a, "puntos", nombre) 
    elif modo=="3":
      if r!="a":
        myf == False
    else:
      puntaje -=a
      puntajes.append(-a)
      print("¡Incorrecto! La respuesta correcta es la d. Has perdido",a,"puntos",nombre) 
    print("Se llaman así porque se celebraban en la ciudad de Olimpia. ¿Lo sabías?")
  def p_4():
    global r, puntaje,modo,a
    if r == "b":
      punje +=a
      puntajes.append(a)
      print("¡Muy bien! Ganaste", a, "puntos", nombre)
    elif r == "l":
      d = randint(0,5001)
      puntaje += d
      puntajes.append(d, "Era un 'extra' uwu")
      print("¡GENIAAL! Ganaste", d, "puntos", nombre)
      print("Ahora tienes",puntaje,"puntos")
    elif modo=="3":
      if r!="b":
        myf == False
    else:
      puntaje -= a
      puntajes.append(-a)
      print("¡Incorrecto! Has perdido", a, "puntos", nombre,". La respuesta correcta es la b.")
  def p_5():
    global r, puntaje,modo,a
    a=randint(0,21)
    if r == "c":
      punjes.append(puntaje)
      puntaje *=2
      print("¡ Muy bien",nombre,"! Tu puntaje ha sido duplicado. Ahora tienes ",puntaje,"puntos.")
    elif r == "a":
      puntaje /=2
      puntajes.append(-puntaje)
      print("Ehhh, ¡totalmente incorrecto! La respuesta es la c. Isaac Netwon es el Padre de la Física Moderna, ¡deberías saberlo! Pierdes"+YELLOW+" la mitad "+RESET+"de tus puntos.")
    elif r == "b":
      puntaje += 1
      puntajes.append(1)
      print("¡Incorrecto! La respuesta correcta es la c. Iván Pavlov es un psicoanalista pero no el padre de esta. Solo ganas"+YELLOW+ " 1 "+RESET+ "punto.")
    elif modo=="3":
      if r!="c":
        myf == False
    else:
      puntaje -= 15
      puntajes.append(-15)
      print("¡Incorrecto! La respuesta correcta es la c. Wilhelm Wundt es el Padre de la Psicología; no del Psicoanálisis. Pierdes "+YELLOW+ "15 "+RESET+ "puntos",nombre,".")
    sleep(2)
  def bon():
    global r, puntaje,modo,a
    a=randint(0,21)
    if r == "a":
      pri("¡Totalmente incorrecto!", nombre, "Este es un número DECIMAL... ¡Deberías saberlo! Pierdes "+YELLOW+"la mitad"+YELLOW+" de tu puntaje")
      puntaje /= 2
      puntajes.append(-puntaje)
    elif r == "b":
      print("¡Incorrecto!", nombre, "Te confundiste por una letra... Los números hexadecimales llegan hasta la F, la G no corresponde. Te damos"+YELLOW+" + 5"+RESET+" puntos por casi acertar")
      puntaje += 5
      puntajes.append(5)
    elif r == "c":
      print("¡Incorrecto!", nombre, "¡este es número binario! Lo siento, pierdes"+YELLOW+" 5"+RESET+" puntos.")
      puntaje -= 5
      puntajes.append(-5)
    elif modo=="3":
      if r!="d":
        myf == False
    else:
      print("¡Correcto!", nombre, "Este es el único número hexadecimal de la lista, ¡ganaste puntos "+YELLOW+"x 2!!"+RESET)
      puntajes.append(puntaje)
      puntaje = puntaje * 2
  
  def sec_p():
    global r, puntaje,modo,t
    while len(A) != 0:
      a = randint(0,21)
      j = choice(A)
      preg(j)
      r=respuesta()
      return a
      if j ==1:
       p_1()
      elif j ==2:
        p_2()
      elif j ==3:
        p_3()
      elif j ==4:
        p_4()
      elif j ==5:
        p_5()
      elif j==6:
        bon()
      A.remove(j)
     
    if modo == "2":
      contra== True
      f_12()
    elif modo == "3":
      f_13()

    print()
  
  #definiendo los game loops de los modos de juego
  if modo == "1":
      sec_p()
  elif modo == "2":
    start = input("\n¡Escribe 'start' para comenzar a tomar el tiempo y correr el temporrizador!  ").lower()
    while start != "start":
      start= input("Escribe 'start' para continuar: ").lower()
    time_start=time()
    
    while ((time()-time_start)<300):
      contra=False
      sec_p()
    if contra == False:
      print("¡Oh no! No lo lograste")
      sleep(.5)
      print("¡Tal vez quieras jugar de nuevo!\n\n")
      sleep(.5)
      print("De cualquier modo...")
      sleep(1)
  elif modo == "3":
    while myf == True:
      sec_p()
  elif modo == "4":
    start = input("\n¡Escribe 'start' iniciar el cronómetro!  ").lower()
    while start != "start":
      start= input("Escribe 'start' para continuar: ").lower()
    ts =time()
    sec_p()
    te = time()
    timec = te - ts

  sleep(2)
  print('''
         __^__                                      __^__
        ( ___ )------------------------------------( ___ )
         | / |                                      | \ |
         | / |        '''+YELLOW+'''    ¡Felicidades!'''+RESET+'''                                 | \ |
         | / |                                      | \ |
         | / |      ¡Terminaste esta trivia!        | \ |
         |___|                                      |___|
        (_____)------------------------------------(_____) 
  ''')
  
  if modo == "3":
    print("¡Completaste esta trivia en",int(timec/60),"minutos y",int(timec%60),"segundos!")
  
  
  s = input(YELLOW+'''\n¿Deseas ver tu Historial de juego?'''+RESET+''' 
     Escribe s para mostrar el historial de esta partida: ''').lower()
  if s == "s" :
    print(Fore.BLACK + Back.WHITE+Style.BRIGHT+'''Historial de juego:'''+R+'''\n''')
       
    for number in range(0, 6):
      print(CYAN+"El puntaje de la pregunta", preguntas[number], "es", puntajes[number])
       
    print("Puntaje total: ",puntaje)
  
  sleep(1.3)
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'R' para repetir, o cualquier tecla para finalizar: ").lower()
  
  A = [1,2,3,4,5,6]
  

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

        


      