extends KinematicBody2D

const UP = Vector2(0, -1)
const GRAVITY = 20
const ACCELERATION = 20
const MAX_SPEED = 300
const JMP_FORCE = -450
const FIREBALL = preload("res://FireBall.tscn")

var motion = Vector2()

func _physics_process(delta):
	motion.y += GRAVITY
	var friction = false
	
	if Input.is_action_pressed("ui_right"):
		$Sprite.flip_h = false
		motion.x = min(motion.x + ACCELERATION, MAX_SPEED)
		$Sprite.play("Run")
		if sign($Position2D.position.x) == -1:
			$Position2D.position *= -1
		
	elif Input.is_action_pressed("ui_left"):
		$Sprite.flip_h = true
		motion.x = max(motion.x - ACCELERATION, -MAX_SPEED)
		$Sprite.play("Run")
		if sign($Position2D.position.x) == 1:
			$Position2D.position *= -1
	else:
		$Sprite.play("Idle")
		friction = true
	
	if is_on_floor() || is_on_wall():
		if Input.is_action_just_pressed("ui_up"):
			motion.y = JMP_FORCE
		if friction == true:
			motion.x = lerp(motion.x, 0, .2)
	else:
		if motion.y < 0:
			$Sprite.play("Jump")
		else:
			$Sprite.play("Fall")
			
		if friction == true:
			motion.x = lerp(motion.x, 0, .2)

	motion = move_and_slide(motion, UP)
	
	# Shooting
	
	if Input.is_action_just_pressed("ui_select"):
		var fireball = FIREBALL.instance()
		get_parent().add_child(fireball)
		fireball.set_fireball_direction(sign($Position2D.position.x))
		fireball.position = $Position2D.global_position
	pass
