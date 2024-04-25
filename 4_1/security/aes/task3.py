
import aes as AES
import rsa as RSA
import json
import numpy as np


def getStringFromMat(mat):
    ret = ""
    for ir in range(len(mat[0])):
        for ic in range(len(mat)):
            ret += mat[ic][ir].replace('0x','')

    return bytes.fromhex(ret).decode("cp437")


def getStringFromList(list):
    ret = ""
    for ir in range(len(list)):
        ret += list[ir].replace('0x','')

    return bytes.fromhex(ret).decode("cp437")


def getListFromString(str):
    ret = []

    for i in range(len(str)):
        ret.append( "0x" + str[i].encode("cp437").hex() )

    return ret


class Sender():

    def __init__(self, rsa_bitsize):
        self.rsa_bitsize = rsa_bitsize

    def send( self, plaintext ):
        
        f = open("do_not_open/alice.in", 'w')
        f.write(plaintext)
        f.close()
                
        plaintext_hex = AES.plaintext_ascii_to_hex( plaintext )
        plaintext_blocks = AES.plaintext_hex_to_blocks( plaintext_hex )
        
        key = AES.generate_random_key(0)
        
        print("key: ", key)
        print("Blocks: ", plaintext_blocks)

        encrypted_blocks = []
        for block in plaintext_blocks:
            encrypted_blocks.append( AES.encrypt( block, key ) )

        public_key, private_key = RSA.generate_keypair( self.rsa_bitsize )
        encrypted_key_arr = RSA.encrypt( public_key, getStringFromList( key ) )

        f = open("do_not_open/private_key", "w")
        f.write( json.dumps(private_key) )
        f.close()


        f = open("do_not_open/alice_out", "w")
        f.write( json.dumps( { 'ciphertext': encrypted_blocks, 'key': encrypted_key_arr } ) )
        f.close()

        return ( encrypted_blocks, encrypted_key_arr )
    



class Receiver():
    def __init__(self, rsa_bitsize):
        self.rsa_bitsize = rsa_bitsize

    def get_hex_arr_from_string( self, str ):
        ret = []
        for i in range(len(str), 2):
            ret.append( f"0x{i[i:i+2]}" )

        return ret

    def receive( self ):

        f = open("do_not_open/alice_out", "r")
        d = f.read()
        d = json.loads( d )
        f.close()
        encrypted_blocks, encrypted_key_arr = ( d["ciphertext"], d["key"] )

        print("Encrypted blocks: ", encrypted_blocks)
        print("Encrypted key: ", encrypted_key_arr)
        
        f = open("do_not_open/private_key", "r")
        private_key = json.loads( f.read() )
        f.close()
        
        key = RSA.decrypt( private_key, encrypted_key_arr )
        print( getListFromString( key ) )

        decrypted_blocks = []
        for block in encrypted_blocks:
            decrypted_blocks.append( AES.decrypt( block, getListFromString( key )) )

        decrypted_hex = []
        for block in decrypted_blocks:
            decrypted_hex.extend( np.array(block).transpose().flatten().tolist() )


        print( "".join( [ bytearray.fromhex(ret[2:]).decode() for ret in decrypted_hex ] ) )
        f = open('do_not_open/bob.out', 'w')
        f.write( "".join( [ bytearray.fromhex(ret[2:]).decode() for ret in decrypted_hex ] ) )
        f.close()



def verify():
    fa = open("do_not_open/alice.in", 'r')
    alice_in = fa.read()
    fb = open("do_not_open/bob.out", 'r')
    bob_out = fb.read()

    if alice_in == bob_out.strip():
        return True
    else:
        return False


alice = Sender( 16 )
bob = Receiver( 16 )


alice.send( "OMYGOWITWORKSOMYGOWITWORKSOMYGOWITWORKSOMYGOWITWORKS" )
bob.receive( )

print( "Transfer Successful" if verify() else "Transfer Failed")
