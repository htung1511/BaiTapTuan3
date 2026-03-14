def degree(poly):
    return poly.bit_length() - 1 if poly > 0 else -1

def poly_div(a, b):
    q = 0
    r = a
    deg_b = degree(b)
    while degree(r) >= deg_b:
        shift = degree(r) - deg_b
        q ^= (1 << shift)  
        r ^= (b << shift)
    return q, r

def poly_mul(a, b):
    p = 0
    while b > 0:
        if b & 1:
            p ^= a
        a <<= 1
        b >>= 1
    return p

def ext_euclid_gf2(m, a):
    r1, r2 = m, a
    t1, t2 = 0, 1
    
    print(f"{'r1':>6} | {'r2':>6} | {'q':>6} | {'r (Du)':>8} | {'t1':>6} | {'t2':>6} | {'t (Nhan)':>8}")
    print("-" * 70)
    
    while r2 > 0:
        q, r = poly_div(r1, r2)
        t = t1 ^ poly_mul(q, t2) 
        
        print(f"{r1:>6} | {r2:>6} | {q:>6} | {r:>8} | {t1:>6} | {t2:>6} | {t:>8}")
        
        r1, r2 = r2, r
        t1, t2 = t2, t
        
    print(f"{r1:>6} | {r2:>6} | {'-':>6} | {'-':>8} | {t1:>6} | {t2:>6} | {'-':>8}")
    return t1

if __name__ == "__main__":
    m_poly = 0b10000001001 
    
    a = 523
    b = 1015
    
    print("========== TIM NGHICH DAO CUA A = 523 ==========")
    inv_a = ext_euclid_gf2(m_poly, a)
    print(f"\n=> KET LUAN: Nghich dao nhan cua a = {a} la: {inv_a}\n")
    
    print("========== TIM NGHICH DAO CUA B = 1015 =========")
    inv_b = ext_euclid_gf2(m_poly, b)
    print(f"\n=> KET LUAN: Nghich dao nhan cua b = {b} la: {inv_b}\n")