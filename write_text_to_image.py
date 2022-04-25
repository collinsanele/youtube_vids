#pip install pillow
#The code link would be in the video description

from PIL import Image, ImageDraw, ImageFont

def write_text_to_image(text, img_path, dest_path):
    image = Image.open(img_path)
    width = image.size[0]
    height = image.size[1]
    x, y = (0.2*width, 0.4*height)
    draw = ImageDraw.Draw(image)
    #Download font from https://fonts.webtoolhub.com/font-n19403-rechtman-plain.aspx?lic=1
    #create font folder and put the downloaded font in it.
    font = ImageFont.truetype("./font/Rechtman_Plain.ttf", 280)
    draw.text((x,y), text, (255,215,0), font=font)
    image.save(dest_path)

#Run it in the terminal with 'python write_text_to_image.py'

if __name__ == "__main__":
    write_text_to_image(text="Codify Rocks!", img_path="./images/0.png", dest_path="./0.png")