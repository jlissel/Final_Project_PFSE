from structural_members import glulam_beams
from handcalcs.decorator import handcalc

CalcGlulamBeam = glulam_beams.GlulamBeam
calc_renderer = handcalc()

CalcGlulamBeam.factored_bending_capacity = calc_renderer(glulam_beams.GlulamBeam.factored_bending_capacity)


def bending_capacity_vs_depth(
    min_depth: int, 
    max_depth: int,
    interval: int,
    L: int,
    b: int,
    d: int,
    fb: int,
    kD: int,
    kH: int,
    ksb: int,
    kT: int,
    kx: int,
    kL: int,
    
) -> dict[str, tuple[list[float], list[float]]]:
    x_values, y_values = beam_mr_over_depth_range(
        min_depth,
        max_depth,
        interval,
        L,
        b,
        d,
        fb,
        kD,
        kH,
        ksb,
        kT,
        kx,
        kL,
    )
    return {
        "Glulam Beam": (x_values, y_values),
    }

def beam_mr_over_depth_range(
        min_depth: int, 
        max_depth: int,
        interval: int,
        L: float,
        b: float, 
        d: float,
        fb=30.6,
        kD=1.0,
        kH=1.0,
        ksb=1.0,
        kT=1.0,
        kx=1.0,
        kL=1.0,

) -> tuple[list[float], list[float], str]:
    x_values = list(range(min_depth, max_depth, interval))
    test_beam = CalcGlulamBeam(
        L=L,
        b=b,
        d=min_depth,
        fb=fb,
        kD=kD,
        kH=kH,
        ksb=ksb,
        kT=kT,
        kx=kx,
        kL=kL,
    )
    y_values = []
    for x_value in x_values:
        test_beam.d = x_value
        mr = test_beam.factored_bending_capacity()
        y_values.append(mr)

    return x_values, y_values


hc_renderer = handcalc(override='long')

calc_bending_capacity = hc_renderer(glulam_beams.factored_bending_capacity)

def calc_mr_at_given_depth(L: float, b: float,d: float,fb: float, kD = 1.0, kH = 1.0, ksb = 1.0, kT = 1.0, kx = 1.0, kL = 1.0, phi=0.9):

    factored_latex, factored_load = calc_bending_capacity(
        L,
        b,
        d,
        fb,
        kD,
        kH,
        ksb,
        kT,
        kx,
        kL,
        phi
        )
    return [factored_latex], factored_load
