
def convert(listed):
    for cha in listed:
        if cha==":":
            posCha=listed.index(cha)
            if listed[posCha+1]==")":
                listed[posCha:posCha+2] = ["", "🙂"]
            if listed[posCha+1]=="(":
                listed[posCha:posCha+2] = ["", "🙁"]
    unlisted = "".join(listed)
    print(unlisted)
    return unlisted

def main():
    inp = input("enter: ")
    listed = list(inp)
    convert(listed)

main()

