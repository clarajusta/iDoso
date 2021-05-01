#include <python2.7/Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <pthread.h>
#include <unistd.h>

void *thread_function(void *arg);

//ver como receber e utilizar argumentos de outros lugares e usar na função

int main(bool argc)
{
pthread_t a_thread;
void *thread_result;
//colocar aqui: se o arg = 1 , criar a thread, senao roda 
system("python main.py");
printf("Criando a thread\n");
if(argc == true){
    pthread_create(&a_thread, NULL, thread_function, NULL);
}
else if(argc == true){
    //se ouvir a palavra-chave no meio da função, interromper a função
    pthread_cancel(a_thread);
}
}

void *thread_function(void *arg)
{
    printf("Dentro da Thread\n");
    system("python main.py");
    pthread_exit(0);
}