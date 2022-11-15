from flask import Flask, request, render_template, url_for, jsonify, session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)

app.secret_key = b'LLAVE_SECRETA'


@app.route('/')
def main():

    if 'username' in session:
        return f'El usuario ya ha hecho login {session["username"]}'
    else:
        return redirect(url_for('login'))

    # app.logger.debug('Mensaje a nivel debug')
    app.logger.info(f'Entramos al path: {request.path}')
    # app.logger.warning('Mensaje a nivel warning')
    # app.logger.error('Mensaje a nivel error')

    return 'Hola mundo desde flask.'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        # session['password'] = request.form['username']
        return redirect(url_for('main'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    try:
        session.pop('username')
    except Exception as e:
        return redirect(url_for('main'))
    return redirect(url_for('main'))

@app.route('/saludar/<nombre>')
def saludar(nombre=''):
    return f'Saludos {nombre.capitalize()}'

@app.route('/edad/<int:edad>')
def edad(edad):
    return f'Edad: {edad:.1f}'

@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar_nombre', nombre='Martín'))

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html', error=error), 404

# REST Representational state transfer
@app.route('/api/mostrar/<nombre>', methods=['GET', 'POST'])
def api_mostrar_json(nombre):
    valores = {'nombre': nombre, 'method': request.method}
    return jsonify(valores)
