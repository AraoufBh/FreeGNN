import random


class MemoryBuffer:

    def __init__(self, capacity=500):
        self.capacity = capacity
        self.buffer = []

    def add(self, sample):

        if len(self.buffer) < self.capacity:
            self.buffer.append(sample)
        else:
            idx = random.randint(0, self.capacity - 1)
            self.buffer[idx] = sample

    def sample(self, batch_size):

        return random.sample(self.buffer, min(batch_size, len(self.buffer)))