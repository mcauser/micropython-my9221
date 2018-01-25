from machine import Pin
from my9221 import MY9221

# ESP8266
ledbar = MY9221(Pin(4), Pin(5))

# PyBoard
# ledbar = MY9221(Pin('X8'), Pin('X6'))

# STM32F407VET6
# ledbar = MY9221(Pin('B6'), Pin('B8'))

# all LEDS on, full brightness
ledbar.level(10)

# four LEDS on, half brightness
ledbar.level(4, 0x0F)

# reverse orientation, first LED is green
ledbar.reverse(True)
ledbar.level(1)

# normal orientation, first LED is red
ledbar.reverse(False)
ledbar.level(1)

# switch on specific leds
ledbar.bits(0b1111100000)
ledbar.bits(0b0000011111)
ledbar.bits(1)
ledbar.bits(3)
ledbar.bits(7)

# first and last LED on, very dim
ledbar.bits(513, 7)

# alternating LEDs
ledbar.bits(0b0101010101)
ledbar.bits(0b1010101010)
buf = b'\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff'
ledbar.bytes(buf)

# fade out LEDs
buf = bytearray([0,1,3,7,15,31,63,127,255,255])
ledbar.reverse(True)
ledbar.bytes(buf)
ledbar.reverse(False)
ledbar.bytes(buf)

# various brightnesses
buf = [0,0,0,0,0,255,127,63,15,7]
ledbar.bytes(buf)

# cycle through LEDS with various brightnesses
from time import sleep_ms
buf = [0,1,3,7,15,31,63,127,255,255]
for i in range(50):
    buf.insert(0,buf.pop())
    ledbar.bytes(buf)
    sleep_ms(100)

# random LEDs
import urandom
for i in range(100):
    ledbar.bits(urandom.getrandbits(10))

# walk through all possible LED combinations
for i in range(1024):
    ledbar.bits(i)

# Use 8bit greyscale mode (default)
# LED brightness 0x00-0xFF
ledbar._write16(0x00) # command
ledbar._write16(0xFF) # led 1
ledbar._write16(0xFF) # led 2
ledbar._write16(0x00) # led 3
ledbar._write16(0x00) # led 4
ledbar._write16(0x00) # led 5
ledbar._write16(0xFF) # led 6
ledbar._write16(0xFF) # led 7
ledbar._write16(0x00) # led 8
ledbar._write16(0x00) # led 9
ledbar._write16(0x00) # led 10
ledbar._write16(0x00) # unused channel, required
ledbar._write16(0x00) # unused channel, required
ledbar._latch()

# Use 12bit greyscale mode
# LED brightness 0x000-0xFFF
ledbar._write16(0x0100) # command
ledbar._write16(0x0FFF) # led 1
ledbar._write16(0x0000) # led 2
ledbar._write16(0x00FF) # led 3
ledbar._write16(0x0000) # led 4
ledbar._write16(0x000F) # led 5
ledbar._write16(0x000F) # led 6
ledbar._write16(0x0000) # led 7
ledbar._write16(0x00FF) # led 8
ledbar._write16(0x0000) # led 9
ledbar._write16(0x0FFF) # led 10
ledbar._write16(0x0000) # unused channel, required
ledbar._write16(0x0000) # unused channel, required
ledbar._latch()

# Use 14bit greyscale mode
# LED brightness 0x000-0x3FFF
ledbar._write16(0x0200) # command
ledbar._write16(0x3FFF) # led 1
ledbar._write16(0x03FF) # led 2
ledbar._write16(0x0000) # led 3
ledbar._write16(0x0000) # led 4
ledbar._write16(0x0000) # led 5
ledbar._write16(0x003F) # led 6
ledbar._write16(0x0003) # led 7
ledbar._write16(0x0000) # led 8
ledbar._write16(0x0000) # led 9
ledbar._write16(0x0000) # led 10
ledbar._write16(0x0000) # unused channel, required
ledbar._write16(0x0000) # unused channel, required
ledbar._latch()

# Use 16bit greyscale mode
# LED brightness 0x0000-0xFFFF
ledbar._write16(0x0300) # command
ledbar._write16(0xFFFF) # led 1
ledbar._write16(0x0FFF) # led 2
ledbar._write16(0x00FF) # led 3
ledbar._write16(0x000F) # led 4
ledbar._write16(0x0007) # led 5
ledbar._write16(0x0003) # led 6
ledbar._write16(0x0001) # led 7
ledbar._write16(0x0000) # led 8
ledbar._write16(0x0000) # led 9
ledbar._write16(0x0000) # led 10
ledbar._write16(0x0000) # unused channel, required
ledbar._write16(0x0000) # unused channel, required
ledbar._latch()
