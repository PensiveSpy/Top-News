import requests 
import webbrowser 

api_key = ""

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
