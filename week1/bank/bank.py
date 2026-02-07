inp=input("Greeting: ").lower().replace(" ","")

match inp:
    case "hello" if inp[:6]=="hello":
        print("$0")
    case _ if inp[0]=="h":
        print("$20")
    case _:
        print("$100")
