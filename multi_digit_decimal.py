"""
Grammar rules for a multi-digit decimal number:
<expr>  ::= +<num>|-<num>|<num>
<num>   ::= <digit>|<digit>.<digit>
<digit> ::= 0|1|2|3|4|5|6|7|8|9
Terminate every input with '$'

reference:http://www.cs.utsa.edu/~wagner/CS3723/rdparse/rdparser6.html
"""
import sys
next = None
digit = ['0','1','2','3','4','5','6','7','8', '9']
   
def P():
  sys.stdout.write("\nEnter string: ")
  lex()
  if next == '$': #'$' as the first token
    print("INAVLID: no number before $")
    sys.exit()
  expr()
  if next == '$': #reaches terminating symbol ('$')
    sys.stdout.write("VALID\n")
  else:
    error()

def expr():
    z() #'+'|'-'
    num()

def z():
  if next in "+-":
    lex()
  
def num():
  digits()
  zz() #'.'<digits>

def zz():
  if next == '.':
    lex()
    digits()

def digits():
  if next in digit: #check if digit
    lex()
    while next in digit:
      digits()
  else:
    error()

def getch():
  char = sys.stdin.read(1) #read 1 character at a time
  if len(char) > 0:
    return char
  else:
    return None

def lex():
  global next
  next = getch() #getting next charcter
  if next == None:
    sys.exit()
  while next.isspace(): #ignore whitespaces
    next = getch()

def error():
  sys.stdout.write("\nINVALID: not part of grammar")
  sys.exit()

while True:
  P()
