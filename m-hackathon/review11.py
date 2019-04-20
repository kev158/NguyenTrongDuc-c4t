dangnhap = input("tên đăng nhập:")
while True:
    matkhau = input("Nhập mật khẩu:")
    matkhau2 = input("Nhập lại mật khẩu:")
    if matkhau2 != matkhau:
        print("không khớp mật khẩu!")
    elif matkhau2 == matkhau:
        
        break
