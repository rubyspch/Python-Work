def translate(lang):
    if lang=="es":
        return "Hola"
    elif lang=="nl":
        return "Hallo"
    elif lang=="fr":
        return "Bonjour"
    else:
     return "Hello"
uname= input("What is your name?")
ulang=input("What language do you speak?")
print(translate(ulang),uname)