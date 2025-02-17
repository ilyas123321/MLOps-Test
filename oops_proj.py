class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input("""Weclome to Chatbook !! how would you like to  proceed ?
                           1. Press 1 to signup 
                           2. Press 2 to signin 3
                           3. press 3 o write a post
                           4. Press 4 to message a friend 
                           5. press any other key to exit""")
        if user_input == "1":
            self.singup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def singup(self):
        email = input("Enter your email here -- >")
        pwd = input("enter your password here")
        self.username = email
        self.password = pwd     
        print("you have signed up successfully !!")
        print("\n")
        self.menu() 

    def signin(self):
        if self.username=='' and self.password=='':
            print("please signu firt by pressing 1 in the main menu")
        else:
            uname = input("enter your email and username here --->")
            pwd = input("Enter  your password here -->")
            if self.username==name and self.password==pwd:
                print("you have sgined in successfully")
                self.loggedin = True
            else:
                print("please input correct credentails ..")
        print("\n")
        self.menu()   



obj = chatbook()           