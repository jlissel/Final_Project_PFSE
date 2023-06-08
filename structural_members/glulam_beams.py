from dataclasses import dataclass

@dataclass
class GlulamBeam:
    L: float
    b: float
    d: float
    fb: float
    kD: float 
    kH: float 
    ksb: float 
    kT: float 
    kx: float
    kL: float
    kzbg: float
    t: float
    xt: float
    phi: float = 0.9
    Bn: float = 0.7

    
    def factored_bending_capacity(self) -> float:
        return factored_bending_capacity(
            self.L, self.b, self.d, self.fb, self.kD, self.kH, self.ksb, self.kT, self.kx, self.kL, self.kzbg
        )
    def factored_bending_capacity_fire(self) -> float:
        return factored_bending_capacity_fire(
            self.L, self.b, self.d, self.fb, self.kD, self.kH, self.ksb, self.kT, self.kx, self.kL, self.kzbg, self.t, self.xt
        )
    


### Functions

def factored_bending_capacity(L: float, b: float, d: float, fb: float, kD: float, kH: float, ksb: float, kT: float, kx: float, kL: float, kzbg: float, phi=0.9) -> float:
    F_b = fb*kD*kH*ksb*kT
    S = b*d**2/6
    Mr_1 = phi*F_b*S*kx*kzbg
    Mr_2 = phi*F_b*S*kx*kL
    Mr_in_N = min(Mr_1, Mr_2)
    Mr_in_kN = Mr_in_N/1000000
    return Mr_in_kN

def factored_bending_capacity_fire(L: float, b: float, d: float, fb: float, kD: float, kH: float, ksb: float, kT: float, kx: float, kL: float, kzbg: float, t: float, xt: float, phi=0.9) -> float:
    F_b = fb*kD*kH*ksb*kT
    Bn = 0.7
    x = Bn*t + xt
    b_fire = b-2*x
    d_fire = d-x
    S_fire = b_fire*d_fire**2/6
    Mr_1 = phi*F_b*S_fire*kx*kzbg
    Mr_2 = phi*F_b*S_fire*kx*kL
    Mr_in_N_fire = min(Mr_1, Mr_2)
    Mr_in_kN_fire = Mr_in_N_fire/1000000
    return Mr_in_kN_fire


