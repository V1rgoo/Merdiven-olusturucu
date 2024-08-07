i=1
a=input("kaç basamaklı merdiven istersiniz?")
b=a
while int(i)<=int(a):
  print((" "*int(b)),("X"*int(i)))
  i=i+1
  b=int(b)-1
