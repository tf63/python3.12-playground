import asyncio
from typing import Literal

a: list[int] | None = [1]
a = None
a = 'a'

b: Literal['b1', 'b2', 'b3'] = 'b1'
b = 'b2'


async def say_hello(delay, name, **kwargs):
    print(f'Hello, {name}')
    return name


async def main():
    assert True
    task1 = asyncio.create_task(say_hello(2, 'Alice'))
    name = await task1
    print(name)
    task2 = asyncio.create_task(say_hello(1, 'Bob'))
    name = await task2
    print(name)


asyncio.run(main())


class A:
    def __init__(self):
        self.a = 1
        self._b = 2


k = A()

print(k.a)
print(k._b)
