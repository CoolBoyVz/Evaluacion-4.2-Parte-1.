# Visualización de Datos X-Y con Flask

### NOMBRE: Marco Dugarte.-

## Descripción
Proyecto para la Evaluación Sumativa 4.2 de la asignatura Desarrollo de Software para Hardware (DCSH01).

## Objetivo
El sistema recibe datos X e Y desde una aplicación móvil (APK) mediante una conexión TCP, y los representa visualmente en tiempo real en una página web utilizando Flask.

## Características Técnicas y Explicación del Código
* **Flask (Python):** Desarrollado con Python y Flask. Se utiliza la librería `socket` para actuar como cliente TCP y obtener las coordenadas del giroscopio del celular.
* **Lógica Dinámica (Jinja):** Se utiliza el motor de plantillas Jinja2 ( `{% if %}`, `{% for %}`, y variables `{{ }}`) directamente en el HTML. Esto permite procesar matemáticamente las coordenadas recibidas e asignar IDs dinámicos para mover los elementos en pantalla.

## Etapa 2: Vistas de Creatividad Personal
Se implementó un menú de navegación en HTML que conecta 3 pestañas con representaciones visuales distintas:
1. **Vista Principal (`/`):** Se implementó una matriz de 4x4. Usando Jinja, se mapean los rangos del sensor para activar dinámicamente el ID de la celda correspondiente y pintarla de rojo.
2. **Vista Radar (`/vista2`):** Diseño de retícula de radar donde un punto objetivo se desplaza libremente en un plano 2D.
3. **Vista Indicadores (`/vista3`):** Visualización de magnitudes a través de barras de progreso horizontales cuyo ancho varía porcentualmente según la intensidad de cada eje.

## Instrucciones de Ejecución
1. Iniciar la aplicación móvil y tomar nota de la IP del "Servidor TCP".
2. En el archivo `app.py`, modificar la variable `HOST` con la IP entregada por la aplicación. (Importante: La I:P seleccionada debe ser cambiada debido a que esta funciona solo con la IP de mi hogar)
3. Ejecutar el servidor web mediante el comando en el terminal de la maquina virtuañ: `python3 app.py`
4. Acceder desde el navegador a la IP local de la máquina virtual/host en el puerto 5000 (Ej: `http://localhost:5000` o la IP correspondiente de la red).

Aqui un Kirby para toque personal:
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣤⠤⠤⠴⠤⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠲⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⢀⣄⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⣾⣠⠎⠀⣸⠁⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⠃⣾⣿⡏⠀⢰⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⠷⠻⠟⠀⠀⠸⣿⠏⠀⠀⢠⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀
⢠⡴⢦⣤⣄⠀⡇⠀⠀⠀⢰⣶⣶⡄⠀⠀⠀⠈⠛⠛⠯⠿⠃⠀⠀⠀⠀⠀⠀⢸⡘⠀⠀
⢸⣹⢿⣾⣹⢿⣿⠀⠀⠀⠀⠹⠏⠀⠀⠀⠀⠀⠀⠀⣀⣶⣆⣀⠀⠀⠀⠀⠀⠀⣿⡀⠀
⠘⣭⢷⣫⡽⣯⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢶⣻⠽⣶⣫⣟⣷⡄⠀⠀⠀⠀⠘⢖⡀
⠀⠘⣯⢷⣻⣽⣻⣿⡄⠀⠀⠀⠀⠀⠀⢀⣼⣳⣻⢞⣟⣳⡽⣞⣳⢿⡀⠀⠀⠀⠀⠘⣡
⠀⠀⠈⢯⢷⣞⣷⣻⣿⣄⠀⠀⠀⠀⢠⣿⣳⡽⣳⣟⣾⡳⣿⠽⣯⣟⣧⠀⠀⠀⠀⠀⠸
⠀⠀⠀⠀⠙⢞⣾⣳⢿⣿⣷⢤⠀⠈⢿⣳⣳⢟⣳⡽⣶⣻⣽⡻⣗⣯⠷⡄⠀⠀⠀⠀⡬
⠀⠀⠀⠀⠀⠀⠱⢏⣿⡿⠁⠀⠉⠶⣸⣷⢏⡿⣷⢿⢷⡿⣶⢿⣹⡎⠁⠈⠳⠶⠶⠊⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠫⣿⣝⡷⣯⠿⣝⣯⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
