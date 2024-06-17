from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    #return "Hola Masterizado!"
    #data={
    #    'titulo':'Index',
    #   'bienvenida':'Saludos!'
    #}
    #return render_template('index.html', data=data)
    return render_template('index.html', 
                           panel_admin_url='Panel_administrador.html', 
                           crear_cuenta_url='Crear_cuenta.html',
                           image_url='/app/static/img/back.png')


if __name__== '__main__':
    app.run(debug=True, port=1997)
