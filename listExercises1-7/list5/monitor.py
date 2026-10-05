import threading

class MonitorBuffer:
    def __init__(self, capacidade):
        self.buffer = []
        self.capacidade = capacidade
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def inserir(self, item):
        with self.not_full:
            if len(self.buffer) == self.capacidade:
                self.not_full.wait()
            self.buffer.append(item)
            self.not_empty.notify()  # acorda consumidor

    def remover(self):
        with self.not_empty:
            if len(self.buffer) == 0:
                self.not_empty.wait()
            item = self.buffer.pop(0)
            self.not_full.notify()  # acorda produtor
            return item

if __name__=='__main__':
    monitor = MonitorBuffer(10)