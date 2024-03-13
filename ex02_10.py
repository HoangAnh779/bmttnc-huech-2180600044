def dao_nguoc_chuoi (chuoi):
    return chuoi[::-1]
input_string = input("Mời Nhập Chuổi Cần Đảo Ngược: ")
print("Chuỗi Đảo Ngược Là:",dao_nguoc_chuoi(input_string))