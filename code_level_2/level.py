import pygame, sys
from tiles import Tile, Tile_Kiri, Tile_Kanan, Tile_Sendiri, Tile_G, Tile_H, Tile_J, Coin, Tile_Flag, Tile_Kanan1, Tile_A, Tile_B
from settings import tile_size, screen_width, screen_height
from player import Player
from particles import ParticleEffect
from enemy import Enemy

class Level:
	def __init__(self,level_data,surface):
		
		# level setup
		self.display_surface = surface 
		self.setup_level(level_data)
		self.world_shift = 0
		self.current_x = 0
		self.game_state = "playing"  # Possible values: "playing", "won", "lost"


		# dust 
		self.dust_sprite = pygame.sprite.GroupSingle()
		self.player_on_ground = False

	def create_jump_particles(self,pos):
		if self.player.sprite.facing_right:
			pos -= pygame.math.Vector2(10,5)
		else:
			pos += pygame.math.Vector2(10,-5)
		jump_particle_sprite = ParticleEffect(pos,'jump')
		self.dust_sprite.add(jump_particle_sprite)

	def get_player_on_ground(self):
		if self.player.sprite.on_ground:
			self.player_on_ground = True
		else:
			self.player_on_ground = False

	def create_landing_dust(self):
		if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
			if self.player.sprite.facing_right:
				offset = pygame.math.Vector2(10,15)
			else:
				offset = pygame.math.Vector2(-10,15)
			fall_dust_particle = ParticleEffect(self.player.sprite.rect.midbottom - offset,'land')
			self.dust_sprite.add(fall_dust_particle)

	def setup_level(self,layout):
		self.tiles = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()
		self.coins = pygame.sprite.Group()
		self.enemies = pygame.sprite.Group()
		self.finishs = pygame.sprite.Group()

		for row_index,row in enumerate(layout):
			for col_index,cell in enumerate(row):
				x = col_index * tile_size
				y = row_index * tile_size
				
				if cell == 'X':
					tile = Tile((x,y),tile_size)
					self.tiles.add(tile)
				if cell == 'E':
					enemy = Enemy(x, y, tile_size)
					self.enemies.add(enemy)
				if cell == 'I':
					tile = Tile_Kiri((x,y),tile_size)
					self.tiles.add(tile)
				if cell == 'N':
					tile = Tile_Kanan((x,y),tile_size)
					self.tiles.add(tile)
				if cell == 'A':
					tile = Tile_A((x,y),tile_size)
					self.tiles.add(tile)
				if cell == 'M':
					tile = Tile_Kanan1((x,y),tile_size)
					self.tiles.add(tile)
				if cell == 'S':
					tile = Tile_Sendiri((x,y),tile_size)
					self.tiles.add(tile)
				if cell == 'G':
					tile = Tile_G((x,y),tile_size)
					self.tiles.add(tile)
				if cell == 'H':
					tile = Tile_H((x,y),tile_size)
					self.tiles.add(tile)
				if cell == 'J':
					tile = Tile_J((x,y),tile_size)
					self.tiles.add(tile)
				if cell == 'B':
					tile = Tile_B((x,y),tile_size)
					self.tiles.add(tile)
				if cell == 'C':
					coin = Coin((x,y),tile_size)
					self.coins.add(coin)
				if cell == 'F':
					finish = Tile_Flag((x,y),tile_size)
					self.finishs.add(finish)
				if cell == 'P':
					player_sprite = Player((x,y),self.display_surface,self.create_jump_particles)
					self.player.add(player_sprite)

	def scroll_x(self):
		player = self.player.sprite
		player_x = player.rect.centerx
		direction_x = player.direction.x

		if player_x < screen_width / 4 and direction_x < 0:
			self.world_shift = 8
			player.speed = 0
		elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
			self.world_shift = -8
			player.speed = 0
		else:
			self.world_shift = 0
			player.speed = 8

			

	def horizontal_movement_collision(self):
		player = self.player.sprite
		player.rect.x += player.direction.x * player.speed

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				if isinstance(sprite, Coin):
					self.handle_coin_collision(sprite)

				if player.direction.x < 0: 
					player.rect.left = sprite.rect.right
					player.on_left = True
					self.current_x = player.rect.left
				elif player.direction.x > 0:
					player.rect.right = sprite.rect.left
					player.on_right = True
					self.current_x = player.rect.right

		if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
			player.on_left = False
		if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
			player.on_right = False

	def vertical_movement_collision(self):
		player = self.player.sprite
		player.apply_gravity()

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.y > 0: 
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
					player.on_ground = True
				elif player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = 0
					player.on_ceiling = True

		if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
			player.on_ground = False
		if player.on_ceiling and player.direction.y > 0.1:
			player.on_ceiling = False

	def check_death(self):
		if self.player.sprite.rect.top > screen_height:
			sys.exit()

	def run(self):
		self.all_sprites = pygame.sprite.Group(self.tiles, self.player, self.coins, self.enemies, self.finishs)
		# dust particles 
		self.dust_sprite.update(self.world_shift)
		self.dust_sprite.draw(self.display_surface)

		self.coins.update(self.world_shift)
		self.coins.draw(self.display_surface)


		# level tiles
		self.tiles.update(self.world_shift)
		self.tiles.draw(self.display_surface)
		self.scroll_x()

		# enemy
		self.enemies.update(self.world_shift)
		self.enemies.draw(self.display_surface)

		# finish
		self.finishs.update(self.world_shift)
		self.finishs.draw(self.display_surface)


		for enemy in self.enemies:
			if enemy.check_collision(self.player.sprite.rect):
				print("Player collided with an enemy!")
				sys.exit()

		for finish in self.finishs:
			if finish.check_collision(self.player.sprite.rect):
				print("Player telah memenangkan match!")
				self.game_state = "won"
				sys.exit()

		self.collected_coins = 0
		coins_to_remove = []

		for coin in self.coins:
			if coin.check_collision(self.player.sprite.rect):
				coins_to_remove.append(coin)
				self.collected_coins += 1
				print("Coin collected! Total Coins:", self.collected_coins)

		# Remove collected coins after the loop
		for coin in coins_to_remove:
			self.coins.remove(coin)

		# player
		self.player.update()
		self.horizontal_movement_collision()
		self.get_player_on_ground()
		self.vertical_movement_collision()
		self.create_landing_dust()
		self.player.draw(self.display_surface)
		self.check_death()