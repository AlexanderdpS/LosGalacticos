numer1=int(input("Ingrese primer numero: "))
numer2=int(input("Ingrese segundo numero: "))

suma=numer1+numer2
resta=numer1-numer2
multiplicacion=numer1*numer2

if numer2>0:
    division=numer1/numer2
    print(f"La division: {division}")
else:
    print("Vuelva a poner el numero no se puede imprimir division")

print(f"La suma es: {suma}")
print(f"La resta es:{resta}" )
print(f"La multiplicacion: {multiplicacion}" )

