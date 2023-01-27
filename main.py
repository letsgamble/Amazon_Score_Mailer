import os
from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart(boundary='')
msg.add_header('X-Unsent', '1')
msg['Subject'] = 'Your individual performance'
msg['From'] = 'kawesolo@amazon.pl'
msg['To'] = 'abc@abc.pl'
msg['Cc'] = '...'

with open('template.html', 'r') as file:
    html_data = file.read()
part = MIMEText(html_data, 'html')
msg.attach(part)


outfile_name = os.path.join("email_sample.msg")
with open(outfile_name, 'w') as outfile:
    gen = generator.Generator(outfile)
    gen.flatten(msg)
