#include <iostream>
using namespace std;

void calculateTimes(int process[],int n, int at[], int bt[]){
    cout<<"Process\tAT\tBT\tCT\tTAT\tWT\n";
    int ct[5], tat[5], wt[5]={0};
    ct[0]=at[0];
    for(int i=0;i<n;i++){
        if(i==0)
            ct[i] = at[i]+bt[i];
        else
            ct[i]= max(ct[i-1],at[i])+bt[i];
        tat[i] =ct[i]-at[i];
        wt[i]=tat[i]-bt[i];
        cout<<process[i]<<"\t"<<at[i]<<"\t"<<bt[i]<<"\t"<<ct[i]<<"\t"<<tat[i]<<"\t"<<wt[i]<<"\n";
    }
}

int main(){
    int process[]={1,2,3,4,5};
    int n=5;
    int at[]={0,1,2,3,4};
    int bt[]={4,3,1,2,5};
    calculateTimes(process,n,at,bt);
    return 0;
}