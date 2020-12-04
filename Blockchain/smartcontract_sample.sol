pragma solidity 0.6.7;

contract sample{
    int num1;
    uint num2;
    string name;
    function getinput(int a,uint b,string memory c)public{
        num1=a;
        num2=b;
        name=c;
    }
    function retrieve()public view returns(int,uint,string memory){
        return(num1,num2,name);
    }
}