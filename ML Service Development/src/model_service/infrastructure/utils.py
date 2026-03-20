import nltk


# Initialize ML requirements
def download_nltk():
    nltk.download("punkt")
    nltk.download("wordnet")
    nltk.download("stopwords")
    nltk.download("averaged_perceptron_tagger_eng")
    nltk.download("punkt_tab")
