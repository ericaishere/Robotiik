# [SOAL NOMOR 1] Buatlah program Python yang mengambil daftar angka dari pengguna dan menampilkan jumlah kuadrat dari angka genap dalam daftar. 
# Namun, program juga harus mengeluarkan pesan kesalahan dan meminta pengguna untuk mencoba lagi jika mereka memasukkan nilai non-numerik. 
# Untuk menghentikan program meminta input bisa diberi input "0".

sum_of_squares = 0

while True:
    user_input = input("Enter a number: ")
    
    if user_input == '0':
        break
        
    try:
        number = int(user_input)
        
        if number % 2 == 0:
            sum_of_squares += number ** 2
            
    except ValueError:
        print("'"+user_input+"'"+"is not a valid number. Please try again.")
        
print("The sum of the squares of the even numbers is:", sum_of_squares)


