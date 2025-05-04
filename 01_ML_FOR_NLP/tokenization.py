corpus = """
Hello welcome to the world of NLP.
I am learning NLP today.
please subscribe to my channel.
"""

# convert paragraph --> sentencs
import nltk
nltk.download('punkt_tab')


from nltk.tokenize import sent_tokenize
sent_tokenizer = sent_tokenize(corpus)

print("sentences tokenize ",sent_tokenizer) 

from nltk.tokenize import word_tokenize
print("tokenize every word fullstop also ",word_tokenize(corpus))


from nltk.tokenize import wordpunct_tokenize
print("tokenize every word fullstop also usgin punct lib ",wordpunct_tokenize(corpus))

from nltk.tokenize import TreebankWordTokenizer
# tokenizer = TreebankWordTokenizer()
print("tokeinzing using tokenizer ",TreebankWordTokenizer().tokenize(corpus))



# convert paragraph --> word
# word_tokenizer = word_tokenize(corpus)

# print(word_tokenizer)

  

