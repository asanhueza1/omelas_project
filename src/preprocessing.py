import re
import string
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

def remove_numbers(text):
    '''Removes integers'''
    text = ''.join([i for i in text if not i.isdigit()])
    return text

def remove_punctuation(text):
    # TODO: we might want to just eliminate periods in BOW. this will help
    # find toxic words masked by punctuation
    text = re.sub("[-]", ' ', text) # certain punctuations should be replaced with space
    text = re.sub("[%s]" % re.escape(string.punctuation), '', text)
    # text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    return text

def text_lowercase(text):
    return text.lower()

def strip_whitespace(text):
    text = " ".join(text.split())
    return text

def remove_stopwords(text, lan='english'):

    if lan == 'english':
        sp_en = set(stopwords.words('english'))
        words_tokens = word_tokenize(text)
        text = [i for i in words_tokens if i not in sp_en]
        text = ' '.join(text)

    else:
        print('''Could not remove stopwords. Please specify a language.
        Only available in English or Spanish''')
        return

    return text

def apply_stemming(text, lan):

    if lan == 'english':
        stemmer_en = SnowballStemmer('english')
        words_tokens = word_tokenize(text)
        text = [stemmer_en.stem(i) for i in words_tokens]
        text = ' '.join(text)
    else:
        print('Stemmer only available in english or spanish')
        return

    return text

def apply_lemmatizer(text):
    wordnet_lemmatizer = WordNetLemmatizer()
    lemm_text = []
    for word in text.split():
        lemm_text.append(wordnet_lemmatizer.lemmatize(word))

    return " ".join(lemm_text)



def clean_text(text, punctuation=True, numbers=True, lowercase=True,
          whitespace=True, lan = 'english', stopwords = True,
          lemmatize=True, stemming = True):

    if stopwords:
        text = remove_stopwords(text, lan = lan)

    if punctuation:
        text = remove_punctuation(text)

    if numbers:
        text = remove_numbers(text)

    if lowercase:
        text = text_lowercase(text)

    if whitespace:
        text = strip_whitespace(text)

    if lemmatize:
        text = apply_lemmatizer(text)

    if stemming:
        text = apply_stemming(text, lan = lan)

    return(text)
