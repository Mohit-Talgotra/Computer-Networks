import random

def insertParityBits(data_bits):
    data = list(data_bits)
    data.reverse()
    h = []
    j = 0
    r = 0

    while (len(data) + r + 1) > (2 ** r):
        r += 1

    for i in range(r + len(data)):
        if (i + 1) == 2 ** j:
            h.append(0)
            j += 1
        else:
            h.append(int(data.pop(0)))

    for i in range(r):
        idx = (2 ** i) - 1
        val = 0
        for j in range(idx, len(h), 2 ** (i + 1)):
            val ^= sum(h[j:j + 2 ** i])
        h[idx] = val % 2

    h.reverse()
    return ''.join(map(str, h))

def flipRandomBit(data):
    index = random.randint(0, len(data) - 1)
    corrupted = list(data)
    corrupted[index] = '1' if corrupted[index] == '0' else '0'
    return ''.join(corrupted)

with open("communicationChannel/File1.txt", "r") as f:
    originalPayload = f.readline().split(": ")[1].strip()

hammingCode = insertParityBits(originalPayload)
messageSent = hammingCode

messageReceived = flipRandomBit(messageSent)

with open("communicationChannel/File3.txt", "w") as f:
    f.write(f"Original bits: {originalPayload}\n")
    f.write(f"Extra bit(s) for correcting errors: {messageSent[len(originalPayload):]}\n")
    f.write(f"Message sent: {messageSent}\n")
    f.write(f"Message received: {messageReceived}\n")
