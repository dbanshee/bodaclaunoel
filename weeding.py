#! /usr/bin/python
# -*- coding: utf-8 -*-

import os,stat
from flask import Flask,render_template,request,abort,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import smtplib
import sys, traceback
#from email.message import EmailMessage
import config
import sys
reload(sys)
sys.setdefaultencoding('utf8')


from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.mime.image import MIMEImage


class LoginForm(FlaskForm):    
    username = StringField('Invitado')
    acompanante = BooleanField('Acompanante')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Confirmar')

app = Flask(__name__,static_url_path='')


@app.route('/flash')
def flash(message):
  message = request.args.get("msg")
  return render_template("flash.html", msg=message)

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def main():
  
  if request.method == "POST":
    nombre=request.form["nombre"]
    acompanante=request.form["acompanante"]
    ninos=request.form["ninos"]
    consulta=request.form["consulta"]
    email=request.form["email"]
    bus=request.form["bus"]
    
    
    
    print('Confirmada asistencia para Nombre: {}, acompanante: {}, ninos: {}, email: {}, bus : {}'.format(nombre, acompanante, ninos, email, bus))
  
    try:
      # Send mail
      to = config.to
      
      
        
      
      gmail_user = config.gmail_user 
      gmail_pwd = config.gmail_pwd
      smtpserver = smtplib.SMTP("smtp.gmail.com",587)
      smtpserver.ehlo()
      smtpserver.starttls()
      smtpserver.login(gmail_user, gmail_pwd)
      header = 'To:' + ", ".join(to) + '\n' + 'From: ' + gmail_user + '\n'
      if email is not None:
        header=header+'CC: {}\n'.format(email)
      
      header=header+'Subject:[BODA CLAUNOEL - Invitacion Confirmada] {}\n'.format(nombre)
      
      
      
      msg = """
                                                             _                             _                            
            /' `\                    /'              /' `\    /'                    ' )    )                    /'
          /'     )                 /'              /'   ._) /'                      //   /'                   /'  
        /' (___,/'____     _____,/' ____         /'       /' ____                 /'/  /' ____     ____     /'    
      /'     )  /'    )--/'    /' /'    )      /'       /' /'    )  /'    /     /' / /' /'    )--/'    )  /'      
    /'      /'/'    /' /'    /' /'    /'     /'       /' /'    /' /'    /'    /'  //' /'    /' /(___,/' /'        
(,/' (___,/' (___,/'  (___,/(__(___,/(__    (_____,/'(__(___,/(__(___,/(__(,/'    (_,(___,/'  (________(__        
                                                                                                                  
        
  OLE OLE Y OLE! 
  Nueva Confirmacion realizada
 
  -------------------------------------------------------
   Nombre        : {} 
   Acompanante   : {}
   Ninos         : {}
   Bus           : {}
   Consulta      : {}
   email         : {}
  -------------------------------------------------------
  
      
          ---@@@@@@@-------------@@@@@@!**
    --@@@@!!!!!;;-.;..@------@...............::;!@**
    '@@@!!!!!!!;;;;;;;.....;@@.................:;;;;;;!@**
    @@@!!!!!!!;;;;;;:::.......................:;;;;;;;;;!@** 
    -@@!!!!;;::::....................................;;:;!@** 
    --@@!!:;;:::...................................;:;!@** 
    ---@!!!!;::: :::..................................@** 
    ------!!!!!;:::::::::..........................@** 
    ----------!!!;;:::::::..:::::..........@** 
    -------------:::::::::::...........@** 
    ----------------::::::::.......@** 
    -------------------:::::..@** 
    ----------------------..@** 
    ----------------------.!
    ----------------------.*
    ----------------------.*
    ---------------------.*
    ----------------------.*
    -----------------------.* 
    ------------------------.* 
    -------------------------.*


  """.format(nombre, acompanante, ninos, bus, consulta, email)
      
      toaddrs = to
      if email is not None:
        toaddrs = to + [email]
      
      
      #smtpserver.sendmail(gmail_user, toaddrs, header + msg)
      #smtpserver.close()
      
      
      outer = MIMEMultipart('related')
      outer['From'] = gmail_user
      outer['To'] = ", ".join(toaddrs)
      outer['CC'] = email
      outer['Subject'] = '[BODA CLAUNOEL - Invitacion Confirmada] {}\n'.format(nombre)
      
      #body = MIMEText(msg) # convert the body to a MIME compatible string
      #outer.attach(body)
      
      
      msgAlternative = MIMEMultipart('alternative')
      outer.attach(msgAlternative)
      
      # We reference the image in the IMG SRC attribute by the ID we give it below
      
      
      htmlMsg="""
        <html>
          <body>
            <img src="cid:image1">
            <br/>
            <br/>
            <br/>
            <br/>
            <i><b>Invitacion Confirmada</b></i>
            <br/>
            <br/>
            Muchas gracias por compartir con nosotros una noche tan especial. 
            <br/>
            Esperamos que te diviertas y te contagies de nuestra felicidad y buen ambiente.
            <br/>
            <br/>
            <br/>
            <b> Nombre :</b> <i>{}</i>
            <br/>
            <b> Acompanante :</b>  <i>{}</i>
            <br/>
            <b> Ninos :</b> <i>{}</i>
            <br/>
            <b> Bus :</b> <i>{}</i>
            <br/>
            <b> Consulta :</b> <i>{}</i>
            <br/>
            <b> email :</b> <i>{}</i>
            <br/>
            <br/>
            <br/>
            <i>Nos vemos el dia <b>23 de Junio</b> a las <b>21:00</b> en <a href="https://goo.gl/maps/dv7HdHYoKaN2"><b>El Hornillero</b></i></a>
            <br/>
            <br/>
            <br/>
            <br/>
            Recuerda que tienes toda la información necesaria en 
            <a href="http://claunoel.cyberlove.us/">http://claunoel.cyberlove.us/</a>
            <br/>
            o puedes llamarnos si necesitas cualquier cosa.
            <br/>
            <br/>
            <i>Claudia :</i> <a href="tel:644-340-248"><b>644340248</b></a>
            <br/>
            <i>Oscar Noel :</i> <a href="tel:665-144-704"><b>665144704</b></a>
            <br/>
          <body>
        <html>
        """.format(nombre, acompanante, ninos, bus, consulta, email)
      
      
      msgText = MIMEText(htmlMsg, 'html')
      msgAlternative.attach(msgText)
      
      # This example assumes the image is in the current directory
      fp = open('static/img/intro-bg.jpg', 'rb')
      msgImage = MIMEImage(fp.read())
      fp.close()
      msgImage.add_header('Content-ID', '<image1>')
      msgImage.add_header('Content-Disposition', 'inline', filename='intro-bg.jpg')
      outer.attach(msgImage)
      
      composed = outer.as_string()
      smtpserver.sendmail(gmail_user, toaddrs, composed)
      smtpserver.close()
      
    except:
      print('Error enviando mail')
      traceback.print_exc(file=sys.stdout)
      #return render_template('flash.html', message='Error enviando confirmacion\nPor favor intentelo de nuevo.')
      return render_template('index.html')
    
    #msg="Asistencia confimada! Gracias por venir: {}".format(form.username.data)
    #return render_template('flash.html', message=msg)
    return render_template('index.html')
  
  
  return render_template('index.html')

if __name__ == '__main__':
  
  sys.setdefaultencoding('utf8')
  app.debug = True
  app.config['SECRET_KEY'] = 'you-will-never-guess'
  app.run(host='0.0.0.0',port=5000)
