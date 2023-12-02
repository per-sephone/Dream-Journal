from google.cloud import language

def text_analysis(prompt):
    client = language.LanguageServiceClient()
    request = {'document' : {"type_": language.Document.Type.PLAIN_TEXT, "content": prompt}}
    sentiment = client.analyze_sentiment(request).document_sentiment
    if sentiment.score > 0.7:
        return "Joyful dream"
    elif sentiment.score > 0.3:
        return "Happy dream"
    elif sentiment.score > -0.2:
        return "Neutral dream"
    elif sentiment.score > -0.6:
        return "Bad dream"
    elif sentiment.score >= -1.0:
        return "Nightmare"
    else:
        return "Ambiguous dream"