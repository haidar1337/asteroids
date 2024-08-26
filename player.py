from constants import *
from shot import Shot
from circleshape import CircleShape
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.rate = 0
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.rate -= dt
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()        

    def move(self, dt):
        movement_vector = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt
        self.position += movement_vector

    def shoot(self):
        if self.rate <= 0:
            bullet = Shot(self.position.x, self.position.y)
            bullet.velocity = (pygame.Vector2(0, 1).rotate(self.rotation)) * PLAYER_SHOT_SPEED
            self.rate = PLAYER_SHOT_COOLDOWN
            return bullet