#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import os
import base64
  
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]
 
key = os.urandom(16) # the length can be (16, 24, 32)
text ="python撖???????
text2="well,this is what i want to show!"
 cipher = AES.new(key)
 encrypted = cipher.encrypt(pad(text))
 print encrypted
 print "next"
 encrypted2 = cipher.encrypt(pad(text2))
 print encrypted2
 decrypted = unpad(cipher.decrypt(encrypted))
 print decrypted  # will be 'to be encrypted'
 decrypted2 = unpad(cipher.decrypt(encrypted2))
 print decrypted2
