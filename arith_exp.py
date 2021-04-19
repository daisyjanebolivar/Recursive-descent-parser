
import sys
next = None
   
def P():
  sys.stdout.write("\nEnter string: ")
  scan()
  if next == '$':
    sys.exit(1)
  expr()
  if next == '$':
    sys.stdout.write("VALID\n")
  else:
    error()

def expr():
  if next in "+-":
    scan()
    num()
  else:
    num()

def num():
  digits()
  if next == '.':
    scan()
    digits()


def digits():
  if next in "0123456789": #check if digit
    scan()
    while next in "0123456789":
      digits()
  else:
    error()


def getch():
  char = sys.stdin.read(1)
  if len(char) > 0:
    return char
  else:
    return None

def scan():
  global next
  next = getch()
  if next == None:
    sys.exit()
  while next.isspace(): #ignore whitespaces
    next = getch()

def error():
  sys.stdout.write("\nINVALID")
  sys.exit()

while True:
  P()
