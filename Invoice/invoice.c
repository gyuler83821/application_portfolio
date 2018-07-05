#include "final.h"
#include <stdio.h>
int bonus_array[9]={0,0,200,1000,10000,40000,200000,2000000,10000000};
int check_bonus(string)
char string[];
{
    int i,k,max=0;
    if(strcmp(string,s1000w)==0)
        return bonus_array[8];
    else if(strcmp(string,s200w)==0)
        return bonus_array[7];
    else if(strcmp(string,h20w)==0)
        return bonus_array[6];
    for(k=0;k<H20;k++){
    	for(i=0;7-i>=0;i++){
	        if(h20w[k][7-i]!=string[7-i]){
	        	break;
			}
	    }
	    if(i<=2){
    		continue;
		} 
    	else
    	    max=bonus_array[i-1];
	} 
    for(k=0;k<E200;k++){
    	for(i=0;i<3;i++){
    		if(string[7-i]!=e200[k][2-i])
    	             break;
		}
		if(i==E200){
		    if(200>max)
			max=200;
		}	
    }
    return max;
}
main(){
    int i,j,k,num=0;
    char mag[9];
    int is_end,money=0;
    char origin[100];
    p1=fopen("final_data","r");
    p2=fopen("output","w");
    while(1){
        is_end=fscanf(p1,"%s",origin);
        if(is_end!=1 || origin[0]=='.')
            break;
        if(strlen(origin)!=8)
            continue;
        for(i=0;i<8;i++){
            if(isdigit(origin[i])){
                tmp[i]=origin[i];
                continue;
            }
            break;
        }
        if(i!=8)  continue;
        for(i=0;i<num;i++){
            if(strcmp(tmp,data[i])==0)
                break;
        }
        if(i!=num){
	    continue; /* same  */
	}  
	strcpy(data[num],tmp);
        money+=check_bonus(tmp);
	num++;

    }
    printf("money:%d\n",money);
    fprintf(p2,"%d\n",money);
}
