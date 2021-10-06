def p_help():
    print("""\x1b[0;35m
_____________                                   ______    ________             
___  __ \__(_)_________________ ___________________  /_______  __ \_______   __
__  /_/ /_  /__  __ \  _ \  __ `/__  __ \__  __ \_  /_  _ \_  / / /  _ \_ | / /
_  ____/_  / _  / / /  __/ /_/ /__  /_/ /_  /_/ /  / /  __/  /_/ //  __/_ |/ / 
/_/     /_/  /_/ /_/\___/\__,_/ _  .___/_  .___//_/  \___//_____/ \___/_____/  
                                /_/     /_/                                   
\x1b[0;31m
###############################################################################
             			    \x1b[0;34mBy x04000
     			    \x1b[0;33mGithub: github.com/x04000
           		          \x1b[0;32mBase: Python
           		          \x1b[0;36mVersion: 1.4
\x1b[0;31m###############################################################################

  /\  /\___| |_ __  
 / /_/ / _ \ | '_ \ 
/ __  /  __/ | |_) |
\/ /_/ \___|_| .__/ 
             |_|    
\x1b[0;35m
p_CFILE(file.extension)                 - Create a file
p_clear()                               - Clear the console
p_credits                               - Show the credits
p_DELFILE(file.extension)               - Delete a file
p_ep(text)                              - Print a text in console
p_exit()                                - Exit the program
p_filemodifiergui                       - A simple files modifier with GUI
p_gitclone(giturl)                      - Use Git clone
p_help                                  - Show this list
p_login("username", "password")         - A simple login
p_logingui("username", "password")      - A simple login with GUI (tkinter)
p_login_nologo("username", "password")  - A simple login without Login logo
p_pin(pin)                              - A simple PIN function
p_pingui(pin)                           - A simple PIN function GUI
p_pin_noint(pin)                        - A simple PIN function without having to be in int format
p_pipinstall(package)                   - Pip install
p_piplist()                             - Pip packahe list
p_pipuninstall(package)                 - Pip uninstall
p_python()                              - Use the python terminal
p_python3()                             - Use the python3 terminal
p_RFILE(file.extension)                 - Read a file
p_setcolor("colorid")                   - Set a color. IDs are from number 30
p_sys(command)                          - Execute a command in your system terminal
p_systemterminal()                      - To use your system terminal commands
p_systemterminalgui()                   - To use your system terminal GUI (tkinter)
p_WFILE(file.extension, text)           - Write a file
    """)
def p_credits():
    print("""\x1b[0;35m
_____________                                   ______    ________             
___  __ \__(_)_________________ ___________________  /_______  __ \_______   __
__  /_/ /_  /__  __ \  _ \  __ `/__  __ \__  __ \_  /_  _ \_  / / /  _ \_ | / /
_  ____/_  / _  / / /  __/ /_/ /__  /_/ /_  /_/ /  / /  __/  /_/ //  __/_ |/ / 
/_/     /_/  /_/ /_/\___/\__,_/ _  .___/_  .___//_/  \___//_____/ \___/_____/  
                                /_/     /_/                                   
\x1b[0;31m
   ______              ___ __      
  / ____/_______  ____/ (_) /______
 / /   / ___/ _ \/ __  / / __/ ___/
/ /___/ /  /  __/ /_/ / / /_(__  ) 
\____/_/   \___/\__,_/_/\__/____/  
\x1b[0;35m
Idea, desing and developer: x04000
Ideas and help: GhostTD
    """)
def p_clear():
    try:
        import os
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    except:
        print("\nPineappleDev > Error with clear command!")
def p_exit():
    try:
        exit()
    except:
        print("")
def p_ep(ep):
    try:
        print(ep)
    except:
        print("")
def p_CFILE(pineappledevfile):
        try:
            f=open(pineappledevfile,"w")
            f.close()
        except:
            print("\nPineappleDev > Error during creating the file!")
def p_DELFILE(pineappledevfile):
    import os
    delfilewin = "del /f /a "+pineappledevfile
    delfilelinux = "rm "+pineappledevfile
    try:
        os.system(delfilewin if os.name in ('nt', 'dos') else delfilelinux)
    except:
        print("\nPineappleDev > Error during deletion of file!")
def p_WFILE(pineappledevfile, pineappledevwrite):
    try:
        f=open(pineappledevfile, "w")
        f.write(pineappledevwrite)
        f.close()
    except:
        print("\nPineappleDev > Error during writting of file")
def p_RFILE(pineappledevfile):
    try:
        with open(pineappledevfile,"r") as file:
            for line in file:
                print(line)
    except:
        print("\nFile can't load!")
def p_gitclone(gitcloneurl):
    gitcloneurl = str(input("URL of Git > "))
    gitclonecommand = "git clone "+gitcloneurl
    try:
        import os
        os.system(gitclonecommand)
    except:
        print("\nPineappleDev > Git error!")
def p_ls():
    try:
        import os
        os.system("dir" if os.name in ('nt', 'dos') else "ls")
        print("")
    except:
        print("\nPineappleDev > Ls error")
def p_pipinstall(pipinstallpackage):
    pipinstallpackage = str(input("Name of package > "))
    pipinstallcommand = "pip install "+pipinstallpackage
    try:
        import os
        os.system(pipinstallcommand)
    except:
        print("\nPineappleDev > Python: Pip error!")
def p_pipuninstall(pipuninstallpackage):
    pipuninstallpackage = str(input("Name of package > "))
    pipuninstallcommand = "pip uninstall "+pipuninstallpackage
    try:
        import os
        os.system(pipuninstallcommand)
    except:
        print("\nPineappleDev > Python: Pip error!")
def p_piplist():
    try:
        import os
        os.system("pip list")
    except:
        print("\nPineappleDev > Python: Pip error!")
def p_systemterminal():
    print("[PineappleDev System Terminal]")
    print("")
    print("""[INFO]

You can use your terminal commands here ;)
To close the System Terminal use: p_closeterminal

    """)
    while(True):
        systemterminalcommand = str(input("PineappleDev SysTerminal > "))
        print("")
        if systemterminalcommand == "p_closeterminal":
            break
        else:
            try:
                import os
                os.system(systemterminalcommand)
            except:
                print("\nPineappleDev > PineappleDev System Terminal error!")
def p_python():
    try:
        import os
        os.system("python")
    except:
        print("\nPineappleDev > PineappleDev can't load python. Revise your python installation")
def p_python3():
    try:
        import os
        os.system("python3")
    except:
        print("\nPineappleDev > PineappleDev can't load python3. Revise your python3 installation")
def p_sys(command):
    try:
        import os
        os.system(command)
    except:
        print("Command error")
def p_login(pineappledevusername, pineappledevpassword):
    global pineappledevloginpassed
    pineappledevloginpassed=0
    try:
        from getpass import getpass
        print("""
    ██▓     ▒█████    ▄████  ██▓ ███▄    █ 
    ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██▒ ██ ▀█   █ 
    ▒██░    ▒██░  ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒
    ▒██░    ▒██   ██░░▓█  ██▓░██░▓██▒  ▐▌██▒
    ░██████▒░ ████▓▒░░▒▓███▀▒░██░▒██░   ▓██░
    ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒ 
    ░ ░ ▒  ░  ░ ▒ ▒░   ░   ░  ▒ ░░ ░░   ░ ▒░
    ░ ░   ░ ░ ░ ▒  ░ ░   ░  ▒ ░   ░   ░ ░ 
        ░  ░    ░ ░        ░  ░           ░   

        """)
        while(True):
            pineappledevusernameinput = str(input("Username: "))
            if pineappledevusernameinput == str(pineappledevusername):
                break
            else:
                print("PineappleDev > Incorrect username!")
        while(True):
            pineappledevpasswordinput = getpass("Password: ")
            if pineappledevpasswordinput == str(pineappledevpassword):
                pineappledevloginpassed=1
                break
            else:
                print("PineappleDev > Incorrect password!")
    except:
        print("\nPineappleDev > Keyboard interruption")
    if pineappledevloginpassed == 1:
        print("PineappleDev > Successfully logged!")
    else:
        return p_login(pineappledevusername, pineappledevpassword)
def p_login_nologo(pineappledevusername, pineappledevpassword):
    global pineappledevloginpassed
    pineappledevloginpassed=0
    try:
        from getpass import getpass
        while(True):
            pineappledevusernameinput = str(input("Username: "))
            if pineappledevusernameinput == str(pineappledevusername):
                break
            else:
                print("PineappleDev > Incorrect username!")
        while(True):
            pineappledevpasswordinput = getpass("Password: ")
            if pineappledevpasswordinput == str(pineappledevpassword):
                pineappledevloginpassed=1
                break
            else:
                print("PineappleDev > Incorrect password!")
    except:
        print("\nPineappleDev > Keyboard interruption")
    if pineappledevloginpassed == 1:
        print("PineappleDev > Successfully logged!")
    else:
        return p_login_nologo(pineappledevusername, pineappledevpassword)
def p_setcolor(pineappledevcolorid):
    try:
        pineappledevcolor = "\x1b[0;"+str(pineappledevcolorid)+"m"
        print(pineappledevcolor)
    except:
        print("PineappleDev > A error ocurred during the setcolor function")
def p_pin(pineappledevpin):
    try:
        from getpass import getpass
        while(True):
            pineappledevpininput = int(getpass("PIN: "))
            if pineappledevpininput == pineappledevpin:
                print("The PIN is correct!")
                break
            else:
                print("Incorrect PIN!")
    except:
        print("\nPineappleDev > A error ocurred during the PIN function")
def p_pin_noint(pineappledevpin):
    try:
        from getpass import getpass
        while(True):
            pineappledevpininput = getpass("PIN: ")
            if pineappledevpininput == pineappledevpin:
                print("The PIN is correct!")
                break
            else:
                print("Incorrect PIN!")
    except:
        print("\nPineappleDev > A error ocurred during the PIN function")
def p_logingui(pineappledevusername, pineappledevpassword):
    global pineappledevloginpassed
    pineappledevloginpassed = 0
    try:
        import tkinter

        login = tkinter.Tk()
        login.geometry("400x300")
        login.title("PineappleDev Login")
        login.configure(bg="black")

        text1 = tkinter.Label(login, text = "PineappleDev Login", bg="blue", fg="white")
        text1.pack(fill = tkinter.X)
        text2 = tkinter.Label(login, text = "", bg="black", fg="white")
        text2.pack(fill = tkinter.X)
        text3 = tkinter.Label(login, text = "Username", bg="black", fg="white")
        text3.pack(fill = tkinter.X)

        input1 = tkinter.Entry(login, width = 50, fg="white", bg="black")
        input1.pack()

        text4 = tkinter.Label(login, text = "", bg="black", fg="white")
        text4.pack(fill = tkinter.X)

        text5 = tkinter.Label(login, text = "Password", bg="black", fg="white")
        text5.pack(fill = tkinter.X)

        input2 = tkinter.Entry(login, show="*", width = 50, fg="white", bg="black")
        input2.pack()

        text5 = tkinter.Label(login, text = "", bg="black", fg="white")
        text5.pack(fill = tkinter.X)

        def pineappledevlogin():
            pineappledevusernameinput = input1.get()
            pineappledevpasswordinput = input2.get()
            if str(pineappledevusernameinput) == str(pineappledevusername):
                if str(pineappledevpasswordinput) == str(pineappledevpassword):
                    global pineappledevloginpassed
                    pineappledevloginpassed = 1
                    text5.configure(text="Successfully login!", fg="green")
                    login.destroy()
                else:
                    text5.configure(text="Incorrect username/password!", fg="red")
            else:
                text5.configure(text="Incorrect username/password!", fg="red")
            
        
        loginbutton = tkinter.Button(login, text = "Login", command = pineappledevlogin, fg="white", bg="black")
        loginbutton.pack()

        text6 = tkinter.Label(login, text = "", bg="black", fg="white")
        text6.pack(fill = tkinter.X)

        def pineappledevexit():
            global pineappledevloginpassed
            pineappledevloginpassed = 2
            exit()

        pinexitbutton = tkinter.Button(login, text = "Exit", command = pineappledevexit, fg="white", bg="black")
        pinexitbutton.pack()

        login.mainloop()
    except:
        print("\nPineappleDev > Keyboard interruption")
    if pineappledevloginpassed == 1:
        print("PineappleDev > Successfully logged!")
    elif pineappledevloginpassed == 2:
        print("PineappleDev > Program aborted")
        exit()
    else:
        return p_logingui(pineappledevusername, pineappledevpassword)
def p_systemterminalgui():
    try:
        import tkinter
        import os

        terminal = tkinter.Tk()
        terminal.geometry("400x150")
        terminal.title("PineappleDev System Terminal")
        terminal.configure(bg="black")

        text1 = tkinter.Label(terminal, text = "PineappleDev System Terminal", bg="blue", fg="white")
        text1.pack(fill = tkinter.X)
        text2 = tkinter.Label(terminal, text = "", bg="black", fg="white")
        text2.pack(fill = tkinter.X)

        commandinput = tkinter.Entry(terminal, width = 200, fg="white", bg="black")
        commandinput.pack()

        text3 = tkinter.Label(terminal, text = "", bg="black", fg="white")
        text3.pack(fill = tkinter.X)

        def terminalcommand():
            pineappledevcommandinput = commandinput.get()
            try:
                os.system(pineappledevcommandinput)
            except:
                print("\nPineappleDev > A error ocurred during in the System Terminal: GUI Input Command")
                
        executebutton = tkinter.Button(terminal, text = "Execute", command = terminalcommand, fg="white", bg="black")
        executebutton.pack()

        terminal.mainloop()
    except:
        print("\nPineappleDev > A error ocurred during in the System Terminal GUI")
def p_filemodifiergui():
    try:
        import tkinter
        import os

        filemodifier = tkinter.Tk()
        filemodifier.geometry("400x550")
        filemodifier.title("PineappleDev File Modifier")
        filemodifier.configure(bg="black")

        text1 = tkinter.Label(filemodifier, text = "PineappleDev File Modifier", bg="blue", fg="white")
        text1.pack(fill = tkinter.X)
        text2 = tkinter.Label(filemodifier, text = "", bg="black", fg="white")
        text2.pack(fill = tkinter.X)
        text3 = tkinter.Label(filemodifier, text = "Create a file", bg="black", fg="white")
        text3.pack(fill = tkinter.X)
        text4 = tkinter.Label(filemodifier, text = "Filename and extension", bg="black", fg="white")
        text4.pack(fill = tkinter.X)

        cfilename = tkinter.Entry(filemodifier, width = 200, fg="white", bg="black")
        cfilename.pack()

        def createfile():
            createfilename = cfilename.get()
            try:
                f=open(str(createfilename),"w")
                f.close()
                print("PineappleDev > File created!")
            except:
                print("\nPineappleDev > Error during of creating of the file!")
                
        cfilebutton = tkinter.Button(filemodifier, text = "Create file", command = createfile, fg="white", bg="black")
        cfilebutton.pack()

        text4 = tkinter.Label(filemodifier, text = "", bg="black", fg="white")
        text4.pack(fill = tkinter.X)
        text5 = tkinter.Label(filemodifier, text = "Delete a file", bg="black", fg="white")
        text5.pack(fill = tkinter.X)
        text6 = tkinter.Label(filemodifier, text = "Filename and extension", bg="black", fg="white")
        text6.pack(fill = tkinter.X)

        dfilename = tkinter.Entry(filemodifier, width = 200, fg="white", bg="black")
        dfilename.pack()

        def deletefile():
            deletefilename = dfilename.get()
            try:
                delfilewin = "del /f /a "+deletefilename
                delfilelinux = "rm "+deletefilename
                os.system(delfilewin if os.name in ('nt', 'dos') else delfilelinux)
                print("PineappleDev > File deleted!")
            except:
                print("\nPineappleDev > Error during deleting of the file!")
                
        dfilebutton = tkinter.Button(filemodifier, text = "Delete file", command = deletefile, fg="white", bg="black")
        dfilebutton.pack()

        text7 = tkinter.Label(filemodifier, text = "", bg="black", fg="white")
        text7.pack(fill = tkinter.X)
        text8 = tkinter.Label(filemodifier, text = "", bg="black", fg="white")
        text8.pack(fill = tkinter.X)
        text9 = tkinter.Label(filemodifier, text = "Read a file", bg="black", fg="white")
        text9.pack(fill = tkinter.X)
        text10 = tkinter.Label(filemodifier, text = "Filename and extension", bg="black", fg="white")
        text10.pack(fill = tkinter.X)

        rfilename = tkinter.Entry(filemodifier, width = 200, fg="white", bg="black")
        rfilename.pack()

        def readfile():
            readfilename = rfilename.get()
            try:
                with open(readfilename,"r") as file:
                    for line in file:
                        print(line)
            except:
                print("\nPineappleDev > Error during redating of the file!")
                
        rfilebutton = tkinter.Button(filemodifier, text = "Read file", command = readfile, fg="white", bg="black")
        rfilebutton.pack()

        text11 = tkinter.Label(filemodifier, text = "", bg="black", fg="white")
        text11.pack(fill = tkinter.X)
        text12 = tkinter.Label(filemodifier, text = "", bg="black", fg="white")
        text12.pack(fill = tkinter.X)
        text13 = tkinter.Label(filemodifier, text = "Write a file", bg="black", fg="white")
        text13.pack(fill = tkinter.X)
        text14 = tkinter.Label(filemodifier, text = "Filename and extension", bg="black", fg="white")
        text14.pack(fill = tkinter.X)

        wfilename = tkinter.Entry(filemodifier, width = 200, fg="white", bg="black")
        wfilename.pack()

        text15 = tkinter.Label(filemodifier, text = "File content", bg="black", fg="white")
        text15.pack(fill = tkinter.X)

        wtext = tkinter.Entry(filemodifier, width = 200, fg="white", bg="black")
        wtext.pack()

        def readfile():
            writefilename = wfilename.get()
            writetext = wtext.get()
            try:
                f=open(writefilename, "w")
                f.write(writetext)
                f.close()
            except:
                print("\nPineappleDev > Error during writing of the file!")
                
        rfilebutton = tkinter.Button(filemodifier, text = "Write file", command = readfile, fg="white", bg="black")
        rfilebutton.pack()

        text16 = tkinter.Label(filemodifier, text = "", bg="black", fg="white")
        text16.pack(fill = tkinter.X)

        filemodifier.mainloop()
    except:
        print("\nPineappleDev > A error ocurred during in the System Terminal GUI")
def p_pingui(pineappledevpin):
    global pineappledevpinpassed
    pineappledevpinpassed = 0
    try:
        import tkinter
        from tkinter import messagebox

        pin = tkinter.Tk()
        pin.geometry("400x300")
        pin.title("PineappleDev Login")
        pin.configure(bg="black")

        text1 = tkinter.Label(pin, text = "PineappleDev Login", bg="blue", fg="white")
        text1.pack(fill = tkinter.X)
        text2 = tkinter.Label(pin, text = "", bg="black", fg="white")
        text2.pack(fill = tkinter.X)
        text3 = tkinter.Label(pin, text = "Username", bg="black", fg="white")
        text3.pack(fill = tkinter.X)

        input1 = tkinter.Entry(pin, show="*", width = 50, fg="white", bg="black")
        input1.pack()

        text4 = tkinter.Label(pin, text = "", bg="black", fg="white")
        text4.pack(fill = tkinter.X)

        def pineappledevpinf():
            pineappledevpininput = input1.get()
            if str(pineappledevpininput) == str(pineappledevpin):
                global pineappledevpinpassed
                pineappledevpinpassed = 1
                text4.configure(text="The PIN is correct!", fg="green")
                pin.destroy()
            else:
                text4.configure(text="Incorrect PIN!", fg="red")
            
        
        pinbutton = tkinter.Button(pin, text = "Enter", command = pineappledevpinf, fg="white", bg="black")
        pinbutton.pack()

        text5 = tkinter.Label(pin, text = "", bg="black", fg="white")
        text5.pack(fill = tkinter.X)

        def pineappledevexit():
            global pineappledevpinpassed
            pineappledevpinpassed = 2
            exit()

        pinexitbutton = tkinter.Button(pin, text = "Exit", command = pineappledevexit, fg="white", bg="black")
        pinexitbutton.pack()

        pin.mainloop()
    except:
        print("\nPineappleDev > Keyboard interruption")
    if pineappledevpinpassed == 1:
        print("PineappleDev > The PIN is correct!")
    elif pineappledevpinpassed == 2:
        print("PineappleDev > Program aborted")
        exit()
    else:
        return p_pingui(pineappledevpin)