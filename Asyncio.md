ASYNCIO
===

Calling a coroutine function does not execute it, but rather returns a coroutine object. (This is analogous to generator functions - calling them doesn’t execute the function, it returns a generator object, which we then use later.)

To execute a coroutine object, either:
1. use it in an expression with await in front of it
2. schedule it with ensure_future() or create_task().