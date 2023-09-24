import wikipedia
user_search = input("Input page title / Search phrase \n>>>")


while user_search != '':
    print('Search :',wikipedia.search(user_search))
    try:
        print('Summary :', wikipedia.summary(user_search))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)

    try:
        print('Page :', wikipedia.page(user_search, auto_suggest=False))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    user_search = input("Input page title / Search phrase \n>>>")