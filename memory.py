class SharedMemory:
    def __init__(self):
        self.state = {}
        self.messages = []

    def set(self, key, value):
        self.state[key] = value

    def get(self, key):
        return self.state.get(key)

    def exists(self, key):
        return key in self.state

    def post_message(self, sender, message):
        self.messages.append({
            "agent": sender,
            "message": message
        })
