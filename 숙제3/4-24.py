import random

cardDeck = [i for i in range(52)]
random.shuffle(cardDeck)
suits = ['스페이드','다이아몬드','하트','클로버']
numbers = ['A',2,3,4,5,6,7,8,9,'J','Q','K']
for number in cardDeck:
    quot = number // 13 #0,1,2,3
    # print(suits[quot],end='')
    rem = number % 12 #0, 1, ..., 12
    # print(numbers[rem])
    print('뽑은 카드 : ',suits[quot],numbers[rem])
    break