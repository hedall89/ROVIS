import threading, time, random
import cv2, numpy

STATE_READY = 0
STATE_RUNNING = 1
STATE_GAME_OVER = 2

BALL_COLORS = (('BLUE', [255,0,0]), ('GREEN', [0,255,0]), ('RED', [0,0,255]), ('YELLOW', [0,255,255]))
BACKGROUND_COLOR = [255,255,255]

class BallGame(threading.Thread):
    game_state = None
    points = None
    time_available = None
    time_left = None

    background_color = None

    ball_center = None
    ball_radius = None
    ball_color = None

    blinking_text_size = 0.8
    blinking_text_size_dir = 0.01

    answer = False

    def __init__(self):
        super(BallGame, self).__init__()

    def run(self):
        while True:
            self.game_state = STATE_READY
            self.points = 0
            self.time_available = 15
            self.ball_center = (250,250)
            self.ball_radius = 100
            self.background_color = BACKGROUND_COLOR
            self.game()

    def submit_answer(self, answer):
        self.answer = answer

    def game(self):
        while self.game_state == STATE_READY:
            game_window = self.construct_ready_window()
            cv2.imshow('Ball Game', game_window)
            cv2.waitKey(50)
            if self.answer != False:
                print('Received: ' + self.answer)
                print('Game started!')
                self.game_state = STATE_RUNNING
                self.answer = False
        while self.game_state == STATE_RUNNING:
            self.ball_color = random.choice(BALL_COLORS)
            print(self.ball_color[0] + ' ball inserted. ', end='')
            end_time = time.time() + self.time_available
            self.time_left = round(self.time_available,2)
            if self.points > 10:
                self.ball_radius = random.randint(50, 220)
            if self.points > 20:
                self.ball_center = (random.randint(100, 400), random.randint(100, 400))
            while True:
                game_window = self.construct_running_window()
                cv2.imshow('Ball Game', game_window)
                cv2.waitKey(50)
                if self.time_left <= 0:
                    self.game_state = STATE_GAME_OVER
                    break
                if self.answer:
                    print('Received: ' + self.answer)
                    if self.answer == self.ball_color[0]:
                        self.answer = False
                        self.points += 1
                        break
                    else:
                        self.answer = False
                        self.game_state = STATE_GAME_OVER
                        break
                self.time_left = round(end_time - time.time(), 2)
            self.time_available *= 0.975
        while self.game_state == STATE_GAME_OVER:
            print('Game over!')
            game_window = self.construct_game_over_window()
            cv2.imshow('Ball Game', game_window)
            cv2.waitKey(0)
            self.answer = False
            self.game_state = STATE_READY
            break


    def putTextCenter(self, img, text, center, font, size, color, thikness=1):
        textSize = cv2.getTextSize(text, font, size, thikness)[0]
        orgX = int(center[0] - textSize[0] / 2 + 0.5)
        orgY = int(center[1] - textSize[1] / 2 + 0.5)
        cv2.putText(img, text, (orgX, orgY), font, size, color, thikness)

    def construct_ready_window(self):
        ready_window = numpy.zeros((500, 500, 3), dtype=numpy.uint8)
        ready_window[:, :, :] = self.background_color

        ball_game_str = 'Ball Game'
        self.putTextCenter(ready_window, ball_game_str , (250, 100), cv2.QT_FONT_BLACK, 2, (0, 0, 0), 2)

        game_ready_str = 'Game Ready'
        self.putTextCenter(ready_window, game_ready_str , (250, 350), cv2.FONT_ITALIC, self.blinking_text_size, (0, 0, 0))

        info_str = 'Send anything to start game'
        self.putTextCenter(ready_window, info_str , (250, 400), cv2.FONT_ITALIC, self.blinking_text_size, (0, 0, 0))

        cv2.circle(ready_window, (100,200), 40, BALL_COLORS[0][1], -1)
        cv2.circle(ready_window, (100,200), 40, (0, 0, 0), 1)
        cv2.circle(ready_window, (200,200), 40, BALL_COLORS[1][1], -1)
        cv2.circle(ready_window, (200,200), 40, (0, 0, 0), 1)
        cv2.circle(ready_window, (300,200), 40, BALL_COLORS[2][1], -1)
        cv2.circle(ready_window, (300,200), 40, (0, 0, 0), 1)
        cv2.circle(ready_window, (400,200), 40, BALL_COLORS[3][1], -1)
        cv2.circle(ready_window, (400,200), 40, (0, 0, 0), 1)

        self.blinking_text_size += self.blinking_text_size_dir
        if self.blinking_text_size > 1:
            self.blinking_text_size_dir *= -1
        elif self.blinking_text_size < 0.8:
            self.blinking_text_size_dir *= -1

        return ready_window

    def construct_running_window(self):
        if self.points > 5:
            current_background_color = numpy.uint8([[self.background_color]])
            current_background_color = cv2.cvtColor(current_background_color, cv2.COLOR_BGR2HSV)
            current_background_color[0,0,0] = (current_background_color[0,0,0]+1) % 180
            if current_background_color[0,0,1] < 255: current_background_color[0,0,1] += 1
            self.background_color = cv2.cvtColor(current_background_color, cv2.COLOR_HSV2BGR)[0,0,:]

        game_window = numpy.zeros((500, 500, 3), dtype=numpy.uint8)
        game_window[:, :, :] = self.background_color

        cv2.circle(game_window, self.ball_center, self.ball_radius, self.ball_color[1], -1)
        cv2.circle(game_window, self.ball_center, self.ball_radius, (0, 0, 0), 1)

        points_str = str(self.points) + ' points'
        cv2.putText(game_window, points_str, (350, 50), cv2.FONT_ITALIC, 0.9, (0, 0, 0))

        time_str = 'Time: ' + str(self.time_left)
        cv2.putText(game_window, time_str, (20,50), cv2.FONT_ITALIC , 0.9, (0,0,0))

        return game_window

    def construct_game_over_window(self):
        game_window = self.construct_running_window()
        self.putTextCenter(game_window, 'Game Over!', (250, 250), cv2.QT_FONT_BLACK, 2.5, (0, 0, 0), 2)
        score_str = 'Score: ' + str(self.points)
        self.putTextCenter(game_window, score_str, (250, 450), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 1)
        return game_window
