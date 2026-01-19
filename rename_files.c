#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <unistd.h>

typedef struct {
    const char *number;
    const char *id;
} ProblemMapping;

ProblemMapping mappings[] = {
    {"10950", "A191"},
    {"10952", "A229"},
    {"8958", "A052"},
    {"10171", "A184"},
    {"10807", "A196"},
    {"10170", "A183"},
    {"5597", "A234"},
    {"11382", "A182"},
    {"1157", "A045"},
    {"2743", "A203"},
    {"1330", "A185"},
    {"7287", "A231"},
    {"2438", "A195"},
    {"15552", "C028"},
    {"14681", "A188"},
    {"9498", "A186"},
    {"10699", "A224"},
    {"2753", "A187"},
    {"10872", "A228"},
    {"4344", "A008"}
};

int main() {
    int count = 0;
    char old_name[256];
    char new_name[256];
    const char *date;

    for (size_t i = 0; i < sizeof(mappings) / sizeof(mappings[0]); i++) {
        // Construct the current expected filename: [ID]_[Number]_김예준_22500134.c
        snprintf(old_name, sizeof(old_name), "%s_%s_김예준_22500134.c", mappings[i].id, mappings[i].number);
        
        // Check if file exists
        if (access(old_name, F_OK) != 0) {
            // Try to see if it might be already renamed or in previous state? 
            // The instructions say files are currently in [ID]_[Number]_... format.
            // But let's just print if not found.
            printf("File %s not found, skipping.\n", old_name);
            continue;
        }

        // Determine date based on count
        if (count < 10) {
            date = "20260109";
        } else {
            date = "20260110";
        }

        // Construct new filename: [ID]_김예준_[Date].c
        snprintf(new_name, sizeof(new_name), "%s_김예준_%s.c", mappings[i].id, date);

        printf("Renaming %s to %s\n", old_name, new_name);
        if (rename(old_name, new_name) == 0) {
            count++;
        } else {
            perror("Error renaming file");
        }
    }
    
    printf("Total files renamed: %d\n", count);
    return 0;
}

