prompt="""you need to provide summarize for
article transcript without gender bias and return important poins as
bullet points.here is my transcript:"""
def get_response(url):
    from newspaper import Article
    from libraries import model
    article = Article(url)
    article.download()
    article.parse()
    text=article.text
    response=model.generate_content(prompt+text)
    return response.text
