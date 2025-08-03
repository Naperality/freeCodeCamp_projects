import random

class Hat:
    def __init__(self, **ball_colors):
        self.contents = []
        for color, num_balls in ball_colors.items():
            self.contents.extend([color] * num_balls)
    
    def draw(self, num_balls):
        # If num_balls exceeds the number of available balls, return all available balls
        num_balls = min(num_balls, len(self.contents))
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)  # Remove the drawn ball from the contents
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    
    # Run num_experiments experiments
    for _ in range(num_experiments):
        # Create a copy of the hat to prevent modifying the original one
        hat_copy = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        
        # Draw the balls from the hat
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Check if the drawn balls match the expected balls
        ball_counts = {color: drawn_balls.count(color) for color in drawn_balls}
        
        # Check if the drawn balls satisfy the expected condition
        if all(ball_counts.get(color, 0) >= count for color, count in expected_balls.items()):
            successful_experiments += 1

    # Calculate the probability as the ratio of successful experiments to total experiments
    probability = successful_experiments / num_experiments
    return probability

# Example usage:
hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat,
                         expected_balls={'red': 1, 'green': 2},
                         num_balls_drawn=4,
                         num_experiments=2000)

print(probability)
