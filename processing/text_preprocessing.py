
import re
from nltk.corpus import stopwords

stop_words = stopwords.words("english")

def preprocess(text, remove_stop_words = False):
    # remove link
    text = re.sub(r"(http?\://|https?\://|www)\S+", " ", str(text).lower()).strip()
    # remove newlines
    text = re.sub(r'\n', ' ', text)
    # remove puctuations and special characters
    text = re.sub(r'\W+', ' ', text)
    # Substituting multiple spaces with single space
    text = re.sub(r'\s+', ' ', text, flags=re.I)
    # remove first space
    text = re.sub(r'^\s+', '', text)
    # Removing prefixed 'b'
    text = re.sub(r'^b\s+', '', text)
    
    if remove_stop_words:
        tokens = []
        for token in text.split():
            if token not in stop_words:
                tokens.append(token)
        return(" ".join(tokens))
    else:
        return(text)