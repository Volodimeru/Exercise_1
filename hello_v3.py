#asks user their name, answers with different greetings depending name inputted.
name = input("Hi, what's your name?").strip().capitalize()
print("Hello",name+",", "nice to meet you!")
if name=="ვლადი":
    print("გამარჯობა",name+",", "სასიამოვნოა შეხვედრა!")
elif name =="Ann":
    print("Hello","Mrs", name+",", "nice to meet you!")
elif name =="Jack":
    print("Hello", "Mr", name+",", "nice to meet you!")