import random

def generateParityBit(payload):
    count = payload.count('1')
    return '0' if count % 2 == 0 else '1'

def flipRandomBit(data):
    index = random.randint(0, len(data) - 1)
    corrupted = list(data)
    corrupted[index] = '1' if corrupted[index] == '0' else '0'
    return ''.join(corrupted)

originalPayload = ''.join(random.choice('01') for _ in range(25))

parityBit = generateParityBit(originalPayload)
messageSent = originalPayload + parityBit

message_received = messageSent
message_received = flipRandomBit(messageSent)

with open("communicationChannel/File1.txt", "w") as f:
    f.write(f"Original bits: {originalPayload}\n")
    f.write(f"Extra bit(s) for detecting errors: {len(messageSent) - len(originalPayload)}\n")
    f.write(f"Message sent: {messageSent}\n")
    f.write(f"Message received: {message_received}\n")

