import  streamlit as st
from Crypto.Cipher import AES
from Crypto.Cipher import DES
import binascii

def check_aes_ecb_enc(plaintext, key):
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(bytes(plaintext))
        return bytearray(ciphertext)

def check_aes_ecb_dec(ciphertext, key):
        cipher = AES.new(key, AES.MODE_ECB)
        plaintext = cipher.decrypt(bytes(ciphertext))
        return bytearray(plaintext)

def check_des_ecb_enc(plaintext,  key):
        cipher = DES.new(key, DES.MODE_ECB)
        ciphertext = cipher.encrypt(bytes(plaintext))
        return bytearray(ciphertext)

def check_des_ecb_dec(ciphertext, key):
        cipher = DES.new(key, DES.MODE_ECB)
        plaintext = cipher.decrypt(bytes(ciphertext))
        return bytearray(plaintext)

st.set_page_config(
    page_title="Cryptograph aplication  ",
    page_icon="🈴",
)

st.title("Cryptography decoder/encoder")
plain_text = st.text_input("Plain text ",value= 'cafebabecafebabe')
key_string = st.text_input("Key",value= 'cafebabecafebabe')
option_cipher = st.selectbox(
    'Cipher',
    ('AES', 'DES'),index= 1)

option_direction = st.selectbox(
    'Direction',
    ('ENC', 'DEC'),index= 0)


if option_cipher == 'AES' and option_direction == 'ENC'  and plain_text != None and key_string != None:
    key = bytearray.fromhex(key_string)
    result = check_aes_ecb_enc(bytearray.fromhex(plain_text), key)
    st.text(f"Cipher:  {binascii.hexlify(result)}")

if option_cipher == 'DES' and option_direction == 'ENC' and  plain_text != None and key_string != None:
    key = bytearray.fromhex(key_string)
    result = check_des_ecb_enc(bytearray.fromhex(plain_text), key)
    st.text(f"Cipher:  {binascii.hexlify(result)}")










