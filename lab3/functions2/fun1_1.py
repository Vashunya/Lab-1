from dictionary import movies

def get_imdb(name):
    for movie in movies:
        if movie['name'] == name:
            return True if movie['imdb'] > 5.5 else False
    return f'No movie with {name} name'


def get_imbds():
    for movie in movies:
        if movie['imdb'] >= 5.5:
            print(f"Name: {movie['name']}   IMDB: {movie['imdb']}", end="\n")

def get_category(category_name):
    for movie in movies:
        if movie['category'] == category_name:
            print(f'Name: {movie['name']}', end = '\n')

def avg_imdb():
    all_imdb = 0
    count = 0
    for movie in movies:
        all_imdb += movie['imdb']
        count+=1
    return all_imdb/count

def avg_imdb_of_category(category_name):
    category_imdb = 0
    count = 0
    for movie in movies:
        if movie['category'] == category_name:
            category_imdb += movie['imdb']
            count+=1
    return category_imdb/count
    

    
print(get_imdb('Hitman'))
print(get_imdb('Exam'))

print()

get_imbds()

print()

get_category('Romance')

print()

print(f'Average imdb: {avg_imdb()}')

print()

print(f"Category average imbd: {avg_imdb_of_category('Romance')}")