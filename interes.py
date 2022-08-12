capital = float(input("Capital inicial: "))
interes = float(input("Interes anual: "))
años = int(input("Cantidad de años: "))
 
x = capital+ (capital * (interes/100) * años)
 
print(("El capita total al cabo de", años, "sera de años",x))