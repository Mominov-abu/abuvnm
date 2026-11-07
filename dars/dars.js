// let son =1;
// for ( let i = 1 ; i <= 5 ; i++);{
// console.log(i)
// };

// let davom  =true

// while(davom){
//     let narx = +prompt("Narxni kiritin");
//     let son = +prompt("Sonini kiritin");
//     let jami = narx * son
//     console.log(jami);
//     davom = confirm("Yana hisoblaysanmi")
// }
// console.log("Dastur tugadi");

// let son = +(prompt("Son kiriting:"));

// for (let i = 1; i <= 10; i++) {
//     console.log(son + " x " + i + " = " + (son * i));
// }

let sirlison = 10; 
let son;
while (son !== sirlison){ 
son = +prompt("1 dan 20 gacha son krting:");
if (son === sirlison) {
    console.log("Togri topdingiz malades");
} else if (son < sirlison) {
    console.log("Kattaroq son oylang");
} else {
    console.log("Kichikroq son oylang");
}
}