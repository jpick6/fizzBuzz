1 /**
2  * Javon Pickett
3  * python.com
4  *
5  * Output the intergers from 1 to 100.
6  *    For each multiple of three, print 'Fizz'.
7  *    For each multiple of five, print 'Buzz'.
8  *    For a multiple of both three and five, print 'FizzBuzz'.
9  */


   for(var i=1; i<101;i++){
       var multipleOfThree = i % 3 === 0;
       var multipleOfFive = i % 5=== 0;
       if(multipleOfThree && multipleOfFive){
           console.log("FizzBuzz");

        }
       else if(multipleOfThree) {
           console.log("Fizz");
        }
       else if (multipleOfFive) {
           console.log("Buzz");
        }
       else {
           console.log(i);
        }
}

    
