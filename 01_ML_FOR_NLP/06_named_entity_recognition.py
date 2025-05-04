sentence="The Eiffel Tower was built from 1887 to 1889 by French engineer Gustave Eiffel, whose company specialized in building metal frameworks and structures."

import nltk

tokenize_words = nltk.word_tokenize(sentence)
print(tokenize_words)
pos_taged_word = nltk.pos_tag(tokenize_words)
print(pos_taged_word)
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
named = nltk.ne_chunk(pos_taged_word)
print(named)
nltk.ne_chunk(pos_taged_word).draw()