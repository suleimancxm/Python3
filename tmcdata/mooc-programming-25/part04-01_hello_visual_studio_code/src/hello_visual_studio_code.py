while True:
    editor = input("Editor: ")
    editor_lower = editor.lower()
    if editor_lower in ["emacs", "vim", "atom"]:
        print("not good")
    elif editor_lower == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("awful")    