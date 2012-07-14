import string

def ascii_to_bitarray(text):
    # Insert length of string first
    result=[int(n) for n in list(bin(len(text))[2:].rjust(16,'0'))]
    for c in text:
        result += [int(n) for n in list(bin(ord(c))[2:].rjust(8,'0'))]

    return result
    
def bitarray_to_ascii(bitarray):
    message_length = int(string.join([str(b) for b in bitarray[:16]],''), 2)
    
    message = ""
    
    for i in range(message_length):
        message += chr(int(string.join([str(b) for b in bitarray[16+i*8:16+(i+1)*8]],''), 2))

    return message
                                  
