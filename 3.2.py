import base64
import string
import subprocess

# Connect to the server and read the output directly
def get_cipher(payload):
    result = subprocess.run(f'echo \'{payload}\' | nc localhost 9999', capture_output=True, text=True, shell=True)
    output = result.stdout.strip().split('\n')
    line = output[-1] if len(output) > 1 else ''
    words = line.split(': ')
    cipher_base64 = words[-1] if len(words) > 1 else ''
    #print(f"Payload: {payload}, Cipher: {cipher_base64}")
    cipher_base64 = cipher_base64.encode('ascii')
    cipher_bytes = base64.b64decode(cipher_base64)
    return cipher_bytes

def bruteforce():
    flag = ''
    total = 16 - 1
    chars = string.printable

    while True:
        payload = '1' * (total - len(flag))
        
        cipher_target = get_cipher(payload)
        #print(f"len(cipher_target): {len(cipher_target)}")
        for char in chars:
            payload = '1' * (total - len(flag)) + flag + char
            cipher = get_cipher(payload)
            #print(f"block_target: {cipher_target[0:32]}, block: {cipher[0:32]}")
            if cipher[0:32] == cipher_target[0:32]:
                flag += char
                break

        print(f"Current flag: {flag}")

        if len(flag) == 0:
            break

        if len(flag) == total:
            break

bruteforce()

