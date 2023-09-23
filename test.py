import pywhatkit


contact = takeCommand()
message = takeCommand()
pywhatkit.sendwhatmsg(contact, message)
