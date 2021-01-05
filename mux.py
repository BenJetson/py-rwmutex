from threading import Lock, Condition


class Status:
    def __init__(self):
        self.lock = Lock()
        self.cv = Condition(self.lock)

        self.reader_count = 0
        self.writer_count = 0


class Reader:
    def __init__(self, status: Status):
        self.status = status

    def __enter__(self):
        with self.status.cv:
            while self.status.writer_count > 0:
                self.status.cv.wait()

            self.status.reader_count += 1

    def __exit__(self, type, value, traceback):
        with self.status.cv:
            self.status.reader_count -= 1
            self.status.cv.notify_all()


class Writer:
    def __init__(self, status: Status):
        self.status = status

    def __enter__(self):
        with self.status.cv:
            while self.status.reader_count > 0 or self.status.writer_count > 0:
                self.status.cv.wait()

            self.status.writer_count += 1

    def __exit__(self, type, value, traceback):
        with self.status.cv:
            self.status.writer_count -= 1
            self.status.cv.notify_all()


class RWLock:
    def __init__(self):
        status = Status()

        self.read = Reader(status)
        self.write = Writer(status)

