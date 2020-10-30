import os
cls = lambda:os.system('cls')
color = lambda:os.system('color 2')
storeinfo = []
color()
best_words=[]
def getinfo():
    cc = len(storeinfo)
    indx = 0
    flist = open(f"password-victim[ {name} ].txt", "w")
    try:
        c = f"{storeinfo[0]}{storeinfo[1]}12345"
        h = f"{storeinfo[0]}{storeinfo[2]}"
        x = f"MyCompany{storeinfo[6]}"
        d = f"{storeinfo[0]}{storeinfo[5]}"
        e = f"Myname{storeinfo[0]}"
        f = f"{storeinfo[0]}{storeinfo[1]}{storeinfo[3]}123456789"
        j=f"{storeinfo[3]}123456789"
        o=f"{storeinfo[3]}1234"
        p=f"{storeinfo[3]}{storeinfo[4]}"
        for i in storeinfo:
            a = i + "1234"
            b = i + storeinfo[indx]
            indx += 1
            flist.write(f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{h}\n{x}\n")
            flist.write(f"{a}123\n{b}123\n{c}123\n{d}123\n{e}123\n{f}123\n{h}123\n{x}123\n")
            for ex in best_words:
                flist.write(ex+"\n")
        ee=email.split("@")[0]
        g = f"{ee}1234"
        h = f"{storeinfo[0]}{phone}"
        flist.write(f"{g}\n{h}")
        flist.close()
        for _ in open(f"password-victim[ {name} ].txt").read().splitlines():
            print(f"[!]{_}")
        input("[*] Thanks For using my tool .. ")
        exit(0)

    except Exception:
        print('')


print("""                                    .------------------------------------------------. 
                                    | .--------------------------------------------. |
                                    | |                                            | |
                                    | |          [ Social Engineering ]            | |
                                    | |   =====================================    | |
                                    | |        [ Github : TNAlotaibi ]             | |
                                    | |                                            | |
                                    | '--------------------------------------------' |
                                    '------------------------------------------------' \n....................................................................................................................
""")
def best_per():
    name_best=input("[+]Name : ")
    keywords=["ilove" , "mylove","myheart","Mylove","MyLove","i#Love","Myheart1234","Mysoul","mysoul","MySoul"]
    if not name_best=="":
        storeinfo.append(name_best)
        storeinfo.append(name_best+"mylove")
        storeinfo.append("ilove"+name_best)
        storeinfo.append("MyLove"+name_best)
        for nbest in keywords:
            best_words.append(nbest+name_best)
            best_words.append(nbest+name_best+"12345")
            best_words.append(nbest+name_best+"1234")
            best_words.append(nbest+name_best+"123")


    father_name=input("[+]Father Name : ")
    if not father_name=="":
        storeinfo.append(father_name)
    nickname_best=input("[+]Nickname : ")
    if not nickname_best=="":
        storeinfo.append(nickname_best)
        if not best_words ==None :
            for kbest in keywords:
                 best_words.append(kbest+nickname_best)
                 best_words.append(kbest + nickname_best+"12345")
                 best_words.append(kbest + nickname_best+"1234")
                 best_words.append(kbest+nickname_best+"123")
    cls()
    getinfo()
try:
    name = input("[+]First Name : ")
    if not name == "":
        storeinfo.append(name)
    fathername11 = input("[+]Father name : ")
    if not fathername11 == "":
        storeinfo.append(fathername11)
    lname = input("[+]Last Name : ")
    if not lname == "":
        storeinfo.append(lname)
    nickname=input("[+]Nickname : ")
    if not nickname =="":
        storeinfo.append(nickname)
    phone = input("[+]Phone Number : ")
    if not phone == "":
        storeinfo.append(phone)
    email = input("[+]Email Address : ")
    if not email == "":
        emailz=email.split("@")[0]
        storeinfo.append(emailz)
    company = input("[+]Company name : ")
    if not company == "":
        storeinfo.append(company)
    brth = input("[+]Birthday Name (DD/MM/YYYY) : ")
    if not brth == "":
        if ("/") in brth:
            DDMMYY=brth.split("/")
            for dmy in DDMMYY:
                 storeinfo.append(dmy)
    print("\n-----------------------------------------------------")
    qu_2=input("[?]You want Enter Any words ? [Y/N] : ")
    if qu_2 == "Y" or qu_2 == "y" or qu_2 == "Yes" or qu_2 == "yes" or qu_2 == "YES":
            words=input("[+]Enter Any Words Example --> (qwer-1234-404.erroz) : ")
            w=words.split("-")
            for wordss in w:
                storeinfo.append(wordss)
    print("\n-----------------------------------------------------")
    qu = input("[?]You Know about The Best Person ? [Y/N] : ")
    if qu == "Y" or qu == "y" or qu == "Yes" or qu == "yes" or qu == "YES":
        best_per()
    for _ in storeinfo:
        print(f"[!]{_}")
    if not qu=="Y" or qu == "y" or qu == "Yes" or qu == "yes" or qu == "YES":
         getinfo()
except:
    print("")
