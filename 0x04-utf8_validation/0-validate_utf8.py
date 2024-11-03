def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Get only the last 8 bits of the integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1  # 2-byte character
            elif (byte >> 4) == 0b1110:
                num_bytes = 2  # 3-byte character
            elif (byte >> 3) == 0b11110:
                num_bytes = 3  # 4-byte character
            elif (byte >> 7):
                return False
            # 1-byte character must start with 0 in the most significant bit
        else:
            # Check if the byte starts with "10" (continuation byte)
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
