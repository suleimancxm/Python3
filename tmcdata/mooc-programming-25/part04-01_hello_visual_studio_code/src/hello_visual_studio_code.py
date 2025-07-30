# Write your solution here
while True:
    editor = input("Editor: ")
    if editor.lower() == "visual studio code":
        print("an excellent choice!")
    elif editor in ['notepad', 'smac']:
        print("not good!")
    else:
        print("awful")    