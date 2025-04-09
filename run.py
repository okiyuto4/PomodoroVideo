from PIL import Image, ImageFont, ImageDraw

W, H = 720, 480
COLOR_BLUE = (65, 204, 250)
COLOR_YELLOW = (250, 226, 65)

# use a truetype font
time_font = ImageFont.truetype("arial.ttf", 100)
text_font = ImageFont.truetype("arial.ttf", 72)
image_counter = 0

def draw_internal(bg_color, text, minute, second):
    global W, H, font, image_counter
    
    # draw background
    image = Image.new('RGB', (W, H), color = bg_color)
    draw = ImageDraw.Draw(image)

    # draw title
    _, _, w, h = draw.textbbox((0, 0), text, font=text_font)
    draw.text(((W-w)/2, (H * 0.6-h)/2), text, font=text_font)

    # draw time
    message = f"{minute:02d}:{second:02d}"
    _, _, w, h = draw.textbbox((0, 0), message, font=time_font)
    draw.text(((W-w)/2, (H * 1.2-h)/2), message, font=time_font)

    filename = f"{image_counter:04d}.png"
    image_counter += 1
    # image.show()
    image.save(filename, 'PNG')
    


def draw_working(session_number, minute, second):
    draw_internal(COLOR_BLUE, session_number, minute, second)
    

def draw_break(is_long, minute, second):
    draw_internal(COLOR_YELLOW, "Long break" if is_long else "Short break", minute, second)


# draw_break(True, 3, 5)


def draw_session(session_number):
    global image_counter
    minute = 25
    for i in range(minute * 60):
        draw_working(f'Session {session_number}', (i + 1) // 60, (i + 1)%60)


def draw_break_session(is_long):
    minute = 30 if is_long else 5
    for i in range(minute * 60):
        draw_break(is_long, (i + 1) // 60, (i + 1)%60)

draw_session(1)
draw_break_session(False)

draw_session(2)
draw_break_session(False)

draw_session(3)
draw_break_session(False)

draw_session(4)
draw_break_session(True)




