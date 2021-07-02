import PyPDF2
import pyttsx3 as ptxs
import PyPDF2 as pdf
speaker= ptxs.init()
rate = speaker.getProperty('rate')
print(rate)
speaker.setProperty('rate', 150)
book = open('bedtime.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
page = pdfreader.getPage(5)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()