import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')


def clean_text(text: str) -> str:
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)

    # Filter out stopwords and punctuation
    cleaned_text = ' '.join([word for word in word_tokens if word.isalpha() and word.lower() not in stop_words])

    return cleaned_text
