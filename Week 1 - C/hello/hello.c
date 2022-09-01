# include <stdio.h>
# include <cs50.h>

int main(void)
{
    // Get user's name and output it 
    string name = get_string("What is your name? ");
    printf("hello, %s\n", name);
}