# Constants
PAGE_SIZE = 4096  # 4KB
FIRST_LEVEL_ENTRIES = 1024
SECOND_LEVEL_ENTRIES = 1024
LOGICAL_ADDRESS_SPACE = 32  # 32-bit
PHYSICAL_MEMORY_SIZE = 1 * 1024 * 1024 * 1024  # 1GB

# Calculated constants
OFFSET_BITS = 12  # 4KB page size -> 12 bits for offset
FIRST_LEVEL_BITS = 10  # 1024 entries -> 10 bits for first level
SECOND_LEVEL_BITS = 10  # 1024 entries -> 10 bits for second level

# Initialize page tables and frame table (simple dictionary-based)
first_level_page_table = {}
physical_memory = {}

# Helper function for address translation
def translate_address(logical_address):
    # Calculate first-level index, second-level index, and offset
    first_level_index = (logical_address >> (OFFSET_BITS + SECOND_LEVEL_BITS)) & ((1 << FIRST_LEVEL_BITS) - 1)
    second_level_index = (logical_address >> OFFSET_BITS) & ((1 << SECOND_LEVEL_BITS) - 1)
    offset = logical_address & ((1 << OFFSET_BITS) - 1)
    
    # Check if the page is loaded
    if first_level_index not in first_level_page_table:
        handle_page_fault(first_level_index, second_level_index)
    
    # Second level page table check
    second_level_page_table = first_level_page_table[first_level_index]
    if second_level_index not in second_level_page_table:
        handle_page_fault(first_level_index, second_level_index)
    
    # Translate to physical address
    frame_number = second_level_page_table[second_level_index]
    physical_address = (frame_number << OFFSET_BITS) | offset
    return first_level_index, second_level_index, offset, physical_address

# Page fault handler
def handle_page_fault(first_level_index, second_level_index):
    # Page fault handling: allocate a new frame for the page
    if first_level_index not in first_level_page_table:
        first_level_page_table[first_level_index] = {}
    
    if second_level_index not in first_level_page_table[first_level_index]:
        frame_number = len(physical_memory)
        physical_memory[frame_number] = None  # Placeholder for page data
        first_level_page_table[first_level_index][second_level_index] = frame_number
        print(f"Page fault handled: Loaded page at frame {frame_number}")

# Test function
def test_translation(logical_address_hex):
    logical_address = int(logical_address_hex, 16)
    first_level_index, second_level_index, offset, physical_address = translate_address(logical_address)
    
    print(f"Logical Address: {logical_address_hex}")
    print(f"  First Level Index: {first_level_index}")
    print(f"  Second Level Index (Page Number): {second_level_index}")
    print(f"  Offset: {offset}")
    print(f"  Physical Address: {hex(physical_address)}")
    print()

# Testing with provided logical addresses
test_addresses = ["0x12345678", "0xABCDEF12", "0x98765432"]
for address in test_addresses:
    test_translation(address)
