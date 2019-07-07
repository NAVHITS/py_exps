import smtplib
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.starttls()
#Mail ID and password removed
mail.login("test@gmail.com", "test123")
message = "Python mail test with smtplib package"
mail.sendmail("sender_email_id", "receiver_email_id", message)
mail.quit() 