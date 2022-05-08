from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from smtplib import SMTP

from pathlib import Path
import json

with open("settings.json") as file:
    settings = json.load(file)

message = MIMEMultipart()
message["From"] = settings["username"]
message["To"] = settings["receiver"]
message["Subject"] = "Python Test Email"

with open("email.html",encoding="utf-8") as file:
    message.attach(MIMEText(file.read(),"html"))

if "attachment" in settings.keys():
    part = MIMEBase("application", "octet-stream")
    with open(settings["attachment"],"rb") as file:
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; filename=" + Path(settings["attachment"]).name)
        message.attach(part)

with SMTP(host=settings["server"],port=settings["port"]) as s:
    s.starttls()
    s.login(settings["username"],settings["password"])
    s.send_message(message)