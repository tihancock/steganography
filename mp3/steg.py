import mmap
from textutils import ascii_to_bitarray, bitarray_to_ascii

def decode_message(file_path):
    f = open(file_path, 'r+b')
    map = mmap.mmap(f.fileno(), 0)

    bit_array = []
    for i in range(len(map)):
        val = ord(map[-(i+1)]) & (1<<0)
        bit_array.append(val)

    print bitarray_to_ascii(bit_array)

    map.close()

    return True

def encode_message(file_path, message):
    f = open(file_path, 'r+b')
    map = mmap.mmap(f.fileno(), 0)

    message_bits = ascii_to_bitarray(message)
   
    for i in range(len(message_bits)):
        val = ord(map[-(i+1)])
        val &= ~(1<<0)
        val |= message_bits[i]
        map[-(i+1)] = chr(val)

    map.flush()

    map.close()
    
    return True
