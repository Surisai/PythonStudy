# define number for input of blocks
blocks = int(input("Enter the number of blocks: "))
#layer start from 1 
layer = 1
# define height
height = 0

while blocks >= layer:
    blocks -= layer
    layer  += 1
    height += 1

print("the height of pyramid : ",height)