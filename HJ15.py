while True:
    try:
        num = int(input())
        print(str(bin(num)).count('1'))
    except:
        break

# C++ version
# #include<iostream>
# using namespace std;
# int main(void){
#     int a, num;
#     num=0;
#     cin>>a;
#     while(a>=1)
#     {
#         if (a % 2 == 1) num++;
#         a = a/2;
#     }
#     cout<<num;
#     return 0;
# }
