# Importar bibliotecas para la interfaz gráfica
desde PyQt5 importar QtCore, QtGui, QtWidgets

# Importar bibliotecas para la conexión I2C y lectura del sensor
importar smbus2
importar bme280

# Biblioteca para interactuar con la base de datos Postgres
importar psycopg2

# Biblioteca para realizar gráficas
desde matplotlib importa pyplot como plt

# Biblioteca para obtener el tiempo actual
tiempo de importación


# Abrir conexión con la BD
conn = psycopg2.connect ( ' dbname = proyectofinal ' )

# Abrir conexión I2C con sensor BME280 de temperatura, presión, y humedad
puerto =  1
direccion =  0x 76  # Dirección predeterminada del sensor
bus = smbus2.SMBus (puerto)
parametros_calibracion = bme280.load_calibration_params (bus, direccion)


def  sensarTemperatura ():
	'' '
	Función que obtiene la temperatura del sensor bme280 y la almacena
	en la base de datos junto con el tiempo de medición
	'' '
	# Obtener todos los datos del sensor
	datos = bme280.sample (bus, direccion, parametros_calibracion)
	# Obtener temperatura
	temperatura = datos.temperature
	# Redondear temperatura a 3 decimales
	temperatura =  redonda (temperatura, 3 )

	# Imprimir resultado
	imprimir ( " Temperatura: "  +  str (temperatura) +  " ºC " )

	# Agregar datos a la base de datos
	# Abrir el cursor para escribir en la BD
	cur = conn.cursor ()
	# Obtener tiempo real
	tiempo =  int (time.time ())
	# Crear comando SQL
	comando =  " insertar en valores de temperatura ( "  +  str (tiempo) +  " , "  +  str (temperatura) +  " ) "
	# Ejecutar el comando
	cur.execute (comando)
	# Guardar los cambios
	conn.commit ()
	# Cerrar el cursor
	cur.close ()


def  sensarPresion ():
	'' '
	Función que obtiene la presión del sensor bme280 y la almacena
	en la base de datos junto con el tiempo de medición
	'' '
	# Obtener todos los datos del sensor
	datos = bme280.sample (bus, direccion, parametros_calibracion)
	# Obtener presionando
	presion = datos.pressure
	# Redondear presionando a 3 decimales
	presionando =  redondo (presionando, 3 )

	# Imprimir resultado
	print ( " Presion: "  +  str (presion) +  " hPa " )

	# Agregar datos a la base de datos
	# Abrir el cursor para escribir en la BD
	cur = conn.cursor ()
	# Obtener tiempo real
	tiempo =  int (time.time ())
	# Crear comando SQL
	comando =  " insertar en valores de presiones ( "  +  str (tiempo) +  " , "  +  str (presion) +  " ) "
	# Ejecutar el comando
	cur.execute (comando)
	# Guardar los cambios
	conn.commit ()
	# Cerrar el cursor
	cur.close ()


def  sensarHumedad ():
	'' '
	Función que obtiene la presión del sensor bme280 y la almacena
	en la base de datos junto con el tiempo de medición
	'' '
	# Obtener todos los datos del sensor
	datos = bme280.sample (bus, direccion, parametros_calibracion)
	# Obtener humedad
	humedad = datos.humedad
	# Redondear humedad a 3 decimales
	humedad =  redonda (humedad, 3 )

	# Imprimir resultado
	print ( " Humedad: "  +  str (humedad) +  "  % r H " )

	# Agregar datos a la base de datos
	# Abrir el cursor para escribir en la BD
	cur = conn.cursor ()
	# Obtener tiempo real
	tiempo =  int (time.time ())
	# Crear comando SQL
	comando =  " insertar en valores de humedades ( "  +  str (tiempo) +  " , "  +  str (humedad) +  " ) "
	# Ejecutar el comando
	
	cur.execute (comando)
	# Guardar los cambios
	conn.commit ()
	# Cerrar el cursor
	cur.close ()


def  medirTodo ():
	'' '
	Función que mide todo (temperatura, presión, humedad) y lo
	guarda en la BD
	'' '
	sensarTemperatura ()
	sensarHumedad ()
	sensarPresion ()
	imprimir ( "  " )
	

def  mostrarTemperatura ():
	'' '
	Función que muestra el registro histórico de la temperatura usando matplotlib
	'' '
	print ( " Mostrando temperatura ... " )

	# Abrir el cursor para obtener datos de la base de datos
	cur = conn.cursor ()
	# Ejecutar comando para obtener toda la información de la tabla de temperaturas
	cur.execute ( ' select * from temperaturas ' )
	# Recuperar los resultados del SQL
	datos = cur.fetchall ()

	# Crear listas para tener el tiempo y temperatura en arreglos individuales
	tiempo = []
	temperatura = []
	para dato en datos:
		tiempo.append (dato [ 0 ])
		temperatura.append (dato [ 1 ])

	# Armar gráfica
	plt.plot (tiempo, temperatura)
	# Mostrar gráfica
	plt.show ()


def  mostrarPresion ():
	'' '
	Función que muestra el registro histórico de la presión usando matplotlib
	'' '
	print ( " Mostrando presion ... " )

	# Abrir el cursor para obtener datos de la base de datos
	cur = conn.cursor ()
	# Ejecutar comando para obtener toda la información de la tabla de presiones
	cur.execute ( ' select * from presiones ' )
	# Recuperar los resultados del SQL
	datos = cur.fetchall ()

	# Crear listas para tener el tiempo y presionar en arreglos individuales
	tiempo = []
	presionando = []
	para dato en datos:
		tiempo.append (dato [ 0 ])
		presion.append (dato [ 1 ])

	# Armar gráfica
	plt.plot (tiempo, presionar)
	# Mostrar gráfica
	plt.show ()

def  mostrarHumedad ():
	'' '
	Función que muestra el registro histórico de la humedad usando matplotlib
	'' '
	print ( " Mostrando humedad ... " )

	# Abrir el cursor para obtener datos de la base de datos
	cur = conn.cursor ()
	# Ejecutar comando para obtener toda la información de la tabla de humedad
	cur.execute ( ' select * from humedades ' )
	# Recuperar los resultados del SQL
	datos = cur.fetchall ()

	# Crear listas para tener el tiempo y la humedad en arreglos individuales
	tiempo = []
	humedad = []
	para dato en datos:
		tiempo.append (dato [ 0 ])
		humedad.append (dato [ 1 ])

	# Armar gráfica
	plt.plot (tiempo, humedad)
	# Mostrar gráfica
	plt.show ()

# Definir interfaz gráfica QT
clase  Ui_MainWindow ( objeto ):
	def  setupUi ( self , MainWindow ):
		MainWindow.setObjectName ( " MainWindow " )
		MainWindow.resize ( 882 , 702 )

		# Ventana principal
		self .centralwidget = QtWidgets.QWidget (MainWindow)
		self .centralwidget.setObjectName ( " centralwidget " )

		# Botón de medir temperatura
		self .botonTemperatura = QtWidgets.QPushButton ( self .centralwidget)
		self .botonTemperatura.setGeometry (QtCore.QRect ( 60 , 90 , 191 , 91 ))
		self .botonTemperatura.setObjectName ( " botonTemperatura " )
		# Mapear ese botón a la función de medición
		self .botonTemperatura.clicked.connect (sensarTemperatura)

		# Botón de medir presionando
		self .botonPresion = QtWidgets.QPushButton ( self .centralwidget)
		self .botonPresion.setGeometry (QtCore.QRect ( 570 , 90 , 191 , 91 ))
		self .botonPresion.setObjectName ( " botonPresion " )
		# Mapear ese botón a la función de medición
		self .botonPresion.clicked.connect (sensarPresion)

		# Botón de medir humedad
		self .botonHumedad = QtWidgets.QPushButton ( self .centralwidget)
		self .botonHumedad.setGeometry (QtCore.QRect ( 310 , 90 , 191 , 91 ))
		self .botonHumedad.setObjectName ( " botonHumedad " )
		# Mapear ese botón a la función de medición
		self .botonHumedad.clicked.connect (sensarHumedad)

		# botón para ver gráfica de temperatura
		self .botonVerTemperatura = QtWidgets.QPushButton ( self .centralwidget)
		self .botonVerTemperatura.setGeometry (QtCore.QRect ( 60 , 240 , 191 , 81 ))
		self .botonVerTemperatura.setObjectName ( " botonVerTemperatura " )
		# Mapear el botón a la función de visualización
		self .botonVerTemperatura.clicked.connect (mostrarTemperatura)

		# botón para ver gráfica de humedad
		self .botonVerHumedad = QtWidgets.QPushButton ( self .centralwidget)
		self .botonVerHumedad.setGeometry (QtCore.QRect ( 310 , 250 , 191 , 81 ))
		self .botonVerHumedad.setObjectName ( " botonVerHumedad " )
		# Mapear el botón a la función de visualización
		self .botonVerHumedad.clicked.connect (mostrarHumedad)

		# botón para ver gráfica de presión
		self .botonVerPresion = QtWidgets.QPushButton ( self .centralwidget)
		self .botonVerPresion.setGeometry (QtCore.QRect ( 570 , 250 , 191 , 81 ))
		self .botonVerPresion.setObjectName ( " botonVerPresion " )
		# Mapear el botón a la función de visualización
		self .botonVerPresion.clicked.connect (mostrarPresion)

		# Crear timer para sensar cada 1 minuto
		self .timer = QtCore.QTimer ( self .centralwidget)
		# Darle un intervalo de 5 segundos
		self .timer.setInterval ( 5000 )
		# Conectar con función de sensado
		self .timer.timeout.connect (medirTodo)
		# Temporizador Empezar
		self .timer.start ()

		# Preparar la ventana (código generador por pyuic5)
		MainWindow.setCentralWidget ( self .centralwidget)
		self .menubar = QtWidgets.QMenuBar (MainWindow)
		self .menubar.setGeometry (QtCore.QRect ( 0 , 0 , 882 , 28 ))
		self .menubar.setObjectName ( " barra de menú " )
		MainWindow.setMenuBar ( self .menubar)
		self .statusbar = QtWidgets.QStatusBar (MainWindow)
		self .statusbar.setObjectName ( " barra de estado " )
		MainWindow.setStatusBar ( self .statusbar)

		self .retranslateUi (MainWindow)
		QtCore.QMetaObject.connectSlotsByName (MainWindow)

	# Función que aplica textos a los botones
	def  retranslateUi ( self , MainWindow ):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle (_translate ( " MainWindow " , " MainWindow " ))

		self .botonTemperatura.setText (_translate ( " MainWindow " , " Temperatura " ))
		self .botonPresion.setText (_translate ( " MainWindow " , " Presion " ))
		self .botonHumedad.setText (_translate ( " MainWindow " , " Humedad " ))
		self .botonVerTemperatura.setText (_translate ( " MainWindow " , " Ver temperatura " ))
		self .botonVerHumedad.setText (_translate ( " MainWindow " , " Ver Humedad " ))
		self .botonVerPresion.setText (_translate ( " MainWindow " , " Ver presión " ))


if  _name_  ==  " _main_ " :
	importación sys
	aplicación = QtWidgets.QApplication (sys.argv)
	MainWindow = QtWidgets.QMainWindow ()
	ui = Ui_MainWindow ()
	ui.setupUi (MainWindow)
	MainWindow.show ()
	sys.exit (app.exec_ ())
