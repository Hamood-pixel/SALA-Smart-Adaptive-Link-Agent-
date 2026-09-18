import math 

def calc_fspl (distance, frequency):
    """
    Calculate the Free Space Path Loss (FSPL) in decibels (dB).
    """
    if distance <= 0 or frequency <= 0:
        raise ValueError("Distance and frequency must be positive values.")
    c = 3e8
    fspl = 20 * math.log10(distance) + 20 * math.log10(frequency) + 20 * math.log10(4*math.pi/c)
    return round(fspl, 2)

def calc_trans_power (
        distance : float,
        frequency: float,
        gt_dbi: float = 0.00,
        gr_dbi: float = 0.00,
        targetpower: float = 0.00
) -> dict:
    """
    calc required power to transmit
    """
    fspl = calc_fspl(distance, frequency)
    #received = transmitted + gt + gr - fspl and then rearranged
    req_power = targetpower  - gt_dbi - gr_dbi + fspl

    return {"distance": distance, 
            "freq" : frequency, 
            "fspl" : fspl, 
            "recommended transmit power" : round(req_power, 2)
    }