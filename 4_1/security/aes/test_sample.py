
from util import *
from const import *

# Example AES encryption with 128-bit input plaintext

def decrypt(cipher_matrix, initial_key):

  # Reshape the initial key into a 4x4 matrix :
  key_matrix = generatingMatrixFromList(initial_key)

  # generating round keys :
  round_keys = keyExpansion(key_matrix)
  round_keys.reverse()

  for i in range (11):
    print("round ", i, " ", round_keys[i])


  cipher_matrix = transpose(cipher_matrix)

  print_matrix(cipher_matrix)
  # print_matrix(round_keys)

  new_state_matrix = xorMatrix(cipher_matrix, round_keys[0])
  # print("after first inverse add round key : ")
  # print_matrix(new_state_matrix)
  # print()

  new_state_matrix = np.array(new_state_matrix).transpose().tolist()

  for i in range(1,10):
    new_state_matrix = invShiftRow(new_state_matrix)
    # print("after inverse shift matrix row : ")
    # print_matrix(new_state_matrix)
    # print()

    new_state_matrix = invSubMatrix(new_state_matrix)
    # print("after inverse substitution : ")
    # print_matrix(new_state_matrix)
    # print()

    new_state_matrix = xorMatrix(new_state_matrix,np.array(round_keys[i]).transpose().tolist())
    # print("after inverse add round key : ")
    # print_matrix(new_state_matrix)
    # print()

    new_state_matrix = invMixColumn(inv_mix_col_matrix, new_state_matrix)
    # print("after inverse mix column : ")
    # print_matrix(new_state_matrix)
    # print()


  # round 10 of aes :
  new_state_matrix = invShiftRow(new_state_matrix)
  # print("after inverse shift matrix row : ")
  # print_matrix(new_state_matrix)
  # print()

  new_state_matrix = invSubMatrix(new_state_matrix)
  # print("after inverse substitution : ")
  # print_matrix(new_state_matrix)
  # print()

  new_state_matrix = xorMatrix(new_state_matrix,np.array(round_keys[0]).transpose().tolist())
  # print("after inverse add round key : ")
  # print_matrix(new_state_matrix)
  # print()

  return new_state_matrix