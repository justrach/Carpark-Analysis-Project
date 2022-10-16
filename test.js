

//Data that needs to change randomly (add noise)

//inputs are [1,x] -

const x = Math.random()
// console.log(x)

const testData1 = [1, 2, 3, 4, 5, 6, 7];

const jitteredData1 = jitterData(testData1, -1, 1);

// console.log(    Math.random()*4);

//let value of item be min and max bound

//list of output data

// let randomVal2 = Math.random()

// function isItSmaller(range,bound){
//     // let item = Math.random()*bound
//     while(range<bound){
//         Math.random()*bound
//     }
// }

function getRandomInt(max) {
    return (Math.random() * max);
  }

// console.log(getRandomInt(10))  
  
function randomBounder(minBound,maxBound){
    const rangeValues = maxBound- minBound
    //to create a list of values to output


    return minBound+ getRandomInt(rangeValues)

    // for x in range(4,5)


}

console.log(randomBounder(4,5))


// // console.log(randomVal2*-3)
// function randomBounder(minBound,maxBound){
//     //to create a binder
//     // Minimum number is a 


//     range2 = Math.random()* maxBound

//     // if(range1<minBound){
        
//     //     range1 = Math.random()*minBound
//     // }
//     if(range2>maxBound){
//         while(range2>maxBound){
//             range2 = Math.random()*maxBound
//         }

//     }


// }


// console.log(randomBounder(3,4))




for(let x; x<testData1.length;x++){
//go through data
// add a numerical value to the data
}
// Outputs:
// [0, 3, 4, 3, 5, 7, 8];
function jitterData(data, minBounds, maxBounds) {
  // TODO
}


// output is [jitterd data]


// add random noise to the data
