# ABSTRACT BASE CLASS

from abc import ABC, abstractmethod


class InvalidOperationError:  # Custom exception, tidak menggunakan builtin ValueError untuk tidak memperumit dengan internal error
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file...")


class NetworkStream(Stream):
    def read(self):
        print("Reading from a network...")


class MemoryStream(Stream):
    def read(self):
        print("Reading from memory stream")


stream = MemoryStream()
stream.open()
