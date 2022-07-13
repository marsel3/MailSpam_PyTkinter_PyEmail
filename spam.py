import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *

screen = Tk()

screen.resizable(width=False, height=False)
screen.geometry('410x230')
screen.title('Spam to mail')


def send_mail( event ):
    login_email = login.get()
    password_email = password.get()
    to_email = toaddr.get()
    tittle = topic.get()
    message = mess.get()
    count_message = int(number.get())

    for to in range(count_message):
        msg = MIMEMultipart()
        msg['Subject'] = tittle
        msg['From'] = login_email
        body = message
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(login_email, password_email)
        server.sendmail(login_email, to_email, msg.as_string())
        server.quit()
        result['text'] = 'x' + str(to)


Tlogin = Label(text='Почта отправителя:', font='Consolas')
login = Entry(screen, font='Consolas')

Tpassword = Label(text='Пароль от почты:', font = 'Consolas' )
password = Entry(screen, font='Consolas', show='*')

Turl = Label(text='URL (gmail.com / mail.ru):', font='Consolas')
url = Entry(screen, font='Consolas')

Ttoaddr = Label(text='Почта получателя:', font='Consolas' )
toaddr = Entry(screen, font='Consolas')

Ttopic = Label(text='Заголовок письма:', font='Consolas')
topic = Entry(screen, font='Consolas')

Tmess = Label(text='Сообщение:', font='Consolas')
mess = Entry(screen, font='Consolas')

Tnumber = Label(text='Количество сообщений:', font='Consolas')
number = Entry(screen, font='Consolas')

enter = Button( text = 'Send', font = 'Consolas', width = 18 )

result = Label( text = 'Result:', font = 'Consolas' )

# Packers
Tlogin.grid(row=0, column=0, sticky = W, padx = 1, pady = 1 )
login.grid(row=0, column=1, padx = 1, pady = 1 )

Tpassword.grid( row = 1, column = 0, sticky = W, padx = 1, pady = 1 )
password.grid( row = 1, column = 1, padx = 1, pady = 1 )

Turl.grid( row = 2, column = 0, sticky = W, padx = 1, pady = 1 )
url.grid( row = 2, column = 1, padx = 1, pady = 1 )

Ttoaddr.grid( row = 3, column = 0, sticky = W, padx = 1, pady = 1 )
toaddr.grid( row = 3, column = 1, padx = 1, pady = 1 )

Ttopic.grid( row = 4, column = 0, sticky = W, padx = 1, pady = 1 )
topic.grid( row = 4, column = 1, padx = 1, pady = 1 )

Tmess.grid( row = 5, column = 0, sticky = W, padx = 1, pady = 1 )
mess.grid( row = 5, column = 1, padx = 1, pady = 1 )

Tnumber.grid( row = 6, column = 0, sticky = W, padx = 1, pady = 1 )
number.grid( row = 6, column = 1, padx = 1, pady = 1 )

enter.grid( row = 7, column = 0, padx = 1, pady = 1 )

result.grid( row = 7, column = 1, padx = 1, pady = 1 )

# Bind
enter.bind('<Button-1>', send_mail)

# The end
screen.mainloop()

