import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from thingspeakVeriCekme import bilgileriDondur

mesaj=MIMEMultipart()
mesaj['from']="mert.erd.apa.proje@gmail.com"
mesaj['to']="umutsezer3353@gmail.com"
mesaj['subject']="Nesnelerin İnterneti Ve Uygulamaları Proje Ödevi"

yazi=bilgileriDondur()

mesaj_yapisi=MIMEText(yazi,'plain')
mesaj.attach(mesaj_yapisi)

def mailGonder(to):
    try:
        mail=smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('mert.erd.apa.proje@gmail.com','123012301230asd')
        mail.sendmail(mesaj['from'],to,mesaj.as_string())
        print ('Mail gönderildi')
        mail.close()
    except:
        print('hata oluştu')    