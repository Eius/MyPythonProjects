# Resolution 16:9, set screen width, screen height is set automatically
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = (SCREEN_WIDTH/16) * 9

PADDLE_HEIGHT = 120
PADDLE_WIDTH = 20
PADDLE_SPEED = 40

BALL_SIZE = 20
BALL_SPEED = 0.02
BALL_COLOR = "red"

L_PADDLE_X_COR = -SCREEN_WIDTH / 2 + PADDLE_WIDTH
"""Left paddle starting x coordinate"""
R_PADDLE_X_COR = SCREEN_WIDTH / 2 - PADDLE_WIDTH
"""Right paddle starting x coordinate"""

TOP_EDGE = SCREEN_HEIGHT / 2
"""If SCREEN_HEIGHT is 600, return 300"""
BOTTOM_EDGE = -SCREEN_HEIGHT / 2
"""If SCREEN_HEIGHT is 600, return -300"""
LEFT_EDGE = -SCREEN_WIDTH / 2
"""If SCREEN_WIDTH is 1200, return -600"""
RIGHT_EDGE = SCREEN_WIDTH / 2
"""If SCREEN_WIDTH is 1200, return 600"""


