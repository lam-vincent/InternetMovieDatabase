from movie.models import Categories

with open("data", "r") as f:
    for line in f.readlines():
        l = line.replace('\n', '')
        c = Categories(name=l)
        c.save()
