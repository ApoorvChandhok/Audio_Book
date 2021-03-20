import pyttsx3
import PyPDF2
 
book = open('opp.pdf', 'rb')  # reading as binary book
Reader = PyPDF2.PdfFileReader(book)
pages = Reader.numPages
print(pages)
speaker = pyttsx3.init()
page = Reader.getPage(2)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
