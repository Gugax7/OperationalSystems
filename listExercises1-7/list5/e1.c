#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handle_sigint(int sig) {
    printf("\n[Captured Signal %d] SIGINT received! COntinuing execution", sig);
}

int main() {
    // Register the handler for SIGINT (Ctrl+C)
    signal(SIGINT, handle_sigint);

    printf("Program running. Press Ctrl+C to test the handler...\n");

    while (1) {
        printf("Working...\n");
        sleep(2); // Keeps the thread alive to intercept signals
    }

    return 0;
}