#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <string>
#include <cctype>
#include <map>


#include <fstream>

typedef unsigned char BYTE;

char *prg_name;
#define MAPPING_FILE "char_to_cell_mapping.txt"
#define UPPER_CASE_MARKER "~"
#define NUMBER_INDICATOR "^"

int show_help(BYTE err_code)
{
	/*error codes
		0 - Wrong number of arguments
		1 - Can not find/read Mapping file.
		2 - Can not find input file
		3 - Couldn't read Mapping file
		4 - Couldn't read input file
	*/
	char *err_msg = NULL;
	switch (err_code){
		case 0:
			strcpy(err_msg, "Wrong Number of Arguments!"); break;
		case 1:
			strcpy(err_msg, "Can Not Find Mapping File. Check if ");
			strcat(err_msg, MAPPING_FILE);
			strcat(err_msg, " Exists in the directory.");
			break;
		case 2:
			strcpy(err_msg, "Can Not Find Input Text File."); break;
		case 3:
			strcpy(err_msg, "Couldn't Read Mapping File."); break;
		case 4:
			strcpy(err_msg, "Couldn't Read Input File."); break;

	}
	printf("ERROR! %s\nUsage: %s <input-text-file> <output-file>", err_msg, prg_name);
	return 1;
}

size_t get_f_size(FILE *file)
{
	fseek(file, 1L, SEEK_END);
	size_t fsize = ftell(file);
	fseek(file, 0L, SEEK_SET);
	return fsize;
}

/*
char *shape_text(std::string txt_str)
{
	std::string final_str;
	uint8_t size = txt_str.size();
	for (int i = 0; i < size; i++)
	{
		if(isupper((int)txt_str.at(i)))
			final_str.append(UPPER_CASE_MARKER);
		else if(isdigit((int)txt_str.at(i)))
			final_str.append(NUMBER_INDICATOR);
		final_str.append(txt_str.at(i));
	}
	return final_str.c_str();
}
*/

int func(){
	printf("This is wrong!\n");
	return 1;
}

int main(int argc, char **argv)
{



	//expected arguments are Program <text-file> <output-file>
	prg_name = argv[0];
	if(3 > argc < 5){
		func();
	}

	FILE *input_file;
	input_file = fopen(argv[1], "r");
	if(input_file == NULL)
		show_help(1);
	fclose(input_file);

	/****************************************************************************/	
	//read rule file
	std::map<char, BYTE> char_cell_map;
	FILE *mapping_rule;
	mapping_rule = fopen(MAPPING_FILE, "r");
	if(mapping_rule == NULL)
		show_help(2); //couldn't open file
	printf("Opened file\n");
	char *buffer, *line;
	size_t read_bytes = 0;
	size_t len; 
	std::string thy_str;
	printf("Read Bytes = %lu\n", read_bytes);
	while((read_bytes = getline(&buffer, &len, mapping_rule)) != -1)
	{
		//printf("Inside Loop - read: %lu\n", read_bytes);
		if (buffer[0] == '#') //ignore comment lines
			continue;
		else
		{
			thy_str = buffer;
			BYTE cell_val = (BYTE)atoi(thy_str.substr(thy_str.find(" "), thy_str.size()-1).c_str());
			// printf("CHAR = %c   INTEGER VALUE = %d\n", buffer[0], cell_val);
			char_cell_map.insert(std::map<char, BYTE>::value_type(buffer[0], cell_val));
		}
			
	}

	fclose(mapping_rule);		

	/****************************************************************************/	

		printf("\n\n\nCHECK DATA IN MAP\n");
		std::map<char, BYTE>::const_iterator map_it = char_cell_map.begin();
		while(map_it != char_cell_map.end())
		{
			printf("Char: %c\nCVal: %d\n", map_it->first, map_it->second);
			map_it++;
		}
		printf("\\n\n\n---------------------------\n");

	
	input_file = fopen(argv[1], "r");
	std::string all_text;
/*	char *text_buff;
	text_buff = new char[f_size];

	size_t frd = fread(text_buff, 1, f_size, input_file);
	if(frd == 0)
		show_help(4);
	all_text = text_buff;
	*/
	char c;
	while((c = getc(input_file)) != EOF){
		if (c == '\n')
			c = ' ';

		printf("%d ", (int)c);
		if(isupper((int)c)){
			all_text.append(UPPER_CASE_MARKER);
			all_text.append<char>(1, tolower(c));
			continue;
		}
		else if(isdigit((int)c))
			all_text.append(NUMBER_INDICATOR);
		all_text.append<int>(1, c);
	}
	printf("THE TEXT -------- %s--\n", all_text.c_str());
	fclose(input_file);
	
	//std::ofstream o_file("outfile.t"); o_file << all_text; o_file.close();
	//FILE *o_file;
	//o_file = fopen("outfile", "w");
	//if(o_file == NULL)
	//	return 1;
	//size_t wrott = fwrite(all_text.c_str(), sizeof(char), all_text.length(), o_file);
	//fclose(o_file);
	return 0;
}