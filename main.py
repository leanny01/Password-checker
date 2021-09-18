#   objective 2

#   1. ask the user to repeat the password
#   2. check if the first password matches the second one
#   3. display a message if the password do not match,
#   4. display an error message if the username is less or equal to two letter long
#   5. string formating style going forward



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
  print("Your passwords do not match!")

print("\n")

print(f"We have found {flag} flag(s)")

print("\n")

if not flag :
  print(f"Hey, { username } your password { len(password) * '*' } is {len(password)} letters long.")
  

