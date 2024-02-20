from score_calculator import Game


def test(game_sequence, final_score):
    print (f'testing with sequence{game_sequence}')
    game = Game()
    calculated_score = game.sequence(game_sequence)
    if calculated_score == final_score:
        print('Test passed')
    else:
        print('Test failed',f'Calculated score: {calculated_score}',f'Real score: {final_score}')

print('Easy tests')
print('-' * 50)

test('20x1',20)

test('20x0',0)

test('10x3 & 10x0',30)

print('Spare')
print('-' * 50)

test('5 & 5 & 3 & 17x0',16)

test('0 & 5 & 5 & 3 & 16x0',13)

test('5 & 5 & 3 & 17x1',33)

print('Strikes')
print('-' * 50)

test('10 & 3 & 2 & 16x0',20)

test('0 & 10 & 3 & 2 & 16x0',18)

test('10 & 3 & 2 & 16x1',36)

print('Final Rule')
print('-' * 50)

test('18x0 & 10 & 1 & 1',12)

test('18x0 & 5 & 5 & 1',11)

test('12x10',300)