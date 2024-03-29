def get_direction(ball_angle: float) -> int:
    """Get direction to navigate robot to face the ball

    Args:
        ball_angle (float): Angle between the ball and the robot

    Returns:
        int: 0 = forward, -1 = right, 1 = left
    """
    if ball_angle >= 340 or ball_angle <= 20:
        return 0
    return -1 if ball_angle < 180 else 1

def get_directionb(ball_angle: float) -> int:
    if ball_angle >= 165 and ball_angle <= 195:
        return 0
    return -1 if ball_angle > 180 else 1
    #return ball_angle

