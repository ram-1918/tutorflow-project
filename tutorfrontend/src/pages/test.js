function calcTime(d){
    var today = new Date();
    var milli = today - d;
    console.log(today, d)
    console.log('total seconds', milli, Math.floor(milli / (24*60*60*1000)));

}
var d = new Date(2023, 5, 8);
calcTime(d);