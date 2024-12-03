#include <iostream>

using namespace std;

void print(int a[9][9]){
  for(int i=0;i<9;i++){
   for(int j=0;j<9;j++)
     cout<<a[i][j]<<" ";
   cout<<endl;  
  }
}

bool isPossible(int a[9][9],int i, int j, int k){
   for(int u=0;u<9;u++){
      if(a[i][u]==k || a[u][j]==k)
        return false;
   }

   for(int l=3*(i/3);l<3*(i/3+1);l++){
    for(int h=3*(j/3);h<3*(j/3+1);h++)
        if(a[l][h]==k)
        return false;
   }

   return true;
}

bool sudoku(int a[9][9]){
    for(int i=0;i<9;i++)
     for(int j=0;j<9;j++)
      if(a[i][j]==0){
        for(int k=1;k<=9;k++){
            if(isPossible(a,i,j,k)){
                a[i][j]=k;
                if(sudoku(a))
                return true;
                a[i][j]=0;
            }
        }
        return false;
      }
      return true; 
}


int main(){

    int a[9][9]={
    {5, 3, 0, 6, 0, 0, 9, 0, 2},
    {0, 7, 2, 0, 9, 5, 0, 0, 8},
    {1, 9, 0, 0, 4, 0, 5, 0, 7},
    {0, 5, 9, 0, 6, 1, 0, 2, 0},
    {4, 0, 0, 0, 5, 0, 0, 9, 1},
    {7, 1, 3, 9, 2, 4, 0, 5, 6},
    {9, 0, 0, 5, 0, 7, 0, 8, 4},
    {0, 8, 0, 4, 1, 9, 0, 0, 5},
    {0, 4, 5, 0, 8, 0, 1, 7, 0}
};

if(sudoku(a))
print(a);

else
cout<<"Invalid Sudoku";

}