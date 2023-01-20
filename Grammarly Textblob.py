# import TextBlob
from textblob import TextBlob
ina = input("Enter a string : ")
str = TextBlob(ina)

# using TextBlob.correct() method
str = str.correct()
print(str)

from translate import Translator
translator= Translator(to_lang="Spanish")
translation = translator.translate(ina)
print(translation)