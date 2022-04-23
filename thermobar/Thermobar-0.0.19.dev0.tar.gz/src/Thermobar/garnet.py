import numpy as np
import matplotlib.pyplot as plt
from functools import partial
import inspect
import warnings as w
import numbers
import pandas as pd
import itertools
from Thermobar.core import *

def T_Ryan1996(gt_comps):

    '''
    Ni-in-garnet thermometer of Ryan et al. (1996)
    :cite:`ryan1996`
    SEE=+-50C
    '''

    temp = (1000.0/(1.506-(0.189*np.log(np.array(gt_comps['Ni_Gt'])))))

    return temp

def T_Sudholz2021(gt_comps):

    '''
    Ni-in-garnet thermometer of Sudholz et al. (2021)
    :cite:`sudholz2021`
    SEE=+-50C
    '''

    xMg, xCa, xFe, xAl, xCr = calculate_fractions_garnet(gt_comps = gt_comps)

    ni_ol = 3e3

    ni_gt_ol = np.array(gt_comps['Ni_Gt']) / ni_ol

    temp = ((-8254.568) / ((xCa*3.023) + (xCr*2.307) + (np.log(ni_gt_ol) - 2.639)))

    return temp

def T_Canil1999(gt_comps):

    '''
    Ni-in-garnet thermometer of Canil (1996)
    :cite:`canil1999`
    SEE=+-50C
    '''

    ni_ol = 3e3

    ni_gt_ol = np.array(gt_comps['Ni_Gt']) / ni_ol

    temp = 8772.0 / (2.53 - (np.log(ni_gt_ol)))

    return temp

def P_Ryan_1996(gt_comps, T_K):

    '''
    Cr-pyrope garnet barometer of Ryan et al. (1996)
    :cite:`ryan1996`
    SEE=+-50C
    '''

    xMg, xCa, xFe, xAl, xCr = calculate_fractions_garnet(gt_comps = gt_comps)

    P_cr = np.zeros(len(T_K))

    Dp_converge = 0.1
    Gasp_1 = 270.0
    Gasp_2 = 4500.0
    Gasp_3 = 15.0
    Cr_veto = 0.1
    R = 1.9872

    T_C = T_K - 273.15

    def xCropx(ca_opx, p_ref, temp):

        cr_opx = 0.0115 * np.exp((0.0033 * temp) - (0.02 * p_ref) - (15.0 * ca_opx) - 2.28)

        return cr_opx

    def CaLherz_(ca,cr):

        Xca_wher = (0.2933 * cr) + 0.14374
        Xca_lherz = (0.29334 * cr) + 0.0971
        Xca_harz = (0.2667 * cr) + 0.07467

        if (ca <= Xca_harz) or (ca >= Xca_wher):
            CaLherz = Xca_lherz
        else:
            CaLherz = ca

        return CaLherz

    def xCaopx(ca,cr,p_ref,temp):

        tk = temp + 273.15
        xCa_opx_lherz = np.exp((-1.0 * (6424 + (26.4*p_ref)) / tk) + 1.84)  #Correct
        xCa_gt_lherz = CaLherz_(ca, cr)

        Kdc = xCa_gt_lherz / xCa_opx_lherz
        Kdc = Kdc * np.exp(-1.27 + (0.000738 * (temp)) + (0.0236 * p_ref) - ((0.577 * cr) / (ca + 0.02)) + (1.79 * ca))

        xCa_opx = ca / Kdc

        return xCa_opx

    for i in range(0,len(T_K)):

        P = 50.0
        P_last = 50.0
        a = 0
        Dp_converge = 0.1

        while True:

            #Breaking after 1000 iteration
            a = a + 1
            if a > 1000:
                 Dp_converge = Dp_converge * 2.0

            Alpha = (((22.86 * P) + (1400.0 * xCa[i]) + 3740.0) / (1.987 * T_K[i])) - 0.986  #Good
            Beta = np.exp(Alpha) * (xMg[i] / xFe[i]) #Good
            mf_Opx = Beta / (1 + Beta) #Good

            Xca_opx = xCaopx(xCa[i], xCr[i], P, T_C[i])

            Xcr_opx = xCropx(Xca_opx, P, T_C[i])

            Xal_opx_m1 = (((1.0 + ((1.0 - mf_Opx) / 3.0)) * ((T_C[i] - Gasp_1 - (Gasp_3 * P))) / (Gasp_2 + (1.04 * (T_C[i] - Gasp_1 - (Gasp_3 * P)))))) -  Xcr_opx

            if Xal_opx_m1 < 0.0:

                Xal_opx_m1 = 0.0

            Xmg_opx_m1 = mf_Opx * (1.0 - Xal_opx_m1 - Xcr_opx)
            Xmg_opx_m2 = mf_Opx * (1.0 - Xca_opx)

            Kd = ((xMg[i]**3.0) * xAl[i] * xCr[i]) / ((Xmg_opx_m2**2.0) * Xmg_opx_m1 * Xcr_opx)

            Kd = Kd * Kd

            P = (-R * T_K[i] * np.log(Kd)) - (14412.0 * (xCa[i]**2.0)) + ((49782.0 - (23.5 * T_K[i])) *\
             xCa[i] * (xAl[i] - xCr[i])) + (23900.0 * (Xca_opx**2.0)) - 2783.0 - (3.94*T_K[i])

            P = P / ((146.0 * (xCa[i]**2.0)) - 397.0)

            if (np.abs(P-P_last) > Dp_converge):

                P_last = P
                continue
            else:

                if P > 0:
                    P_cr[i] = P / 10.0
                    break
                else:
                    P_cr[i] = -1
                    break

    return P_cr
