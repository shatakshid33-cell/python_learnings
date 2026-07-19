


LINE = "=" * 50
THIN_LINE = "-" * 50


# Step 1: Get the DNA sequence from the user
def get_dna_sequence():
    dna = input("Enter the DNA sequence: ").upper()
    dna = dna.strip()  # remove extra spaces
    return dna


# Step 2: Check if the sequence only contains A, C, G, T
def is_valid_dna(dna):
    for base in dna:
        if base not in "ACGT":
            return False
    return True


# Step 3: Count how many times each base appears
def count_bases(dna):
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0

    for base in dna:
        if base == "A":
            a_count = a_count + 1
        elif base == "C":
            c_count = c_count + 1
        elif base == "G":
            g_count = g_count + 1
        elif base == "T":
            t_count = t_count + 1

    return a_count, c_count, g_count, t_count


# Step 4: Calculate GC content and AT content
def calculate_content(a_count, c_count, g_count, t_count, total_length):
    gc_content = (g_count + c_count) / total_length * 100
    at_content = (a_count + t_count) / total_length * 100
    return gc_content, at_content


# Step 5: Build the report as a single piece of text
# (this way we can print it AND save it to a file using the same content)
def build_report(dna, a_count, c_count, g_count, t_count, gc_content, at_content):
    lines = []
    lines.append(LINE)
    lines.append("DNA SEQUENCE ANALYSIS REPORT".center(50))
    lines.append(LINE)
    lines.append("")
    lines.append("1. SEQUENCE OVERVIEW")
    lines.append(THIN_LINE)
    lines.append(f"Sequence            : {dna}")
    lines.append(f"Length              : {len(dna)} bases")
    lines.append("")
    lines.append("2. BASE COUNTS")
    lines.append(THIN_LINE)
    lines.append(f"Adenine (A)         : {a_count}")
    lines.append(f"Cytosine (C)        : {c_count}")
    lines.append(f"Guanine (G)         : {g_count}")
    lines.append(f"Thymine (T)         : {t_count}")
    lines.append("")
    lines.append("3. COMPOSITION")
    lines.append(THIN_LINE)
    lines.append(f"GC content          : {gc_content:.2f}%")
    lines.append(f"AT content          : {at_content:.2f}%")
    lines.append("")
    lines.append(LINE)
    lines.append("END OF REPORT".center(50))
    lines.append(LINE)

    report_text = "\n".join(lines)
    return report_text


# Step 6: Save the report to a text file
def save_report(report_text, filename="dna_report.txt"):
    with open(filename, "w") as file:
        file.write(report_text)
    print(f"\nReport saved as '{filename}'")



# Main program
def main():
    dna = get_dna_sequence()

    # keep asking until the user enters a valid sequence
    while is_valid_dna(dna) == False or dna == "":
        print("Invalid input. Please enter only A, C, G, T characters.")
        dna = get_dna_sequence()

    a_count, c_count, g_count, t_count = count_bases(dna)
    gc_content, at_content = calculate_content(a_count, c_count, g_count, t_count, len(dna))

    report_text = build_report(dna, a_count, c_count, g_count, t_count, gc_content, at_content)

    print("\n" + report_text)
    save_report(report_text)

    


# Run the program
main()