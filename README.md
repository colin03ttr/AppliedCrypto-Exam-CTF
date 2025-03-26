# Exam OCC3 - CTF
Colin TANTER 

To access the ctf, we run this command in WSL :
```
nc 34.155.90.0 1337
```

**1. Give an input for `username` so that the server accepts:**
---

From the source code, we see the first step is to enter the right `username`. The code explicitly says :
```python
if username.split("\n")[0] == "OCC3 students":
    # returns the encrypted message
```
So we know we have to input `OCC3 students` when asked for the username to get the encrypted message.

**2. Give two different inputs for `username` so that the server accepts both?**
---

The code splits the differents lines of the input and takes only the first line to check the username, so we can also enter more than one line and the server still accepts it as long as the first line is `OCC3 students`.
2 valid inputs :
```
OCC3 students
```
```
OCC3 students
fkgbsldfg
```

**3. How many blocks are there in the ciphertext?**
---

here is the answer from the server :
```
----------------------------------------------------------------
Here is you encrypted message:

8ec2bbbc72f87e8643ba18365351b40f10ac8e79e6247c816c6d20db95999a41887cef899569792101db7a28cbb80938b279d3e4c14829651d7fcffe4033a8aab6696963b212865a7710cd70281dcf139a5e45be79c4b36d98b5c19639049949
```
The code says in the beginning that the key in 16 bytes long, and after the plaintext message is padded to match a multiple of 16. So we know the block length is 16 bytes.

Then, for the output, it is displayed in hexadecimal characters, each byte is represented with 2 chars to make it a hex character. 

So, knowing the output length is 192 characters, we divide by 2 to get the number of bytes of the output :
$$ 192 / 2 = 96 \text{ bytes}$$

And to get the number of blocks, we divide by 16 :
$$ 96 / 16 = 6 \text{ blocks}$$

**4. Give a visualization of the plaintext based on answers from question 1 and question 3.**
---

We know the plaintext message is made of the `username` then a **known text** and then the `FLAG` :
```python
message = f"{username}, here is your secret flag for today exam: {FLAG}"
```
The valid username is `OCC3 students`, and we don't know the flag yet so it should look like this (each line is a block):

```
|OCC3 students, h| 
|ere is your secr|
|et flag for toda|  
|y exam: FLAGFLAG|    
|FLAGFLAGFLAGFLAG|
```
The flag is 24 bytes long so it doesnt need padding as you see above.

