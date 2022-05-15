from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

import json
import os

with open("settings.json") as file:
    settings = json.load(file)

SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]

creds = None
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", 
            SCOPES)
        creds = flow.run_local_server(port=0)

    with open("token.json","w") as token:
        token.write(creds.to_json())
service = build("gmail","v1",credentials=creds)

with open("email.html",encoding="utf-8") as file:
    message = MIMEText(file.read(),"html")

message["To"] = settings["receiver"]
message["From"] = service.users().getProfile(userId="me").execute()["emailAddress"]
message["Subject"] = "Python Test Email"

encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
service.users().messages().send(userId="me",body = {"raw" : encoded_message}).execute()