#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while - Infinite loop for parent process
 *
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Displays zombie process
 *
 * Return: always 0
 */
int main(void)
{
	pid_t child_pid;
	int k;

	for (k = 0; k < 5; k++)
	{
		child_pid = fork();

		if (child_pid == -1)
		{
			perror("Fork failed");
			exit(EXIT_FAILURE);
		}
		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
