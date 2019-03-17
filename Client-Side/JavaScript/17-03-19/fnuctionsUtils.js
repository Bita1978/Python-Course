function doWithName(fn) {
    
    return function newFunciton(name) {
        return fn(name);
    }
}

function consoleHi(name) {
    console.log(`Hi ${name}`);
}

function consoleBye(name) {
    console.log(`Bye ${name}`);
}

const consoleHiName = doWithName(consoleHi);
const consoleByeName = doWithName(consoleBye);

consoleHiName('Enosh');
consoleByeName('Enosh');


