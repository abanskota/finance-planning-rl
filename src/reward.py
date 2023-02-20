def reward_function(current_balance, goal_amount):
    if current_balance >= goal_amount:
        # if current balance is greater than or equal to the goal amount, return a high reward
        reward = 1
    else:
        # otherwise, calculate a reward based on the distance to the goal amount
        reward = 1 - abs(current_balance - goal_amount) / goal_amount
    return reward