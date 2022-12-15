#include<iostream>
#include<string.h>
#define maxTexto 400
#define maxPatron 400


using namespace std;

void FuerzaBruta(char[], char[], int, int);
int main(void)
{
      char Patron[maxPatron];
      char Texto[maxTexto];
      int x, y;
      cout << "Ingresa el Texto:";
      cin>>(Texto);
      x = strlen(Texto);
      do {
        
                 cout <<"\nIngresa el Patron:";
                 cin >> Patron;
                 y = strlen(Patron);
      } while (y>x);
      
      FuerzaBruta(Texto, Patron, x, y);
}

void FuerzaBruta(char texto[], char patron[], int x, int y)
{
       int i,j,k, cont=0;
       char temp[100];
       for (i = 0; i <= x; i++)
       {
         
             for (j = i, k = 0; j<y; j++, k++)
                  temp[k] = Texto[i + k];
             temp[k] = '\0';
             if (strcmp(Patron, temp) == 0)
             {
                  cout << "\nLa posision es : "<< i << "\n";
                  cont++;
             }
             y++;
       }
       cout << "\n\nLas inetraciones que se hicieron fueron :"<< cont << end1;
}
