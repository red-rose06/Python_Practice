movie={}

def update():
    print("Enter details: ")
    m = input("Enter movie name: ")
    g = input("Enter genre: ")
    y = int(input("Enter movie year: "))
    r = input("Enter movie rating: ")
    movie[m]={"genre":g, "year":y, "rating":r}
    print(f"Updated dictionary is: {movie}")

def genre():
    g = input("Enter genre: ")
    f=0
    for n, details in movie.items():
        if details["genre"].lower()==g.lower():
            print(f"Movie name: {n}")
            f=1
    if f==0:
        print(f"Sorry, no movies of genre {g} available")

def delete():
    y = int(input("Enter year: "))
    f=0
    to_delete = []
    for n, details in movie.items():
        if details["year"]<y:
            to_delete.append(n)
            f=1
    if f==0:
        print(f"Sorry, no such movie found")
    
    for n in to_delete:
        del movie[n]
        print(f"Movie: {n} is deleted")

n=1
while(n!=0):
    print("Options: ")
    print("Enter 1 to add or update a movie.")
    print("Enter 2 to search movies by genre.")
    print("Enter 3 to delete movies before a certain year.")
    print("Enter 0 to exit.")
    n = int(input("Enter now: "))

    if n==1:
        update()
    elif n==2:
        genre()
    elif n==3:
        delete()
    elif n==0:
        print("See you next time!")
    else:
        print("Please enter one of the given numbers")