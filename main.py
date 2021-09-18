
import re

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

username = input("Please input your username:        \t")
password = input("Please input your password:        \t")
passwordConf = input("Please confirm your password:  \t")
flag = 0

print("\n")
if len(username) <= 2:
  flag = flag + 1 
  print("username length too short")


if password != passwordConf :
  flag += 1 
  print(f"{bcolors.FAIL}Your passwords do not match! {bcolors.RESET}")

if not re.search("[A-Z]",password):
  flag +=1
  print(f"{bcolors.FAIL}Password should have atleast one capital letter!{bcolors.RESET}")

if not re.search("[a-z]",password):
  flag +=1
  print(f"{bcolors.FAIL}Password should have atleast one lowercase!{bcolors.RESET}")

if not re.search("[0-9]",password):
  flag +=1
  print(f"{bcolors.FAIL}Password should have atleast one number!{bcolors.RESET}")

if not re.search("[$&+,:;=?@#|'<>.^*()%!-]",password):
  flag +=1
  print(f"{bcolors.FAIL}Password should atleast one special character including $&+,:;=?@#|'<>.^*()%!-!{bcolors.RESET}")



print("\n")

print(f"{bcolors.WARNING}We have found {flag} flag(s){bcolors.RESET}")

print("\n")

if not flag :
 
  print(f"{bcolors.OK}Hey, { username } You have successfully registered 😀!\n your password { len(password) * '*' } is {len(password)} letters long.{bcolors.RESET}")
  

