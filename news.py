import requests 
import webbrowser 

api_key = "6e0fc6c18abe4b0f83db47a36faa2d74"

def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=ca&category=general&apiKey="+api_key
    news= requests.get(main_url).json()
    #print(news)
    article = news["articles"]  
    # print(article) 
    
    
    news_article= []
    for arti in article:
        news_article.append(arti['title'])
        #print(news_article)
    for i in range(10):
        print(news_article[i])
        

news()