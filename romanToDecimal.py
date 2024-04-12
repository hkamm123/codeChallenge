romanDict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def isValidRoman(str):
    for s in str:
        if s not in romanDict:
            return False
    return True

# def convertToDecimal(str):
#     nums = []


if __name__ == "__main__":
    romanString = ""
    while True:
        romanString = input("Roman numeral: ").upper()
        if romanString == "":
            break
        if isValidRoman(romanString):
            print(f"Converting {romanString} to decimal...")
        else:
            print("Invalid string. Please enter only Roman numerals.")