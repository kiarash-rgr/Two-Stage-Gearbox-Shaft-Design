# Mechanice Design Element!!!
# Mahak Mehdipour
# Kiarash Rooygar
# Wendsday, Last day of December 2025 :)

import math

S_y = 490
S_E0 = 590 / 2.0
K_A = 0.832
K_C = 1.0
K_E = 0.814

def K_b(d_mm: float) -> float:
    if d_mm <= 2.79:
        d_eff = 2.79
    else:
        d_eff = d_mm

    if 2.79 < d_eff <= 51.0:
        return 1.24 * (d_eff ** (-0.107))
    else:
        return 1.51 * (d_eff ** (-0.157))


def S_e(d_mm: float, S_e0: float = S_E0, k_a: float = K_A, k_c: float = K_C, k_e: float = K_E) -> float:
    base = S_e0 * k_a * k_c * k_e
    return base * K_b(d_mm)


def range(d_start: float = 2.79, d_stop: float = 254.0, step: float = 0.25):
    d = d_start
    rows = []
    while d <= d_stop + 1e-12:
        rows.append((d, K_b(d), S_e(d)))
        d += step
    return rows


n_d = 3
K_f = 2.05
K_fs = 1.85
# T_m = 9.138
# M_a_s = [2.593112, 16.85505, 23.33772, 20.09637]


def diameter(M, T, S_e_vraible):
    d = ((
        ((16 * n_d) / math.pi) * 
        (
        (math.sqrt(3*(K_fs * T)**2)) / S_y +
        (math.sqrt(4*(K_f * M)**2 + 3*(K_fs * T)**2)) / S_e_vraible
        )
    ) ** (1/3)) * 10
    return d


def main(M, T):
    rows = range()
    print("\tMa()\td(mm)\t\tKb\t\tS_e(MPa)\t\t d(mm)__calc")
    Error = 1
    found = False
    d_final_g = float
    d_final = float
    kb_val_final = float
    se_val_final = float
    for d, kb_val, se_val in rows[:1000]:
        d_calc = diameter(M, T, se_val)
        if d - (0.01*d_calc) < d_calc < d + (0.01*d_calc):
            if abs(d - d_calc) < Error:
                Error = abs(d - d_calc) 
                d_final_g = d
                d_final = d_calc
                kb_val_final = kb_val
                se_val_final = se_val
                # M_i_final = i
                found = True
    if found:
        print(f"for {M}:   {d_final_g}\t{kb_val_final}\t{se_val_final}\t", d_final)
        input("\n\nPress Enter to continue...")
        print("\n\n")
        

while True:
    T = float(input("Enter the value of T (Torque in Nm): "))
    M = float(input("Enter the value of M (Bending Moment in Nm): "))
    print()
    main(M, T)

# Hooof :) The End..! 