from PIL import Image


x = input("Enter the path of the image: ")
img = Image.open(x)
img.show()

while True :
    print("1. Rotate the image")
    print("2. Resize the image")
    print("3. Crop the image")
    print("4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        continue
    elif ch == 2:
        continue
    elif ch == 3:
        continue
    elif ch == 4:
        break
    else:
        print("Invalid choice")
