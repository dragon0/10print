import random
import pygame

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        self._init()

    def run(self):
        while self.running:
            self.clock.tick(60)
            self._events()
            self._update()
            self._draw()

    def _events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def _init(self):
        self.x = 0
        self.y = 0
        self.size = 10

    def _update(self):
        if self.y < self.height:
            self.x += self.size
            if self.x > self.width:
                self.x = 0
                self.y += self.size

    def _foreslash(self):
        pygame.draw.line(self.screen,
                (255,255,255),
                (self.x, self.y + self.size),
                (self.x + self.size, self.y))

    def _backslash(self):
        pygame.draw.line(self.screen,
                (255,255,255),
                (self.x, self.y),
                (self.x + self.size, self.y + self.size))

    def _draw(self):
        if random.random() < 0.5:
            self._foreslash()
        else:
            self._backslash()
        pygame.display.flip()


if __name__ == '__main__':
    game = Game(640, 480)
    game.run()

