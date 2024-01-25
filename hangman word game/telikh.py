def printhanger(tries,maxtries):
    if tries==5:
        print(" +-----+ ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("5 tries left")
    elif tries==4:  
        print(" +-----+ ")
        print(" |     0 ")
        print(" |       ")
        print(" |       ")
        print("4 tries left")
    elif tries==3:  
        print(" +-----+ ")
        print(" |     0 ")
        print(" |   --+ ")
        print(" |       ")
        print("3 tries left")
    elif tries==2:   
        print(" +-----+ ")
        print(" |     0 ")
        print(" |   --+-- ")
        print(" |       ")
        print("2 tries left")
    elif tries==1:  
        print(" +-----+ ")
        print(" |     0 ")
        print(" |   --+-- ")
        print(" |    /   ")
        print("1 tries left")
    elif tries==0:  
        print(" +-----+ ")
        print(" |     0 ")
        print(" |   --+-- ")
        print(" |    / \  ")
playagain="yes"
while playagain=="yes":
 type=str(input('Type g<Enter> or G<Enter> if word will be given by another player:'))
 if type=='g' or type=='G':
    k=True
 else:
    k=False
 print(k)
 x=0
 if k==True:
  word=str(input("Player don't look! 2nd player,type in word,must be in English and at least 3 letters long: "))
  l="\n"
  x=int(len(word))
  n=False
  while n==False:
   if x>=3 and x<=20:
    n=True
    z=0
    while z==0:
     if word.__add__(l) in open('words.txt').readlines():
      import os
      os.system('cls')
      z=1
     else:
      print("Wrong word,try again")
      word=input("Player don't look! 2nd player,type in word,must be in English and at least 3 letters long:")
      x=int(len(word))
   else:
    print("Wrong word,try again")
    word=input("Player don't look! 2nd player,type in word,must be in English and at least 3 letters long: ")
    x=int(len(word))
 else:
    #an dwseis <r> tote 8a parei mia tuxaia le3h pou 8 thn diale3ei o upologisths 
    wordran=str(input('Type r<Enter> or R<Enter> for word of random length'))
    if wordran=='r' or wordran=='R':
     import random
     word=random.choice(open('words.txt').readlines())
     length=len(word)
     print(word)
     import os
     os.system('cls')
     print(length)
    #an den dwseis <r> nwritera tote 8a exeis thn eukairia n diale3eis esu to mhkos ths le3hs pou 8eleis
    else:  
     leng=int(input("Give me the length of the word: "))
     while int(leng)<3 or int(leng)>20:
      leng=int(input("Give me the length of the word: "))
     import random
     word=random.choice(open('words.txt').readlines())
     while (len(word)-1)!=leng:
      word=random.choice(open('words.txt').readlines())
     print(word)
    x=len(word)-1
 word=word.lower()
 board=[]
 # h <cl> lista einai mia lista me ta swsta grammata pou uparxoun sthn le3h
 cl=[]
 choosen_letters=[]
 for i in range(x):
    board.append("-")
 y=list(word)
 print(board)
 max_tries=5
 tries=max_tries
 while len(cl) != x and tries!=-1:
  printhanger(tries,max_tries)
  print(tries,"tries left")
  print("chosen letters: " ,choosen_letters)
  if tries!=0:
   whatplayersaid=input("Give me a letter: ")
   if whatplayersaid.upper() in board:
    print("You've already said this letter")
   elif whatplayersaid in word:
    for i in range(len(word)):
     if whatplayersaid==word[i]:
      board[i]=whatplayersaid.upper()
      cl.append(whatplayersaid)
    choosen_letters.append(whatplayersaid)
    print(board)
   else:
    if whatplayersaid not in choosen_letters:
     tries=tries-1
     choosen_letters.append(whatplayersaid)
    else:
     print("You've already said this letter")
  else:
   tries-=1   
 if tries>-1:
    print("Congratulations! You've found word",word,"!")
 else:
    print("Sorry! You lost! The word was",word)
 playagain=input("Do you want to play again? ")
