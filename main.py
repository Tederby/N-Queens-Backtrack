import time
import os

"""
Nama: Muhammad Afiffatin Hariz
NIM: 21120124130073

"""

# Fungsi untuk membersihkan layar terminal
def clear_screen():
    # "cls" untuk Windows, "clear" untuk Unix/Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk mencetak papan catur dengan status saat ini
def print_board(board, step, action):
    clear_screen()
    print(f"--- Langkah {step} ---")
    print(f"Status: {action}\n")
    for row in board:
        print("  " + " ".join(row))
    print("\n" + "="*30)
    time.sleep(0.6) # Kecepatan animasi, bisa disesuaikan

# Fungsi untuk memeriksa apakah aman menempatkan ratu di posisi (row, col)
def is_safe(board, row, col, N):
    # Cek baris di sebelah kiri
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Cek diagonal atas kiri
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Cek diagonal bawah kiri
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

# Fungsi utama untuk menyelesaikan masalah N-Queens menggunakan backtracking
def solve_n_queens_util(board, col, N, step_counter):
    if col >= N:
        return True

    for i in range(N):
        step_counter[0] += 1
        # Tandai posisi yang sedang dievaluasi dengan '?'
        board[i][col] = '?'
        print_board(board, step_counter[0], f"Mencoba evaluasi baris {i}, kolom {col}...")
        
        if is_safe(board, i, col, N):
            # Jika aman, tempatkan ratu di posisi ini
            board[i][col] = 'Q'
            step_counter[0] += 1
            print_board(board, step_counter[0], f"Aman! Ratu ditaruh di ({i}, {col})")

            # Rekursi ke kolom berikutnya
            if solve_n_queens_util(board, col + 1, N, step_counter):
                return True

            # Jika gagal, tarik mundur (backtrack)
            board[i][col] = 'x' # Penanda bahwa posisi ini sudah dicoba tapi gagal
            step_counter[0] += 1
            print_board(board, step_counter[0], f"Buntu! BACKTRACK dari ({i}, {col})")
            board[i][col] = '.' # Dikosongkan lagi untuk mencoba posisi lain
        else:
            # Gagal, langsung tandai dengan 'x' untuk visualisasi bahwa posisi ini tidak aman
            board[i][col] = '.'
            step_counter[0] += 1
            print_board(board, step_counter[0], f"Tabrakan! taruh di ({i}, {col})")

    return False

# Fungsi untuk memulai proses penyelesaian N-Queens
def solve_n_queens():
    # Ukuran papan catur (N x N)
    N = 4
    board = [['.' for _ in range(N)] for _ in range(N)]
    step_counter = [0]
    
    clear_screen()
    print("Menyiapkan Papan Catur...")
    time.sleep(1)
    
    if not solve_n_queens_util(board, 0, N, step_counter):
        print("\nSolusi nggak ketemu.")
        return False

    clear_screen()
    print("\n=========================")
    print(" SOLUSI DITEMUKAN! ")
    print(f"Total langkah evaluasi: {step_counter[0]}")
    print("=========================\n")
    for row in board:
        print("  " + " ".join(row))
    print("\n=========================")
    return True

# Jalankan program
if __name__ == "__main__":
    solve_n_queens()