#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


//JPGs have special patterns: the first three bytes are always 0xff,0xd8,0xff. The first bits of the fourth byte are 1110.
//Data always stored in 512 bits > always search for the above beginnings at the start of these chunks > open new file for the respective JPG >then write to file until new JPG begins.
//Read chunks from 512 into buffer to increase efficiency
//pick 50 JPGs

//Procedure:

//1.Open Memory card
//2.repeat until end of card:
//3a.read 512 bytes into a buffer (fread)
//4.if start of new JPEG (check buffer values of array > video Brian)
//4a.if first JPEG
//4aa....write file
//4b. Else
//4ba....close file, open new file and write
//4c.Else
//4ca.If already found JPEG keep writing to it
//4cb. If no bytes left = close files & end



int main(int argc, char *argv[])
{
    typedef uint8_t BYTE;

    BYTE buffer [512];
    int bytes_left, data_count = 0;
    char filename [8];
    FILE *img = NULL;
    // must be defined here so that it is not subject to the scope of the individual conditions and can be used as a prototype

    //one cmd-line argument
    if (argc != 2)
    {
        printf("Error! Look for correct usage\n");
        return 1;
    }

    //open file
    FILE *file = fopen(argv[1], "r");

    //check if valid
    if (file == NULL)
    {

        printf("file invalid");
        return 1;
    }

    //with malloc/free:
    // bytes_left = fread(buffer, sizeof(BYTE), 512, file);
    // while (fread (buffer, sizeof(BYTE), 512, file) == bytes_left) // endless loop bis kein byte mehr vorhanden
    //etc... (liked this or similar)


    while (1)
    {
        //only reserves the space for BYTES currently being processed, therefore no malloc/free. Useful in general for file transfers.

        bytes_left = fread(buffer, sizeof(BYTE), 512, file);
        // count the bytes read so that there is no core dump at the end of the file. // it is read byte by byte.
        // If sizeof(BYTE) or 1 is selected for "size", this is the element value. The "number" 512 specifies how often the element value is to be read out.

        //explanation: buffer use/procedure
        //The buffers are limited by the array Buffer[512] and completely filled by fread. If a JPEG start is detected, the entire buffer is first transferred BYTE by BYTE to the target file using the fwrite function.
        //Transferred data is deleted in the buffer, so to speak.
        //In this way, a buffer can be used to go through all files and the last buffer is completely transferred to the last file.
        //bytes_left is used to catch the actual number of bytes still available; the return value of fread is number (512).

        //if start of new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && ((buffer[3] & 0xf0) == 0xe0))
        //searches only at the beginning of the buffer, i.e. not in the 512 chunks

        {
            if (data_count == 0) //no current data for JPEG
            {
                sprintf(filename, "%03i.jpg", data_count); //creates string with filename
                img = fopen(filename, "w"); //for the prototype value *img, the pointer img is created with the respective file name
                fwrite(buffer, sizeof(BYTE), bytes_left, img); //The entire buffer is transferred to the address of the img file
                data_count ++; //increase count for next filename
            }
            else if (data_count > 0) //if jpeg already exists
            {
                fclose(img);
                sprintf(filename, "%03i.jpg", data_count);
                img = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), bytes_left, img);
                data_count++;
            }
        }
        else if (data_count != 0) //if no jpeg-start
        {

            fwrite(buffer, sizeof(BYTE), bytes_left, img);

            if (bytes_left == 0) // if there are no more bytes close and stop files // if there are no bytes if condition of buffer 1-4 is false.
            //fwrite on the last else if works writes 0 bytes to the file. the last if condition then ends the loop.
            {
                fclose(img);
                fclose(file);
                return 0;
            }


        }
    }

}
