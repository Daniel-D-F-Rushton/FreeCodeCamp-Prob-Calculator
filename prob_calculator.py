import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **balls):
    self.contents = [key for key, value in balls.items() for values in range(value)]

  def draw(self, balls_to_draw):
    if balls_to_draw >= len(self.contents):
      balls_to_draw = len(self.contents)
    to_be_returned = []
    for i in range(balls_to_draw):
      to_be_returned.append(self.contents.pop(random.randrange(0, len(self.contents))))
    return to_be_returned;

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successes = 0
  for _ in range(num_experiments):
    expected_hat = [key for key, value in expected_balls.items() for values in range(value)]
    test_hat = copy.deepcopy(hat)
    balls_drawn_this_time = test_hat.draw(num_balls_drawn)
    fail = False;
    for ball_drawn in range(len(balls_drawn_this_time)):
      if balls_drawn_this_time[ball_drawn] in expected_hat:
        expected_hat.remove(balls_drawn_this_time[ball_drawn])
      if len(expected_hat) == 0:
        break
    if len(expected_hat) > 0:
      fail = True
    if fail == False:
      successes += 1
  return successes / num_experiments
  