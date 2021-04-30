//imports

// valor de comparação = 0

//Thread Pai:
//Está sempre funcionando e pode interromper a thread filho
// o que faz: fica convertendo os áudios em string e procurando por uma palavra-chave
// encontrou a palavra chave => valor de comparação = 1

//Thread Filho:
// é chamada quando o valor de comparação é igual a 1.
// chama execução do main.py