def volume(R):
    pi = 3.14159
    return (4.0/3)*pi*R**3

R = float(input())
vol = volume(R)
print("VOLUME = {:.3f}".format(vol))