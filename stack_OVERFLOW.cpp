#include <iostream>

using namespace std;

int foo(){
	cout<<"Hello, Sergey "<<endl;
	return 2;
}

int test(){
	int *m[1];
	m[3]=(int *) &foo;
	return 1;
}

int main(){
	test();
	return 0;
}

