# 큐(Queue)

- 먼저 넣은 것을 먼저 꺼내는 FIFO 자료구조다. 뒤(rear)로 넣고(enqueue) 앞(front)에서 꺼낸다(dequeue).
- Python에서는 `collections.deque`의 `append()`와 `popleft()`로 쓴다. `list.pop(0)`은 나머지를 다 옮겨서 O(n)이라 느리다.
- 예: 프린터 대기열, 작업 대기열, 너비 우선 탐색(BFS).
