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
    
    print('Confirmada asistencia para Nombre: {}, acompanante: {}, ninos: {}, email: {}'.format(nombre, acompanante, ninos, email))
  
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
        header=header+'cc: {}\n'.format(email)
      
      header=header+'Subject:[TEST BODA CLAUNOEL - Nueva confirmacion] {}\n'.format(nombre)
      
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
   Consulta      : {}
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


  """.format(nombre, acompanante, ninos, consulta)
      
      smtpserver.sendmail(gmail_user, to, header + msg)
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
  app.debug = True
  app.config['SECRET_KEY'] = 'you-will-never-guess'
  app.run(host='0.0.0.0',port=5000)
