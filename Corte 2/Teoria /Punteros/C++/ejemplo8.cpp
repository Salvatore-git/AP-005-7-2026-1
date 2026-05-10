#include <iostream>

int* crearNumeroIncorrecto() {
    int x = 50; // Variable local en el Stack
    return &x;  // ERROR: x deja de existir al salir de la función
}

int main() {
    int* p = crearNumeroIncorrecto();

    // Esto es peligroso y probablemente imprima basura o cause un crash
    std::cout << "Valor = " << *p << std::endl;

    return 0;
