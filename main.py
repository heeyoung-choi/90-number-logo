from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np

def drawBoard(image, font, x, y, w, h, space, table, id="#00"):
    d = ImageDraw.Draw(image)
    d.text((1300, 100) , id, font=font,fill="black")
    for i in range(9):
        for j in range(9):
            d.rounded_rectangle((x + i * (w + space), y + j * (h + space),x + i * (w + space) + w, y + j * (h + space) + h),
            radius=w / 100  * 30, fill=None, outline='black', width=10 )
            if table[j][i]: d.text((x + i * (w + space) + w/4 - 5, y + j * (h + space) + h/4 -20),("0" if table[j][i] < 10 else "") + str(table[j][i]), font=font, fill='black')
    return image
def generate_table():
    table = [[0] * 9]*9
    table = np.array(table)
    listed = []
    for i in range(9):
        selected_column = (random.sample(range(9), k=5))
        for j in selected_column:
            selected_number = random.randint(j * 10 + 1, (j + 1) * 10)
            while selected_number in listed:
                selected_number = random.randint(j * 10 + 1, (j + 1) * 10)
            listed.append(selected_number)
            table[i][j] = selected_number
    return table
font = ImageFont.truetype('PlayfairDisplay-VariableFont_wght.ttf', 90)
# table = generate_table()
# bg = Image.new('RGB', (1500, 2400), color=(230,230,230))
# new = drawBoard(bg, font_roboto_100, 30, 400, 150, 200, 10, table)
# new.show()

for i in range(100):
    text ="#" + ("0" if i < 10 else "") + str(i)
    table = generate_table()
    bg = Image.new('RGB', (1500, 2400), color=(230,230,230))
    new = drawBoard(bg, font, 30, 400, 150, 200, 10, table, text)
    new.save("bingo" + text + ".png")
