import smtplib,asyncio,time
from email.mime.text import MIMEText

sender="neerajnarn2016@gmail.com"
pw="qhcu giga eafu rqme"
receivers=["neerajnrn2016@gmail.com","ashek8246@gmail.com"]


start=int(time.time())
async def sendmail(subject,body,to,sender,pw):
    try:
        msg=MIMEText(body)
        msg['Subject']=subject
        msg['From']=sender
        msg['To']=', '.join(to)

        server=smtplib.SMTP('smtp.gmail.com',587)

        server.starttls()
        server.login(sender,pw)
        server.sendmail(sender,to,msg.as_string())
        server.quit()

        print('Email sent succesfully')
        
    except Exception as e:
        print(f'Error: {e}')


async def main():
    print('Main started')
    await asyncio.create_task(sendmail('Supppppp','You doing good BRUH!!',receivers,sender,pw))
    print('Main ended')


asyncio.run(main())
print(f'Total time taken= {int(time.time()) - start}')