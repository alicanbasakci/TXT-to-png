from PIL import Image, ImageDraw, ImageFont
import matplotlib.font_manager as fm

def get_valid_color():
    while True:
        color = input("Enter the color (as a hex code, e.g., #FF0000): ")
        if color.startswith("#") and len(color) == 7 and all(c.isdigit() or c.lower() in "abcdef" for c in color[1:]):
            return color
        print("Invalid color format. Please enter a valid hex code.")

def get_italicbold_preference():
    while True:
        preference = input("Do you want the text to be italic and bold? (Enter 'y' for yes, 'n' for no): ")
        if preference.lower() == 'y':
            return True
        elif preference.lower() == 'n':
            return False
        print("Invalid input. Please enter 'y' or 'n'.")

def get_font_path(italicbold_preference):
    if italicbold_preference:
        return input("Enter the path for the italic and bold font file: ")
    else:
        return input("Enter the path for the regular font file: ")

# Get user input for the text and attributes
text = input("Enter the text: ")
color = get_valid_color()
font_size = int(input("Enter the font size: "))
background_color = get_valid_color()
italicbold_preference = get_italicbold_preference()
font_path = get_font_path(italicbold_preference)

font_properties = fm.FontProperties(fname=font_path)
font = ImageFont.truetype(font_properties.get_file(), font_size)

# Create a temporary Image object to get text size
temp_image = Image.new("RGB", (1, 1), background_color)
temp_draw = ImageDraw.Draw(temp_image)

# Get the size of the text using the font
text_size = temp_draw.textbbox((0, 0), text, font=font)

# Create a blank image with the specified background color
image = Image.new("RGB", (text_size[2] + 10, text_size[3] + 10), background_color)

# Draw the text on the image
draw = ImageDraw.Draw(image)
draw.text((5, 5), text, fill=color, font=font, anchor="lt", align="left")

# Save the image
image.save("output.png")

# Display the image
print("Image saved as output.png")
