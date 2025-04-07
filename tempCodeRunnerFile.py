    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender,pw)

        message=f'Subject : {subject}\n\n{body}'
        server.sendmail(sender,receiver,message)

        server.quit()
        print('Email sent succesfully')
        
    except Exception as e:
        print(f'Error: {e}')