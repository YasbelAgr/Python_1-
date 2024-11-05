 
renta_anual=0

renta_anual=float (input("ingrse su renta anual "))

if renta_anual <= 1000:
    input("le corresponde pagar el 5% de impositivo por la renta")
elif renta_anual >= 1001 and renta_anual <= 2000:
    input("le corresponde pagar el 10% de impositivo de la renta")
elif renta_anual >= 2001 and renta_anual <= 3500:
    input("le corresponde pagar el 20% de impositivo de la renta")
elif renta_anual >= 3501 and renta_anual <= 6000:
    input("le corresponde pagar el 30% de impositivo de la renta")
else:
    input("le corresponde pagar el 40% de impositivo de la renta")
