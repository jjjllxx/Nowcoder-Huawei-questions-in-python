while True:
    try:
        string1 = input()
        num = string1.count(' ')
        print(len(string1.split(' ')[num]))
    except:
        break

# C++ code
# #include<iostream>
# using namespace std;
# int main(){
#     string s;
#     while(cin>>s);
#     cout<<s.size();
#     return 0;
# }
