#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <map>

using namespace std;

map<string,int> tab;

int checkGame (string d, string l, string p)
{
    vector<int> jok;
    jok.assign(3,0);
    jok[tab[d]]++; jok[tab[l]]++; jok[tab[p]]++;
    // Empate
    if (jok[0] == jok[1] && jok[1] == jok[2] ) return 0;
    if (jok[0] == 3) return 0;
    if (jok[1] == 3) return 0;
    if (jok[2] == 3) return 0;
    if (jok[0] == 2 && jok[1] == 1) return 0;
    if (jok[1] == 2 && jok[2] == 1) return 0;
    if (jok[2] == 2 && jok[0] == 1) return 0;
    // Dodo
    if (d == "papel" && jok[1] == 2) return 1;
    if (d == "pedra" && jok[2] == 2) return 1;
    if (d == "tesoura" && jok[0] == 2) return 1;
    // Leo
    if (l == "papel" && jok[1] == 2) return 2;
    if (l == "pedra" && jok[2] == 2) return 2;
    if (l == "tesoura" && jok[0] == 2) return 2;
    // Pepper
    if (p == "papel" && jok[1] == 2) return 3;
    if (p == "pedra" && jok[2] == 2) return 3;
    if (p == "tesoura" && jok[0] == 2) return 3;

    return -1;
}

int main ()
{
    string d, l, p;
    tab["papel"] = 0; tab["pedra"] = 1; tab["tesoura"] = 2;

    while (cin >> d >> l >> p)
    {
        int victory = checkGame(d,l,p);
        switch (victory)
        {
            case 0: cout << "Putz vei, o Leo ta demorando muito pra jogar..." << endl;
                    break;
            case 1: cout << "Os atributos dos monstros vao ser inteligencia, sabedoria..." << endl;
                    break;
            case 2: cout << "Iron Maiden's gonna get you, no matter how far!" << endl;
                    break;
            case 3: cout << "Urano perdeu algo muito precioso..." << endl;
                    break;
        }
    }
    return 0;
}