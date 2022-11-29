english_news_subscribers = int(input())
roll_no_english_news_subscribers = input()
french_news_subscribers = int(input())
roll_no_french_news_subscribers = input()

list_english_news_subscribers = set()
list_french_news_subscribers = set()

# splitting roll nos, converting to integers and appending to list_english_news_subscribers
for _ in roll_no_english_news_subscribers.split():
    list_english_news_subscribers.add(int(_))

# splitting roll nos, converting to integers and appending to list_french_news_subscribers
for _ in roll_no_french_news_subscribers.split():
    list_french_news_subscribers.add(int(_))

# print the number of subscribers who have atleast one subscription
no_of_subscribers = list_english_news_subscribers & list_french_news_subscribers
print(len(no_of_subscribers))
