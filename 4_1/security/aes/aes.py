from aes_steps import *
from aes_steps import *

###############################################
################# Encryption ##################

def encrypt(initial_state, initial_key):
  """_summary_
  encrypts AES state matrix generated from plaintext

  Args:
      initial_state (matrix of hex_str): 
      initial_key (matrix of hex_str): 

  Returns:
      matrix of hex_str: encrypted state matrix
  """
  
  print(initial_key, initial_state)

  # Reshape the initial key into a 4x4 matrix :
  key_mat = generate_matrix_from_list(initial_key)

  # generating round keys :
  round_keys = key_expansion(key_mat)

  state_mat = transpose( generate_matrix_from_list(initial_state) )
  
  intermediate_state_mat = xor_matrix(state_mat, transpose( round_keys[0] ) )

  for i in range(1,10):
    intermediate_state_mat = sub_matrix(intermediate_state_mat)

    intermediate_state_mat =  shift_matrix_row(intermediate_state_mat)

    intermediate_state_mat = mix_column(mix_col_matrix, intermediate_state_mat)

    intermediate_state_mat = xor_matrix(intermediate_state_mat, transpose( round_keys[i] ) )

  intermediate_state_mat = sub_matrix(intermediate_state_mat)

  intermediate_state_mat =  shift_matrix_row(intermediate_state_mat)

  intermediate_state_mat = xor_matrix(intermediate_state_mat, transpose( round_keys[10] ) )

  return intermediate_state_mat




###############################################
################# Decryption ##################

def decrypt(cipher_matrix, initial_key):
  """_summary_
  decrypts AES cipher matrix
  
  Args:
      cipher_matrix (matrix of hex_str): 
      initial_key (matrix of hex_str): 

  Returns:
      decrypted state matrix:
  """
  
  ### turn initial key into 4 x 4 matrix ###
  key_mat = generate_matrix_from_list(initial_key)

  ### generating round keys ###
  round_keys = key_expansion(key_mat)
  round_keys.reverse()


  intermediate_state_mat = xor_matrix(cipher_matrix, transpose( round_keys[0]) )

  for i in range(1,10):
    intermediate_state_mat = inverse_shift_matrix_row(intermediate_state_mat)

    intermediate_state_mat = inverse_sub_matrix(intermediate_state_mat)

    intermediate_state_mat = xor_matrix(intermediate_state_mat, transpose( round_keys[i] ) )

    intermediate_state_mat = inverse_mix_column(inv_mix_col_matrix, intermediate_state_mat)


  ### The last round of decryption which is a little different ###
  intermediate_state_mat = inverse_shift_matrix_row(intermediate_state_mat)

  intermediate_state_mat = inverse_sub_matrix(intermediate_state_mat)

  intermediate_state_mat = xor_matrix(intermediate_state_mat, transpose(round_keys[10]) )

  return intermediate_state_mat