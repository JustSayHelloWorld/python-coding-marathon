/*The function filterByN receives an array of integers, a number and a parameter (greater, less). Print a new array, where all elements will be greater/less than this number

By default, the number is 0, the parameter is greater.



Example:

filterNums([-1, 2, 4, 0, 55, -12, 3], 11, 'greater');  //[ 55]

filterNums([-2, 2, 3, 0, 43, -13, 6], 6, 'less'); // [-2, 2, 3, 0, -13]

filterNums([-2, 2, 3, 0, 43, -13, 6], -33, 'less'); //  []

filterNums([-2, 2, 3, 0, 43, -13, 6]); // [2, 3, 43, 6]

filterNums([-2, 2, 3, 0, 43, -13, 6], 23);  // [43]*/

const filterNums = (nums,number=0,parameter="greater") => {
    return nums.filter(value => parameter == "greater" ? value > number:value < number);
};

const filterNums = (arr, n = 0, how = 'greater') => {
    return arr.filter(el => how == 'less' ? el < n : el > n);
}

/*The user enters as arguments the number of seconds, minutes, hours, days, weeks, months, years.
Output how many seconds are in all this.
All parameters are optional. Consider 30 days in a month

Example:

howMuchSec(12, 3); //192

howMuchSec(1, 33, 22); //81181

howMuchSec(); //0*/

const howMuchSec = (seconds=0, minutes=0, hours=0, days=0, weeks=0, months=0, years=0) => {
    return ((((((years*12+months)*30+weeks*7+days)*24)+hours)*60)+minutes)*60+seconds

}

const howMuchSec = (sec = 0, min = 0, hours = 0, days = 0, weeks = 0, months = 0, years = 0) => {
    const secIn = {
        min     : 60,
        hour    : 3600,
        day     : 86400,
        week    : 604800,
        month   : 2592000,
        year    : 31536000
    };

    return sec + min * secIn.min + hours * secIn.hour + days * secIn.day + weeks * secIn.week + months * secIn.month + years * secIn.year;
}


/*Find the maximum interval between two consecutive numbers. Numbers are entered as arguments

Example:

maxInterv(3, 5, 2, 7); //5
maxInterv(3, 5, 2, 7, 11, 0, -2); //11
maxInterv(3, 5); //2
maxInterv(3); //0*/

const maxInterv = (...values) => {

    var loop_border
    var max = 0
    if (values.length%2!=0) {
        loop_border = values.length-1
    } else {loop_border = values.length}

    if (loop_border==0) {
        return 0;
    }
    else
    {
        for (let i = 0; i <= loop_border; i++)
        {
            let temp = Find_max(values.shift(),values.shift())
            if (temp>max) {
                max = temp
            }
        }
        return max
    }


    function Find_max(first, second)
    {
        if (first>second){return first-second}
        else {return second-first}

    }


}

const maxInterv = (...nums) => {
    let interval = 0;
    for(let i = 1; i < nums.length; i++){
        const interv = Math.abs(nums[i - 1] - nums[i]);
        if(interv > interval){
            interval = interv;
        }
    }

    return interval;
}


/*The function takes any number of strings and returns the sum of their lengths.

Example:


console.log(sumOfLen('hello', 'hi')); //7
console.log(sumOfLen('hi')); //2
console.log(sumOfLen()); //0
console.log(sumOfLen('hello', 'hi', 'my name', 'is')); //16*/

const sumOfLen = (...strings) => {
   return strings.length == 0 ? 0 : strings.reduce(function myFunction(total, value, index, array) {
  return total + value;}).length;

}

const sumOfLen = (...strings) => {
    return strings.reduce((acc, el) => acc + el.length, 0);
}
