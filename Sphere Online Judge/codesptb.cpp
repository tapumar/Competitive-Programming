#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
int a[200001];
int te[200001];
unsigned long long merge(int arr[],int temp[],int left,int mid,int right)
{
    int i=left;
    int j=mid;
    int k=left;
    unsigned long long int icount=0;
    while((i<=mid-1) && (j<=right))
    {
        if(arr[i]<=arr[j])
        temp[k++]=arr[i++];
        else
        {
            temp[k++]=arr[j++];
            icount+=(mid-i);
        }
    }
    while(i<=mid-1)
    temp[k++]=arr[i++];
    while(j<=right)
    temp[k++]=arr[j++];
    for(int i=left;i<=right;i++)
    arr[i]=temp[i];
    return icount;
}
unsigned long long int mergesort(int arr[],int temp[],int left,int right)
{
    unsigned long long int i=0;
    if(right>left){
        int mid=(left+right)/2;
        i=mergesort(arr,temp,left,mid);
        i+=mergesort(arr,temp,mid+1,right);
        i+=merge(arr,temp,left,mid+1,right);
    }
    return i;
}
int main()
{
    int t,n;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
        }
        printf("%llu\n",mergesort(a,te,0,n-1));
    }
    return 0;
}
