# py-rwmutex

This package provides a simple read/write mutex lock for threads, based upon
the `threading` package. It supports Python's context manager interface, so
it may be used within `with` statements.

## Purpose

This read/write lock can improve performance by allowing multiple threads to
reaad from a shared resource at once. For safety, only one thread is granted
a write lock at a time, and only when no threads have a read lock.

## Installation

This package is available from [PyPi](https://pypi.org/project/rwmutex/), which
means it can be easily acquired via [`pip`](https://pypi.org/project/pip/).

Run this command at a shell prompt:

```bash
pip3 install rwmutex
```

## Usage

To get started, import the package like so:

```py
from rwmutex import RWLock
```

Then you can declare a lock object:

```py
lock = RWLock()
```

To use the lock, you can use `with` blocks:

```py
with lock.write
    # some operation that writes
    pass

with lock.read:
    # some operation that just needs to read
    pass
```

For a working example, see [example.py](example.py).
