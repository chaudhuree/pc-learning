# install textblob and pyttsx3 from pypi.org
import pyttsx3
from textblob import TextBlob

engine = pyttsx3.init()
engine.say('''Hello Employee Number 21783619736. We hope you hadagreat day of work.It's
time to submit your employee wellness statement''')
engine.runAndWait()
print("Enter your employee wellness statement:")
phrase = input(">")
blob = TextBlob(phrase)
while blob.sentiment.polarity < 0.5:
    engine.say('''Employee Number 21783619736,that was notavery positive employee
    wellness statement.Please try again and be more positive this time.We know how
    much you love working here.''')
    engine.runAndWait()
    print("More positive please:")
    phrase = input(">")
    blob = TextBlob(phrase)
print("We appreciate you too!")
engine.say(
    '''Employee Number 21783619736,Thank you for suchakind and positive statement!''')
engine.runAndWait()
