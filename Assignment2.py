instruction_bytes = []
binary_array = []
instruction_array = []

# Opens and reads file and adds to instruction bytes
with open("arm_thumb_instructions.bin", 'rb') as inst_file:
    instr_str = inst_file.readlines()[0]
for byte in bytearray(instr_str):
    instruction_bytes.append(byte)

# formats each one and puts into the binary array, with each separate value
for i in range(len(instruction_bytes)):
    binary_array.append(format(instruction_bytes[i], '08b'))

# Reinitialize iterator
i = 0
# Combines the instructions and places into instruction array
while i < len(binary_array) - 1:
    instruction_array.append(binary_array[i] + binary_array[i + 1])
    i += 2

# Puts values back into list instruction bytes
instruction_bytes = instruction_array
print(instruction_bytes)

# MACHINE TO ASSEMBLY FUNCTION
def machine_to_assembly(instruction):
    single_instructions = []
    if instruction[:3] == '000':
        single_instructions.append('Move Shifted Register')
    if instruction[:3] == '000' and instruction[3:6] == '111':
        single_instructions.append('Add and Subtract')
    print(single_instructions)


# int('0111', 2) # to convert to decimal
for instruction in instruction_bytes:
    machine_to_assembly(instruction)
print(instruction_bytes)
