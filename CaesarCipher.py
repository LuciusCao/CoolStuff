class CaesarCipher:
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.__index_to_alpha, self.__alpha_to_index = self.__make_dict(self.alphabet)

    def __make_dict(self, alphabet):
        d1 = dict()
        d2 = dict()
        for i in range(len(alphabet)):
            d1[i] = alphabet[i]
        for i in range(len(alphabet)):
            d2[alphabet[i]] = i
        return d1,d2

    def encode(self,message,n):
        target = ''
        for i in range(len(message)):
            idx = self.__alpha_to_index[message[i]]
            shifted_idx = (idx+n)%len(self.alphabet)
            target += self.__index_to_alpha[shifted_idx]
        return target

if __name__ == '__main__':
    caesar_cipher = CaesarCipher()
    print(caesar_cipher.encode('message',4))
