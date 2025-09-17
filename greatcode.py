
def cmd(x):
    if x == 1: 
         print("hello")

def menu(): 
    print(         " === ACTION MENU ===")
    print("== cmd1       cmd2 ==")
    print("")
    print("== cmd3       cmd4 ==")
    choice = int(input("execute cmd?"))
    cmd(choice)

menu()