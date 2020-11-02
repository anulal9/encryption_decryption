
def calculate_C0(K):

    arr = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36]
    c0 = []
    for a in arr:
        c0.append(K[a - 1])

    c0 = ''.join(c0)
    return c0

def calculate_D0(K):
    arr = [63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    d0 = []
    for a in arr:
        d0.append(K[a - 1])

    d0 = ''.join(d0)
    return d0


def get_vi(i):
    shift_1 = {1, 2, 9, 16}

    if i in shift_1:
        return 1
    else:
        return 2


def calculate_streami(Cprev, Dprev, i):

    vi = get_vi(i)

    ci = shift_stream(Cprev, vi)
    di = shift_stream(Dprev, vi)

    return ci, di


def shift_stream(stream, vi):

    final_stream = []
    for a in range(vi, len(stream)):
        final_stream.append(stream[a])

    for a in range(0, vi):
        final_stream.append(stream[a])

    return ''.join(final_stream)


def calculate_Ki(Ci, Di):
    arr = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20,
           13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

    combined_stream = Ci + Di
    ki = []
    for a in arr:
        ki.append(combined_stream[a - 1])

    return ''.join(ki)


def convert_K_to_binary(K):
    scale = 16

    converted_k = bin(int(K, scale)).zfill(65)
    str_k = str(converted_k)
    str_k = str_k.replace('b', '')
    return str_k


def permute_x(arr, x):
    y = []
    for a in arr:
        y.append(x[a - 1])

    y = ''.join(y)

    return y

def initial_p(x):
    arr = [58 ,50 ,42 ,34 ,26 ,18 ,10 ,2,
           60 ,52 ,44 ,36 ,28 ,20, 12, 4,
           62 ,54 ,46 ,38 ,30 ,22 ,14, 6,
           64 ,56 ,48 ,40 ,32 ,24 ,16, 8,
           57 ,49 ,41 ,33 ,25 ,17 ,9 ,1,
           59 ,51 ,43 ,35 ,27 ,19 ,11 ,3,
           61 ,53 ,45 ,37 ,29 ,21 ,13 ,5,
           63 ,55 ,47 ,39 ,31 ,23 ,15 ,7]

    return permute_x(arr, x)

def convert_r0(x):
    arr = [32, 1, 2, 3, 4, 5,
           4, 5, 6, 7, 8, 9,
           8, 9, 10, 11 ,12, 13,
           12, 13, 14, 15 ,16, 17,
           16 ,17 ,18 ,19 ,20 ,21,
           20, 21 ,22 ,23 ,24 ,25,
           24, 25 ,26, 27 ,28 ,29,
           28, 29, 30 ,31 ,32 ,1]

    return permute_x(arr, x)

def add_bits(x, y):

    output = []

    for i in range(0, len(x)):
        a = int(x[i])
        b = int(y[i])
        result = (a + b) % 2
        output.append(str(result))

    output = ''.join(output)
    return output

def break_into_groups(output):

    output_list = []
    inner_list = []

    for i in range(0, 48):
        if i % 6 == 0 and i != 0:
            output_list.append(inner_list)
            inner_list = [output[i]]
        else:
            inner_list.append(output[i])

    output_list.append(inner_list)
    return output_list

def convert_to_4_bits(group, s_box):
    b1 = group[0]
    b6 = group[5]
    b1_b6 = b1 + b6
    row = int(b1_b6, 2)
    b2_b5 = group[1:5]
    b2_b5 = ''.join(b2_b5)
    col = int(b2_b5, 2)
    value = s_box[row][col]
    binary_value = str(bin(value).zfill(5))
    binary_value = binary_value.replace('b', '')
    return binary_value

def convert_groups_to_4_bit_groups(group_lists):
    s_box_lists = [
        [
            [14, 4, 13, 12, 15, 11, 8, 3 ,10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15,12, 9, 7,3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10,0, 6, 13]
        ],
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],
        [
            [2, 12,4,1,7,10,11,6,8,5,3,15,13,0,14,9 ],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
        ],
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
    ]

    results = []
    for i, group in enumerate(group_lists):
        four_bit_result = convert_to_4_bits(group, s_box_lists[i])
        if len(four_bit_result) == 5:
            four_bit_result = four_bit_result[1:]
        results.append(four_bit_result)

    return results

def add_p(s_box_result):
    arr = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    return permute_x(arr, s_box_result)

def get_keys(k):

    bin_k = convert_K_to_binary(k)
    c0 = calculate_C0(bin_k)
    # print(c0)
    d0 = calculate_D0(bin_k)

    keys = []
    cprev = c0
    dprev = d0
    for i in range(1, 16):
        ci, di = calculate_streami(cprev, dprev, i)
        ki = calculate_Ki(ci, di)
        keys.append(ki)
        cprev = ci
        dprev = di

    return keys


def encrypt(x, keys):
    bin_x = convert_K_to_binary(x)
    l0_r0 = initial_p(bin_x)
    l0 = l0_r0[:32]
    r0 = l0_r0[32:]

    lprev = l0
    rprev = r0
    for key in keys:
        li = rprev
        converted_rprev = convert_r0(rprev)
        output = add_bits(converted_rprev, key)
        group_lists = break_into_groups(output)
        four_bit_groups = convert_groups_to_4_bit_groups(group_lists)
        s_box_result = ''.join(four_bit_groups)
        permuted_sbox_result = add_p(s_box_result)
        ri = add_bits(str(permuted_sbox_result), str(lprev))
        rprev = ri
        lprev = li

    return lprev, rprev


def invert_encryption(l_final, r_final):
    r_l_final = r_final + l_final
    inverse_permutation = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]

    return permute_x(inverse_permutation, r_l_final)



if __name__ == '__main__':

    #k = '1122334455667788'
    k = '133457799BBCDFF1'

    keys = get_keys(k)
    l_final, r_final = encrypt('0123456789ABCDEF', keys)
    print(l_final, r_final)
    print(invert_encryption(l_final, r_final)

    '''
    l1 = R0
    r1 = lo + f(r0, k1)
    f(r0, k1) 
        - r0 -> 48 bits with permuatation E
        - converted_r0 + k1 = result
        - break result into 8 groups of 6 bits
        - for each group:
            use sbox to go from 6 bits -> 4 bits
        - append results of sboxes to get 32 bits
        - use permutation p to permute bits
        - add this result to l0 
    '''


