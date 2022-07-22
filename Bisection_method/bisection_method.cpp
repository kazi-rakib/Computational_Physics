#include <iostream>
#include <cmath>

using namespace std;

// global variable for the co-efficients of the equation
double a, b, c, d, epsilon;

// initialize the global variable for a given equation
// Complexity: O(1)
void equation(double p, double q, double r, double s, double precision=1e-15){
  a = p;
  b = q;
  c = r;
  d = s;
  epsilon = precision;
}

// Complexity: O(1)
double solveFor(double x){
  // solve for an specific value
  double result = (a*x*x*x + b*x*x + c*x + d);

  return result;
}

/** BISECTION METHOD
 * Actual algorithm has been implemented here.
 * 
 * complexity: O(n)
 * 
*/
double solve(){
  // range
  double L = -abs(a*d);
  double R = abs(a*d);

  // Bisect the range [L, R]
  double X = (L+R)/2;

  // precision has already been set when initialized

  // Number of steps required
  int steps = log(abs(a*d)/epsilon)/(log(2));
	steps = int(steps)+1;
  
  for(int i = 0; i < steps; i++){
    
    if( solveFor(X) > 0.0 ){
			// look for root in the first half
			R = X;
    }
		else{
			// look for root in the last half
			L = X;
    }

    // bisection
		X = (L+R)/2;
  }
  
  return X;
}

int main(void){

  equation(1, 0, -2, -5);
  cout<<"Solution, X = "<<solve()<<endl;

  cout<<"\n\nPlease input the co-efficients of the desired equation:\n\n";

  cin>>a;
  cin>>b;
  cin>>c;
  cin>>d;

  cout<<"Solution, X = "<<solve()<<endl;

  return 0;
}
