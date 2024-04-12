romanDict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def isValidRoman(str):
    # checks if a string contains only valid roman numeral characters
    """
    >>>isValidRoman("X")
    True
    >>>isValidRoman("IX")
    True
    >>>isValidRoman("XCCIVH")
    False
    >>>isValidRoman("Hello, World!")
    False
    >>>isValidRoman("IC")
    False
    >>>isValidRoman("LD")
    False
    """
    lastVal = 0
    for s in reversed(str):
        if s not in romanDict:
            return False
        currentVal = romanDict[s]
        if lastVal // currentVal in (5, 10):
            return False
        else:
            lastVal = currentVal
    return True

def stringToDecimal(str):
    # converts a string of roman numerals into a decimal number
    """
    >>>stringToDecimal("I")
    1
    >>>stringToDecimal("IX")
    9
    >>>stringToDecimal("CC")
    200
    >>>stringToDecimal("MMMCMXCIX")
    3999
    """
    nums = []
    while len(str) != 0:
        nums.append(romanDict[str[-1]])
        str = str[:-1]
        if len(str) > 0:
            if romanDict[str[-1]] < nums[-1]:
                newNum = nums[-1] - romanDict[str[-1]]
                nums.pop()
                str = str[:-1]
                nums.append(newNum)
    return sum(nums)

if __name__ == "__main__":
    romanString = ""
    while True:
        romanString = input("Roman numeral: ").upper()
        if romanString == "":
            break
        if isValidRoman(romanString):
            print(f"Converting {romanString} to decimal...")
            print(stringToDecimal(romanString))
        else:
            print("Invalid string. Please enter only Roman numerals.")