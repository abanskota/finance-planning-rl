import gym
import numpy as np
from distributions import GBM
from reward import reward_function

class GoalPlanEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, usr, one_hot):
        """
        Parameters
        ----------
        usr : dataclass
            profile of investor
        one_hot : list
            list of one hot encodings of time horizon
        """
        super(GoalPlanEnv, self).__init__()
        self.action_space = gym.spaces.Box(low=np.array([-1]), high=np.array([1]), dtype=np.float16)
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(len(one_hot) + 1,), dtype=np.float16) 
        self.usr = usr
        self.one_hot = one_hot
        self.total_steps = 0
        self.SCALE_FACTOR = usr.goal_amount * 2
        
    def step(self, action):
        action_rescaled = 1 / 2 * (action + 1)
        if self.usr.inflation_adjust:
            self.max_adjusted = self.max_adjusted * (1 + self.usr.inflation_factor)
        this_year_saving = action_rescaled * self.max_adjusted
        self.current_balance = GBM(self.current_balance, self.usr.portfolio_return
                                   , self.usr.portfolio_stdv).sample()
        reward = reward_function(self.current_balance, self.usr.goal_amount)
        self.current_balance += this_year_saving
        self.total_steps += 1
        self.current_step += 1
        done = (self.current_step == self.usr.target_year) | (self.current_balance >= self.usr.goal_amount)
        obs = np.array([self.current_balance / self.SCALE_FACTOR] + self.one_hot[self.current_step])
        self.action = action_rescaled
        return obs, reward, done, {'current_step': self.current_step,
                                   'savings': self.current_balance, 'action': self.action}

    def reset(self):
        # reset the state of the environment to an initial state
        self.current_balance = self.usr.current_balance
        self.current_step = 0
        self.max_adjusted = self.usr.max_annual_amount
        return np.array([self.current_balance / self.SCALE_FACTOR] + self.one_hot[self.current_step])

    def render(self, mode='human', close=False):
        print(f'Step: {self.current_step} current_balance: {self.current_balance} action: {self.action}')