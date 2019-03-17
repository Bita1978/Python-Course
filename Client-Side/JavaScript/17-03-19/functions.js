function getAgeByBirthYear(birthYear, currentYear) {
    return currentYear - birthYear;
}

function getAttachedString(...args) {
    return args.join(' ');
}

function getFullName(fname, lname) {

    return `${fname[0].toUpperCase()}${fname.slice(1)} ${lname[0].toUpperCase()}${lname.slice(1)}`;  
}

const myAge = getAgeByBirthYear(1989, 2019);
const stringArgs =  getAttachedString('Hi', "I'm", "Enosh" , "What", "Is" , "5");
const fullName = getFullName('enosh', 'tsur');

console.log('Age:' , myAge)
console.log('Stirng Args:' , stringArgs)
console.log('Full Name:' , fullName)