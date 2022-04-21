Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def openOrSenior(data):
    result = []
    for i in data:
      if i[0] >= 55 and i[1] > 7:
        result.append("Senior")
      else:
        result.append("Open")
    return result