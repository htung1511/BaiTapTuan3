if __name__ == "__main__":
    S = [6, 1, 8, 5, 9, 0, 2, 3, 7, 4]  
    plaintext = "cybersecurity"
    i = 0
    j = 0
    keystream = []
    ciphertext_ascii = []
    
    print("--- QUA TRINH TAO KHOA VA MA HOA RC4 (MOD 10) ---")
    
    for char in plaintext:
        i = (i + 1) % 10
        j = (j + S[i]) % 10
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 10
        k = S[t]
        keystream.append(k)
        m_val = ord(char)     
        c_val = m_val ^ k    
        ciphertext_ascii.append(c_val)
        print(f"Ký tự '{char}' (ASCII: {m_val:3}) XOR Khoá k: {k} = Ciphertext: {c_val:3}")
        
    print("-" * 50)
    print("=> Ban ro (Plaintext):    ", plaintext)
    print("=> Dong khoa (Keystream): ", keystream)
    print("=> Ban ma (Ciphertext):   ", ciphertext_ascii)