from abc import abstractmethod


class Env:

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def get_all_states(self):
        pass

    @abstractmethod
    def is_terminal(self, state):
        pass

    @abstractmethod
    def get_possible_actions(self, state):
        pass

    @abstractmethod
    def get_next_state(self, state, action):
        pass

    @abstractmethod
    def get_reward(self, state, action, next_state):
        pass

    @abstractmethod
    def step(self, action):
        pass

    @abstractmethod
    def get_state(self):
        pass
