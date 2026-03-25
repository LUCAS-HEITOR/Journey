#include <iostream> //input, output, 
#include <string>
#include <cstdlib>

int main() {
    char texto;
    std::string Hello = "Hello World!!!";

    std::cout << "Hello, World!" << std::endl;
    std::cout << Hello << std::endl;
    
    std::cout << "Wanna clear console\n 1-Yes, 2-No" << std::endl;
    std::cin >> texto;

    if (texto == '1') {
        std::cout << "Choosed Yes... Cleaning Console" << std::endl;
        system("cls");
    } else if (texto == '2') {
        std::cout << "Choosed No... Doing Nothing" << std::endl;
    } else {
        std::cout << "Not Valid..." << std::endl;
    } 

    return 0;
}

//PlaceHolder -- HandManual