import csv

# Define the input CSV file and output TSV file paths
input_csv_file = 'C:/Users/smhhborg/Documents/GitHub/DCAT-ap-as-LinkML-template/CSV_Files/dcat Dataset.csv'
output_tsv_file = 'C:/Users/smhhborg/Desktop/DCAT_AP_via_LinkML_for_Dataverse_2.tsv'

# Open the input CSV file for reading
with open(input_csv_file, mode='r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_data = list(csv_reader)

# Define the metadata block and dataset fields
metadata_block = [
    "#metadataBlock\tname\tdataverseAlias\tdisplayName\tblockURI",
    "\tDCAT_ap_via_LinkML\t\tDCAT_ap_via_LinkML Metadata\thttps://github.com/HendrikBorgelt/DCAT-ap-as-LinkML-template"
]

dataset_fields_header = [
    "#datasetField\tname\ttitle\tdescription\twatermark\tfieldType\tdisplayOrder\tdisplayFormat\tadvancedSearchField\tallowControlledVocabulary\tallowmultiples\tfacetable\tdisplayoncreate\trequired\tparent\tmetadatablock_id\ttermURI"
]

dataset_fields = [
    "\tDCAT_ap_via_LinkML_0000\tDataset\t-\t\tnone\t1\t\tFALSE\tFALSE\tFALSE\tFALSE\tTRUE\tTRUE\t\tDCAT_ap_via_LinkML"
]

# Function to convert CSV rows to the required TSV format
def convert_csv_to_tsv_row(csv_row, index):
    tsv_row = ["", # empty first row'
        f"DCAT_ap_via_LinkML_{index:04d}", # name
        csv_row[0],  # title (empty as per the example)
        "-",          # description (empty as per the example)
        "",          # watermark (empty as per the example)
        "text" if csv_row[3] == "Literal" else "none",   # fieldType
        index + 1,   # displayOrder (1-based index)
        "#VALUE" if csv_row[3] == "Literal" else "",  # displayFormat
        "FALSE",     # advancedSearchField
        "FALSE",     # allowControlledVocabulary
        csv_row[6],     # allowmultiples
        "FALSE",     # facetable
        "TRUE",      # displayoncreate
        "TRUE" if csv_row[2] == "mandatory" else "FALSE",  # required
        "Dataset",   # parent
        "DCAT_ap_via_LinkML",  # metadatablock_id
        csv_row[1]   # termURI
    ]
    return "\t".join(map(str, tsv_row))

# Convert each CSV row to TSV format
for index, row in enumerate(csv_data[1:], start=1):
    dataset_fields.append(convert_csv_to_tsv_row(row, index))

# Write the metadata block and dataset fields to the output TSV file
with open(output_tsv_file, mode='w', newline='', encoding='utf-8') as tsv_file:
    tsv_file.write("\n".join(metadata_block) + "\n")
    tsv_file.write("\n".join(dataset_fields_header) + "\n")
    tsv_file.write("\n".join(dataset_fields) + "\n")

print(f"TSV file '{output_tsv_file}' generated successfully.")
