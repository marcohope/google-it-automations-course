# =============================================
# Practice Quiz — calculate_storage()
# Given a filesize, return the bytes needed using fixed-size blocks.
# =============================================

def calculate_storage(filesize):
    block_size = 4096

    # Floor division → how many full blocks are needed
    full_blocks = filesize // block_size

    # Modulo → is there leftover that needs a partial block?
    partial_block_remainder = filesize % block_size

    # If there's a remainder, allocate one more block for it
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size
    return full_blocks * block_size


# ---------- Tests ----------
print(calculate_storage(1))      # 4096
print(calculate_storage(4096))   # 4096
print(calculate_storage(4097))   # 8192
print(calculate_storage(6000))   # 8192
