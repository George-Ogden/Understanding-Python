import pdfkit
from glob import glob

# pdfkit.from_url("https://google.com","out.pdf")
# pdfkit.from_file("snake.html","out.pdf")
# pdfkit.from_string("<h1>This works!</h1>","out.pdf")

options = {
    "margin-top" : "0",
    "margin-bottom" : "0",
    "margin-right" : "0",
    "margin-left" : "0",
    "orientation" : "landscape"
}

pdfkit.from_file(glob("*.html"),"out.pdf",options=options,cover="cover.htm",verbose=True)