movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


#1
name = input()
def imdbdb(name) -> bool:
    for i in range(len(movies)):
        if name == movies[i]["name"] and movies[i]["imdb"] > 5.5:
            return True
print(imdbdb(name))

#2
def score():
    for i in range(len(movies)):
        if movies[i]["imdb"] > 5.5:
            print(movies[i]["name"])
            
score()

#3
category = input()
def cate(category):
    for i in range(len(movies)):
        if category == movies[i]["category"]:
            print(movies[i]["name"])
cate(category)

#4
def average():
    summa = 0
    for i in range(len(movies)):
        summa+=movies[i]["imdb"]
    print(summa/len(movies))

average()
#5
def categoryAverage(category):
    summa = 0
    cnt = 0
    for i in range(len(movies)):
        if category == movies[i]["category"]:
            summa+=movies[i]["imdb"]
            cnt+=1
    print(summa/cnt)

categoryAverage(input())
