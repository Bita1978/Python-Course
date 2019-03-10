const friends = ['Elly', 'Itay', 'Yaniv', 'Leon', 'Zack', 'Yaniv2'];

// for (let i = 0; i < friends.length; i++) {
//     console.log(friends[i]);
// }

// for(let name of friends) {
//     console.log(name);
// }


let quit = false;
let counter = 0;


// while(!quit) {
//     console.log(counter);
//     counter++;
//     quit = counter === 10 ? true : false;
    
// }


const range = (fn) => (start, end) => {
    for(let i = start; i < end; i ++) {
        fn(i)
    }
}

const logIt = i => console.log(i);

const consoleRange = range(logIt);



consoleRange(1, 3895700);


// friends.forEach( x => console.log(x));