"""
In this programming exercise, you will create a simple trivia game for two players. The program will work like this:
Starting with player 1, each player gets a turn at answering 5 trivia questions. (There should be a total of 10 questions.)
When a question is displayed, 4 possible answers are also displayed. Only one of the answers is correct, and if the player
 selects the correct answer, he or she earns a point.
After answers have been selected for all the questions, the program displays the number of points earned by each player
 and declares the player with the highest number of points the winner.
"""


class Question:

    def __init__(self, question, a, b, c, d, word_answer):
        self.__question = question
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__word_answer = word_answer

    def set_question(self, question):
        self.__question = input('set the question')

    def set_a(self, a):
        self.__a = input('set solution a')

    def set_b(self, b):
        self.__b = input('set solution for b')

    def set_c(self, c):
        self.__c = input('set solution for c')

    def set_d(self, d):
        self.__d = input('set solution for d')

    def set_answer(self, answer):
        self.__word_answer = input('set the answer')

    def get_question(self):
        return self.__question

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d

    def get_answer(self):
        if self.__word_answer == self.__a:
            return 'a'
        elif self.__word_answer == self.__b:
            return 'b'
        elif self.__word_answer == self.__c:
            return 'c'
        elif self.__word_answer == self.__d:
            return 'd'
    def get_word_answer(self):
        return self.__word_answer


def main():
    player1 = 0
    player2 = 0
    question1 = Question('What is the fastest land animal?', 'A. The cheetah', 'B. The gazelle', 'C. The dolphin', 'D. The corvette', 'A. The cheetah')
    question2 = Question('What is the largest planet in the solar system?', 'A. Earth', 'B. Earth 2', 'C. Jupiter', 'D. Pluto', 'C. Jupiter')
    question3 = Question('What ocean borders California?', 'A. The Atlantic', 'B. The Specific', 'C. The Pacific', 'D. The Arctic', 'C. The Pacific')
    question4 = Question('What movie made the Randy Newman and Lyle Lovett song, Youve got a friend in me, famous?', 'A. Up', 'B. Wall-E', 'C. Alien Vs. Predator: Requiem', 'D. Toy Story', 'D. Toy Story')
    question5 = Question('Harry Styles was once a member of this popular musical group?', 'A. Two Direction', 'B. One Direction', 'C. Kiss', 'D. AC/DC', 'B. One Direction')
    question6 = Question('What is the most popular sport in Indonesia?', 'A. soccer', 'B. water polo', 'C. badminton', 'D. boat racing', 'C. badminton')
    question7 = Question('SpongeBob SquarePants live in which fruit?', 'A. apple', 'B. banana', 'C. sponge', 'D. pineapple', 'D. pineapple')
    question8 = Question('What is the internal Temperature of a TaunTaun?', 'A. hothly cold', 'B. freezing', 'C. luke-warm', 'D. smelly', 'C. luke-warm')
    question9 = Question('What country has a unicorn as part of its national emblem?', 'A. Pakistan', 'B. Canada', 'C. Wales', 'D. Scotland', 'D. Scotland')
    question10 = Question('What is the correct term to describe a fact?', 'A. True', 'B. False', 'C. trivia', 'D. true', 'C. trivia')
    l1 = [question2, question4, question6, question8, question10]
    l2 = [question1, question3, question5, question7, question9]
    print('player1 ready?')
    print()
    for question in l1:
        print('-------------------', 'q', '-------------------')
        print(str(question.get_question()), '\n')
        print(str(question.get_a()), str(question.get_b()), '\n', str(question.get_c()), str(question.get_d()), '\n')
        choice = input('enter the correct answer letter:')
        print()
        if choice.lower() == question.get_answer():
            print('that is correct!')
            player1 += 1
            print()
            print()
            print()
        else:
            print('the answer was incorrect. The correct choice is ', str(question.get_word_answer()))
            print()
            print()
    print()
    print()
    print('player2 ready?')
    for question in l2:
        print('-------------------', 'q', '-------------------')
        print(str(question.get_question()), '\n')
        print(str(question.get_a()), str(question.get_b()), '\n', str(question.get_c()), str(question.get_d()), '\n')
        choice = input('enter the correct answer letter:')
        print()
        if choice.lower() == question.get_answer():
            print('that is correct!')
            player2 += 1
            print()
            print()
            print()
        else:
            print('the answer was incorrect. The correct choice is ', str(question.get_word_answer()))
    print()
    print()
    print()
    print()
    print('Thats Game!')
    print()
    print()
    if player1 > player2:
        print('player 1 wins with score: ', str(player1), '\n player 2: ', str(player2))
    elif player1 == player2:
        print('the game is a tie! score: ', str(player1))
    elif player1 < player2:
        print('player 2 wins with score: ', str(player2), '\n player 1: ', str(player1))


main()
