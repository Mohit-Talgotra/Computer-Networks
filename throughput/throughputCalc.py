import random
import matplotlib.pyplot as plt
import numpy as np

T = 1000

class Req:
    def __init__(self, node_id, slot_time, attempt_no, msg_no):
        self.node_id = node_id
        self.slot_time = slot_time
        self.attempt_no = attempt_no
        self.msg_no = msg_no

class ReqLL:
    def __init__(self, R):
        self.R = R
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        self.length = 0

    def insert_sorted(self, R):
        node = ReqLL(R)
        if self.start is None or R.slot_time < self.start.R.slot_time:
            node.next = self.start
            self.start = node
        else:
            cur = self.start
            while cur.next and cur.next.R.slot_time <= R.slot_time:
                cur = cur.next
            node.next = cur.next
            cur.next = node
        self.length += 1

def simulate_throughput_linked(N, k, T=1000):
    timeline = LinkedList()
    throughput = 0

    for node in range(1, N+1):
        first_slot = random.randint(1, T)
        timeline.insert_sorted(Req(node, first_slot, 1, 1))

    while timeline.start and timeline.start.R.slot_time <= T:
        current_slot = timeline.start.R.slot_time
        same_slot = []

        cur = timeline.start
        while cur and cur.R.slot_time == current_slot:
            same_slot.append(cur.R)
            cur = cur.next

        timeline.start = cur
        timeline.length -= len(same_slot)

        if len(same_slot) == 1:
            throughput += 1
            r = same_slot[0]
            if r.msg_no < k and current_slot < T:
                next_slot = random.randint(current_slot + 1, T)
                timeline.insert_sorted(Req(r.node_id, next_slot, 1, r.msg_no + 1))
        else:
            for r in same_slot:
                if current_slot < T:
                    retry_slot = random.randint(current_slot + 1, T)
                    timeline.insert_sorted(Req(r.node_id, retry_slot, r.attempt_no + 1, r.msg_no))

    return throughput

k_values = list(range(1, 11))
N_values = range(10, 300, 10)
plt.figure(figsize=(10, 6))

for k in k_values:
    print(f"Processing throughput vs N for k={k}")
    throughputs = []
    for N in N_values:
        trials = [simulate_throughput_linked(N, k, T) for _ in range(10)]
        throughputs.append(np.mean(trials))
    plt.plot(N_values, throughputs, label=f'k={k}')

plt.xlabel('Number of Nodes (N)')
plt.ylabel('Throughput (Successful Requests)')
plt.title('Throughput vs Number of Nodes (with collision retry)')
plt.legend()
plt.grid(True)
plt.show()

N_values_fixed = list(range(50, 300, 30))
k_values = list(range(1, 11))
plt.figure(figsize=(10, 6))

for N in N_values_fixed:
    print(f"Processing throughput vs k for N={N}")
    throughputs = []
    for k in k_values:
        trials = [simulate_throughput_linked(N, k, T) for _ in range(10)]
        throughputs.append(np.mean(trials))
    plt.plot(k_values, throughputs, label=f'N={N}')

plt.xlabel('k (messages per node per day)')
plt.ylabel('Throughput (Successful Requests)')
plt.title('Throughput vs k (with collision retry)')
plt.legend()
plt.grid(True)
plt.show()
