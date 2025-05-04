import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

words = ["eating" ,"eats" , "eaten" , "writing" , "writes " , "programming" , "programs", "history","finally","finallize","fairly", "sportingly"] 
lemmatizer = WordNetLemmatizer()

for word in words:
    print(lemmatizer.lemmatize(word, pos="a"))

print(lemmatizer.lemmatize("congratulation", pos="r"))
