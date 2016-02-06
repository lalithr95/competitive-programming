#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
 
// A O(n^2) function to find sum of all sub-squares of size k x k
// in a given square matrix of size n x n
int printSumTricky(int **mat, int k, int n)
{
   // k must be smaller than or equal to n
   if (k > n) return 0;
 
   // 1: PREPROCESSING
   // To store sums of all strips of size k x 1
   int stripSum[n][n];
    vector<int> final;
   // Go column by column
   for (int j=0; j<n; j++)
   {
       // Calculate sum of first k x 1 rectangle in this column
       int sum = 0;
       for (int i=0; i<k; i++)
          sum += mat[i][j];
       stripSum[0][j] = sum;
 
       // Calculate sum of remaining rectangles
       for (int i=1; i<n-k+1; i++)
       {
            sum += (mat[i+k-1][j] - mat[i-1][j]);
            stripSum[i][j] = sum;
       }
   }
   // 2: CALCULATE SUM of Sub-Squares using stripSum[][]
   for (int i=0; i<n-k+1; i++)
   {
      // Calculate and print sum of first subsquare in this row
      int sum = 0;
      for (int j = 0; j<k; j++) {
        final.push_back(sum);
           sum += stripSum[i][j];
      }
 
      // Calculate sum of remaining squares in current row by
      // removing the leftmost strip of previous sub-square and
      // adding a new strip
      for (int j=1; j<n-k+1; j++)
      {
        final.push_back(sum);
         sum += (stripSum[i][j+k-1] - stripSum[i][j-1]);

         
      }
      for(int i =0;i<final.size();i++)
        cout<<final[i]<<" ";
      
   }
   // if(k==2) {
   //    int sum_f;
   //    for(int i=0;i<final.size();i++) {
   //      sum_f += final[i];

   //    }
   //    return sum_f;
   // }
   int max = 0;
   for(int i=0;i<final.size();i++) {
    if(final[i]>max) {
      max = final[i];
    }
   }
   return max;
}
 
// Driver program to test above function
int main()
{
    int t;
    cin>>t;
    int xt = 0;
    while(t--) {
      int n,k,c,x;
      cin>>n;
      cin>>k;
      cin>>c;
      cin>>x;
      std::vector<int> v;
      int *a = new int[n];
      int *b = new int[n];
      int i=0,j=0;
      for(i=0;i<n;i++) {
        cin>>a[i];
      }
      for(i=0;i<n;i++) {
        cin>>b[i];
      }
      int **matrix;
      matrix = new int*[n];
      for(i=0;i<n;i++) {
        matrix[i] = new int[n];
      }
      for (i=0;i<n;i++)
      {
        for(j=0;j<n;j++){
          matrix[i][j] = (a[i]*(i+1) + b[j]*(j+1) + c)%x;
        }
      }
    // int final = printSumTricky(matrix, k, n);
    // cout<<"case #"<<xt+1<<": "<<final<<endl;
    // xt++;
    int dir = 0;
    int m,l,p=0,q=0;

      int max;
      for(m=0;m<=n-k;m++) {
      for(l=0;l<=n-k;l++) {
        max = matrix[p][q];
        for(i=p;i<p+k;i++){
          for(j=q;j<q+k;j++){
            if(matrix[i][j]>max){
              max = matrix[i][j];
            }
          }
        }
        v.push_back(max);
        q++;

      }
      p++;
      q=0;
    }
     int max1 = 0;
   for(int i=0;i<v.size();i++) {

      max1 += v[i];

   }   
  cout<<"case #"<<xt+1<<": "<<max1<<endl;
 xt++;



    


  }
    return 0;
}