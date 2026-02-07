inp=input("File name: ").lower()

match inp:
    case _ if inp[-5:]==".jpeg":
        print("image/jpeg")
    case _ if inp[-4:]==".jpg":
        print("image/jpeg")
    case _ if inp[-4:]==".gif" or inp[-4:]==".png":
        print("image/"+str(inp[-3:]))
    case _:
        print("application/"+str(inp[-3:]))