from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 1000

# Player settings
player_pos = [0, 0, 50]
player_angle = 0
player_speed = 50
player_health = 5
max_health = 5
player_score = 0
is_dead = False
game_paused = False
dash_mode = False
dash_timer = 0
dash_duration = 0.5
dash_cooldown = 0
dash_cooldown_duration = 2.0
dash_speed_multiplier = 3.0

# Health bar colors (5 parts) - from green (full) to red (low)
HEALTH_COLORS = [
    (1.0, 0.0, 0.0),    # Red - lowest health
    (1.0, 0.5, 0.0),    # Orange
    (1.0, 1.0, 0.0),    # Yellow
    (0.8, 1.0, 0.0),    # Light Green
    (0.0, 1.0, 0.0)     # Green - full health
]

# Arena boundaries
ARENA_SIZE = 8000
BOUNDARY_SIZE = ARENA_SIZE - 400
GROUND_Z = 0

# Camera settings - Drone-like camera following player
camera_distance = 1200  # Increased to thrice the distance
camera_height = 600     # Increased height for better view
camera_angle = 0  # For orbiting around player

# Environment settings - More bustling
tree_count = 300        # Increased trees
rock_count = 150        # Increased rocks
house_count = 30        # Added houses


# Environment settings - More bustling
tree_count = 300        # Increased trees
rock_count = 150        # Increased rocks
house_count = 30        # Added houses

# Jungle environment
trees = []
rocks = []
houses = []

# Diamond spawn management
last_diamond_spawn = time.time()
diamond_spawn_interval = 4.0
ground_diamonds = []
falling_diamonds = []
regular_diamond_score = 10
special_diamond_health = 1
diamond_ground_lifetime = 10




