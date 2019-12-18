from __future__ import annotations
from abc import ABC, abstractmethod

class Compressor():
    def __init__(self, compression: Compression) -> None:
        self.p = compression

    @property
    def compression(self) -> Compression:
        return self.p

    @compression.setter
    def compression(self, compression: Compression) -> None:
        self.p = compression

    def compress(self) -> None:
        self.p.compress()

class Compression(ABC):
    @abstractmethod
    def compress(self):
        pass

class RAR_Compression(Compression):
    def compress(self) -> None:
        print("RAR compression")

class ZIP_Compression(Compression):
    def compress(self) -> None:
        print("ZIP compression")

if __name__ == "__main__":
    compressor = Compressor(RAR_Compression())
    compressor.compress()
    print()
    compressor.p = ZIP_Compression()
    compressor.compress()