#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while(x<5):
    print(x)
    x=x+1

  # define a for loop
  for i in range(0,5):
    print(i)

  # use a for loop over a collection
  days = ["MOn", "Tues", "Wed", "Thus", "fri", "sat", "sun"]
  for j in days:
    print(j)
  
  # use the break and continue statements
  for i in range(5,10):
    if(i%2==0): continue
    print(i)
  for j in range(5,10):
    if(j==8): break
    print(j) 

  #using the enumerate() function to get index 
  days = ["MOn", "Tues", "Wed", "Thus", "fri", "sat", "sun"]
  for t,j in enumerate(days):
    print(t, j)
if __name__ == "__main__":
  main()
