#include <iostream>
#include <limits>
#include <chrono>
#include <random>
#include <cmath>
#include <iomanip>

int main()
{
    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    std::default_random_engine gen (seed);
    std::uniform_real_distribution<double> dist (0.0, 1.0);

    double x = 0.0;
    double y = 0.0;

    std::size_t n = 0;
    std::size_t N = 10000000;

    for(std::size_t i = 0; i < N; ++i){

        x = dist(gen);
        y = dist(gen);

        if(std::sqrt( pow(x - 0.5 , 2) + pow(y - 0.5 , 2)) <= 0.5){

            ++n;
        }
    }

    std::cout << "Lim  pi = " << std::setprecision(15) << 4.0 * n / N << std::endl;
    std::cout << "True pi = " << std::setprecision(15) << 3.1415926535897932 << std::endl;

    return 0;
}
