import Image
from textutils import ascii_to_bitarray, bitarray_to_ascii

def decode_message(file_path):
    im = Image.open(file_path)
    
    pix = im.load()
    width, height = im.size
    bitarray = []

    for i in range(width*height):
        bitarray.append(pix[i%width,i/width][0] & (1<<0))

    print pix[15,0]
    
    bitarray_to_ascii(bitarray)

def encode_message(file_path, message):
    im = Image.open(file_path)

    pix           = im.load()
    width, height = im.size
    bit_array     = ascii_to_bitarray(message)
    
    if len(bit_array) > width*height:
        return False

    #for i in range(len(bit_array)):
    for i in range(16):
        pixel_vals = pix[i%width,i/width]
        modified = pixel_vals[0]
        modified &= ~(1<<0)
        modified |= bit_array[i]
        pix[i%width,i/width] = (modified, pixel_vals[1], pixel_vals[2])
        if i < 16:
            print "(%d, %d): %d" % (i%width, i/width, pix[i%width,i/height][0])

    
    pix[15,0]=(1,2,3)

    im.save('./modified_'+file_path.split('/')[-1], im.format)

    return True
