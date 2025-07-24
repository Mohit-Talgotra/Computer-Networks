def correctHamming(hamming_code):
    h = list(map(int, hamming_code))
    h.reverse()
    n = len(h)
    r = 0
    while (2 ** r) < n:
        r += 1

    error_pos = 0
    for i in range(r):
        idx = (2 ** i) - 1
        val = 0
        for j in range(idx, n, 2 ** (i + 1)):
            val ^= sum(h[j:j + 2 ** i])
        if val % 2 != 0:
            error_pos += 2 ** i

    if 0 < error_pos <= len(h):
        h[error_pos - 1] ^= 1

    corrected = []
    for i in range(len(h)):
        if (i + 1) & i:
            corrected.append(h[i])
    corrected.reverse()
    return ''.join(map(str, corrected)), error_pos != 0

with open("communicationChannel/File1.txt", "r") as f:
    originalPayload = f.readline().split(": ")[1].strip()
    message_received = f.readlines()[2].split(": ")[1].strip()

with open("communicationChannel/File3.txt", "r") as f:
    lines = f.readlines()
    messageReceived = lines[3].split(": ")[1].strip()

correctedMessage, wasError = correctHamming(messageReceived)

isCorrupted = 'Yes' if wasError else 'No'
isMatch = 'Yes' if correctedMessage == originalPayload else 'No'

with open("communicationChannel/File4.txt", "w") as f:
    f.write(f"Message received: {message_received}\n")
    f.write(f"Is message corrupted: {isCorrupted}\n")
    f.write(f"Rectified Message: {correctedMessage}\n")
    f.write(f"Original Message: {originalPayload}\n")
    f.write(f"Is there a match between rectified message and original message? {isMatch}\n")
