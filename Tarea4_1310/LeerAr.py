import pandas as np
from datetime import datetime

df = np.read_csv('junio.dat', sep=',')
now = datetime.now()
horae = 276.5
#print(df)
for j in range(len(df)):
    prestacion = (now.year-df[' Año de ingreso'][j]) *.03
    sueldo = df[' Sueldo base'][j] + (horae * df[' Horas extra'][j]) + (df[' Sueldo base'][j]*prestacion)
    print(df[' Nombres'][j]+": Sueldo base: " + str(df[' Sueldo base'][j]) +", Año de ingreso: " + str(df[' Año de ingreso'][j])
     + ", Horas extra: " + str(df[' Horas extra'][j]) + ", Prestacion: " + str(prestacion))
    print("Sueldo final: " + str(sueldo))

max = max(df[' Año de ingreso'])
min = min(df[' Año de ingreso'])
for j in range(len(df)):
    if df[' Año de ingreso'][j] == max:
        print("Empleado con menor antiguedad: " + df[' Nombres'][j])
    else:
        if df[' Año de ingreso'][j] == min:
            print("Empleado con mayor antiguedad: " + df[' Nombres'][j])
