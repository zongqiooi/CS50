# Get the height of pyramind+
while True:
    try:
        height = int(input("Height: "))
    except ValueError:
        height = -1 
    if height >= 1 and height <= 8:
        break

# For each row of pyramind
for i in range(height):
    # For each column of pyramind
    for j in range((height + 1) * 2):
        # Print left spaces
        if j < height - i - 1:
            print(" ", end="")
        # Print left hashes
        elif j >= height - i - 1 and j < height:
            print("#", end="")
        # Print gap
        elif j == height or j == height + 1:
            print(" ", end="")
        # Print right hashes
        elif j > height + 1 and j < ((height + 1) * 2) - height + i + 1:
            print("#", end="")
    print()

