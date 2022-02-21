# Importing Libraries
import math # Computational Library
import pygame as pg # Visual Library
import random as r # Random Numbers
import time as t # Keeping Time
import string # Naming System
import datetime as date # Time and Date
import webbrowser #Sending Links


# Multiplayer Names
names = ['Frank', 'Alexander', 'Marcus', 'James', 'Robert', 'John', 'Liam', 'Noah', 'William', 'Ben', 'Lucas',
         'Olivia', 'Liam', 'Emma', 'Noah', 'Amelia', 'Oliver', 'Ava', 'Elijah', 'Sophia', 'Lucas',
         'Charlotte', 'Levi', 'Isabella', 'Mason', 'Mia', 'Asher', 'Luna,', 'James', 'Harper', 'Ethan', 'Gianna',
         'Mateo', 'Evelyn', 'Leo', 'Aria', 'Jack', 'Ella', 'Benjamin', 'Ellie', 'Aiden', 'Mila', 'Logan', 'Layla',
         'Grayson', 'Avery', 'Jackson', 'Camila', 'Henry', 'Lily', 'Wyatt', 'Scarlett', 'Sebastian', 'Sofia', 'Carter',
         'Nova', 'Daniel', 'Aurora', 'William', 'Chloe', 'Alexander', 'Riley', 'Ezra', 'Nora', 'Owen', 'Hazel', 'Michael',
         'Abigail', 'Muhammad', 'Rylee', 'Julian', 'Penelope', 'Hudson', 'Elena', 'Luke', 'Zoey', 'Samuel', 'Isla', 'Jacob',
         'Eleanor', 'Lincoln', 'Elizabeth', 'Gabriel', 'Madison', 'Jayden', 'Willow', 'Luca', 'Emilia', 'Maverick', 'Violet',
         'David', 'Emily', 'Josiah', 'Eliana', 'Elias', 'Stella', 'Jaxon', 'Maya', 'Kai', 'Paisley', 'Anthony', 'Everly', 'Isaiah',
         'Addison', 'Eli', 'Ryleigh', 'John', 'Ivy', 'Joseph', 'Grace', 'Matthew']

quotes = ['Ask yourself if what you are doing today is getting you closer to where you want to be tomorrow',
          'You may not be there yet, but you are closer than you were yesterday',
          'Do something today that your future self will thank you for',
          "The only bad workout is the one that didn't happen",
          'A little progress each day adds up to big results',
          'First they will laugh. Then they will copy. Don’t give up',
          'Don’t be afraid of being a beginner',
          'I may not be there yet, but I’m closer than I was yesterday',
          "Remember, Rome wasn’t built in a day. Work hard, good results will come",
          'Less sugar, more fruit. Less soda, more water. Less driving, more walking. Less worry, more sleep. Less words, more action',
          'Nothing truly great ever came from a comfort zone',
          'Believe in yourself and all that you are. Know that there is something inside of you that is greater than any obstacle',
          "Don’t limit your challenges, challenge your limits",
          "Obstacles can’t stop you. Problems can’t stop you. People can’t stop you. Only you can stop you",
          'When you feel like quitting think about why you started',
          'No pain, no gain. Shut up and train']

question_info = {}
diagnostic_extras = ['',
                     '',
                     '',
                     '',
                     'This includes many things like happiness, stress, and stability',
                     '',
                     'These are like drugs, alcohol, and smoking',
                     'If it is intense (weightlifting), multiply by 2',
                     '',
                     '',
                     'An average stress level would be about 30-45',
                     'This means being included, having friends, and not being a misfit',
                     'This includes financial status, social status, and intelligence',
                     '']

def function1(selected):  #Question Number
    question_info.update(Gender=selected)     #Algorithm
    depression_levels = 0.4 if selected == 'Female' else 0.2
    return 1, depression_levels, 2       #Physical or Mental, Amount, Total Max


def function2(selected):
    question_info.update(Age=float(selected))
    selected = float(selected)
    if selected <= 1:
        question_info.update(Class=0)
    elif selected == 2:
        question_info.update(Class=1)
    elif 2 < selected < 6:
        question_info.update(Class=2)
    elif 5 < selected < 13:
        question_info.update(Class=3)
    elif 12 < selected < 19:
        question_info.update(Class=4)
    else:
        question_info.update(Class=5)
    return 0, 0, 0

def function3(selected):
    question_info.update(Height=float(selected))
    return 1, 0, 0

def function4(selected):
    question_info.update(Weight=float(selected))
    question_info.update(BMI=(question_info["Weight"]/question_info["Height"]/question_info["Height"]) * 703)
    extra = 2 if question_info["Gender"] == 'Male' else 4
    score = round(float((question_info["BMI"] - 30)**1.21), 1) + extra if question_info["BMI"] > 30 else extra
    return 1, score * 2, 40

def function5(selected):
    question_info.update(QOL=float(selected))
    if question_info["Age"] < 70 and question_info["QOL"] < 65:
        score = (80 - question_info["QOL"]) * 5/question_info["Age"]
    else:
        score = (80 - question_info["QOL"])/2
    return 1, score, 25

def function6(selected):
    question_info.update(Sleep=float(selected))
    if 14.5 - question_info["Class"] >= float(selected) >= 12 - question_info["Class"]:
        return 0, 10, 10
    elif 12 - question_info["Class"] > float(selected):
        return 0, (10 - (12 - question_info["Class"] - float(selected))) - (12 - question_info["Class"] - float(selected)), 10
    else:
        return 0, (10 - abs(14 - question_info["Class"] - float(selected))), 10

def function7(selected):
    question_info.update(Addiction=selected)
    result = 5 if selected == 'No' else 1
    return 0, result, 5

def function8(selected):
    question_info.update(PA=float(selected))
    selected = float(selected) * 60
    exercise = 5 + (selected-150)/100 if selected >= 150 else selected/30
    value = 23 - (20-question_info["Age"])*.75 if question_info["Age"] < 20 else 23
    return 0, exercise + 10-(abs(question_info["BMI"]-value)), 5 + 10

def function9(selected):
    question_info.update(Junk=selected)
    if selected == 'None':
        return 0, 20, 20
    elif selected == 'A Bit':
        return 0, 15.5, 20
    elif selected == 'A Decent Amount':
        return 0, 4, 20
    else:
        return 0, 0, 30

def function10(selected):
    question_info.update(Healthy=selected)
    if selected == 'None':
        return 0, 0, 15
    elif selected == 'A Bit':
        return 0, 2, 10
    elif selected == 'A Decent Amount':
        return 0, 8, 12
    else:
        return 0, 10, 10

def function11(selected):
    question_info.update(Stress=float(selected))
    return 1, float(selected)/4, 25

def function12(selected):
    question_info.update(FittingIn=selected)
    if selected == 'Yes':
        return 1, 0, 15
    else:
        return 1, 10, 15

def function13(selected):
    question_info.update(Status=float(selected))
    selected = 100 - float(selected)
    socials = selected ** 1.1
    return 1, socials/5, 20

def function14(selected):
    question_info.update(Status=float(selected))
    selected = float(selected)
    if selected < question_info["Weight"] *.7:
        return 0, 13 - .18 * (question_info["Weight"] * .7 - selected), 13
    else:
        return 0, 13, 13

mental_health_response = {0:["Exercise, Sleep, and Socialization could help", "Ok", "That's Amazing!"],
                          1:["Great!", "Focus on wellness, staying connected, and having fun", "Visiting a specialist, being health, and mindfulness are suggestions"],
                          2:["Amazing!", "You might want to exercise and become more mindful", "You should take care of yourself with exercise, calming yourself and other relaxing activities"],
                          3:["That's Good!", "Be sure to not use screens and stay away from vigorous work before bed", "Exercise, rise and wake at normal times, and stay away from screens"],
                          4:["Good!", "You should try being active or trying to find similar people to you", "It is best if you try to make new friends, be around pets, or get support"],
                          5:["Nice!", "Practicing Mindfulness and calming the body is good for this", "Have a healthy lifestyle, try to have a positive attitude, and do things that make you feel good"],
                          6:["Get involved with your passion, do not put it aside", "Try new things, hang out with people who have the same interests, and put happiness first", "Ok, that's good"],
                          7:["Wonderful!", "Make sure you sleep and eat well and exercise", "Try to live healthier, exercise, sleep well, and do activities that excite you"]}



level = [(255, 0, 0), (255, 153, 153), (255, 128, 0), (255, 255, 102), (153, 255, 153), (0, 255, 0)]
challenge_info = []
logged_info = []
fade_color1 = [50, t.time(), 1]
diagnostic_info = [[0, 0], [0, 0]]
colors = [(124, 124, 132), (255, 255, 255), (6, 108, 250), (0, 0, 0), (112, 180, 235), (58, 59, 61), (168, 183, 200), (2, 55, 129)]
finished_questions = []
diagnostic_results = []

# Setting up the window
pg.init()
pg.display.init()
screen = pg.display.set_mode((1000, 500), pg.RESIZABLE)
heart = pg.image.load('heart.png')
pg.display.set_caption('Health Assistant')
pg.display.set_icon(heart)
fonts = [pg.font.SysFont('comicsansms', 30, False, False),
         pg.font.SysFont('comicsansms', 20, False, False),
         pg.font.SysFont('comicsansms', 15, False, False),
         pg.font.SysFont('comicsansms', 40, False, False),
         ]
health_points = [0, 0, 0, 0]
pause_frame = [False]

#Loading Images
image_pack = {
    "DownArrow": pg.image.load('arrow.png'),
    "UpArrow": pg.transform.flip(pg.image.load('arrow.png'), False, True),
    "Weight": [pg.image.load('images/weight_40x40.png')],
    "BMI": [pg.image.load('images/bmi.png'), 3],
    "Calories": [pg.image.load('images/calories.png')],
    "Diet": [pg.image.load('images/diet_40x40.png')],
    "Sleep": [pg.image.load('images/sleep.png'), 3],
    "Activity": [pg.image.load('images/physical_activity_40x40.png')],
    "ColorFade": pg.image.load('images/colorfade.jpeg'),
    "Water": [pg.image.load('images/waterbottle.png'), 18],
    "Cigar": [pg.image.load('images/cigar.png')],
    "Waist": [pg.image.load('images/waist.png'), 0],
    "Heart Rate": [pg.image.load('images/heart_rate.png')],
    "Blood": [pg.image.load('images/blood.png')],
    "Dumbbell": [pg.image.load('images/dumbell.png'), 10],
    "PushUp": [pg.image.load('images/pushup.png'), 8],
    "PullUp": [pg.image.load('images/pullup.png'), 15],
    "Cycle": [pg.image.load('images/cycle.png'), 12],
    "Swimming": [pg.image.load('images/swimming.png'), 10],
    "None": [None]
}


recalculate = [False]

#Loading the save file

with open('health.txt', 'r+') as save:
    for index, lines in enumerate(save):
        if 0 <= index <= 3:
            health_points[index] = int(lines.strip())
        if index == 4:
            if lines.strip().split('-')[-1] != str(date.date.today()).split('-')[-1]:
                health_points.append(True)
            else:
                health_points.append(False)
        if index > 4:
            properties = lines.strip().split('  ')
            if len(properties[2]) == 1 and properties[2] == '.':
                properties[2] = ''
            logged_info.append({'Info':properties[1], 'Date': properties[2], 'Extra':properties[0]})

leader_info = [] # Weekly Points, Weekly Days Left, Today points, Beginning Point

with open('leaderboard.txt', 'r+') as leaders:
    try:
        for index, lines in enumerate(leaders):
            leader_info.append(int(lines.strip()))
        if leader_info[1] == 0:
            leader_info[1] = 7
            leader_info[0] = 0
        if health_points[4]:
            leader_info[1] -= 1
            leader_info[2] = 0
        leader_info.pop()
        leader_info.append(health_points[0])
    except:
        leader_info = [0, 0, 0, 0]



def center(surface, x, y):
    w, h = surface.get_width(), surface.get_height()
    screen.blit(surface, (x - w / 2, y - h / 2))


def globalize():
    global screen
    global heart
    global health_points


def click(x, y, x1, y2, w, h):
    return x1 < x < (x1 + w) and y2 < y < (y2 + h)


def blit_text(text, pos, font, w, h):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = w, h
    orx, ory = pos
    x, y = pos
    total_lines = 0
    for line in words:
        current_words = ''
        for word in line:
            word_surface = font.render(word, True, colors[3])
            word_width, word_height = word_surface.get_size()
            if x + word_width  >= max_width + orx or line.index(word) + 1 == len(line):
                center(font.render(current_words + word, True, colors[3]), orx + max_width/2, y)
                current_words = ''
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
                total_lines += 1
            if x == pos[0] and total_lines != 0:
                current_words = ''
            else:
                current_words += f'{word} '
            x += word_width + space
    return total_lines


class InputBox:
    def __init__(self, x, y, w, h, text='', title='', extra='', isint=False):
        self.rect = pg.Rect(x, y, w, h)
        self.isint = isint
        self.color = (0, 0, 0)
        self.text = text
        self.start = text
        self.txt_surface = fonts[1].render(text, True, self.color)
        self.active = False
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.title = title
        self.extra = extra

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    if self.text == self.start:
                        self.text = ''
                    else:
                        self.text = self.text[:-1]
                else:
                    if self.isint:
                        try:
                            self.text += str(int(event.unicode))
                        except:
                            if event.unicode == '.':
                                self.text += '.'
                            else:
                                pass
                    else:
                        self.text += event.unicode
                # Re-render the text.
                self.color = colors[2] if self.active else (0, 0, 0)

    def update(self):
        # Resize the box if the text is too long.
        width = max(self.w, self.txt_surface.get_width() + 10)
        self.rect.w = width
        # Change the current color of the input box.
        self.color = colors[2] if self.active else (0, 0, 0)
        self.txt_surface = fonts[1].render(self.text + self.extra, True, self.color)

    def draw(self):
        text = fonts[1].render(self.title, True, colors[3])
        w, h = text.get_width(), text.get_height()
        screen.blit(text, (self.x, self.y))
        # Blit the text.
        screen.blit(self.txt_surface, (self.x + 5 + w, self.rect.y + 5))
        # Blit the rect.
        self.rect.x = self.x + w
        pg.draw.rect(screen, self.color, self.rect, 4, 5)
        second_text = fonts[1].render(self.text, True, colors[3])


class Button:

    def __init__(self, x, y, w, h, font, text, color, checkbox=False, img=None, forward=0):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.font, self.text, self.color = font, text, color
        self.checkbox = checkbox
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.box = [self.x + 30 + self.text_surface.get_width(), self.y + (self.h/2 - 10), 20, 20]
        self.clicked = False
        self.image = img
        self.forward = forward

    def draw(self):
        pg.draw.rect(screen, self.color, [self.x + 5, self.y + 5, self.w - 10, self.h - 10])
        if self.image is not None:
            center(self.image, self.x + self.w - self.image.get_width()/2 - 5 + self.forward, self.y + self.h/2)
        pg.draw.rect(screen, (0, 0, 0), [self.x, self.y, self.w, self.h], 5, 10)
        screen.blit(self.text_surface, (self.x + 10, self.y + (self.h / 2) - (self.text_surface.get_height() / 2)))
        if self.checkbox:
            if self.clicked:
                pg.draw.line(screen, (0, 255, 0), (self.x + 30 + self.text_surface.get_width(), self.y + self.h/2 - 3),
                             (self.x + 37 + self.text_surface.get_width(), self.y + self.h/2 + 7), 3)
                pg.draw.line(screen, (0, 255, 0), (self.x + 37 + self.text_surface.get_width(), self.y + self.h/2 + 7),
                             (self.x + 48 + self.text_surface.get_width(), self.y + self.h/2 - 10), 3)
                pause_frame[0] = True
            pg.draw.rect(screen, (0, 0, 0), [self.x + 30 + self.text_surface.get_width(), self.y + (self.h/2 - 10), 20, 20], 3)
    def check(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and click(*pg.mouse.get_pos(), *self.box):
            self.clicked = not self.clicked
        return event.type == pg.MOUSEBUTTONDOWN and click(*pg.mouse.get_pos(), self.x, self.y, self.w, self.h) and not click(*pg.mouse.get_pos(), *self.box)


class Event:

    def __init__(self):
        self.run = True

    # Checking all Events
    def check(self, all_tabs):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = not self.run
            if event.type == pg.RESIZABLE:
                pg.display.set_mode((event.w, event.h))
            all_tabs.check(event)
            all_tabs.switch_tabs(event)


class Challenge:
    def __init__(self, title, points, days, x, y):
        self.title = title
        self.points_given = points
        self.days_left = days
        text = fonts[0].render(title, True, (255, 0, 0))
        self.position = x, y
        self.main_button = Button(x, y, 200, text.get_height() + 10, fonts[1], title, colors[4], True)
        self.show = False


    def draw(self):
        self.main_button.draw()
        if self.show:
            pg.draw.rect(screen, colors[0], [self.position[0] + 5, self.position[1] + 65, self.main_button.w - 10, 70])
            pg.draw.rect(screen, (0, 0, 0), [self.position[0], self.position[1] + 60, self.main_button.w, 80], 5, 10)
            screen.blit(fonts[2].render(f'Title: {self.title}', True, colors[3]), (self.position[0] + 10, self.position[1] + 65))
            screen.blit(fonts[2].render(f'Days left: {self.days_left}', True, colors[3]), (self.position[0] + 10, self.position[1] + 85))
            screen.blit(fonts[2].render(f'Points Given: {self.points_given}', True, colors[3]), (self.position[0] + 10, self.position[1] + 105))

    def check(self, event):
        if self.main_button.check(event):
            self.show = not self.show


class HomePage:

    def __init__(self, x, y, text):
        self.show = True
        self.tab = Button(x, y, 205, 50, fonts[1], text, colors[0])
        self.leaderboard = []
        for randomness in names:
            randomness = f'{randomness} {r.choice(string.ascii_uppercase)}.'
            main_int = int((r.randint(0, 1000) * r.randint(0, 1000)) / 10000)
            self.leaderboard.append({'Name':randomness, 'Points':main_int, 'Multiply': r.randint(20, 70) / 10 * main_int})
        player = {'Name':'You', 'Points':leader_info[2], 'Multiply':leader_info[0]}
        self.leaderboard.append(player)
        self.player = player
        self.week_leaderboard = sorted(self.leaderboard, key = lambda p: p['Multiply'], reverse=True)
        self.leaderboard = sorted(self.leaderboard, key = lambda p: p['Points'], reverse=True)

        self.mini_pages = ['True Home', 'Challenges', 'Leaderboards', 'Inspiration', 0]
        self.mini_buttons = [Button(0 + 50/3, 410, 300, 80, fonts[0], 'Challenges', colors[1]),
                             Button(350, 410, 300, 80, fonts[0], 'Leaderboards', colors[1]),
                             Button(600 + 250/3, 410, 300, 80, fonts[0], 'Inspiration', colors[1])]
        self.mini_functions = [self.true_home, self.challenges, self.competition, self.inspiration]
        self.exit = Button(850, 100, 125, 60, fonts[0], 'Exit', colors[4])
        self.locations = [(10, 100), (220, 100), (430, 100), (640, 100), (10, 250), (220, 250), (430, 250), (640, 250)]
        self.all_challenge = []
        self.input_title = InputBox(50, 340, 150, 45, 'Title')
        self.input_days = InputBox(250 + 50/3, 340, 150, 45, 'Days', '', '', True)
        self.input_points = InputBox(450 + 100/3, 340, 150, 45, 'Points', '', '', True)
        self.inputs = [self.input_title, self.input_days, self.input_points]
        self.enter_button = Button(700, 340, 200, 45, fonts[1], 'Add Challenge', (0, 255, 0))
        self.index = 0
        for index1, c in enumerate(challenge_info):
            self.all_challenge.append(Challenge(*c, *self.locations[index1]))


    def true_home(self):
        screen.blit(fonts[0].render(f'Health Points: {health_points[0]}', True, colors[3]), (100, 100))
        screen.blit(fonts[0].render(f'Physical Health Rating: {health_points[3]}', True, colors[3]), (100, 140))
        screen.blit(fonts[0].render(f'Mental Health Rating: {health_points[2]}', True, colors[3]), (100, 180))
        screen.blit(fonts[0].render(f'Days Active: {health_points[1]}', True, colors[3]), (100, 220))

    def challenges(self):
        self.exit.draw()
        pg.draw.line(screen, (0, 0, 0), (0, 320), (1000, 320), 5)
        self.enter_button.draw()
        for boxes in self.inputs:
            boxes.update()
            boxes.draw()
        [challenges1.draw() for challenges1 in self.all_challenge if True]
        for index_of, challenge1 in enumerate(self.all_challenge):
            if challenge1.days_left == 0 or challenge1.main_button.clicked:
                self.all_challenge.remove(challenge1)
                challenge_info.remove(challenge_info[index_of])
                health_points[0] = health_points[0] + challenge1.points_given if not challenge1.days_left == 0 else health_points[0]
                self.player['Points'] = self.player['Points'] + challenge1.points_given if not challenge1.days_left == 0 else self.player['Points']
                self.player['Multiply'] = self.player['Multiply'] + challenge1.points_given if not challenge1.days_left == 0 else self.player['Multiply']

                for people in self.leaderboard:
                    if people['Name'] == 'You':
                        people['Points'] = self.player['Points']
                        people['Multiply'] = self.player['Multiply']
                self.leaderboard = sorted(self.leaderboard, key=lambda p: p['Points'], reverse=True)
                self.week_leaderboard = sorted(self.leaderboard, key=lambda p: p['Points'], reverse=True)


                for index, c in enumerate(self.all_challenge):
                    c.position = self.locations[index]
                    c.main_button.x = self.locations[index][0]
                    c.main_button.y = self.locations[index][1]
                    c.main_button.box[0] = c.main_button.x + 30 + c.main_button.text_surface.get_width()
                    c.main_button.box[1] = c.main_button.y + (c.main_button.h / 2 - 10)

    def competition(self):
        self.exit.draw()
        pg.draw.rect(screen, (0, 0, 0), [540, 115, 260, 265], 5, 10)
        pg.draw.rect(screen, (0, 0, 0), [140, 115, 260, 265], 5, 10)
        center(fonts[0].render('Daily Leaderboard', True, colors[3]), 670, 95)
        center(fonts[0].render('Weekly Leaderboard', True, colors[3]), 270, 95)
        if self.leaderboard.index(self.player) <= 10:
            for i, people in enumerate(self.leaderboard[:10]):
                screen.blit(fonts[1].render(f'{people["Name"]} - {people["Points"]} points', True, colors[3]), (550, i*25 + 120))
        else:
            for i, people in enumerate(self.leaderboard[:9]):
                screen.blit(fonts[1].render(f'{people["Name"]} - {people["Points"]} points', True, (0, 0, 0)), (550, i*25 + 120))
            screen.blit(fonts[1].render(f'{self.player["Name"]} - {self.player["Points"]} points', True, colors[3]),
                        (550, 9 * 25 + 120))

        if self.week_leaderboard.index(self.player) <= 10:
            for i, people in enumerate(self.week_leaderboard[:10]):
                screen.blit(fonts[1].render(f'{people["Name"]} - {int(people["Multiply"])} points', True, colors[3]), (150, i*25 + 120))
        else:
            for i, people in enumerate(self.week_leaderboard[:9]):
                screen.blit(fonts[1].render(f'{people["Name"]} - {int(people["Multiply"])} points', True, colors[3]), (150, i*25 + 120))
            screen.blit(fonts[1].render(f'{self.player["Name"]} - {self.player["Multiply"]} points', True, colors[3]), (150, 9*25 + 120))

    def inspiration(self):
        blit_text(quotes[self.index], (50, 100), fonts[0], 500, 200)
        screen.blit(fonts[1].render('Click for Next Inspirational Quote', True, colors[3]), (150, 350))
        self.exit.draw()


    def check(self, event):
        for index, mini_sections in enumerate(self.mini_buttons):
            if mini_sections.check(event):
                self.mini_pages[4] = index + 1
        if self.mini_pages[4] != 0 and self.exit.check(event):
            self.mini_pages[4] = 0
        if self.mini_pages[4] == 1:
            for challenges in self.all_challenge:
                challenges.check(event)
            for boxes in self.inputs:
                boxes.handle_event(event)
            if self.enter_button.check(event):
                try:
                    self.all_challenge.append(Challenge(self.input_title.text, int(self.input_points.text),
                                                        int(self.input_days.text), *self.locations[len(self.all_challenge)]))
                    challenge_info.append([self.input_title.text, int(self.input_points.text), int(self.input_days.text)])
                except ValueError:
                    screen.blit(fonts[1].render('You have entered an invalid value', True, (255, 0, 0)), (500, 250))
                    pg.display.update()
                    t.sleep(1)
                finally:
                    self.input_title.text = 'Title'
                    self.input_points.text = 'Points'
                    self.input_days.text = 'Days'

        if self.mini_pages[4] == 3:
            if event.type == pg.MOUSEBUTTONDOWN:
                self.index = r.randint(0, len(quotes) - 1)



    def draw(self):
        self.tab.draw()

    def page(self):
        self.mini_functions[self.mini_pages[4]]()
        pg.draw.rect(screen, colors[2], [0, 400, 1000, 100])
        pg.draw.line(screen, (0, 0, 0), (0, 400), (1000, 400), 5)
        for mini_sections in self.mini_buttons:
            mini_sections.draw()


class MultipleChoice:

    def __init__(self, num, total, question, algorithm, choices):
        self.show_string = f'Question {num} of {total}'
        self.question = question + '?'
        self.extra = diagnostic_extras[num - 1]
        self.submit = Button(800, 400, 100, 50, fonts[1], 'Next', colors[0])
        if num == total:
            self.submit.text = 'Submit'
            self.submit.text_surface = self.submit.font.render(self.submit.text, True, colors[3])
        self.choices = []
        self.selected = None
        self.algorithm = algorithm
        for ints, options in enumerate(choices):
            self.choices.append(Button(350, 210 + ints * 70, 300, 60, fonts[0], f'{options}', colors[0]))


    def draw(self):
        center(fonts[0].render(self.show_string, True, colors[3]), 500, 100)
        center(fonts[1].render(f'{self.extra}', True, colors[3]), 500, 185)
        center(fonts[3].render(self.question, True, colors[3]), 500, 140)
        for options in self.choices:
            options.draw()
        self.submit.draw()

    def check(self, event):
        if self.submit.check(event) and self.selected is not None:
            return True
        for choices in self.choices:
            if choices.check(event):
                for options in self.choices:
                    options.color = colors[0]
                choices.color = colors[6]
                self.selected = choices.text

    def execute(self):
        result = self.algorithm(self.selected)
        diagnostic_info[result[0]][0] += result[1]
        diagnostic_info[result[0]][1] += result[2]

class InputChoice:

    def __init__(self, num, total, question, algorithm, extra, integers):
        self.show_string = f'Question {num} of {total}'
        self.extra = diagnostic_extras[num - 1]
        self.question = question + '.'
        self.submit = Button(800, 400, 100, 50, fonts[1], 'Next', colors[0])
        if num == total:
            self.submit.text = 'Submit'
            self.submit.text_surface = self.submit.font.render(self.submit.text, True, (0, 0, 0))
        self.algorithm = algorithm
        self.text_box = InputBox(375, 210, 250, 50, '', '', extra, integers)

    def draw(self):
        center(fonts[0].render(self.show_string, True, colors[3]), 500, 100)
        center(fonts[1].render(f'{self.extra}', True, colors[3]), 500, 185)
        center(fonts[3].render(self.question, True, colors[3]), 500, 140)
        self.text_box.draw()
        self.text_box.update()
        self.submit.draw()

    def check(self, event):
        self.text_box.handle_event(event)
        if self.submit.check(event) and self.text_box.text != '':
            return True

    def execute(self):
        result = self.algorithm(self.text_box.text)
        diagnostic_info[result[0]][0] += result[1]
        diagnostic_info[result[0]][1] += result[2]


class Diagnostic:

    def __init__(self):
        self.main_button = Button(325, 220, 350, 60, fonts[3], 'Take Diagnostic', colors[2])
        self.show = False
        self.previous = Button(100, 400, 100, 50, fonts[1], 'Previous', colors[0])
        self.exit = Button(775, 75, 175, 40, fonts[2], 'Save and Exit', (200, 0, 0))
        self.active_question = 1
        self.questions = {1:[1, 2, 'What is your Gender', function1, ['Female', 'Male'], True],
                          2:[2, 2, 'How old are you', function2, ' years old', True, False],
                          3:[3, 3, 'How tall are you', function3, ' inches', True, False],
                          4:[4, 4, 'What is your body weight', function4, ' pounds', True, False],
                          5:[5, 4, 'On a scale of 1-100, what is your quality of life', function5, '', True, False],
                          6:[6, 4, 'How much do you sleep a day', function6, ' hours', True, False],
                          7:[7, 5, 'Do you have any extreme addictions', function7, ['Yes', 'No'], True],
                          8:[8, 1, 'How much physical activity do you do each week', function8, ' hours', True, False],
                          9:[9, 1, 'How much junk/unhealthy food do you eat', function9, ['None', 'A Bit', 'A Decent Amount', 'A Lot'], True],
                          10:[10, 0, 'How much healthy food do you eat', function10, ['None', 'A Bit', 'A Decent Amount', 'A Lot'], True],
                          11:[11, 0, 'On a scale of 1-100, how much stress do you have', function11, '', True, False],
                          12:[12, 0, 'Do you feel like you fit into society', function12, ['Yes', 'No'], True],
                          13:[13, 0, 'On a scale of 1-100, rate your status in life', function13, '', True, False],
                          14:[14, 5, 'How many fluid ounces of water do you drink a day', function14, '', True, False]}
        for indexes in range(1, len(self.questions.keys()) + 1):
            self.questions[indexes][1] = len(self.questions.keys())
            if self.questions[indexes][-1]:
                self.questions[indexes].pop()
                self.questions[indexes] = MultipleChoice(*self.questions[indexes])
            else:
                self.questions[indexes].pop()
                self.questions[indexes] = InputChoice(*self.questions[indexes])
        self.submit = False
        self.exit_button = Button(400, 400, 200, 50, fonts[0], 'Exit', colors[0])

    def display(self):
        self.main_button.draw()

    def active(self):
        if self.submit:
            center(fonts[0].render('You have finished this diagnostic', True, colors[3]), 500, 100)
            center(fonts[0].render(f'Physical Health Rating: {int(diagnostic_info[0][0]/diagnostic_info[0][1]*100)}', True, colors[3]), 500, 200)
            center(fonts[0].render(f'Mental Health Rating: {int((1-diagnostic_info[1][0]/diagnostic_info[1][1])*100)}', True, colors[3]), 500, 300)
            self.exit_button.draw()
        else:
            self.exit.draw()
            if self.active_question != 1:
                self.previous.draw()
            self.questions[self.active_question].draw()

    def active_execution(self, event):
        if self.exit.check(event):
            self.show = False
        if self.questions[self.active_question].check(event):
            if self.active_question < len(self.questions.keys()):
                self.active_question += 1
            else:
                for questions in range(1, len(self.questions) + 1):
                    self.questions[questions].execute()
                self.show = True
                self.submit = True
                self.active_question = 1
                for index_of_list in range(1, 2):
                    if diagnostic_info[index_of_list][0] > diagnostic_info[index_of_list][1]:
                        diagnostic_info[index_of_list][0] = diagnostic_info[index_of_list][1] * 0.9
                    if diagnostic_info[index_of_list][0] < 0:
                        diagnostic_info[index_of_list][0] = 0
                if diagnostic_info[0][0] > diagnostic_info[0][1]:
                    diagnostic_info[0][0] = diagnostic_info[0][1]
                logged_info.insert(0, {
                    "Info": f'Physical Rating - {int(diagnostic_info[0][0] / diagnostic_info[0][1] * 100)} Mental Rating - {int((1 - diagnostic_info[1][0] / diagnostic_info[1][1]) * 100)}',
                    "Date": date.date.today(), "Extra": 'Diagnostic: '})
                health_points[2:3] = int(diagnostic_info[0][0] / diagnostic_info[0][1] * 100), int(
                    (1 - diagnostic_info[1][0] / diagnostic_info[1][1]) * 100)
        if self.active_question != 1 and self.previous.check(event):
            self.active_question -= 1
        if self.exit_button.check(event) and self.submit:
            self.submit, self.show = False, False
            diagnostic_info[0] = [0, 0]
            diagnostic_info[1] = [0, 0]



    def execution(self, event):
        if self.main_button.check(event):
            self.show = True


class DiagnosticHome:
    def __init__(self, x, y, text):
        self.show = False
        self.active = False
        self.tab = Button(x, y, 205, 50, fonts[1], text, colors[1])
        self.diagnostic = Diagnostic()

    def draw(self):
        self.tab.draw()

    def page(self):
        if self.diagnostic.show:
            self.diagnostic.active()
        else:
            self.diagnostic.display()

    def check(self, event):
        if self.diagnostic.show:
            self.diagnostic.active_execution(event)
        else:
            self.diagnostic.execution(event)

class Logger:

    def __init__(self, x, y, text):
        self.show = False
        self.drop = False
        self.selected = None
        self.tab = Button(x, y, 205, 50, fonts[1], text, colors[1])
        self.page_scroll = 0
        self.sections = [{'Name':'Weight', 'Named': 'Weight: '},
                         {'Name':'BMI', 'Named': 'BMI: '},
                         {'Name':'Burned Calories', 'Named': 'Burned '},
                         {'Name':'Exercise', 'Named': 'Exercised for '},
                         {'Name':'Consumed Calories', 'Named': 'Ate '},
                         {'Name':'Sleep', 'Named': 'Slept for '},
                         {'Name':'Hydration', 'Named': 'Drank '},
                         {'Name':'Smoking', 'Named': 'Smoked '},
                         {'Name':'Waist Circumference', 'Named':''},
                         {'Name':'Neck Circumference', 'Named':''},
                         {'Name':'Sys. Blood Pressure', 'Named':'Systolic Blood Pressure is '},
                         {'Name':'Dia. Blood Pressure', 'Named':'Systolic Blood Pressure is '},
                         {'Name':'Active Heart Rate', 'Named':'Active Heart Rate is '},
                         {'Name':'Resting Heart Rate', 'Named':'Resting Heart Rate is '},
                         {'Name':'Squats', 'Named':'Squatted '},
                         {'Name':'Bench Press', 'Named':'Benched '},
                         {'Name':'Deadlift', 'Named':'Deadlifted '},
                         {'Name':'Leg Press', 'Named':'Leg pressed '},
                         {'Name':'Bicep Curl', 'Named':'Bicep curled '},
                         {'Name':'Push Up', 'Named':''},
                         {'Name':'Pull Up', 'Named':''},
                         {'Name':'Overhead Press', 'Named':'Overhead pressed '},
                         {'Name':'Snatches', 'Named':'Snatched '},
                         {'Name':'Running', 'Named':'Ran for '},
                         {'Name':'Cycling', 'Named':'Cycled for '},
                         {'Name':'Swimming', 'Named':'Swam for '},
                         {'Name':'Carbohydrates', 'Named':'Consumed '},
                         {'Name':'Protein', 'Named':'Consumed '},
                         {'Name':'Sugar', 'Named':'Consumed '},
                         {'Name':'Fat', 'Named':'Consumed '},
                         {'Name':'Sat. fat', 'Named':'Consumed '},
                         {'Name':'Trans. fat', 'Named':'Consumed '},
                         {'Name':'Sodium', 'Named':'Consumed '},
                         {'Name':'Dietary Fiber', 'Named':'Consumed '},
                         {'Name':'Cholesterol', 'Named':'Consumed '}]
        self.measuring = [' lbs', ' BMI', ' calories', ' minutes',' calories', ' hours', ' gallons of fluid',
                          ' cigs/vapes', ' inch circum.', ' inch circum.', ' mm Hg', ' mm Hg', ' BPM', ' BPM', ' lbs',
                          ' lbs', ' lbs', ' lbs', ' lbs', ' push ups', ' pull ups', ' lbs', ' lbs', ' minutes', ' minutes',
                          ' minutes', ' grams of carbs', ' grams of protein', ' grams of added sugar', ' grams of fat',
                          ' grams of saturated fat', ' grams of trans fat', ' milligrams of sodium', ' grams of dietary fiber',
                          ' milligrams of cholesterol']
        self.selector = []
        self.dropdown = Button(100, 75, 200, 50, fonts[0], 'Select', colors[2])
        self.input = InputBox(375, 75, 190, 45, '', '', '', True)
        self.extra = InputBox(625, 75, 150, 45, '', '', '', True)
        self.submit = Button(820, 75, 150, 50, fonts[1], 'Log Info', colors[0])
        self.index = None
        self.extra_active = False
        images = ["Weight", "BMI", "Calories", "Activity", "Diet", "Sleep", "Water", "Cigar", "Waist", "Waist", "Blood",
                  "Blood", "Heart Rate", "Heart Rate", "Dumbbell", "Dumbbell", "Dumbbell", "Dumbbell", "Dumbbell", "PushUp", "PullUp", "Dumbbell", "Dumbbell",
                  "Activity", "Cycle", "Swimming", "None", "None", "None", "None", "None", "None", "None", "None", "None"]
        self.extra_input = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', [' for ', ' reps'], [' for ', ' reps'],
                            [' for ', ' reps'], [' for ', ' reps'], [' for ', ' reps'], '', '', [' for ', ' reps'],
                            [' for ', ' reps'], '', '', '', '', '', '', '', '', '', '', '', '']
        for index_i, image in enumerate(self.sections):
            self.selector.append(Button(100 + (index_i % 28)// 7 * 195, 150 + ((index_i % 28) % 7) * 45, 200, 50, fonts[2], image["Name"], colors[6], False, *image_pack[images[index_i]]))
        self.total_pages = math.ceil(len(images)/28)

    def check(self, event):
            if click(*pg.mouse.get_pos(), 20, 175, 50, 50) and event.type == pg.MOUSEBUTTONDOWN and self.page_scroll > 0:
                self.page_scroll -= 1
            if click(*pg.mouse.get_pos(), 20, 275, 50, 50) and event.type == pg.MOUSEBUTTONDOWN and self.page_scroll < self.total_pages - 1:
                self.page_scroll += 1

            if self.dropdown.check(event):
                self.drop = not self.drop
            if self.drop:
                for var in self.selector:
                    if var.check(event):
                        indexed = [titles["Name"] for titles in self.sections]
                        self.selected = var
                        self.input.extra = self.measuring[indexed.index(var.text)]
                        if self.extra_input[indexed.index(var.text)] != '':
                            self.extra.extra = self.extra_input[indexed.index(var.text)][1]
                            self.extra_active = True
                        else:
                            self.extra_active = False
                        self.index = self.sections[indexed.index(var.text)]
            if self.selected is not None:
                self.input.handle_event(event)
                if self.extra_active:
                    self.extra.handle_event(event)
            if self.input.active and event.type == pg.KEYDOWN and pg.key.name(event.key) == 'return' and self.input.text != '':
                today = date.date.today()
                if self.extra_active:
                    if self.extra.text != '':
                        logged_info.insert(0, {"Info": self.input.text + self.input.extra + self.extra_input[self.selector.index(self.selected)][0] + self.extra.text +
                                    self.extra_input[self.selector.index(self.selected)][1], "Date": today, "Extra": self.index["Named"]})
                        recalculate[0] = not recalculate[0]
                        self.selected = None
                        self.input.text = ''
                        self.extra.text = ''
                else:
                    logged_info.insert(0, {"Info": self.input.text + self.input.extra, "Date": today,
                                           "Extra": self.index["Named"]})
                    recalculate[0] = not recalculate[0]
                    self.selected = None
                    self.input.text = ''
            if self.submit.check(event) and self.selected is not None and self.input.text != '':
                today = date.date.today()
                if self.extra_active:
                    if self.extra.text != '':
                        logged_info.insert(0, {
                            "Info": self.input.text + self.input.extra + self.extra_input[self.selector.index(self.selected)][0] + self.extra.text +
                                    self.extra_input[self.selector.index(self.selected)][1], "Date": today, "Extra": self.index["Named"]})
                        recalculate[0] = not recalculate[0]
                        self.selected = None
                        self.input.text = ''
                        self.extra.text = ''
                else:
                    logged_info.insert(0, {"Info": self.input.text + self.input.extra, "Date": today,
                                           "Extra": self.index["Named"]})
                    recalculate[0] = not recalculate[0]
                    self.selected = None
                    self.input.text = ''

    def draw(self):
        self.tab.draw()

    def page(self):
            self.dropdown.draw()
            screen.blit(image_pack["UpArrow"], (20, 175))
            screen.blit(fonts[1].render(f'{self.page_scroll + 1} of {self.total_pages}', True, (0, 0, 0)), (18, 238))
            screen.blit(image_pack["DownArrow"], (20, 275))
            if self.drop:
                for var in self.selector[0 + self.page_scroll * 28:28 + self.page_scroll*28]:
                    var.draw()
            if self.selected is not None:
                self.input.draw()
                self.input.update()
                if self.extra_active:
                    self.extra.draw()
                    self.extra.update()
                    screen.blit(fonts[1].render(self.extra_input[self.selector.index(self.selected)][0], True, (0, 0, 0)), (575, 85))
            self.submit.draw()





class MentalQuestion:

    def __init__(self, begin_text, option1, option2, option3, x, y, scores, position, w=120, h=40):
        self.scores = scores
        self.position = position
        self.show = False
        self.first = begin_text
        text = fonts[1].render(begin_text.replace('{}', '_'), True, (0, 0, 0))
        text_w = text.get_width()
        self.main = Button(x, y, text_w + 30, h, fonts[1], begin_text.replace('{}', '_'), colors[0])
        self.options = [Button(x + 40 + text_w, y - 10, w * 3 + 45, h + 20, fonts[0], '', colors[2]),
                        Button(x + text_w + 50, y, w, h, fonts[2], option1, colors[6]),
                        Button(x + w + 60 + text_w, y, w, h, fonts[2], option2, colors[6]),
                        Button(x + w * 2 + 70 + text_w, y, w, h, fonts[2], option3, colors[6])
                        ]

    def draw(self):
        self.main.draw()
        if self.show:
            for button in self.options:
                button.draw()

    def check(self, event, parent):
        if self.main.check(event):
            self.show = not self.show
        if self.show:
            for i, button in enumerate(self.options):
                if button.check(event) and i != 0:
                    finished_questions[self.position] = True
                    parent.questions[self.position] = None
                    parent.chat.append(f'{mental_health_response[self.position][i - 1]}')
                    parent.chat.append(f'{self.first.replace("{}", button.text)}')
                    health_points[3] += self.scores[i - 1]

    def finish(self, parent):
        finished_questions[self.position] = True
        parent.questions[self.position] = None


class MentalHealth:

    def __init__(self, x, y, text):
        self.show = False
        self.text_lines = []
        self.tab = Button(x, y, 205, 50, fonts[1], text, colors[1])
        self.questions = [MentalQuestion('I feel {}', 'sad', 'normal', 'happy', 100, 200, [-3, 0, 3], 0),
                          MentalQuestion('I am {} depressed', 'not', 'a bit', 'very', 100, 250, [3, -2, -7], 1),
                          MentalQuestion('I am {} stressed', 'not', 'a bit', 'very', 100, 300, [3, 0, -2], 2),
                          MentalQuestion('My sleep was {}', 'great', 'ok', 'bad', 100, 350, [2, 0, -3], 3),
                          MentalQuestion('I have {} been alone/lonely', 'not', 'a bit', 'very', 100, 400, [3, -1, -4], 4),
                          MentalQuestion('My anxiety has {}', 'stagnated', 'decreased', 'increased', 100, 450, [0, 3, -3], 5),
                          MentalQuestion('My passions have {}', 'been put aside', 'lost meaning', 'not changed', 100, 200, [-5, -3, 0], 6),
                          MentalQuestion('My energy levels are {}', 'normal', 'a bit low', 'very low', 100, 250, [1, -1, -4], 7)]
        self.copy_questions = self.questions
        self.chat = []
        self.rating = None
        self.page_num = 0
        self.scroll = 1
        self.advice = ['Go to a mental institution/professional immediately',
                       'Seek professional assistance swiftly',
                       'Focus on your mental well being and ask for help',
                       'All is relatively normal',
                       'Your mental well-being is amazing']
        for indexes in range(len(self.questions)):
            finished_questions.append(False)
        with open('challenges.txt', 'r+') as mental_challenges:
            for indicies, mental_challenge in enumerate(mental_challenges):
                if indicies < len(self.questions):
                    if mental_challenge.strip() == 'False':
                        finished_questions[indicies] = False
                    elif mental_challenge.strip() == 'True':
                        finished_questions[indicies] = True
                elif mental_challenge.strip() != '':
                    n_c = mental_challenge.strip().split('  ')
                    challenge_info.append([n_c[0], int(n_c[1]), int(n_c[2]) if not health_points[4] else int(n_c[2]) - 1])
        try:
            if not health_points[4]:
                for location, questions in enumerate([questions for questions in self.questions]):
                    if finished_questions[location]:
                        questions.finish(self)
        except Exception:
            pass

        else:
            for variables in finished_questions:
                variables = False
        try:
            if health_points[4]:
                health_points[1] += 1
        except:
            pass

    def draw(self):
        self.tab.draw()

    def page(self):
        pg.draw.line(screen, (0, 0, 0), (650, -10), (650, 510), 5)
        for locations, text_line in enumerate(reversed(self.chat)):
            if locations % 2 == 0:
                screen.blit(fonts[1].render(text_line, True, (colors[2])), (700, 480 - self.scroll * 25))
                self.scroll += 3
            else:
                increase = blit_text(text_line, (680, 480 - self.scroll * 25), fonts[1], 280, 20)
                self.scroll += 3 * increase

        self.scroll = 1
        for questions in self.questions[0 + self.page_num * 6:6 + self.page_num * 6]:
            if questions is not None:
                questions.draw()
        screen.blit(fonts[0].render(f'Mental Health Rating - {health_points[3]}', True, level[int(health_points[3]/20)]), (100, 100))
        screen.blit(fonts[2].render(f'Advice - {self.advice[int(int((health_points[3]-1)/20))]}', True, (0, 0, 0)), (100, 150))
        screen.blit(image_pack["UpArrow"], (20, 180))
        screen.blit(image_pack["DownArrow"], (20, 320))
        screen.blit(fonts[0].render(f'{self.page_num + 1} of {1 + len(self.questions)//6}', True, (0, 0, 0)), (5, 250))

    def check(self, event):
        for questions in self.questions[0 + self.page_num * 6:6 + self.page_num * 6]:
            questions.check(event, self) if questions is not None else None
        if event.type == pg.MOUSEBUTTONDOWN:
            if click(*pg.mouse.get_pos(), 20, 180, 50, 50) and self.page_num > 0:
                self.page_num -= 1
            if click(*pg.mouse.get_pos(), 20, 320, 50, 50) and self.page_num < len(self.questions)//6:
                self.page_num += 1



class Log:
    def __init__(self, x, y, name):
        self.show = False
        self.tab = Button(x, y, 205, 50, fonts[1], name, colors[1])
        self.scroll = 0
        self.total_pages = math.ceil(len(logged_info) / 14)
        if self.total_pages == 0:
            self.total_pages = 1

    def draw(self):
        self.tab.draw()

    def page(self):
        pg.draw.rect(screen, (0, 0, 0), [140, 75, 720, 425], 3, 5)
        for integers in range(1, 14):
            pg.draw.line(screen, (0, 0, 0), (140, integers * 30 + 75), (857, integers * 30 + 75), 3)
        for iteration, data in enumerate(logged_info[0 + 14 * self.scroll:14 + 14 * self.scroll]):
            screen.blit(fonts[1].render(f'{data["Date"]}: {data["Extra"]}{data["Info"]}', True, (0, 0, 0)), (150, iteration * 30 + 77))
        screen.blit(image_pack["UpArrow"], (900, 125))
        screen.blit(image_pack["DownArrow"], (900, 375))
        screen.blit(fonts[1].render(f'Page {self.scroll + 1} of {self.total_pages}', True, (0, 0, 0)), (880, 270))


    def check(self, event):
        if recalculate[0]:
            self.total_pages = math.ceil(len(logged_info) / 14)
            recalculate[0] = not recalculate[0]
        if event.type == pg.MOUSEBUTTONDOWN and click(*pg.mouse.get_pos(), 900, 375, 50, 50) and self.scroll + 1< self.total_pages:
            self.scroll += 1
        if event.type == pg.MOUSEBUTTONDOWN and click(*pg.mouse.get_pos(), 900, 125, 50, 50) and self.scroll > 0:
            self.scroll -= 1


class AllTab:

    def __init__(self):
        tab_names = ['Homepage', 'Mental Assistant', 'Health Logger', 'Health Log', 'Diagnostic']
        self.all_tabs = []
        self.all_tabs.append(Log(800, 20, tab_names[3]))
        self.all_tabs.append(Logger(600, 20, tab_names[2]))
        self.all_tabs.append(MentalHealth(200, 20, tab_names[1]))
        self.all_tabs.append(DiagnosticHome(400, 20, tab_names[4]))
        self.blend = pg.Surface((1000, 40))
        self.fade = pg.transform.scale(image_pack["ColorFade"], (1000, 40))
        for var in self.all_tabs:
            var.tab.color = colors[6]
        self.all_tabs.append(HomePage(0, 20, tab_names[0]))


    def switch_tabs(self, event):
        for tab in self.all_tabs:
            if tab.tab.check(event):
                for var in self.all_tabs:
                    var.show = False
                    var.tab.color = colors[6]
                tab.show, tab.tab.color = True, colors[0]

    def draw(self):
        for tabs in self.all_tabs:
            if tabs.show:
                tabs.page()
        pg.draw.line(screen, (0, 0, 0), (0, 68), (1000, 68), 5)
        pg.draw.rect(screen, colors[7], [0, 0, 1000, 40])
        for tabs in self.all_tabs:
            tabs.draw()


    def check(self, event):
        for tabs in self.all_tabs:
            if tabs.show:
                tabs.check(event)


class Clock:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.cool_down = t.time()

    def tick(self):
        self.clock.tick()
        if t.time() - self.cool_down > 0.5:
            pg.display.set_caption(f'Bodytastic Health Assistant   FPS - {int(round(self.clock.get_fps(), -2))}')
            self.cool_down = t.time()

class Link:
    def __init__(self, url, text, x, y, font_size):
        font = pg.font.SysFont('comicsansms', font_size, False, False)
        font.set_underline(True)
        self.text_value = text
        self.font = font
        self.text = font.render(text, True, (0, 0, 0))
        self.x, self.y = x, y
        self.url = url

    def draw(self):
        screen.blit(self.text, (self.x, self.y))

    def check(self, event):
        if click(*pg.mouse.get_pos(), self.x, self.y, *self.text.get_size()):
            self.text = self.font.render(self.text_value, True, colors[2])
            if event.type == pg.MOUSEBUTTONDOWN:
                webbrowser.open(self.url, 2)
                return True
        else:
            self.text = self.font.render(self.text_value, True, (0, 0, 0))






def loading(events):
    logo = pg.image.load('bodytastic.png')
    load = True
    demo_link = Link('https://www.youtube.com/watch?v=U-k14AzKnts&t=22s', 'Demo Video', 800, 400, 20)
    web_link = Link('https://bodytastic.godaddysites.com/', 'Website', 800, 430, 20)
    while events.run and load:
        screen.fill((217, 224, 230))
        center(logo, screen.get_width()/2, screen.get_height()/2 - 80)
        center(fonts[0].render('Click Anywhere to Start', True, (0, 0, 0)), screen.get_width()/2, screen.get_height()/2 + 70)
        demo_link.draw()
        web_link.draw()
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                events.run = not events.run
            if not demo_link.check(event) and not web_link.check(event) and event.type == pg.MOUSEBUTTONDOWN:
                load = not load


def render(all_tab):
    # Drawing and updating the screen
    screen.fill(colors[4])
    all_tab.draw()
    pg.draw.rect(screen, colors[4], [1000, 0, 20, 100])
    pg.display.update()
    if pause_frame[0]:
        t.sleep(0.5)
        pause_frame[0] = not pause_frame[0]


def fade():
    if t.time() - fade_color1[1] > 0.1:
        fade_color1[0] += 2 * fade_color1[-1]
        if fade_color1[0] == 50 or fade_color1[0] == 150:
            fade_color1[2] *= -1
        fade_color1[1] = t.time()


# Main Run Loop
def main():
    events = Event()
    loading(events)
    globalize()
    all_tab = AllTab()
    clock = Clock()
    while events.run:
        # Drawing and updating the screen
        render(all_tab)

        # Checking All Events
        events.check(all_tab)

        # Run Clock
        clock.tick()

        # Fade Colors
        fade()

    pg.quit()


if __name__ == '__main__':
    main()
    with open('health.txt', 'w') as save:
        save.truncate()
        for i in range(4):
            save.write(f'{health_points[i]}\n')
        save.write(f"{date.date.today()}\n")
        for info in logged_info:
            info["Extra"] = '.' if info["Extra"] == '' else info["Extra"]
            save.write(f'{info["Extra"]}  {info["Info"]}  {info["Date"]}\n')
    with open('challenges.txt', 'w') as challenges:
        for var in finished_questions:
            challenges.write(f'{var}\n')
        for challenge in challenge_info:
            challenges.write(f'{challenge[0]}  {challenge[1]}  {challenge[2]}\n')
    with open('leaderboard.txt', 'w') as leaders:
        leaders.truncate()
        leader_info[0] += health_points[0] - leader_info[3]
        leader_info[2] += health_points[0] - leader_info[3]
        for var in leader_info:
            leaders.write(f'{var}\n')
