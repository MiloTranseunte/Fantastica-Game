# Listado de Escenas y sus dependencias
# Para Video Juego Fantástica Adventure
# Primer Template 11/05/2019

# Modificaciones 12/05/2019 7:20 pm


# Carpeta directorio principal con las escenas de los niveles, 
# donde tendrán las siguientes dependencias


# Cambiar estilo de estructura de esta parte de las entidades ya que no corresponde a 
# los datos de la estructura del proyecto sino a los nodos en "built-in" en Godot

NODO_GODOT Universo():
	SubCarpeta World_x():
		Player_x.tscn				# Escena del Jugador o jugadores
		Tilemap_x					# Basado en un Tilemap.tscn y un .tres
		Token_nextWorld_x			# Token Area2D con export variable File, str con dir de la escena siguiente
		Enemy_x.enemyType.tscn		# Escena con Nodo de enemigos. O puede ser una carpeta de enemigos con carpeta por enemigo
		Item_x.tscn					# Escena de Item/s
		PowerUps_x.tscn				# Escena con Tokens powerUps



# Carpeta de las entidades tipo caracter que comparten comportamientos
Entities():
	Carpeta Player(Player_x):				
		KinimaticBody2D.script:
			Camera2D
			AnimatedSprite
			CollisionShape2D
			Position2D				# Posición utilizada para la dirección del disparo
			Timer					# Timer para controlar la cantidad de disparos por vez y otras secuencias
			VisibilityNotifier2D	# Desde donde se lanza un Signal() hacia el nodo padre para notificar la desaparición de child Bullet_Player() de la pantalla
			
		SubCarpeta AnimatedSprite():
			img_x.png
			
			SubCarpeta Bullet_Player():
				Area2D.script:
					AnimatedSprite
					CollisionShape2D
				

	Carpeta Enemies(Enemy_x):
		KinimaticBody2D.script
			AnimatedSprite
			CollisionShape2D
			Position2D				# Posición utilizada para la dirección del disparo
			Timer					# Timer para controlar la cantidad de disparos por vez y otras secuencias
			
				SubCarpeta Bullet_Enemy():
					Area2D.script:
						AnimatedSprite
						CollisionShape2D
						
Carpeta Items():
	GenericItem.tscn				# main scene of a generic item
	GenericItem.gd					# script of the generic item
	SubCarpeta x_item():			# each instance of a particular item
		x_item.tscn					# With its propierty nodes attached on it
		x_item.gd					# gd script of the particular item
		Sprite/ AnimatedSprite

Carpeta Weapons():
	genericWeapon.tscn
	genericWeapon.gd
	SubCarpeta x_weapon():
		x_weapon.tscn
		x_weapon.gd
		Sprite / AnimatedSprite

Carpeta WORLDS():
	
	# Carpeta donde se alojan los mundos y lo necesario y único para su funcionamiento
	
	SubCarpeta World_x():
		SubCarpeta Tilemap():
			Tilemap_x.tscn
			Tilemap_x.tres				

			# Carpeta donde se aloja la escena del Token_nextWorld			

			SubCarpeta TokenNextWorld(Token_nextWorld):
				TokenNextWorld.tscn
					Area2D.script:
						CollisionShape2D
						Sprite