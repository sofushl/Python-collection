def f(x):
  return x**4 - 3*x**3 + 2*x - 1

svar1 = input("Velg verdi for x:")
a = float(svar1)  #Fordi input returnerer en string,
                  # må vi konverte svar1 til flyttall

svar2 = input("Velg verdi for delta x:")
dx = float(svar2)

print("f'(" +svar1 + ") er tilnærmet lik", round((f(a + dx)-f(a - dx))/(2*dx), 6))
# Write your code here :-)
