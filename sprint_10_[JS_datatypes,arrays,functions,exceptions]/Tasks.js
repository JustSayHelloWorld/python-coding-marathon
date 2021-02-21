/*
Implement the modifyArray(array) function, which takes an arbitrary array, changes the value of the first element of the array to “Start”, the last element of the array to “End” and returns the modified array.

Function example:
modifyArray([12, 6, 22, 0, -8])); // [‘Start’, 6, 22, 0, ‘End’]

* For correct passing of all tests don't use console.log() method in your code.
*/

/* and end with */

function modifyArray(array) {
   array[0]="Start";
   array[array.length-1]="End";
   return array;
}

/*
Write a function combineArray(arr1, arr2), which takes 2 arrays, and returns a new array consisting only of numeric elements of arrays arr1 and arr2.

Function example:
combineArray([12, "User01", 22, true, -8], ["Index", 6, null, 15]));  // [12, 22, -8, 6, 15]

* For correct passing of all tests don't use console.log() method in your code.
*/

function combineArray(arr1, arr2) {
    let check = function (value, index, array)
    {
    return typeof value == "number";
    }
    return arr1.filter(check).concat(arr2.filter(check))

}

/*
Implement the longestLogin(loginList) function, which takes an array of user logins loginList  and returns the longest login. If the logins of the same length are the longest in the array, the login element with the largest index is returned. Tip: You can use the reduce() method to solve the task.

Function examples:
longestLogin(["serg22", "tester_2", "Prokopenko", "guest"]);   //  Prokopenko
longestLogin(["user1", "user2", "333", "user4", "aa"]);   //  user4

* For correct passing of all tests don't use console.log() method in your code.
*/

function longestLogin(loginList) {

    return loginList.reduce(function(longest, currentWord) {
    if(currentWord.length >= longest.length)
       return currentWord;
    else
       return longest;
  })

}

/*
Implement the processArray(arr, factorial) function, which takes the first parameter of the array arr, and the second parameter the function factorial and processes each element of the array arr with the function factorial, returning a new array (the source array arr does not change)
The function factorial(n) calculates and returns the factorial of the number n. For example factorial(4) returns 24.

Example
// determines the factorial of the number n
function factorial(n) { // your code};
processArray([1, 2, 3, 4, 5], factorial); // [1, 2, 6, 24, 120]

* For correct passing of all tests don't use console.log() method in your code.
*/

function factorial(n) {
    if(n === 0) {
        return 1
    } else {
        return n*factorial(n-1);
    }

}


function processArray(arr, factorial) {
   return arr.map(function(el){return factorial(el)});
}

/*
Write a checkAdult(age) function whose input parameter is the age of the user age. The function checks whether the set age parameter is set correctly, if it is set incorrectly, the corresponding error should be generated and displayed in the console:

- if the age value has not been set, you need to create the following error: "Please, enter your age",

- If you set a negative age value, you need to create the following error: "Please, enter positive number",

- if a non-numeric value of age was specified, you need to create the following error: "Please, enter number",

- if the integer value of age was not specified, you need to create the following error: "Please, enter Integer number",

- If the user is under 18, you need to create the following error: "Access denied - you are too young!".

If there is no error, the message “Access allowed” is displayed in the console.

In the function, implement the handling of possible exceptions, providing the output to the console of the name and description of the error.

Regardless of whether the age parameter was set correctly or incorrectly, the message “Age verification complete” should be displayed at the end of the test.



Function usage example:
checkAdult(15);
// Error Access denied - you are too young!
// Age verification complete

checkAdult(25);
// Access allowed
// Age verification complete
*/

function checkAdult(age){
    try {
    if (typeof age == "undefined")
    {
        throw Error("Please, enter your age");
    }
    else
    {
        if (typeof age != "number")
        {
            throw Error("Please, enter number");
        }
        else
        {
            if (age<0)
            {
                throw Error("Please, enter positive number");
            }
            else
            {
                if (!Number.isInteger(age))
                {
                    throw Error("Please, enter Integer number");
                }
                else
                {
                    if (age<18) {throw Error("Access denied - you are too young!");}
                }
            }

        }

    }
    console.log("Access allowed");



    }
    catch (exception) {
        console.log(exception.name +" "+ exception.message);
    }
    finally{
        console.log("Age verification complete");
    }

}