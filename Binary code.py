#convert text to binary code
def text_binary():
    test_str = input(" Enter your text: ")
    print()
    res = ''.join(format(ord(i), '08b') for i in test_str)
    print(" The binary code of the text : " + str(res))
   
#convert binary code to text 
def binary_text():
    bins=input(" Enter your binary code: ")
    print()
    binc = [bins[i:i + 8] for i in range(0, len(bins), 8)]
    nums = [int(chunk, 2) for chunk in binc]
    str1 = ''.join(chr(num) for num in nums)
    print(" The normal text is:", str1)

#convert according to choise
def repeat():
    choise = input(" B for text to binary and T for binary to text: ")
    print()
    if choise == "B" or choise == "b":
        text_binary()
    elif choise == "T" or choise == "t":
        binary_text()
    else:
        print(" Invalid Input!")
    print("————————————————————————————————————————————————————————————")

for i in range(100):
    repeat()