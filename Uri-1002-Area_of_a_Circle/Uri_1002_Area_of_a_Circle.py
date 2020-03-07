def circle(R):
    pi = 3.14159
    A = pi*(R**2)
    return A

inR = float(input())
A = circle(round(inR,2))
print(f"A={A:.4f}\n")