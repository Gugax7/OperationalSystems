// ## Exercise 2: Inter-Process Communication (Pipes)
// 2. Implement a pipe in C, as presented during class.

#include <stdio.h>
#include <unistd.h>

int main() {
    int fd[2], child;
    
    pipe(fd);

    child = fork();

    if(child) {
        char buf[1024];
        close(fd[1]);

        read(fd[0], buf, 1024);

        printf("-->%s\n", buf);
        
        close(fd[0]);
    } else {
        char string[] = "heaaaallo";
        close(fd[0]);

        write(fd[1], string, sizeof(string));

        close(fd[1]);
    }

    return 0;
}