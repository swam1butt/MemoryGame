import pygame
import sys
import random
import collections
from pygame import mixer
from pygame.locals import *

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


class Pane(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Memory Game')
        self.icon = pygame.image.load('memory.png')
        pygame.display.set_icon(self.icon)
        self.screen = pygame.display.set_mode((800, 600))
        self.bkg = pygame.image.load('back.png')
        self.screen.blit(self.bkg, (0, 0))
        self.screen.fill(white)
        self.numbers = []
        self.pic_num = 1
        self.pics = []
        self.user_answer = []
        self.counter = 1
        self.ans_dict = {}
        self.answers = {}
        self.expected_answers = {}
        self.right_answers = {}
        self.final_ans = []
        self.score = 0
        pygame.display.update()

    def start_screen(self):
        self.screen.blit(self.bkg, (0, 0))
        start1 = self.font.render('WELCOME TO THE MEMORY GAME', True, (10, 10, 10))
        self.screen.blit(start1, (170, 20))
        start2 = self.font.render('PRESS ENTER TO BEGIN', True, (10, 10, 10))
        self.screen.blit(start2, (220, 300))
        pygame.display.update()

    def random_number(self):
        num_list = []
        for i in range(50):
            r = random.randint(1, 5)
            if r not in num_list: num_list.append(r)
            self.numbers = num_list[:5]
        print(self.numbers)
        return self.numbers

    def show_picture(self, n):
        self.screen.blit(self.bkg, (0, 0))
        header = self.font.render('MEMORIZE THE ORDER OF THESE PICTURES', True, (0, 0, 0))
        self.screen.blit(header, (130, 10))
        x = 40
        j = 0
        for i in n:
            self.screen.blit(pygame.image.load('{}.png'.format(i)), (x, 200))
            x += 150
        # getting dictionary of answers
        self.ans_dict = {i: n[i] for i in range(0, len(n))}
        # swapping the keys and values
        self.answers = dict([(value, key) for key, value in self.ans_dict.items()])
        # sort by key
        self.expected_answers = collections.OrderedDict(sorted(self.answers.items()))
        # list of answers -1
        self.right_answers = list(self.expected_answers.values())
        footer = self.font.render('PRESS SPACE TO CONTINUE', True, (0, 0, 0))
        self.screen.blit(footer, (200, 450))
        pygame.display.update()

    def show_pic_ans(self, n):
        self.screen.blit(self.bkg, (0, 0))
        header = self.font.render('IDENTIFY THE POSITION OF THIS PICTURE', True, (0, 0, 0))
        self.screen.blit(header, (120, 10))
        self.screen.blit(pygame.image.load('{}.png'.format(n)), (350, 200))
        footer = self.font.render('PRESS YOUR ANSWER (1-5) TO CONTINUE', True, (0, 0, 0))
        self.screen.blit(footer, (120, 450))
        pygame.display.update()

    def _message_(self, final_score):
        if final_score == 0:
            msg = 'YOU ARE RETARDED'
        elif final_score == 1:
            msg = 'YOU ARE ALMOST RETARDED'
        elif final_score == 2:
            msg = 'YOU ARE AVERAGE'
        elif final_score == 3:
            msg = 'YOU ARE ABOVE AVERAGE'
        elif final_score == 4:
            msg = 'YOU ARE SMART'
        elif final_score == 5:
            msg = 'YOU ARE A GENIUS'
        else:
            msg = 'CHEATER'
        return msg

    def ans_checker(self, user_answer):
        self.screen.blit(self.bkg, (0, 0))
        x = 40
        y = 40
        header = self.font.render('CONGRATS! YOU HAVE COMPLETED THE TEST!', True, (0, 0, 0))
        self.screen.blit(header, (130, 10))
        footer1 = self.font.render('YOUR ANSWERS: ' + str(user_answer), True, (0, 0, 0))
        self.screen.blit(footer1, (220, 90))
        for i in user_answer:
            self.screen.blit(pygame.image.load('{}.png'.format(i)), (x, 130))
            x += 150
        # final list of answers
        self.final_ans = [x + 1 for x in self.right_answers]
        footer2 = self.font.render('RIGHT ANSWERS: ' + str(self.final_ans), True, (0, 0, 0))
        self.screen.blit(footer2, (220, 300))
        for i in self.final_ans:
            self.screen.blit(pygame.image.load('{}.png'.format(i)), (y, 350))
            y += 150
        final_score = self.score_calculator(self.user_answer, self.final_ans)
        footer2 = self.font.render('YOUR SCORE: ' + str(final_score), True, (0, 0, 0))
        self.screen.blit(footer2, (270, 500))
        footer3 = self.font.render('COMMENTS: ' + self._message_(final_score), True, (0, 0, 0))
        self.screen.blit(footer3, (170, 570))
        pygame.display.update()
        pass

    def score_calculator(self, lst1, lst2):
        for i in range(0, len(lst1)):
            if lst1[i] == lst2[i]:
                self.score += 1
        return self.score

    def functionApp(self):
        if __name__ == '__main__':
            # self.addRect()
            # self.addText()
            self.start_screen()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            n = self.random_number()
                            self.show_picture(n)
                            pygame.display.update()
                        if event.key == pygame.K_SPACE:
                            self.show_pic_ans(self.counter)
                            pygame.display.update()
                        if event.key == pygame.K_1:
                            self.user_answer.append(1)
                            if self.counter < 5:
                                self.counter += 1
                                self.show_pic_ans(self.counter)
                            elif self.counter == 5:
                                self.ans_checker(self.user_answer)
                            else:
                                return
                        if event.key == pygame.K_2:
                            self.user_answer.append(2)
                            if self.counter < 5:
                                self.counter += 1
                                self.show_pic_ans(self.counter)
                            elif self.counter == 5:
                                self.ans_checker(self.user_answer)
                            else:
                                return
                        if event.key == pygame.K_3:
                            self.user_answer.append(3)
                            if self.counter < 5:
                                self.counter += 1
                                self.show_pic_ans(self.counter)
                            elif self.counter == 5:
                                self.ans_checker(self.user_answer)
                            else:
                                return
                        if event.key == pygame.K_4:
                            self.user_answer.append(4)
                            if self.counter < 5:
                                self.counter += 1
                                self.show_pic_ans(self.counter)
                            elif self.counter == 5:
                                self.ans_checker(self.user_answer)
                            else:
                                return
                        if event.key == pygame.K_5:
                            self.user_answer.append(5)
                            if self.counter < 5:
                                self.counter += 1
                                self.show_pic_ans(self.counter)
                            elif self.counter == 5:
                                self.ans_checker(self.user_answer)
                            else:
                                return


display = Pane()
display.functionApp()
