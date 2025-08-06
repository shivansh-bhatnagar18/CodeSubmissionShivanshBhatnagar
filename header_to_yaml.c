#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "inst_data.h"

void print_multiline_yaml(const char* key, const char* value) {
    printf("%s: >\n", key);
    char* copy = strdup(value);
    char* line = strtok(copy, "\n");
    while (line != NULL) {
        printf("  %s\n", line);
        line = strtok(NULL, "\n");
    }
    free(copy);
}

int main() {
    printf("$schema: %s\n", _schema);
    printf("kind: %s\n", kind);
    printf("name: %s\n", name);
    printf("long_name: %s\n", long_name);

    print_multiline_yaml("description", description);

    printf("access_s: %s\n", access_s);
    printf("access_u: %s\n", access_u);
    printf("access_vs: %s\n", access_vs);
    printf("access_vu: %s\n", access_vu);

    printf("data_independent_timing: %s\n", data_independent_timing ? "true" : "false");

    return 0;
}
