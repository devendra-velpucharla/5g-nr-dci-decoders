def reverse_byte(byte):
    """Reverse bits in a single byte (8 bits)"""
    return int('{:08b}'.format(byte)[::-1], 2)

def get_bits(binary_str, start, length):
    """Extract bits from a binary string starting at 'start' of 'length'"""
    return binary_str[start:start + length]

def dci1_1_decoder(decimal_bytes):
    if len(decimal_bytes) != 7:
        raise ValueError("Exactly 7 decimal values (bytes) required.")

    print("Input Decimal Bytes and Reversed Binaries:")
    reversed_bin_str = ""
    for i, byte in enumerate(decimal_bytes):
        original_bin = format(byte, '08b')
        reversed_bin = format(reverse_byte(byte), '08b')
        print(f"Byte {i+1}: {byte} -> {original_bin} -> reversed: {reversed_bin}")
        reversed_bin_str += reversed_bin

    print("\nCombined 48-bit binary after reversing each byte:")
    print(reversed_bin_str)

    fields = {
        'D':                  (0, 1),
        'FreqDomain Rsrc':    (1, 16),
        'TimeDomain Rsrc':    (17, 2),
        'MCS':                (19, 5),
        'NDI':                (24, 1),
        'RV_INDX':            (25, 2),
        'HARQ PROC ID':       (27, 4),
        'DAI':                (31, 2),
        'TPC':                (33, 2),
        'PUCCH_RI':           (35, 3),
        'K1':                 (38, 3),
        'Antenna':            (41, 4),
        'SRS':                (45, 2),
        'DMRS':               (47, 1),
    }

    print("\nDecoded Fields:")
    for name, (start, length) in fields.items():
        value = int(get_bits(reversed_bin_str, start, length), 2)
        print(f"{name:<18}: {value}")

# Example usage:
# Input: 7 decimal values, each representing a byte
input_bytes = [129, 8, 33, 177, 73, 49, 0]  # You can change these
dci1_1_decoder(input_bytes)
