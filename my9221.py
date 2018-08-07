"""
MicroPython MY9221 LED driver
https://github.com/mcauser/micropython-my9221

MIT License
Copyright (c) 2018 Mike Causer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from time import sleep_ms
from machine import Pin

class MY9221:
    def __init__(self, di, dcki, reverse=False):
        self._d = di
        self._c = dcki
        self._r = reverse
        self._d.init(Pin.OUT, value=0)
        self._c.init(Pin.OUT, value=0)

    def _latch(self):
        self._d(0)
        sleep_ms(1)
        for i in range(4):
            self._d(1)
            self._d(0)
        sleep_ms(1)

    def _write16(self, data):
        for i in range(15,-1,-1):
            self._d((data >> i) & 1)
            state = self._c()
            self._c(not state)

    def _begin(self):
        self._write16(0) # command: 8bit mode

    def _end(self):
        # unused last 2 channels are required to fill the 208 bit shift register
        self._write16(0)
        self._write16(0)
        self._latch()

    def reverse(self, val=None):
        if val is None:
            return self._r
        self._r = val

    def level(self, val, brightness=255):
        self._begin()
        for i in range(9,-1,-1) if self._r else range(10):
            self._write16(brightness if val > i else 0)
        self._end()

    def bits(self, val, brightness=255):
        val &= 0x3FF
        self._begin()
        for i in range(9,-1,-1) if self._r else range(10):
            self._write16(brightness if (val >> i) & 1 else 0)
        self._end()

    def bytes(self, buf):
        self._begin()
        for i in range(9,-1,-1) if self._r else range(10):
            self._write16(buf[i])
        self._end()
