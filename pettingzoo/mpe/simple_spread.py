from ._mpe_utils.simple_env import SimpleEnv
from .scenarios.simple_spread import Scenario

class env(SimpleEnv):
    def __init__(self):
        super(env, self).__init__(Scenario())
