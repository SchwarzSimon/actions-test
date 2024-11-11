#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

// Constructor attribute to execute before main()
__attribute__((constructor)) void preload_function() {
    system("echo 'Command executed on startup'");
    exit(0); // Exits the program immediately
}