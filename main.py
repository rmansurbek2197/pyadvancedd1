import asyncio
import heapq
from typing import Any, Optional

class AsyncPriorityQueue:
    def __init__(self):
        self._queue = []
        self._lock = asyncio.Lock()

    async def put(self, item: Any, priority: int):
        async with self._lock:
            heapq.heappush(self._queue, (priority, item))

    async def get(self) -> Optional[Any]:
        async with self._lock:
            if not self._queue:
                return None
            return heapq.heappop(self._queue)[1]

    async def empty(self) -> bool:
        async with self._lock:
            return not bool(self._queue)

    async def size(self) -> int:
        async with self._lock:
            return len(self._queue)

async def produce(queue: AsyncPriorityQueue, item: Any, priority: int):
    await queue.put(item, priority)

async def consume(queue: AsyncPriorityQueue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(item)

async def main():
    queue = AsyncPriorityQueue()
    await produce(queue, 'low', 10)
    await produce(queue, 'high', 1)
    await produce(queue, 'medium', 5)
    await consume(queue)

asyncio.run(main())

class Item:
    def __init__(self, name: str, priority: int):
        self.name = name
        self.priority = priority

async def main2():
    queue = AsyncPriorityQueue()
    item1 = Item('low', 10)
    item2 = Item('high', 1)
    item3 = Item('medium', 5)
    await produce(queue, item1.name, item1.priority)
    await produce(queue, item2.name, item2.priority)
    await produce(queue, item3.name, item3.priority)
    while not await queue.empty():
        print(await queue.get())

asyncio.run(main2())

class PriorityQueue:
    def __init__(self):
        self._queue = []

    def put(self, item: Any, priority: int):
        heapq.heappush(self._queue, (priority, item))

    def get(self) -> Optional[Any]:
        if not self._queue:
            return None
        return heapq.heappop(self._queue)[1]

    def empty(self) -> bool:
        return not bool(self._queue)

    def size(self) -> int:
        return len(self._queue)

async def main3():
    queue = PriorityQueue()
    queue.put('low', 10)
    queue.put('high', 1)
    queue.put('medium', 5)
    while not queue.empty():
        print(queue.get())

asyncio.run(main3())