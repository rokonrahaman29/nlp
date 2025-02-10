import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK stopwords data if not already present.  This prevents repeated downloads.
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')


def remove_stopwords(text, language):
    try:
        # Tokenize the input text into words
        words = word_tokenize(text)

        # Get the list of stopwords.  Lowercase the language code.
        stop_words = set(stopwords.words(language.lower()))

        # Remove stopwords from the list of words
        filtered_words = [word for word in words if word.lower() not in stop_words]

        # Join the filtered words to form the cleaned text
        cleaned_text = ' '.join(filtered_words)
        return cleaned_text
    except LookupError:
        print(f"Error: Stopwords for '{language}' not found. Please download the corresponding NLTK resource.")
        return text  #Return the original text if stopwords aren't available.


# Example text in various languages
english_text = "This is an example sentence in English."
spanish_text = "Este es un ejemplo de frase en español."
french_text = "Ceci est un exemple de phrase en français."
german_text = "Dies ist ein Beispiel für einen Satz in Deutsch."
italian_text = "Questo è un esempio di frase in italiano."


english_result = remove_stopwords(english_text, 'english')
spanish_result = remove_stopwords(spanish_text, 'spanish')
french_result = remove_stopwords(french_text, 'french')
german_result = remove_stopwords(german_text, 'german')
italian_result = remove_stopwords(italian_text, 'italian')

print("English:", english_result)
print("Spanish:", spanish_result)
print("French:", french_result)
print("German:", german_result)
print("Italian:", italian_result)
