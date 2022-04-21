Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def diamond(n):
    if n % 2 == 0 or n < 0:
        return None
    middlenumb = int(n/2) + (n % 2 > 0)
    diamond = ''
    previousnumb = 0
    for numb in range(1, n+1):
        if numb == 1 or numb == n:
            diamond += "*/n" if middlenumb == 1 else " " * (middlenumb - 1) + '*\n"
            
SyntaxError: unterminated string literal (detected at line 9)
def diamond(n):
    if n % 2 == 0 or n < 0:
        return None
    middlenumb = int(n/2) + (n % 2 > 0)
    diamond = ''
    previousnumb = 0
    for numb in range(1, n+1):
        if numb == 1 or numb == n:
            diamond += "*/n" if middlenumb == 1 else " " * (middlenumb - 1) + "*\n"
            previousnumb = numb
        else numb < middlenumb:
            
SyntaxError: expected ':'
def diamond(n):
    if n % 2 == 0 or n < 0:
        return None
    middlenumb = int(n/2) + (n % 2 > 0)
    diamond = ''
    previousnumb = 0
    for numb in range(1, n+1):
        if numb == 1 or numb == n:
            diamond += "*/n" if middlenumb == 1 else " " * (middlenumb - 1) + "*\n"
            previousnumb = numb
        elif numb < middlenumb:
            diamond += (" " * (middlenumb - numb)) + "*" * (previousnumb + 2) + "\n"
            previousnumb += 2
        elif numb == middlenumb:
            diamond += "*" * n + "\n"
            previousnumb = n
        elif numb > middlenumb:
            diamond += (" " * (numb - middlenumb)) + "*" * (previousnumb -2) + "\n"
            previousnumb -= 2
    return diamond

result = diamond(7)
print(result)
   *
  ***
 *****
*******
 *****
  ***
   *

