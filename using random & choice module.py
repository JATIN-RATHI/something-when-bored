def dice():
    import random
    random_no = random.randint(1,6)
    print(random_no)


def coin():
    import random
    l = ["Head","Tail"]
    r = random.choice(l)
    print(r)

def card():
    import random
    l = ["SPACE","HEART","DIAMOND","CLUB"]
    c = random.choice(l)
    print(c)

def cloth():
    import random
    l = ["BLUE","GREEN","YELLOW","WHITE","PINK","BLACK","GREY","RED","MULTICOLOR"]
    c = random.choice(l)
    print(c)
    
def todaydate():
    from datetime import date
    date = date.today()
    print(date)
    
def todaytime():
         
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    
#main menu
if __name__ == "__main__":
    from pygame import mixer
    mixer.init()
    mixer.music.load('c:/Users/JATIN RATHI/Downloads/tone1.mp3')
    mixer.music.play(10)

    print("--------WELCOME----------")
    print("Choose any option")
    print("\n1:Flip the Dice")
    print("2:Flip the Coin")
    print("3:The Lucky Card")
    print("4:The Color of cloths to wear today")
    print("5:Show current date")
    print("6:Show current time")
    ch = int(input())

    if ch == 1:
        dice()
    elif ch == 2:
        coin()
    elif ch == 3:
        card()
    elif ch == 4:
        cloth()
    elif ch == 5:
        todaydate()
    elif ch == 6:
        todaytime()
    else:
        print("INVALID INPUT!!")

    print("Coded by     Jatin Rathi")