import re


def cipher_decryption(cipher: str):
    """
    暗号を解読するメソッド
    :param cipher:
    :return:
    """
    int_split_cipher_lis = re.split("[a-z]", cipher)
    initial_split_cipher_lis = re.findall("[a-z]", cipher)
    split_cipher_lis = [initial_split_cipher + int_split_cipher for initial_split_cipher, int_split_cipher in
                        zip(initial_split_cipher_lis, int_split_cipher_lis[1:])]

    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

    calc_chars_nums_dic = {i: num for num, i in enumerate(chars)}

    chars_decryption_lis = []

    for n, split_cipher in enumerate(split_cipher_lis):

        give_num_to_chr = calc_chars_nums_dic[split_cipher[0]]

        calc_raw_value = int("".join(split_cipher[1:]))
        calc_value = calc_raw_value if calc_raw_value < 26 else calc_raw_value % 26

        if calc_value % 2 == 0:
            chars_num = give_num_to_chr + calc_value
        else:
            chars_num = give_num_to_chr - calc_value

        chars_decryption = chars[chars_num] if chars_num < 26 else chars[chars_num % 26]
        chars_decryption_lis.append(chars_decryption)

    return "".join(chars_decryption_lis)


if __name__ == '__main__':
    sample_0 = "a0b1d3f5"  # aaaa
    sample_1 = "a0y2d3w4"  # aaaa
    sample_2 = "d4543i12q77n65c16d4f49a61w76"  # kurashiru
    sample_3 = "w526373x522568s87766h305218c894703"  # trill
    cipher = "d4543i12q77n65c16d4f49a61w76w526373x522568s87766h305218c894703"
    print(cipher_decryption(cipher))
