
# REMINDER: Change filepath to your system configuration
file = open("/Users/josephgalasso/Documents/COVIDGenomeAnalysis/human_only_MOA_fastas_86.txt", "r")
lines = file.readlines()

def getIDName(newHeader, id):
    for item in newHeader:
        itemID = item.split("=")[0]
        if itemID == id:
            return item.split("=")[1]


for i in range(len(lines)):
    line = lines[i]
    if line[0:4] == ">lcl":
        newHeader = line.replace("]", "")
        newHeader = newHeader.split(" [")
        accessionNumber = newHeader[0][5:].split("prot")[0][0:-1]
        proteinName = getIDName(newHeader, "protein")
        proteinID = getIDName(newHeader, "protein_id")
        
        #proteinName = newHeader[1].split("=")[1]
        #proteinID = newHeader[2].split("=")[1]
        
        newHeader = ">" + proteinName + "," + proteinID + "," + accessionNumber + "\n"
        lines[i] = newHeader

file.close()

# REMINDER: Change file name to your preference
filename = "parsedMOA"

# REMINDER: Change filepath to your system configuration
out = open("/Users/josephgalasso/Documents/COVIDGenomeAnalysis/" + filename, 'w')
out.writelines(lines)
out.close()
