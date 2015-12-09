__author__ = 'amrit'

#AUX: 6

def EVM(r_list):
    #Auxiliaries
    PDR_F, ADR_F, ASR_F = 0, 0, 0
    PCM_S, ACM_S, ACWP_S, CPI, SPI = 0, 0, 0, 0, 0

    ADR_F= r_list[2]+0.4*r_list[3]+0.1*ACM_S
    ACM_S=ADR_F

    PDR_F=r_list[0]+r_list[1]+0.3*ACM_S
    PCM_S=PDR_F
    BCWS_A=PCM_S+0.2*ACM_S+0.4*r_list[5]
    BCWP_A=0.2*ACM_S+0.6*r_list[5]

    ASR_F=r_list[4]+0.6*r_list[3]+0.2*ACM_S

    ACWP_S=ASR_F
    try:
            if BCWS_A > 0:
                SPI = BCWP_A / float(BCWS_A)
            else:
                SPI = 1
            if ACWP_S > 0:
                CPI = BCWP_A / float(ACWP_S)
            else:
                CPI = 1
    except ZeroDivisionError:
            CPI=1

    return CPI*100, SPI*100