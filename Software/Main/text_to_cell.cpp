#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <string>
#include <cctype>
#include <math.h>
#include <map>
#include <vector>
#include <fstream>


#define DEBUG true


typedef uint8_t BYTE;

char *prg_name;
#define MAPPING_FILE "char_to_cell_mapping.txt"
#define UPPER_CASE_MARKER "~"
#define NUMBER_INDICATOR "^"

#define CELLS_HORIZONTAL 27
#define CELLS_VERTICAL 30
#define DOT_SPACING 2.5 //2.5mm spacing betwee dots in a cell
#define CELL_SPACING 4  //4mm spacing between adjacent cells


uint8_t DOT_NUMBERS[3][2] = {{1, 2}, {3, 4}, {5, 6}};

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
	printf("ERROR! %s\nUsage: %s <input-text-file> <output-file>",
                        err_msg, prg_name);
	return 1;
}

size_t get_f_size(FILE *file)
{
	fseek(file, 0L, SEEK_END);
	size_t fsize = ftell(file);
	fseek(file, 0L, SEEK_SET);
	return fsize;
}


std::string shape_text(std::string txt_str)
{
    //XXX FIXME - the method sucks man! It sucks ass!
    uint8_t size = txt_str.size();
    std::string btxt = "";
    for (int i = 0; i < size; i++)
	{
		if(isupper((int)txt_str[i]))
		{
            btxt.append(UPPER_CASE_MARKER);
            btxt.append<char>(1, tolower(txt_str[i]));
        }
		else if(isdigit((int)txt_str[i]))
        {
			btxt.append(NUMBER_INDICATOR);
            char *numc = &txt_str[i];
            int num = atoi(numc);
            int n = ((num == 0)? 106 : 96);
            num += n;
            btxt.append<char>(1, (char)num);
        }
        else
        {
            btxt.append<char>(1, txt_str[i]);
        }
    }
    return btxt;
}


const char *shape_char(char c)
{
    std::string btxt = "";
    if(isupper((int)c))
	{
        btxt.append(UPPER_CASE_MARKER);
        btxt.append<char>(1, (char)tolower((int)c));
    }
	else if(isdigit((int)c))
    {
		btxt.append(NUMBER_INDICATOR);
        int num = atoi(&c);
        int n = ((num == 0)? 106 : 96);
        num += n;
        btxt.append<char>(1, (char)num);
    }
    else
        btxt.append<char>(1, c);

    return btxt.c_str();
}


std::pair<BYTE*, uint8_t> celler(std::string str, std::map<char, BYTE> *char_cell)
{
    /*
        Doing conversion here.
        Iterate on the string and replace each char with byte from char_cell_map
    */
        uint8_t s_size = str.size();
        if (DEBUG) printf("Size of the string: %d\n", s_size);
        uint8_t *b_cells = new uint8_t[s_size];
        for (int i = 0; i < s_size; i++)
        {
            b_cells[i] = char_cell->find(str[i])->second;
            if (DEBUG) printf("%d ", b_cells[i]);
        }
        return std::make_pair(b_cells, s_size);
}


void cell_locations(std::pair<BYTE*, uint8_t> cells)
{
    /*
    TODO
        Do mapping to coordinate here

        Iterate over chars of a single line cheking
        if they have first level, middle level then
        bottom level dots.

        Calculate x,y coordinates depending on the page
        width, height and make an array of coordinate
        values that follow the printing path rule.

        top level dots    ->  2,4
        middle level dots ->  8,16
        butt level dots   ->  32,64

        starting with top level dots of the first line,
        there's a DOT_SPACING gap between shifting by
        2 and 4 and there is CELL_SPACING gap between
        one cell and the next

        iterate over each line three times.
    */
    if (DEBUG) printf("\nSize of the array is %d\n", cells.second);
    std::vector<std::pair<float, float> > cell_positions;
    float x_position = 0, y_position = 0;
    uint8_t no_lines = ceil(cells.second / (float)CELLS_HORIZONTAL);
    uint8_t last_line_cells = cells.second % CELLS_HORIZONTAL;

    if (DEBUG) printf("\nMax Number of Lines: %d\nLast Line: %d\n", no_lines,
                    last_line_cells);

    if (no_lines <= CELLS_VERTICAL)
    {
        for (int line_no = 1; line_no <= no_lines; line_no++)
        {
            uint8_t no_cells = (line_no != no_lines)? CELLS_HORIZONTAL : last_line_cells;
            for (int dot_level = 0; dot_level < 3; dot_level++) // for each dot level
            {
                if (DEBUG) printf("Current Dot Level: %d\n", dot_level);
                //if middle level -> reversed
                uint8_t offset = (line_no-1) * CELLS_HORIZONTAL;
                uint8_t start = offset + ((dot_level == 1)? no_cells-1 : 0);
                int8_t stop = offset + ((dot_level == 1)? -1 : no_cells);
                int8_t dir = (dot_level == 1)? -1 : 1;

                if (DEBUG) printf("Start: %u\nStop: %u\n", start, stop);

                for (int cell_h = start; cell_h != stop; cell_h+=dir)
                {
                    if (cell_h == start && dot_level == 1)
                    {
                        x_position += (dir * DOT_SPACING);
                        x_position += (dir * CELL_SPACING);
                    }
                    if (DEBUG) printf("On Cell: %d ---- On Location: (%f, %f) +++ ", cell_h, x_position, y_position);
                    //printf("Dot Level Check: %d & %d ", DOT_NUMBERS[dot_level][0], DOT_NUMBERS[dot_level][1]);
                    if((cells.first[cell_h] & (1 << DOT_NUMBERS[dot_level][0])) > 0){
                        cell_positions.push_back(std::make_pair(x_position, y_position));
                        if (DEBUG) printf("**AHA**");
                    }
                    x_position += (dir * DOT_SPACING);

                    if((cells.first[cell_h] & (1 << DOT_NUMBERS[dot_level][1])) > 0){
                        cell_positions.push_back(std::make_pair(x_position, y_position));
                        if (DEBUG) printf("**AHA**");
                    }
                    x_position += (dir * CELL_SPACING);

                }//finish one row of dots
                y_position += DOT_SPACING;
                if (DEBUG) printf("\nOne Level Down: %f\n", y_position);
            }//finish one row of cells
            y_position += CELL_SPACING;
        }
    }

    if (DEBUG) printf("SIZE OF LOCATIONS VECTOR: %lu\n", cell_positions.size());
    if (DEBUG) printf("\n\n***** DOT LOCATIONS *****\n\n");
    std::vector<std::pair<float, float> >::iterator v = cell_positions.begin();
    while (v != cell_positions.end())
    {
        printf("(%f, %f) ", v->first, v->second);
        v++;
    }
    printf("\n\n**** DONE TESTING ****\n");
}


int func(){
	printf("This is right!\n");
	return 1;
}



int main(int argc, char **argv)
{
	//expected arguments are Program <input text-file> <output-file>
    prg_name = argv[0];
	if(3 > argc < 5){
		if (DEBUG) func();
	}

	FILE *input_file;
	input_file = fopen(argv[1], "r");
	if(input_file == NULL)
		show_help(1);
	fclose(input_file);

	//--------------------------------------------------------------
	//read rule file
	FILE *mapping_rule;
    std::map<char, BYTE> char_cell_map;

    mapping_rule = fopen(MAPPING_FILE, "r");
	if(mapping_rule == NULL)
		show_help(2); //couldn't open file
	if (DEBUG) printf("Opened file\n");
	char *buffer, *line;
	size_t read_bytes = 0;
	size_t len;
	std::string thy_str;
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
    if (DEBUG) printf("Closing file\n");

	//----------------------------------------------------------------------------

		if (DEBUG) printf("\n\n\nCHECK DATA IN MAP\n");
		std::map<char, BYTE>::const_iterator map_it = char_cell_map.begin();
		while(map_it != char_cell_map.end())
		{
			if (DEBUG) printf("Char: %c\nCVal: %d\n", map_it->first, map_it->second);
			map_it++;
		}
		if (DEBUG) printf("\\n\n\n---------------------------\n");


	input_file = fopen(argv[1], "r");
    std::string all_text = "";


    char c;
	while((c = getc(input_file)) != EOF){
		if (c == '\n')
			c = ' ';
        all_text.append((std::string)shape_char(c));
	}
	fclose(input_file);
	if (DEBUG) printf("THE TEXT -------- %s--\n", all_text.c_str());

    cell_locations(celler(all_text, &char_cell_map));




    return 0;
}
