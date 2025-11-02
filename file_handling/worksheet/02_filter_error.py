def filter_log_errors(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                if "ERROR" in line:
                    outfile.write(line)
        with open(output_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "ERROR" not in line:
                    print("Validation failed: Found a non-ERROR line in the output.")
                    return
            print("Validation passed: All lines in the output contain 'ERROR'.")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

i = r'file_handling\files\mixed_logs.log'       
o = r'file_handling\files\error_logs.txt'    
filter_log_errors(i, o)