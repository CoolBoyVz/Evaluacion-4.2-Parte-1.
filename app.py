from flask import Flask, render_template
import socket

app = Flask(__name__)
HOST = "192.168.1.81"    ## Ip del servidor
PORT = 12345        ## Puerto del servidor

def leer_sensor():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            data = s.recv(1024).decode().strip()
            print("RECIBIDO:", data)
            ejeX, ejeY = data.split(',')
            ejeX = float(ejeX.replace('X:', ''))
            ejeY = float(ejeY.replace('Y:', ''))
            return ejeX, ejeY
    except Exception as e:
        print("ERROR:", e)
        return 0, 0

# --- Pestaña 1: Principal ---
@app.route('/')
def index():
    ejeY, ejeX = leer_sensor()
    return render_template('index.html', ejeX=ejeX, ejeY=ejeY)

# --- Pestaña 2: Vista Creativa 1 ---
@app.route('/vista2')
def vista2():
    ejeY, ejeX = leer_sensor()
    return render_template('vista2.html', ejeX=ejeX, ejeY=ejeY)

# --- Pestaña 3: Vista Creativa 2 ---
@app.route('/vista3')
def vista3():
    ejeY, ejeX = leer_sensor()
    return render_template('vista3.html', ejeX=ejeX, ejeY=ejeY)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
