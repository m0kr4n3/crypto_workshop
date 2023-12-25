from pwn import *
from base64 import b64decode as b64dec
from string import ascii_lowercase as low,ascii_uppercase as up, punctuation as punc, digits as dig

printable=low+up+dig+punc
host="localhost"
port=8000
BLOCK_LENGTH=128
logging.disable(logging.INFO)

def start():
    global r
    r=remote(host,port)
    r.recvuntil("=> ")

def encrypt(plaintext):
    r.sendline(plaintext)
    result=r.recvline().decode().split(':')[1].strip()
    r.recvuntil("=> ")
    return b64dec(result)


def leak_flag():
    flag=""
    while "}" not in flag:
        for char in printable:
            payload="A"*(BLOCK_LENGTH-len(flag)-1)+flag+char+"A"*(BLOCK_LENGTH-len(flag)-1)
            res=encrypt(payload)
            blocks = [res[i:i+BLOCK_LENGTH] for i in range(0,len(res),BLOCK_LENGTH)]
            if blocks[0]==blocks[1]:
                flag+=char
                print("The flag is : {}".format(flag))


if __name__=="__main__":
    start()
    leak_flag()