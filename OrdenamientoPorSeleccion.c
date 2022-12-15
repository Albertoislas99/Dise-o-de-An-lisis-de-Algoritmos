#include <studio.h>

int main(){
  
  int num []={43, 32, 45, 54, 21};
  int aux, min;
  
  for(int i = 0 ;i < 5; i++){
    min = i;
    for(int j = i+1; j < 5; j++){
       if (num[j] < num[min]){
          min = j;
       }
    }
    aux = num[i];
    num[i] = num[min];
    num[min] = aux;
  }
  printf("El orden es:");
  for(int i = 0 ;i<5; i++){
    printf("%i", num[i]);
  }
} 
