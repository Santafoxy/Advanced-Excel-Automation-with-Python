# USING APPEND MODE
input_file = "Outlook Week 13  Infrastructure, utilities, and heavy civil projects companies.txt"
output_file = "Outlook Week 13 Infrastructure, utilities, and heavy civil projects companies Demacated in Hundreds.txt"

input_file_2 = "Google Week 13  Infrastructure, utilities, and heavy civil projects companies.txt"
output_file_2 = "Google Week 13 Infrastructure, utilities, and heavy civil projects companies Demacated in Hundreds.txt"

insert_every = 100

# Process first file
print(f"Processing: {input_file}")
with open(input_file, "r", encoding="utf-8") as f, \
     open(output_file, "w", encoding="utf-8") as g:  # 'w' for write (creates new file)
    
    for i, line in enumerate(f, start=1):
        g.write(line)
        
        if i % insert_every == 0:
            g.write(f"{i} ----------------------------------------------------------------\n")
            print(f"  Added separator after line {i}")
    
    print(f"✓ Completed: {i} lines written to {output_file}")

print()

# Process second file
print(f"Processing: {input_file_2}")
with open(input_file_2, "r", encoding="utf-8") as f2, \
     open(output_file_2, "w", encoding="utf-8") as g2:  # 'w' for write
    
    for i, line in enumerate(f2, start=1):
        g2.write(line)
        
        if i % insert_every == 0:
            g2.write(f"{i} ----------------------------------------------------------------\n")
            print(f"  Added separator after line {i}")
    
    print(f"✓ Completed: {i} lines written to {output_file_2}")

print("\nOutput files created:")
print(f"  1. {output_file}")
print(f"  2. {output_file_2}")