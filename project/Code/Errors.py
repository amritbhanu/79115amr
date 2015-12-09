__author__ = 'amrit'

#AUX: 14

def errors(r_list):
    #Auxiliaries
    AEGenR_F, AERegenR_F, AERetirementR_F, PEGenR_F, PEDCR_F, CER_F, CTT_F = 0, 0, 0, 0,0,0,0
    UAE_S, QAR_S, UPE_S, CER_S = 0, 0, 0, 0


    AED_A=0.3*QAR_S + 0.8*UAE_S*+0.2*UAE_S+0.4*r_list[12]
    MRED_A=0.6*r_list[4]+ 0.3*r_list[5]+0.2*AED_A

    #Flows

    CTT_F=0.7*r_list[5]+r_list[6]+0.6*r_list[12]
    AEGenR_F=r_list[0] + r_list[1] + r_list[2]
    AERegenR_F=r_list[3] + 0.4*r_list[4] + MRED_A + 0.7 * AED_A
    UAE_S=AEGenR_F+AERegenR_F

    AERetirementR_F=0.6*UAE_S+r_list[7]
    #Stocks
    UPE_S = AERetirementR_F+r_list[8] +r_list[9]+r_list[10]
    PED_A=r_list[11]+0.4*UPE_S
    PEDCR_F=0.6*UPE_S+PED_A+0.35*CTT_F

    CER_S=PEDCR_F+r_list[13]

    return CER_S, CTT_F


