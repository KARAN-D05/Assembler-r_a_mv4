instruction1 = input("Enter Instruction1: ")
instruction2 = input("Enter Instruction2: ")

ins1 = instruction1[0:4]
ins2 = instruction1[5]
ins3 = instruction1[7:11]

if ins1 == "LOAD":
    print("Machine Code Program:")
    print(f"00{ins2}{ins3[0]}00{ins3[1]}000{ins3[2]}{ins3[3]}0000")

if instruction2 == "STORE":
    print(f"01{ins2}0000000000000")