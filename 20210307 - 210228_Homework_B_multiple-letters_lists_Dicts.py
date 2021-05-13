# "Big Letters", 5 rows per letter, just do Letter "A" for this assignment
# create a function that can be passed a number (1-5 [inclusive you stupid motherfucker])
# function returns the line of text for that row
# call it 5 times, to get each row (and print the string returned)
# probable length of each letter is 5 (including M you dumbass)


# 3/7/21
# modify this to use > 1 letter
# use a dictionary/lists to get the lines for each letter
# make a function:
#
#     def get_line(letter, linenumber):

# Give the function the letter and which of the 5 lines of that number.  It will return the text for the line


import time

A1 = ' AAA   '
A2 = 'A   A  '
A3 = 'AAAAA  '
A4 = A2
A5 = A2
A = [A1,A2,A3,A4,A5]

B1 = 'BBBB   '
B2 = 'B   B  '
B3 = B1
B4 = B2
B5 = B1
B = [B1,B2,B3,B4,B5]

C1 = ' CCC   '
C2 = 'C   C  '
C3 = 'C      '
C4 = C2
C5 = C1
C = [C1,C2,C3,C4,C5]

D1 = 'DDD    '
D2 = 'D  D   '
D3 = 'D   D  '
D4 = D2
D5 = D1
D = [D1,D2,D3,D4,D5]

E1 = 'EEEEE  '
E2 = 'E      '
E3 = 'EEEE   '
E4 = E2
E5 = E1
E = [E1,E2,E3,E4,E5]

F1 = 'FFFFF  '
F2 = 'F      '
F3 = 'FFFF   '
F4 = F2
F5 = F2
F = [F1,F2,F3,F4,F5]

G1 = ' GGGG  '
G2 = 'G      '
G3 = 'G  GG  '
G4 = 'G   G  '
G5 = ' GGGG  '
G = [G1,G2,G3,G4,G5]

H1 = 'H   H  '
H2 = H1
H3 = 'HHHHH  '
H4 = H1
H5 = H1
H = [H1,H2,H3,H4,H5]

I1 = 'IIIII  '
I2 = '  I    '
I3 = I2
I4 = I2
I5 = I1
I = [I1,I2,I3,I4,I5]

J1 = 'JJJJJ  '
J2 = '  J    '
J3 = J2
J4 = 'J J    '
J5 = 'JJJ    '
J = [J1,J2,J3,J4,J5]

K1 = 'K   K  '
K2 = 'K K    '
K3 = 'KK     '
K4 = K2
K5 = K1
K = [K1,K2,K3,K4,K5]

L1 = 'L      '
L2 = L1
L3 = L1
L4 = L1
L5 = 'LLLLL  '
L = [L1,L2,L3,L4,L5]

M1 = 'M   M  '
M2 = 'MM MM  '
M3 = 'M M M  '
M4 = M1
M5 = M1
M = [M1,M2,M3,M4,M5]

N1 = 'N   N  '
N2 = 'NN  N  '
N3 = 'N N N  '
N4 = 'N  NN  '
N5 = N1
N = [N1,N2,N3,N4,N5]

O1 = ' OOO   '
O2 = 'O   O  '
O3 = O2
O4 = O2
O5 = O1
O = [O1,O2,O3,O4,O5]

P1 = 'PPPP   '
P2 = 'P   P  '
P3 = P1
P4 = 'P      '
P5 = P4
P = [P1,P2,P3,P4,P5]

Q1 = ' QQQ   '
Q2 = 'Q   Q  '
Q3 = 'Q Q Q  '
Q4 = 'Q  QQ  '
Q5 = ' QQQQ  '
Q = [Q1,Q2,Q3,Q4,Q5]

R1 = 'RRRR   '
R2 = 'R   R  '
R3 = R1
R4 = 'R  R   '
R5 = R2
R = [R1,R2,R3,R4,R5]

S1 = ' SSSS  '
S2 = 'SS     '
S3 = ' SSS   '
S4 = '   SS  '
S5 = 'SSSS   '
S = [S1,S2,S3,S4,S5]

T1 = 'TTTTT  '
T2 = '  T    '
T3 = T2
T4 = T2
T5 = T2
T = [T1,T2,T3,T4,T5]

U1 = 'U   U  '
U2 = U1
U3 = U1
U4 = U1
U5 = ' UUU   '
U = [U1,U2,U3,U4,U5]

V1 = 'V   V  '
V2 = 'V   V  '
V3 = 'V   V  '
V4 = ' V V   '
V5 = '  V    '
V = [V1,V2,V3,V4,V5]

W1 = 'W   W  '
W2 = W1
W3 = 'W W W  '
W4 = 'WWWWW  '
W5 = W1
W = [W1,W2,W3,W4,W5]

X1 = 'X   X  '
X2 = ' X X   '
X3 = '  X    '
X4 = X2
X5 = X1
X = [X1,X2,X3,X4,X5]

Y1 = 'Y   Y  '
Y2 = 'Y   Y  '
Y3 = ' YYY   '
Y4 = '  Y    '
Y5 = '  Y    '
Y = [Y1,Y2,Y3,Y4,Y5]

Z1 = 'ZZZZZ  '
Z2 = '   Z   '
Z3 = '  Z    '
Z4 = ' Z     '
Z5 = Z1
Z = [Z1,Z2,Z3,Z4,Z5]


Space1 = '   '
Space2 = '   '
Space3 = '   '
Space4 = '   '
Space5 = '   '
Space = [Space1,Space2,Space3,Space4,Space5]

CR1 = '   OOOO     '
CR2 = ' O  CC  O   '
CR3 = 'O  C     O  '
CR4 = CR2
CR5 = CR1
Copyright = [CR1,CR2,CR3,CR4,CR5]

letter_lib = {
    'A' : A,
    'B' : B,
    'C' : C,
    'D' : D,
    'E' : E,
    'F' : F,
    'G' : G,
    'H' : H,
    'I' : I,
    'J' : J,
    'K' : K,
    'L' : L,
    'M' : M,
    'N' : N,
    'O' : O,
    'P' : P,
    'Q' : Q,
    'R' : R,
    'S' : S,
    'T' : T,
    'U' : U,
    'V' : V,
    'W' : W,
    'X' : X,
    'Y' : Y,
    'Z' : Z,
    '@' : Copyright,
    ' ' : Space,
    }
print()
print()


word = str(input('What would you like printed (use only letters and spaces, screenwidth dependent)?  ')).upper()
print()
print()

def grab_letter (letter : str, line : int) -> str:
    letter_line = letter_lib[letter][line]
    return letter_line

def append_letters (statement : str, line: int) -> str:
    text_line = ''
    length = len(statement)

    i = 0
    while i < length:
        text_line += grab_letter(statement[i:i+1],line)
        i += 1
    return text_line

if all(x.isalpha() or x.isspace() for x in word) == 0:
    while all(x.isalpha() or x.isspace() for x in word) == 0:
        time.sleep(2)
        retard = str('Try again').upper()
        follow = str('Follow the instructions').upper()
        question1 = str('What would you like printed?').upper()
        question2 = str('use only letters and spaces').upper()
    
        time.sleep(2)
        print()
        print()
        line = 0
        while line < 5:
            print(append_letters(retard,line))
            line += 1

        time.sleep(2)
        print()
        print()
        line = 0
        while line < 5:
            print(append_letters(follow,line))
            line += 1

        time.sleep(2)
        print()
        print()
        print(question1)
        

        time.sleep(2)
        print()
        print()
        line = 0
        while line < 5:
            print(append_letters(question2,line))
            line += 1
        print()
        print()
        word = str(input()).upper()
        print()
        print()

line = 0
while line < 5:
    print(append_letters(word,line))
    line += 1
print()
print()

time.sleep(2)
FSINC = '@' + str('Teddies Inc').upper()

line = 0
while line < 5:
    print(append_letters(FSINC,line))
    line += 1
print()
print()
print()