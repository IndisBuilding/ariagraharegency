from email.mime.image import MIMEImage
from kirimemail import kirim

toaddr = ['faicanhas@gmail.com','Lina.indrawati@ymail.com','tetty.tjandrawati@yahoo.com']
#toaddr = ['okyzaprabowo@gmail.com','wahyuputrarama@gmail.com','ceceraraa@gmail.com','faicanhas@gmail.com']
subjectmail = "Pemberitahuan dari Ruko Cipamokolan"
body = "Peringatan! Pintu rumah Anda terbuka!"

kirim(toaddr, subjectmail, body)
