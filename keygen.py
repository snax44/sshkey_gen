#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author : snax44
Date   :
Desc   :
'''

import tkinter

def main():

  top = tkinter.Tk()
  top.title("SSH Key generator")
  top.geometry("840x600")

  KEY_SIZE = tkinter.IntVar()

  def make_key_pair():
    from Crypto.PublicKey import RSA
    key = RSA.generate(KEY_SIZE.get())
    private_key = key.export_key('PEM')
    public_key = key.publickey().export_key('OpenSSH')

    text_pub = tkinter.Text(top, height=10, width=85)
    text_priv = tkinter.Text(top, height=15, width=85)

    text_pub.insert(tkinter.END, public_key)
    text_priv.insert(tkinter.END, private_key)
    text_pub.place(x=120, y=1)
    text_priv.place(x=120, y=210)

  radio1 = tkinter.Radiobutton(top, text="1024 bits", variable=KEY_SIZE, value=1024)
  radio1.place(x=25, y=100)
  radio2 = tkinter.Radiobutton(top, text="2048 bits", variable=KEY_SIZE, value=2048)
  radio2.place(x=25, y=120)
  radio3 = tkinter.Radiobutton(top, text="4096 bits", variable=KEY_SIZE, value=4096)
  radio3.select()
  radio3.place(x=25, y=140)

  button_generate = tkinter.Button(top, text="Generate", command=make_key_pair)
  button_generate.place(x=25, y=25)

  button_quit = tkinter.Button(top, text="Quit", command=top.destroy)
  button_quit.place(x=25, y=60)

  top.mainloop()

if __name__ == '__main__':
    main()
