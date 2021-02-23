/*Implement the getMin(arr) function, which takes an array of numbers arr and returns the smallest number of the array.
To solve the problem, you must use one of the methods to specify the context of this. It is forbidden to use any cycles.
*/
function getMin(arr) {
    return Math.min(...arr)
}

/*The product() function finds the product of an arbitrary number of arguments. You must specify the desired execution context for the product() function by implementing a new getProduct() function bound to the context of the object, which takes 2 additional arguments.
The value of the 1st additional parameter is 2, the value of the 2nd additional parameter is 3. The object in the context of which the product() function is called has 1 property.
*/

const product = function() {
    return [].reduce.call(arguments, function(res, elem) {
      return res * elem;
    }, this.product);
};

const contextObj = {product: 10}

const getProduct = product.bind(contextObj,2,3);

/*Create a Movie class, the constructor of which accepts 3 parameters: movie name name, movie genre category and start year of startShow.
The class has a watchMovie() method that returns a phrase and adds a movie name name parameter to it at the end. For example, "I watch the movie Titanic!"
Create an instance of the movie1 class with the title of the movie "Titanic", the genre "drama" and 1997 release.
Create an instance of the movie2 class with the title of the movie "Troya", the genre "historical" and the 2004 release.

* For correct passing of all tests don't use console.log() method in your code.

*/
const Checker = require('./Checker.js');

class Movie {
    constructor(name, category, startShow) {
    this.name = name;
    this.category = category;
    this.startShow = startShow;
  }

  watchMovie() {
    return "I watch the movie "+this.name+"!";
  }
}

let movie1 = new Movie("Titanic", "drama", 1997);
let movie2 = new Movie("Troya", "historical", 2004);

/*
Implement the Student class, the constructor of which accepts 2 parameters fullName - the name and surname of the student, direction - the direction in which he studies.

Create a showFullName() method that returns the student's first and last name.

Create a nameIncludes(data) method that, using the showFullName() method, checks for the text data argument in the student’s name and returns true if a match is found or false if not found.

Create a static studentBuilder() method that returns a new instance of the class named ‘Ihor Kohut’ and the direction ‘qc’.

Create a getter and setter direction() to read and specify the direction field.

Create an instance of class stud1 named 'Ivan Petrenko' and direction 'web'.

Create an instance of class stud2 named 'Sergiy Koval' and direction 'python'.

Create an instance of the stud3 class named ‘Ihor Kohut’ and the direction ‘qc’ using the static studentBuilder() method.



Usage example:

const stud1 = new Student('Ivan Petrenko', 'web');

stud1.nameIncludes('Ivan');   // true

stud1.nameIncludes('Denysenko'); // false
*/

const Checker = require('./Checker.js');

class Student {

    constructor(fullName, direction) {
      this._fullName = fullName;
      this._direction = direction;
    }

    showFullName() {
        return this._fullName;
    }

    nameIncludes(data) {
        return this.showFullName().includes(data);

    }

    get direction() {
        return this._direction;

    }

    set direction(value) {
        this._direction = value;
    }

    static studentBuilder() {
        return new Student("Ihor Kohut","qc");
    }
}

const stud1 = new Student('Ivan Petrenko', 'web');
const stud2 = new Student('Sergiy Koval', 'python');
const stud3 = Student.studentBuilder();


/*Write a mapCreator(keys, values) function that takes two arrays of equal length. Using these arrays, the function must create an object of type Map, the keys of which are the values from the first array keys, and the values of Map - the values from the second array values. Moreover, the values of the map elements can be only string values. The function returns this Map object.

Usage example:
const map = mapCreator([1, 2, 3, 4, 5, 6, 7],["Lviv", "Rivne", "Kyiv", "Dnipro", "Kharkiv", "Chernivtsi", "Ivano-Frankivsk"]);
map.size;  // 7
map.get(1); // Lviv

const map2 = mapCreator([1, 2, 3, 4, 5, 6, 7], ["Lviv", 23, "Kyiv", "Dnipro", "Kharkiv", "Chernivtsi", true]);
map2.size;  // 5
map2.get(2);  // undefined
*/

function mapCreator(keys, values) {
   let map_object = new Map();
   let iterator = 0;
   for (let value of values) {


           if (typeof value == "string") {
               map_object.set(keys[iterator], value)
           }
           iterator++


   }


   return map_object
}
