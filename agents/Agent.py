from abc import ABC, abstractmethod


class Agent(ABC):

    def __init__(self, alpha, epsilon, discount):
        self.alpha = alpha
        self.epsilon = epsilon
        self.discount = discount
        self.learning_is_enabled = True

    @abstractmethod
    def update(self, state, action, reward, next_state):
        pass

    @abstractmethod
    def get_best_action(self, state):
        pass

    @abstractmethod
    def get_action(self, state):
        pass

    @abstractmethod
    def get_value(self, state):
        pass

    def turn_off_learning(self):
        self.learning_is_enabled = False

    def turn_on_learning(self):
        self.learning_is_enabled = True
