#include <bits/stdc++.h>
using namespace std;

struct Result{
    char* output[100];
};
Result res;
void autocorrect(char *input1,char *input2)
{
    int str_length = 0;

    string s1 = input1;
    string s2 = input2;

    unsigned int ptr = 0;
    int cur =0;
    while(ptr<s1.size())
    {
        string temp;

        while(ptr<s1.size() && s1[ptr]!=' ')
        {
            temp.push_back(s1[ptr]);
         
            ptr++;
        }
        if(temp.substr(0,s2.size()) == s2 )
        {
            // char a[temp.size()+1];
            // strcpy(a,temp.c_str());
            // mine[]
            // res.output[cur++]= &a[0];
            res.output[cur] = (char* )malloc(10);
            strcpy(res.output[cur],temp.c_str());
            cur++;
            
        }
        // cout<<res.output[0]<<" "<<0<<"\n";
        ptr++;
    }
    
}
int main() 
{
    #ifndef ONLINE_JUDGE
    // for getting input from input.txt
    freopen("input.txt", "r", stdin);
    // for writing output to output.txt
    freopen("output.txt", "w", stdout);
    #endif
    char input1[1000],input2[100];
    cin.getline(input1,1000);
    cin.getline(input2,100);
    autocorrect(input1,input2);
    for(int i=0;i<100;i++){
    cout<<res.output[i]<<"\n";
    }
}
