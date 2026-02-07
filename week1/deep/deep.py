inp=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().replace(" ","")

match inp:
    case "42"|"forty-two"|"fortytwo":
        print("Yes")
    case _:
        print("No")