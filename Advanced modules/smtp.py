import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

email = input("Please enter the your e-mail adresses. The e-mail will be send from this adress.")
password = input("Please enter the password of sender e-mail adress.")
subject = input("Please enter e-mail subject")
mail_content = input("Please enter the conctent of the mail.")

e_mail_list = []
print("""
    Please enter reciever e-mail adresses

    When you finish adding e-mail adresses just press "q" and "enter"

    """)
while True:
    newemail = input("Enter the e-mail adress")
    if newemail == "q" :
        break
    else:
        e_mail_list.append(newemail)

for i in e_mail_list:


    message = MIMEMultipart()

    message["From"] = email

    message["To"] = i

    message["subject"] = subject


    message_body = MIMEText(mail_content,"plain")

    message.attach(message_body)

    try:
        mail = smtplib.SMTP("smtp.gmail.com",587) # this creates a smtb object
                                                  # 587 is related with G-mail.
        # To connect ;
        mail.ehlo()

        mail.starttls()

        mail.login(email,password)

        mail.sendmail(message["From"],message["To"],message.as_string())

        print("E-mail is successfuly sent")

        mail.close()

    except:
        sys.stderr.write("An error occured")
        sys.stderr.flush()

