'''
function decryptStirng (strVal) {
var strArr = strVal.split("");
var final = "";
for (var i in strArr){
final += String.fromCharCode(strArr[i].charCodeAt(0) - i);
}
console.log(final);
}

decryptStirng("23f<957h");

program created to decrypt a string and solve the 6th excersice in www.hackthissite.org
'''

def decrypt_string(string):
