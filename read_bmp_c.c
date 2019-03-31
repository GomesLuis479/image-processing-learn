#include <stdio.h>

int main(void) {
	int counter; 			//initiallize counter
	unsigned char b[1]; 	//set buffer

	//pointer initialisation
	FILE *in, *out; 

	//open the original file
	if ((in = fopen("hpf.bmp", "rt")) == NULL) {
		//if there is error print msg
		fprintf(stderr, "Cannot open input file.\n"); 
		return 1;
	}

	//open the new file
	if ((out = fopen("new.bmp", "wt")) == NULL) {
		fprintf (stderr, "Cannot open output file.\n");
		return 1;
	}

	for (counter=0;counter<=55;counter++) {
		// this function is use to read from buffer
		fread (b, 1, 1, in); 

		// this function is use to write from buffer
		fwrite (b, 1, 1, out); 
	}

	while(1) {
		if (fread (b, 1, 1, in) <= 0) {
			break;
		}
			
		b[0] = b[0]; // L-1-r
		fwrite (b, 1, 1, out);
	}

	fclose(in);
	fclose(out);

	return 0;
}