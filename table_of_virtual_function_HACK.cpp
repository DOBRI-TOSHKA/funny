#include <iostream>

using namespace std;


struct Cls {
    Cls(char c, double d, int i):c(c),d(d),i(i){}
private:
    char c;
    double d;
    int i;
};

char &get_c(Cls &cls) {
    return  *((char*)(&cls));
}

double &get_d(Cls &cls) {
    return *((double*)(&cls)+sizeof(Cls)/(sizeof(double))-2);
}

int &get_i(Cls &cls) {
    return *((int*)(&cls)+2*(sizeof(double))/sizeof(int));
}

int main(){

    Cls ob('H',3.14,8);
    cout<<get_c(ob)<<endl;
    cout<<get_d(ob)<<endl;
    cout<<get_i(ob)<<endl;

    return 0;
}
