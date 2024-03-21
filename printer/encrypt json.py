from cryptography.hazmat.primitives import serialization, hashes # Thêm 'hashes' vào danh sách các module được import

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

# Khởi tạo cặp khóa RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Đọc nội dung từ file
with open('encoded_dict.json', 'rb') as f:
    data = f.read()

# Mã hóa nội dung bằng khóa công khai
cipher_text = public_key.encrypt(
    data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()), # Sửa thành 'hashes.SHA256()'
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Ghi nội dung đã mã hóa vào file mới
with open('encoded_dict_encrypted.bin', 'wb') as f:
    f.write(cipher_text)
