import sys
from SmaliClassDef import SmaliClassDef

flags = []


# Operates on just one file
def main():
    global flags

    # Read source code into list of lines
    class_smali_file = sys.argv[-1]
    #print("File: " + class_smali_file)
    scd = SmaliClassDef(class_smali_file)
    num_lines_before = scd.get_num_lines()

    flags = sys.argv[1:-1]
    #print("main flags: " + str(flags))

    # main parsing loop is done
    # manual check correct parsing
    if "-D" in flags:
        # print("---unused lines---\n" + str(lines))
        print("------------------\n")
        print("---header---\n" + str(scd.header))
        print("------------------\n")
        print("---static fields---\n" + str(scd.static_fields))
        print("------------------\n")
        print("---instance fields---\n" + str(scd.instance_fields))
        print("------------------\n")
        print("---methods---\n" + str(scd.methods))
        print("------------------\n")

    # Do the actual instrumentation
    #print("Instrumenting: " + str(class_smali_file))
    scd.instrument()
    #print(scd.class_name)
    # scd.verbose()
    # Write out to file if flags specify to do so
    if "-ow" in flags:
        print("Overwriting: " + str(class_smali_file))
        scd.write_to_file(class_smali_file)

    if "-o" in flags:
        file_name = flags[flags.index("-o") + 1]
        print("Writing to: " + str(file_name))
        scd.write_to_file(file_name)
        
    if "-a" in flags:
        num_lines_after = scd.get_num_lines()
        file_name = flags[flags.index("-a") + 1]
        fh = open(file_name, "a")
        fh.write(str(scd.file_name) + ", " + str(num_lines_before) + ", " + str(num_lines_after) + ", " + str(num_lines_after - num_lines_before) + "\n")
        fh.close()
        
if __name__ == "__main__":
    main()
