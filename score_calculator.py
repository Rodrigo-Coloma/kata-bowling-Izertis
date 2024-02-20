#We define a game class

class Game():
    score = 0   
    round = 0
    throw = 0
    strike = (0,0)
    last_throw = 0

    def play(self,pins):
        self.round += (self.throw +1) % 2
        self.score += pins * (1 + self.strike[0] - (self.round > 10))
        if self.throw == 0 and pins == 10 and (self.round < 11):
            self.strike = (self.strike[1]+1,1)
        elif self.throw == 1 and ((pins + self.last_throw) == 10) and (self.round < 11):
            self.strike = (self.strike[1]+1,0)
            self.throw = 0
        else:
            self.last_throw = pins
            self.strike = (self.strike[1],0)
            self.throw = (self.throw + 1) % 2

    def sequence(self,seq):
        for sequence_part in seq.split(' & '):
            if 'x' in sequence_part:
                punctuation =int(sequence_part.split('x')[-1]) 
                times = int(sequence_part.split('x')[0])
                [Game.play(self, punctuation) for n in range(times)]
            else:
                Game.play(self,int(sequence_part))
        return self.score