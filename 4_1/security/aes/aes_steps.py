
import random
import numpy as np


#############################################################
###################  AES Constants  #########################

sub_box = (
    '0x63', '0x7C', '0x77', '0x7B', '0xF2', '0x6B', '0x6F', '0xC5', '0x30', '0x01', '0x67', '0x2B', '0xFE', '0xD7', '0xAB', '0x76',
    '0xCA', '0x82', '0xC9', '0x7D', '0xFA', '0x59', '0x47', '0xF0', '0xAD', '0xD4', '0xA2', '0xAF', '0x9C', '0xA4', '0x72', '0xC0',
    '0xB7', '0xFD', '0x93', '0x26', '0x36', '0x3F', '0xF7', '0xCC', '0x34', '0xA5', '0xE5', '0xF1', '0x71', '0xD8', '0x31', '0x15',
    '0x04', '0xC7', '0x23', '0xC3', '0x18', '0x96', '0x05', '0x9A', '0x07', '0x12', '0x80', '0xE2', '0xEB', '0x27', '0xB2', '0x75',
    '0x09', '0x83', '0x2C', '0x1A', '0x1B', '0x6E', '0x5A', '0xA0', '0x52', '0x3B', '0xD6', '0xB3', '0x29', '0xE3', '0x2F', '0x84',
    '0x53', '0xD1', '0x00', '0xED', '0x20', '0xFC', '0xB1', '0x5B', '0x6A', '0xCB', '0xBE', '0x39', '0x4A', '0x4C', '0x58', '0xCF',
    '0xD0', '0xEF', '0xAA', '0xFB', '0x43', '0x4D', '0x33', '0x85', '0x45', '0xF9', '0x02', '0x7F', '0x50', '0x3C', '0x9F', '0xA8',
    '0x51', '0xA3', '0x40', '0x8F', '0x92', '0x9D', '0x38', '0xF5', '0xBC', '0xB6', '0xDA', '0x21', '0x10', '0xFF', '0xF3', '0xD2',
    '0xCD', '0x0C', '0x13', '0xEC', '0x5F', '0x97', '0x44', '0x17', '0xC4', '0xA7', '0x7E', '0x3D', '0x64', '0x5D', '0x19', '0x73',
    '0x60', '0x81', '0x4F', '0xDC', '0x22', '0x2A', '0x90', '0x88', '0x46', '0xEE', '0xB8', '0x14', '0xDE', '0x5E', '0x0B', '0xDB',
    '0xE0', '0x32', '0x3A', '0x0A', '0x49', '0x06', '0x24', '0x5C', '0xC2', '0xD3', '0xAC', '0x62', '0x91', '0x95', '0xE4', '0x79',
    '0xE7', '0xC8', '0x37', '0x6D', '0x8D', '0xD5', '0x4E', '0xA9', '0x6C', '0x56', '0xF4', '0xEA', '0x65', '0x7A', '0xAE', '0x08',
    '0xBA', '0x78', '0x25', '0x2E', '0x1C', '0xA6', '0xB4', '0xC6', '0xE8', '0xDD', '0x74', '0x1F', '0x4B', '0xBD', '0x8B', '0x8A',
    '0x70', '0x3E', '0xB5', '0x66', '0x48', '0x03', '0xF6', '0x0E', '0x61', '0x35', '0x57', '0xB9', '0x86', '0xC1', '0x1D', '0x9E',
    '0xE1', '0xF8', '0x98', '0x11', '0x69', '0xD9', '0x8E', '0x94', '0x9B', '0x1E', '0x87', '0xE9', '0xCE', '0x55', '0x28', '0xDF',
    '0x8C', '0xA1', '0x89', '0x0D', '0xBF', '0xE6', '0x42', '0x68', '0x41', '0x99', '0x2D', '0x0F', '0xB0', '0x54', '0xBB', '0x16',
)


# Mapping Matrix Required For Using in InvSubBytes Step
inverse_sub_box = (
    '0x52', '0x09', '0x6A', '0xD5', '0x30', '0x36', '0xA5', '0x38', '0xBF', '0x40', '0xA3', '0x9E', '0x81', '0xF3', '0xD7', '0xFB',
    '0x7C', '0xE3', '0x39', '0x82', '0x9B', '0x2F', '0xFF', '0x87', '0x34', '0x8E', '0x43', '0x44', '0xC4', '0xDE', '0xE9', '0xCB',
    '0x54', '0x7B', '0x94', '0x32', '0xA6', '0xC2', '0x23', '0x3D', '0xEE', '0x4C', '0x95', '0x0B', '0x42', '0xFA', '0xC3', '0x4E',
    '0x08', '0x2E', '0xA1', '0x66', '0x28', '0xD9', '0x24', '0xB2', '0x76', '0x5B', '0xA2', '0x49', '0x6D', '0x8B', '0xD1', '0x25',
    '0x72', '0xF8', '0xF6', '0x64', '0x86', '0x68', '0x98', '0x16', '0xD4', '0xA4', '0x5C', '0xCC', '0x5D', '0x65', '0xB6', '0x92',
    '0x6C', '0x70', '0x48', '0x50', '0xFD', '0xED', '0xB9', '0xDA', '0x5E', '0x15', '0x46', '0x57', '0xA7', '0x8D', '0x9D', '0x84',
    '0x90', '0xD8', '0xAB', '0x00', '0x8C', '0xBC', '0xD3', '0x0A', '0xF7', '0xE4', '0x58', '0x05', '0xB8', '0xB3', '0x45', '0x06',
    '0xD0', '0x2C', '0x1E', '0x8F', '0xCA', '0x3F', '0x0F', '0x02', '0xC1', '0xAF', '0xBD', '0x03', '0x01', '0x13', '0x8A', '0x6B',
    '0x3A', '0x91', '0x11', '0x41', '0x4F', '0x67', '0xDC', '0xEA', '0x97', '0xF2', '0xCF', '0xCE', '0xF0', '0xB4', '0xE6', '0x73',
    '0x96', '0xAC', '0x74', '0x22', '0xE7', '0xAD', '0x35', '0x85', '0xE2', '0xF9', '0x37', '0xE8', '0x1C', '0x75', '0xDF', '0x6E',
    '0x47', '0xF1', '0x1A', '0x71', '0x1D', '0x29', '0xC5', '0x89', '0x6F', '0xB7', '0x62', '0x0E', '0xAA', '0x18', '0xBE', '0x1B',
    '0xFC', '0x56', '0x3E', '0x4B', '0xC6', '0xD2', '0x79', '0x20', '0x9A', '0xDB', '0xC0', '0xFE', '0x78', '0xCD', '0x5A', '0xF4',
    '0x1F', '0xDD', '0xA8', '0x33', '0x88', '0x07', '0xC7', '0x31', '0xB1', '0x12', '0x10', '0x59', '0x27', '0x80', '0xEC', '0x5F',
    '0x60', '0x51', '0x7F', '0xA9', '0x19', '0xB5', '0x4A', '0x0D', '0x2D', '0xE5', '0x7A', '0x9F', '0x93', '0xC9', '0x9C', '0xEF',
    '0xA0', '0xE0', '0x3B', '0x4D', '0xAE', '0x2A', '0xF5', '0xB0', '0xC8', '0xEB', '0xBB', '0x3C', '0x83', '0x53', '0x99', '0x61',
    '0x17', '0x2B', '0x04', '0x7E', '0xBA', '0x77', '0xD6', '0x26', '0xE1', '0x69', '0x14', '0x63', '0x55', '0x21', '0x0C', '0x7D',
)


mix_col_matrix = [['0x02', '0x03', '0x01', '0x01'], ['0x01', '0x02', '0x03', '0x01'], [
    '0x01', '0x01', '0x02', '0x03'], ['0x03', '0x01', '0x01', '0x02']]

inv_mix_col_matrix = [['0x0E', '0x0B', '0x0D', '0x09'], ['0x09', '0x0E', '0x0B', '0x0D'], [
    '0x0D', '0x09', '0x0E', '0x0B'], ['0x0B', '0x0D', '0x09', '0x0E']]

# Mapping dictionary for hexadecimal to integer
hex_to_int_mapping = {
    '0': 0,  '1': 1,  '2': 2,  '3': 3,
    '4': 4,  '5': 5,  '6': 6,  '7': 7,
    '8': 8,  '9': 9,  'a': 10, 'b': 11,
    'c': 12, 'd': 13, 'e': 14, 'f': 15,
    'A': 10, 'B': 11, 'C': 12, 'D': 13,
    'E': 14, 'F': 15
}

# Rcon values for key expansion
rcon = [
    ['0x01', '0x00', '0x00', '0x00'],
    ['0x02', '0x00', '0x00', '0x00'],
    ['0x04', '0x00', '0x00', '0x00'],
    ['0x08', '0x00', '0x00', '0x00'],
    ['0x10', '0x00', '0x00', '0x00'],
    ['0x20', '0x00', '0x00', '0x00'],
    ['0x40', '0x00', '0x00', '0x00'],
    ['0x80', '0x00', '0x00', '0x00'],
    ['0x1b', '0x00', '0x00', '0x00'],
    ['0x36', '0x00', '0x00', '0x00']
]


nc_s = 4  # Number of columns (32-bit words) in the state



#############################################################
#################  Utility Functions ########################


def print_matrix(matrix):
    for row in matrix:
        print(row)


def transpose(mat):
    return np.array(mat).transpose().tolist()


def generate_matrix_from_list(initial_key):
    key_matrix = [
        [initial_key[0], initial_key[1], initial_key[2], initial_key[3]],
        [initial_key[4], initial_key[5], initial_key[6], initial_key[7]],
        [initial_key[8], initial_key[9], initial_key[10], initial_key[11]],
        [initial_key[12], initial_key[13], initial_key[14], initial_key[15]]
    ]
    return key_matrix



####################################################################
################### Data Preprocessing #############################


def plaintext_ascii_to_hex(plaintext):
    plaintext_hex = []
    for i in plaintext:
        plaintext_hex.append(hex(ord(i))[2:])
    return "".join(plaintext_hex)


def plaintext_hex_to_blocks(key_hex):
    idx = 0
    ret = []
    while idx < len(key_hex):

        key_list = [key_hex[i:i+2]
                    for i in range(idx, min(idx+31, len(key_hex)), 2)]

        while (len(key_list) < 16):
            key_list.append("20")

        key_list = [f'0x{byte}' for byte in key_list]
        idx += 32
        ret.append(key_list)
    return ret


def generate_random_key(seed=0):
    random.seed(seed)
    key = []
    for _ in range(4*4):
        key.append(hex(random.randint(0, 2**7))[2:].rjust(2, "0"))

    return plaintext_hex_to_blocks("".join(key))[0]





#############################################################
################ Operation Functions ########################


### Mathematical Operations ###


def xor_hex(hex_string_1, hex_string_2):

    int1 = int(hex_string_1, 16)
    int2 = int(hex_string_2, 16)
    # Perform XOR operation
    result = int1 ^ int2
    # Convert result back to hexadecimal string
    hex_result = hex(result)[2:]  # Remove '0x' prefix
    # Pad with leading zeros if necessary
    hex_result = hex_result.zfill(
        max(len(hex_string_1), len(hex_string_2)) - 2)
    hex_result = '0x' + hex_result
    return hex_result

def xor_hex_word(w1, w2):
    ret = [ xor_hex(w1[i], w2[i]) for i in range(4) ]
    return ret

def multiply_hex_strings(hex_string_1, hex_string_2):

    # Convert hexadecimal strings to integers
    int1 = int(hex_string_1, 16)
    int2 = int(hex_string_2, 16)

    # Perform multiplication
    result = int1 * int2

    # Convert result back to hexadecimal string
    hex_result = hex(result)[2:]  # Remove '0x' prefix
    hex_result = hex_result.zfill(
        max(len(hex_string_1), len(hex_string_2)) - 2)

    return hex_result



### Finite Field Multiplication within 2^8 ###

def finite_field_mul(a, b):

    a = int(a, 16)
    b = int(b, 16)

    if b == 1:
        return hex(a)
    
    tmp = (a << 1) & 0xff
    if b == 2:
        return hex(tmp) if a < 128 else xor_hex(hex(tmp), hex(0x1b))
    if b == 3:
        return xor_hex(finite_field_mul(hex(a), hex(2)), hex(a))
      
def inv_finite_field_mul(x, y):

    x = int(x, 16)
    y = int(y, 16)

    p = 0b100011011             # mpy modulo x^8+x^4+x^3+x+1
    m = 0                       # m will be product
    for i in range(8):
        m = m << 1
        if m & 0b100000000:
            m = m ^ p
        if y & 0b010000000:
            m = m ^ x
        y = y << 1
    return hex(m)
  
  
  
### Rotation operation ###
  
def rotate_word(word):
    return word[1:] + [word[0]]



### Substitution operation ###

def sub_word(word):
    for i in range(4):
        char1 = word[i][2]
        char2 = word[i][3]
        word[i] = sub_box[(hex_to_int_mapping[char1]*16) +
                       hex_to_int_mapping[char2]]
    return word

def inverse_sub_word(word):
    for i in range(4):
        char1 = word[i][2]
        char2 = word[i][3]
        word[i] = inverse_sub_box[(hex_to_int_mapping[char1]*16) +
                          hex_to_int_mapping[char2]]
    return word






#############################################################
#################  Matrix Operations ########################


### Multiply matrices ###

def matrix_multiply(matrix1, matrix2):
    
    result = []
    for i in range(0, 4):
        result.append(['0x00' for i in range(4)])
        
    for i in range(4):
        for j in range(4):
            # Compute the dot product of the ith row of matrix1 and the jth column of matrix2
            for k in range(4):
                ff_mul_ans = finite_field_mul(matrix2[k][j], matrix1[i][k])
                # Perform XOR operation for each element
                result[i][j] = xor_hex(result[i][j], ff_mul_ans)

    return result
  
def inv_matrix_multiply(matrix1, matrix2):
    
    result = []
    for i in range(0, 4):
        result.append(['0x00' for i in range(4)])

    for i in range(4):
        for j in range(4):
            # Compute the dot product of the ith row of matrix1 and the jth column of matrix2
            for k in range(4):
                ff_mul_ans = inv_finite_field_mul(matrix2[k][j], matrix1[i][k])
                # Perform XOR operation for each element
                result[i][j] = xor_hex(result[i][j], ff_mul_ans)

    return result
  

### XOR of matrices ###

def xor_matrix(mat1, mat2):
    for i in range(4):
        for j in range(4):
            mat1[i][j] = xor_hex(mat1[i][j], mat2[i][j])
    return mat1


### Substitution Operation ###

def sub_matrix(state):
    for i in range(nc_s):
        state[i] = sub_word(state[i])
    return state

def inverse_sub_matrix(state):
    for i in range(nc_s):
        state[i] = inverse_sub_word(state[i])
    return state
  
  

### Shift row operation ###

def shift_matrix_row(state):
    for i in range(1, 4):
        state[i] = state[i][i:] + state[i][:i]
    return state

def inverse_shift_matrix_row(state):
    for i in range(1, 4):
        state[i] = state[i][-i:] + state[i][:-i]
    return state



### Mix column operation ###

def mix_column(mix_col_matrix, state):
    return matrix_multiply(mix_col_matrix, state)
  
def inverse_mix_column(inv_mix_col_matrix, state):
    return inv_matrix_multiply(inv_mix_col_matrix, state)
  









#############################################################
#################  Key Expansion  ###########################



def g(w, round_i):
    tmp = sub_word( rotate_word( w.copy() ) )
    result = xor_hex_word(tmp, rcon[round_i - 1])
    return result

def generate_round_key(round_keys, round_i):
    
    prev = round_keys[round_i-1]
    
    w0, w1, w2, w3 = prev
    w4 = xor_hex_word(w0, g(w3, round_i))
    w5 = xor_hex_word(w4, w1)
    w6 = xor_hex_word(w5, w2)
    w7 = xor_hex_word(w6, w3)
    
    return [w4, w5, w6, w7]

def key_expansion(key):
    round_keys = [key]

    for round_i in range(1, 11):
        round_keys.append(generate_round_key(round_keys, round_i))

    return round_keys













