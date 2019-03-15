import smtplib

def send(id):

    receiver = 'receiver mail'
    sender = 'sender mail'
    sender_pass = 'sender password'
    message = "You have a todo in your schedule."
    
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587) 
  
        s.starttls() 
        s.login(sender, sender_pass)         
        s.sendmail(sender, receiver, message) 
        s.quit()   

        print ("Successfully sent email")
    except Exception as e:
        print ("Error: unable to send email")


def sendAll(todos):

    receiver = 'receiver mail'
    sender = 'sender mail'
    sender_pass = 'sender password'
    message = "You have a todos in your schedule."
    
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587) 
  
        s.starttls() 
        s.login(sender, sender_pass)         
        s.sendmail(sender, receiver, message) 
        s.quit()   

        print ("Successfully sent email")
    except Exception as e:
        print ("Error: unable to send email")
