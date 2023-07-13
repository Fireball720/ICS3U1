

# Letter A
letter_a = [
    "     L     ",
    "    L L    ",
    "   L   L   ",
    "  L L L L  ",
    " L       L "
]


# Letter B
letter_b = [
    "L L L L    ",
    "L      L   ",
    "L L L L    ",
    "L      L   ",
    "L L L L    "
]


# Letter C
letter_c = [
    " L L L  ",
    "L       ",
    "L       ",
    "L       ",
    " L L L  "
]


# Letter D
letter_d = [
    "L L L    ",
    "L     L  ",
    "L     L  ",
    "L     L  ",
    "L L L    "
]


# Letter E
letter_e = [
    "L L L L L",
    "L        ",
    "L L L L  ",
    "L        ",
    "L L L L L"
]


# Letter F
letter_f = [
    "L L L L L",
    "L        ",
    "L L L L  ",
    "L        ",
    "L        "
]


# Letter G
letter_g = [
    " L L L L  ",
    "L         ",
    "L     L L ",
    "L       L ",
    " L L L L  "
]


# Letter H
letter_h = [
    "L       L",
    "L       L",
    "L L L L L",
    "L       L",
    "L       L"
]


# Letter I
letter_i = [
    "  L L L  ",
    "    L    ",
    "    L    ",
    "    L    ",
    "  L L L  "
]


# Letter J
letter_j = [
    "       L ",
    "       L ",
    "       L ",
    "L      L ",
    " L L L   "
]


# Letter K
letter_k = [
    "L     L  ",
    "L   L    ",
    "L L      ",
    "L   L    ",
    "L     L  "
]


# Letter L
letter_l = [
    "L        ",
    "L        ",
    "L        ",
    "L        ",
    "L L L L  "
]


# Letter M
letter_m = [
    "L       L ",
    "LL     LL ",
    "L L   L L ",
    "L   L   L ",
    "L       L "
]


# Letter N
letter_n = [
    "LL      L",
    "L L     L",
    "L   L   L",
    "L     L L",
    "L      LL"
]


# Letter O
letter_o = [
    "  L L L  ",
    " L     L ",
    " L     L ",
    " L     L ",
    "  L L L  "
]


# Letter P
letter_p = [
    "L L L L  ",
    "L      L ",
    "L L L L  ",
    "L        ",
    "L        "
]

# Letter Q
letter_q = [
    " L L L   ",
    "L     L  ",
    "L     L  ",
    "L   L L  ",
    " L L  L  "
]


# Letter R
letter_r = [
    "L L L L  ",
    "L      L ",
    "L L L L  ",
    "L   L    ",
    "L     L  "
]


# Letter S
letter_s = [
    "  L L L L",
    "L        ",
    "  L L L  ",
    "        L",
    "L L L L  "
]


# Letter T
letter_t = [
    "L L L L L",
    "    L    ",
    "    L    ",
    "    L    ",
    "    L    "
]


# Letter U
letter_u = [
    "L      L ",
    "L      L ",
    "L      L ",
    "L      L ",
    " L L L   "
]


# Letter V
letter_v = [
    "L      L ",
    "L      L ",
    "L      L ",
    " L    L  ",
    "   LL    "
]


# Letter W
letter_w = [
    "L       L",
    "L       L",
    "L   L   L",
    "L L   L L",
    "L       L"
]


# Letter X
letter_x = [
    "L       L",
    "  L   L  ",
    "    L    ",
    "  L   L  ",
    "L       L"
]


# Letter Y
letter_y = [
    " L     L ",
    " L     L ",
    "  L   L  ",
    "    L    ",
    "    L    "
]


# Letter Z
letter_z = [
    "L L L L L",
    "      L  ",
    "    L    ",
    "  L      ",
    "L L L L L"
]

# Letter  
letter_  = [
    "     ",
    "     ",
    "     ",
    "     ",
    "     "
]



def lillie(word):
    row0 = []
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    print('```')
    for i in range(5):
        for letter in word.lower():
            command = f"row{i}.append(letter_{letter}[i])"
            eval(command)

    print('  '.join(row0))
    print('  '.join(row1))
    print('  '.join(row2))
    print('  '.join(row3))
    print('  '.join(row4))
    print('```')

def loballs(word):
    print('```')
    for letter in word.lower():
        command = f"letter_{letter}"
        letter = eval(command)
        print('\n'.join(letter))
        print('\n')
    print('```')


while True:
    lillie(input("Word: "))
    loballs(input("Word: "))








    

