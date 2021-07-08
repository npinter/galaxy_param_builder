tsv_file = "C:\\Users\\Niko\\Desktop\\galaxy_params.tsv"

with open(tsv_file, "r") as file:
	tsv_read = file.readlines()

param_temp = []
param_list = []

for line in tsv_read:
	param_val = line.split("\t")

	if len(param_val) > 2:
		if len(param_val[2].split(",")) == 1 and param_val[2].split(",")[0].isdigit():
			print(
				"<param name=\"{}\" label=\"{}\" type=\"int\" value=\"{}\" min=\"0\" \n"
				"       help=\"{}\"/>".format(param_val[1], param_val[0], param_val[2], "" if param_val[3][0] == "-" else param_val[3][:-1]))
		elif len(param_val[2].split(",")) == 2 and param_val[2].split(",")[0].isdigit():
			print(
				"<param name=\"{}\" label=\"{}\" type=\"float\" value=\"{}\" min=\"0\" \n"
				"       help=\"{}\"/>".format(param_val[1], param_val[0], param_val[2].replace(",", "."), "" if param_val[3][0] == "-" else param_val[3][:-1]))
		elif param_val[2] in ["FALSE", "TRUE"]:
			print(
				"<param name=\"{}\" label=\"{}\" type=\"boolean\" checked=\"{}\" \n"
				"       truevalue=\"True\" falsevalue=\"False\" \n"
				"       help=\"{}\"/>".format(param_val[1], param_val[0], "true" if param_val[2] == "TRUE" else "false", "" if param_val[3][0] == "-" else param_val[3][:-1]))
		elif param_val[2][0] == "\"":
			param_temp.append(param_val[0])
			param_temp.append(param_val[1])
			param_list.append(param_val[2][1:-1])
		else:
			print("Not an int, float or bool", param_val[0], param_val[1], param_val[2], param_val[3])
	elif len(param_val) == 1 and param_val[0][-1] == "\n":
		param_list.append(param_val[0][:-1])
	elif len(param_val) == 2 and param_val[0][-1] == "\"":
		param_list.append(param_val[0][:-1])
		print(
			"<param name=\"{}\" label=\"{}\" type=\"select\" \n"
			"       help=\"{}\">".format(param_temp[1], param_temp[0], "" if param_val[1][0] == "-" else param_val[3][:-1]))
		for i, item in enumerate(param_list):
			print(
				"\t<option value=\"{}\"{}>{}</option>".format(i, " selected=\"true\"" if item[0] == "~" else "", item[1:] if item[0] == "~" else item))
		print("</param>")
		param_temp = []
		param_list = []
