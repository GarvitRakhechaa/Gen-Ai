words = ["eating" ,"eats" , "eaten" , "writing" , "writes " , "programming" , "programs", "history","finally","finallize","fairly", "sportingly"] 

# porter stemming

import nltk
from nltk.stem import PorterStemmer

stemming = PorterStemmer()
for word in words:
    print(word,"-------->",stemming.stem(word))

# regex stemmer
from nltk.stem import RegexpStemmer

reg_stemmer = RegexpStemmer('ing$|s$|e$|able$|ion$', min=4)
print(reg_stemmer.stem('congratulation'))

# Snowball Stemmer
from nltk.stem import SnowballStemmer
SnowballStemmmer=SnowballStemmer("english")
for word in words:
    print(word,"-------->",SnowballStemmmer.stem(word))
    

