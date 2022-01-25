import smtplib

email = ""
password = ""

to_addresses  = ["ian.holl@ndow.org"]
body = "I sent this with Python"

header = ("From: {}\r\nTo: {}\r\n\r\n".format(email, ", ".join(to_addresses)))
message = header + body

server = smtplib.SMTP(host="smtp-mail.outlook.com", port=587)
server.starttls()
server.login(email, password)
print("Server started and ready")

server.set_debuglevel(1)
server.sendmail(email, to_addresses, message)
server.quit()
print("Complete")