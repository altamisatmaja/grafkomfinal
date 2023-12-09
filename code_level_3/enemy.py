import pygame, os
from settings import screen_width

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, size, image_folder = 'assets/silver', animation_speed = 70):
        super().__init__()
        self.image_folder = image_folder
        self.images = self.load_images()
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 4 
        self.animation_speed = animation_speed
        self.last_update = pygame.time.get_ticks()

    def load_images(self):
        images = []
        image_files = sorted(os.listdir(self.image_folder))
        for image_file in image_files:
            image_path = os.path.join(self.image_folder, image_file)
            image = pygame.image.load(image_path).convert_alpha()
            images.append(image)
        return images

    
    def update(self, world_shift):
        self.rect.x += self.speed
        self.rect.x += world_shift
        now = pygame.time.get_ticks()

        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
            if (self.rect.right > screen_width) or (self.rect.left < 0):
                self.speed = -self.speed

    def check_collision(self, player_rect):
        return self.rect.colliderect(player_rect)
