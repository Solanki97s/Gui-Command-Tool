def generate_response(value):
    if value in ("GPRSSTATUS", "gprsstatus", "Gprsstatus"):
        response = """
        CN: airtel
        DBTON-100 MTR
        SOFF
        SS: 28
        CC: airteliot.com,,
        IP: 45.113.189.20,38395
        WTI: 30S,30S,30S
        GPS: A
        SF: 0
        CF: 0
        MU: 0,0,0
        PD: 0
        GMS: 0
        """
        return response
    elif value in ("version", "VERSION", "Version"):
        return "Made By Harsh Singh"
    elif value == "Sysstatus":
        return "MPON\nIGNON\nARMED\nAC OFF\nDBGOFF\nDIPOFF\nGOUTOFF\nOBDOK\nODO: 11.22\nTEMP: 33\nBAT: 3.40V"
    else:
        return "SMS NOT ACCEPTED"
