import csv
from pig_class_HC import
Human_Computer
from pig_class_HH import
Human_Human
class Registration:
    def register(self)
    username=input('Enter your username').lower
    passwd=input('enter the password')
    confirm_passwd=input('enter confirm password')
    if passwd=confirm_passwd:
        print("You have been registered successfully")
    else:
        print("password mismatch try again!")
with_open('user_data.csv', 'a+' newline=" ") as file:
write=csv.writer(file)
write.writerow([username, password])
def login(self):
    while True:
        username=input("Enter your username")
        passwd=input("enter your password")
        with_open('user_data.csv,r') as file_read:
            read=csv.reader(file_read)
        if(user_name,passwd) in read:
            print('logged in')
        else:
            print('invalid username and passwd')
def loginpage(self):
    print('The pig welcomes you')
    choose=input('enter 1 for login and 2 for registration')
    if '1'==choose:
        log = Registration()
        log.login()
        choose1=input('Press 1 for Quick match and 2 for Multiplayer')
        if choose1 =='1':
            hc = Human_Computer()
            hc.human_player()
        elif choose1 =='2':
            hh = Human_Human()
            hh.player_one()
            hh.player_two(obj)
        else:
            log = Registration()
            log.register()
            log.login()
obj=Registration()
obj.loginpage()