def say_hello(name):
    print('Hello, ' + name + '!')

def insert_separator(char="=",repeat=20):
    print(char*repeat)

def recite_poem():
    print("How about a song?")
    insert_separator("=",20)
    print("I'm a little tea pot, short and stout.")
    print("Here is my handle. Here is my spout.")
    print("When I get all steamed up, hear me shout.")
    print("Tip me over and pour me out.")

def say_goodbye(name):
    print('Goodbye, ' + name + '!')

def main():
    your_name = input('What is your name? ')
    insert_separator("=",20)
    say_hello(your_name)
    insert_separator()
    recite_poem()
    insert_separator()
    say_goodbye(your_name)

main()