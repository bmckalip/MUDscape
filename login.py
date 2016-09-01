import config, player

def createList():
    f = open('userlist','r') #load user list
    linelist = []
    for line in f:
        linelist.append(line[:-1])

    for n in range(0,len(linelist)-1,3): #make list into login tuples
        config.userlist.append((linelist[n],linelist[n+1]))
        
def login():
    print( '        - Welcome to RuneScape -         ')
    print( '                                         ')
    print( '                                         ')
    print( '   )       1.Enter Login             )   ')
    print( '  ) \      2.Type "New"             ) \  ')
    print( ' / ) (                             / ) ( ')
    print( ' \(_)/                             \(_)/ ')
    print( ' (|||)     World: 1                (|||) ')
    print( '  |||        NULL Players           |||  ')
    print( '  |||                               |||  ')
    print( '  |||                               |||  ')
    print( ' (|||)    Copyright Jagex 1999     (|||) ')
    print( '                                         ')

    loggedIn = False
    
    while loggedIn == False:
        username = input('Username:').lower()
        password = input('Password:').lower()

        if (username,password) in config.userlist: #check valid login
            print( 'Welcome ' + username)
            return config.userlist.index((username,password)),username #userid is position
            break
        #elif username == 'new'
        else:
            print( 'Incorrect Login')


        
        
        

        


