import csv
import re

def transform_text_to_csv(input_file, output_file):
    # Read the contents of the text file
    with open(input_file, 'r') as file:
        contents = file.read()

    # Split the contents into individual lines
    lines = contents.split('\n')

    # Initialize an empty list to store the rows of the CSV file
    csv_rows = []
    csv_rows.append(["Modelname","round name", "time", "valid loss", "loss", "ppl"])
    model_name = "" 
    epoch = 0  
    ppl = ""
    # Iterate over the lines of the text file
    for line in lines:
        line = line.strip()

        # Check if the line consists of "-"
        if "-" in line:
            continue
         
        
        # Check if the line starts with "NAME:"
        if "NAME:" in line:
            # Extract the model name
            model_name = line.split("NAME:")[1].strip()
            print("found name: ", model_name)
            continue
        elif "end" not in line:
            # Use regular expression to find the numbers for epoch and ppl
            epoch_match = re.search(r'epoch\s+(\d+)', line)
            ppl_match = re.search(r'ppl\s+([\d.]+)', line)
            if epoch_match and ppl_match:
                epoch = str(int(epoch_match.group(1)))
                ppl = str(float(ppl_match.group(1)))
                
        elif "end" in line:
            time_match = re.search(r'time:\s*([\d.]+)s', line)
            loss_match = re.search(r'valid loss\s*([\d.]+)', line)
            ppl_match = re.search(r'valid ppl\s*([\d.]+)', line)
            
            metrics = {}
            if time_match:
                time = time_match.group(1)
            if loss_match:
                valid_loss = loss_match.group(1)
            if ppl_match:
                valid_ppl = ppl_match.group(1)
            csv_rows.append([model_name, epoch, time, valid_loss, valid_ppl, ppl])

    # Write the rows of the CSV file to a new file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_rows)

# Example usage
transform_text_to_csv("/Users/laurachristoph/Library/CloudStorage/OneDrive-UniversitätZürichUZH/CL/05_F24_MachineTranslation/mt-exercise-03/ex02_log.txt", "log.csv")
