from ecdsa import ellipticcurve, numbertheory
p  = 115792089237316195423570985008687907853269984665640564039457584007908834671663
a  = 0
b  = 7
n  = 115792089237316195423570985008687907852837564279074904382605163141518161494337

Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424

curve = ellipticcurve.CurveFp(p, a, b)
G = ellipticcurve.Point(curve, Gx, Gy, n)

# Private key and public key
d = 4190296
Q = d * G 

print("Public Key Q:")
print("Q_x =", Q.x())
print("Q_y =", Q.y())
print("\n")


# Signature and message hash
r = 79323126093046758369655349332114091945595435009598470048408441702460186837515
s = 50526178812893965485550567808618939342736854432409702676949606701162832321694
h = 141526133049835145792487473113728803181285321912

print("Signature:")
print("r =", r)
print("s =", s)
print("Message hash h =", h)
print("\n")


# Step 1: Compute w = s^-1 mod n
w = numbertheory.inverse_mod(s, n)
print("Step 1: Modular inverse of s")
print("w = s^-1 mod n =", w)
print("\n")


# Step 2: Compute u1 and u2
u1 = (h * w) % n
u2 = (r * w) % n
print("Step 2: Compute u1 and u2")
print("u1 = (h * w) mod n =", u1)
print("u2 = (r * w) mod n =", u2)
print("\n")


# Step 3: Compute X = u1*G + u2*Q
X1 = u1 * G
X2 = u2 * Q
X = X1 + X2
print("Step 3: Compute X = u1*G + u2*Q")
print("X1 = u1*G = (", X1.x(), ",", X1.y(), ")")
print("X2 = u2*Q = (", X2.x(), ",", X2.y(), ")")
print("X = X1 + X2 = (", X.x(), ",", X.y(), ")")
print("\n")


# Step 4: Verify signature
print("Step 4: Verify if r ≡ X.x mod n")
if r % n == X.x() % n:
    print("Signature is valid!")
else:
    print("Signature is invalid!")