# Import the library
import ipypng

# Get the data of the image (as bytes)
data = open("non-cgbi-image.png", "rb").read()

# Convert the image to CgBI
new_data = ipypng.convert(data)

# Save the image
with open("cgbi-image.png", "wb") as f:
    f.write(new_data)
