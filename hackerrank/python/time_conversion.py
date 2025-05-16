# Time-Conversion

def timeConversion(s):
    if s[-2:] == "AM":
        if s[:2] == "12":
            return "00" + s[2:-2]
        return s[:-2]
    else:
        if s[:2] == "12":
            return s[:-2]
        return str(int(s[:2]) + 12) + s[2:-2]