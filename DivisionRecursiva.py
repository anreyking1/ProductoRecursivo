p,q=1,0
Dividendo=int(input("Ingresa Dividendo\n"))
Divisor=int(input("Ingresa Divisor\n"))
if(Dividendo>=Divisor):
 while((Dividendo-Divisor)>=q):
  q=Divisor*p
  p=p+1
 print("El cociente es "+str(p-1)+" y el residuo es "+str((Dividendo-q)))
else:
 print("el denominador debe ser menor")
