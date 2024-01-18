import requests
import webbrowser

api_key = "6e0fc6c18abe4b0f83db47a36faa2d74"

def get_news():
    main_url = f"https://newsapi.org/v2/top-headlines?country=ca&category=general&apiKey={api_key}"
    news = requests.get(main_url).json()

    articles = news.get("articles", [])
    news_articles = [{'title': article.get('title', ''), 'url': article.get('url', '')} for article in articles]

    for i, article in enumerate(news_articles[:10], 1):
        print(f"{i}. {article['title']}")

    article_number = int(input("Enter the number of the article you want to read (1-10). Enter 0 if you don't want to read anything. : "))
    
    if 1 <= article_number <= 10:
        webbrowser.open(news_articles[article_number - 1]['url'])
    elif article_number == 0:
        exit()
        

get_news()
