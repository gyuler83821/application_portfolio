#include <iostream>
#include <iomanip>
using namespace std;
int ktmove1[8]={-2,-1,1,2, 2, 1,-1,-2};
int ktmove2[8]={ 1, 2,2,1,-1,-2,-2,-1}; //direction
int getNumExit(int position_y,int position_x,int move_y,int move_x,int numboard,int board[8][8]){  
//get the number of exits of the next step 
	int current_y=position_y+move_y;
	int current_x=position_x+move_x;
	int sumExit=0,temp_y,temp_x;
	
	//if the next step is invalid,give it value -1 to separate them from others
	if(current_x>=numboard||current_x<0||current_y>=numboard||current_y<0||board[current_y][current_x]!=0||board[current_y][current_x]==-1){
		return -1;
	}
	
	//if the next step is valid, then count its valid exits and then return it
	for(int i=0;i<8;i++){
		temp_x=current_x+ktmove1[i];
		temp_y=current_y+ktmove2[i];
		if(temp_x<numboard&&temp_x>=0&&temp_y<numboard&&temp_y>=0&&board[temp_y][temp_x]==0){
			sumExit++;
		}
	}
	return sumExit;
}
bool output(int num){
	//to the situation which there is no nops to continue the game
	cout<<num<<":"<<endl;
	cout<<"no solution"<<endl;
	cout<<endl;
	return false; //to the later determining whether output the board 
}
int main(){	
	for(int n=1;n<=8;n++){
		bool isOutput=true;
		int board[8][8]={0};  
		int x=0,y=0;
		board[0][0]=1;  //the begining (0,0), step 1
		//initialize the board by changing blanks to -1 in this round  
		for(int set=0;set<8;set++){
			for(int inter=0;inter<8;inter++){
				if(set>=n||inter>=n)
					board[set][inter]=-1;
			}
		}
		//entering the game form
		for(int i=0;i<n*n-1;i++){
			int exit[8]={0};  //exits of 8 directions' steps
			
			for(int a=0;a<8;a++){
				exit[a]=getNumExit(y,x,ktmove1[a],ktmove2[a],n,board); //get the set of exits 
			}
			int numFalse=0;  //numFalse: number of the next steps' exits.
			//if the value is 8 ,meaning that there is no choice//
			for(int check=0;check<8;check++){
				if(exit[check]==-1){
					numFalse++;
				}
			}
			if(numFalse==8){
				isOutput=output(n); //output "no solution" and end this round
				break;
			}
			
			bool defined=false;
			int p_min;
			//find out the next position owning the least exits 
			for(int start=0;start<8;start++){
				//initialize the p_min by taking the first valid number
				if(defined==false&&exit[start]!=-1){
					p_min=start;
					defined=true;  
				}
				else if(defined==true&&exit[start]<exit[p_min]&&exit[start]!=-1){
					p_min=start;
				}
			}
			//updated x and updated y is the next step we find out
			x=x+ktmove2[p_min];
			y=y+ktmove1[p_min];
			//record the next step
			board[y][x]=i+2;
			//the next step is the last step 
			if(i+2==n*n){
				board[y][x]=n*n;
			}
		}
		if(isOutput==true){  //isOutput stands for successfully going through the disk
			cout<<n<<":"<<endl;
			for(int aa=0;aa<n;aa++){
				for(int bb=0;bb<n;bb++){
					cout<<setw(2)<<board[aa][bb]<<" ";
				}
				cout<<endl;
			}
			cout<<endl;
		}
	}
	return 0;
}


