function a(){
    x=5
    function b(){
        x=4
        console.log(x)
    }
    return b
}

s=a()
console.log(s)
s()