from keybert import KeyBERT
import os


def extract_keywords(text: str, nb_keywords: int) -> str:
    """
    Extracts keywords from a text


    Parameters
    ----------
    text : str
        The text we want to extract keywords from
    nb_keywords : int
        Number of keywords extracted

    Returns
    -------
    str
        A string containing the keywords extracted from the text, separated by a space

    """
    kw_model = KeyBERT()

    keywords = kw_model.extract_keywords(
        text, keyphrase_ngram_range=(1, 1), top_n=nb_keywords)

    res = ""
    for tuple in keywords:
        res = res + tuple[0] + " "

    return res





