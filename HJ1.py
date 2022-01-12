"""
File: HJ1.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2022-01-13 00:48:27
Function:


"""
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