#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;



int main(){

    ifstream i_stream("playData.csv");
    ofstream o_stream("newdata.csv");

    string stuff;

    while(!i_stream.eof()){
        getline(i_stream,stuff);
        cout << stuff << "\n";
    } 

    i_stream.close();

    return 0;
}