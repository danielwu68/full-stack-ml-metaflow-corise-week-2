import string
import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('vader_lexicon')

def normalize_word(word: str) -> str:
    if word is None: return ''
    return word.lower().translate(str.maketrans('', '', string.punctuation))


def nltk_stopwords_eng():
    words = [normalize_word(w) for w in list(nltk.corpus.stopwords.words("english"))]
    for new_word in [ "I'm", "You're", "he's" ]:
        new_word = normalize_word(new_word)
        if new_word not in words:
            print("adding new word:", new_word)
            words.append(new_word)
    return set(words) - {'not', 'no', 'nor'}


class NlHelper:
    NLTK_STOPWORDS = nltk_stopwords_eng()

    @staticmethod
    def tokenize(text: str, stopwords_list = NLTK_STOPWORDS):
        return [t for t in normalize_word(text).split() if t.isalpha() and t not in stopwords_list]

    @staticmethod
    def normalize_text(text, stopwords_list = NLTK_STOPWORDS):
        return " ".join(NlHelper.tokenize(text))
    

if __name__ == '__main__':
    print("NLTK_STOPWORDS:", NlHelper.NLTK_STOPWORDS)
