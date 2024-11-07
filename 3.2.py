from Crypto.Util.number import getPrime
from sympy import mod_inverse  # 从 sympy 导入 mod_inverse


class RSA:
    def __init__(self, key_len: int = 100):
        # 密钥生成
        while True:
            try:
                # 生成两个随机质数
                p, q = getPrime(key_len), getPrime(key_len)

                # RSA 运算模 n
                n = p * q

                # 计算欧拉函数 φ(n)
                et = (p - 1) * (q - 1)
                e = 3  # 公钥指数

                # 计算私钥 d 使用 mod_inverse 来代替 invmod
                d = mod_inverse(e, et)
                break
            except ValueError:
                continue

        # 密钥保存
        self.n = n
        self.d = d
        self.e = e

    def encrypt(self, m: bytes) -> int:
        # 将消息从字节转为整数并加密
        m = self.bytes_to_num(m)
        c = pow(m, self.e, self.n)
        return c

    def decrypt(self, c: int) -> bytes:
        # 解密并将整数结果转回字节
        m = pow(c, self.d, self.n)
        m = self.num_to_bytes(m)
        return m

    @staticmethod
    def bytes_to_num(seq: bytes) -> int:
        # 将字节序列转为整数
        return int(seq.hex(), 16)

    @staticmethod
    def num_to_bytes(seq: int) -> bytes:
        # 将整数转回字节序列
        hex_rep = hex(seq)[2:]
        hex_rep = '0' * (len(hex_rep) % 2) + hex_rep  # 确保偶数长度
        return bytes.fromhex(hex_rep)


def main():
    rsa_obj = RSA(key_len=1024)
    m = b'RSA implementation'

    # 加密消息
    c = rsa_obj.encrypt(m)
    print(f'{c=}')

    # 解密消息
    m_rec = rsa_obj.decrypt(c)
    print(f'{m_rec=}')


if __name__ == '__main__':
    main()
