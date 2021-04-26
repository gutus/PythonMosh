# QUEUES
# FIFO (First In First Out)
from collections import deque
# Membuat list dengan variabel queue list kosong dan mengisinya dengan class deque deque yg module nya sudah diimport
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()  # Digunakan untuk menghapus item paling kiri dari item list
print(queue)
