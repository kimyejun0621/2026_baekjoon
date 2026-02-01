#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(){
    ios::sync_with_stdio(0); // 정상 작동
    cin.tie(0);
    
    int T;
    cin >> T;


    while(T--){
        stack<char> st;
        bool is_valid = true;

        string s;
        cin >> s;

        for(char c : s){
            if(c == '('){
                st.push(c);
            }
            else{
                if(st.empty()){
                    is_valid = false;
                    break;
                }
                st.pop();
            }
        }

        if(is_valid && st.empty()){
            cout<< "YES\n";
        }
        else{
            cout <<"NO\n";
        }
        
    }

    return 0;
}


