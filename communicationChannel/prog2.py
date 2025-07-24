def checkParity(received_message):
    count = received_message.count('1')
    return count % 2 == 0

with open("communicationChannel/File1.txt", "r") as f:
    lines = f.readlines()
    message_received = lines[3].split(": ")[1].strip()

isValid = checkParity(message_received)

with open("communicationChannel/File2.txt", "w") as f:
    f.write(f"Message received: {message_received}\n")
    f.write(f"Is message corrupted: {'No' if isValid else 'Yes'}\n")
