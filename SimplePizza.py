print("Hello welcome to python pizza shop!!")
size = input("What size pizza do you want? S, M, or L: ")
paneer = input("Do you want paneer? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "S":
   bill += 15

elif size == "M":
   bill = 20
elif size == "L":
   bill = 25
else:
   print("wrong input")

if paneer == "Y":
   if size == "S":
      bill += 2
   else:
      bill += 3

if cheese == "Y":
   bill += 1

print(f"Final bill is:${bill}")