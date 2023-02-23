import pandas as pd

def operand(type="POWP",    
            param1=0,param2=0,param3=0.0,param4=0.0,
            param5=0.0,param6=0.0,param7=0.0,param8=0.0,
            target=0.0,weight=0.0,value=0.0):

    # PMGT   3  14 0.000000000000E+00 0.000000000000E+00 0.000000000000E+00 0.000000000000E+00 0.000000000000E+00 0.000000000000E+00 -1.500000000000E+01 -1.000000000000E+00 -1.500000000000E+01

    operand_str = f"{type}   {param1}  {param2} {param3} {param4} {param5} {param6} {param7} {param8} {target} {weight} {value}\n"
    return operand_str
def powp(surf, y, diameter, target,weight):
    py=y/(diameter/2)
    return operand(type="POWP", param1=surf, param6=py, target=target, weight=weight)

def build_merit_function(
        power_profile, 
        lens_front_rowIndex,
        lens_back_rowIndex,
        
        lens_diameter,
        thickness_min, 
        thickness_max, 
        
        if_1st_differential,
        thickness_weight=1.0,
        power_weight=1.0,
        differential_weight=1.0
        ):
    ver_str = "VERS 190513\n"
    thickness_str=operand(type="FTGT", 
                    param1=lens_front_rowIndex,target=thickness_min,weight=thickness_weight)
    thickness_str+=operand(type="FTLT",
                    param1=lens_front_rowIndex,target=thickness_max,weight=thickness_weight)
    p=power_profile.apply(lambda x: powp(lens_back_rowIndex,x[0],lens_diameter,x[1],power_weight), axis=1)
    powp_str="".join(p)

    d=power_profile.diff().dropna()
    powp_start_index=3
    diff_str=""
    for i in range(len(d)):
        op_No2=powp_start_index+i 
        op_No1=op_No2+1
        diff_str+=operand("DIFF", param1=op_No1, param2=op_No2,weight=0.0)
    # divb_start_index=2+len(p)+len(d)+1
    diff_start_index=2+len(p)+1

    divb_str=""
    for i in range(len(d)):
        op_No=diff_start_index+i
        divb_str+=operand("DIVB", param1=op_No, param3=d.iloc[i][0],target=d.iloc[i][1]/d.iloc[i][0],weight=differential_weight)

    if if_1st_differential:
        merit_str=ver_str+thickness_str+powp_str+diff_str+divb_str
    else:
        merit_str=ver_str+thickness_str+powp_str

    return merit_str




    pass 