# byte_array = "CC".encode()
 
# # Converting the byte_array into a binary 
# # integer
# binary_int = int.from_bytes(byte_array, "big")
 
# # Converting binary_int to a string of 
# # binary characters
# binary_string = bin(binary_int)
 
# # Getting the converted binary characters
# print(binary_string)

# for  i in binary_string:
#     print(i)


# def encode(inp):
#     """
#     Encodes given input to 7-bit ASCII.
#     :param inp: the 8-bit ASCII input in binary
#     :return: the input encoded in 7-bit ASCII in binary
#     Pre-Conditions: the input exists and has already been converted to binary
#     Post-Conditions: The input still exists but is encoded in 7-bit ASCII (still in binary)
#     """
#     bit_mask = 0b1111111
#     e = []
#     for b in inp:
#         e.append(b & bit_mask)
#     return e

# print(encode(binary_string[2:]))

m = "CC"
g = ""

for c in m:
    g += str(bin(ord(c)))[2:]

print(g)
