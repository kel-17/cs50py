inp = input("type ur msg: ")

def main(inp):
    res=convert(inp)
    return res
def convert(d):
    edited=d.title()
    return edited
result=main(inp)
print("Converted!", result)