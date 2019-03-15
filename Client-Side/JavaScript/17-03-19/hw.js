// Task 1

const name = 'Gil';
const age = 28;
const isCool = true;
const friends = ['liat', 'dana', 'efrat', 'oded', 'amos', 'nimrod'];

console.log(`Name: ${name}\nAge: ${age}\nIs cool: ${isCool}\nFriends: ${friends}`);

// Task 2
const person = {
    name,
    age,
    isCool,
    friends
}

for (const value of Object.values(person)) {
    console.log(value)
}

for (const friend of person.friends) {
    console.log(friend);
}

// Task 3
const pFriends = person.friends;

for (let i = 0; i < pFriends.length; i++) {
    if (pFriends[i].toLowerCase().startsWith('a')) {
        console.log(pFriends[i]);
    } else {
        continue;
    }
}

for (let i = 0; i < pFriends.length; i++) {
    pFriends[i].toLowerCase().startsWith('a') && console.log(pFriends[i]);
}

// Task 4
for (const fr of pFriends) {
    fr === 'liat' ? console.log('hi liat') :
        fr === 'dana' ? console.log('hi dana') :
            fr === 'efrat' ? console.log('hi efrat') :
                fr === 'oded' ? console.log('bye oded') :
                    fr === 'amos' ? console.log('hi amos') :
                        fr === 'nimrod' ? console.log('hi nimrod') :
                            console.log(`whor are you ${fr}??`);
}

for (const fr of pFriends) {
    switch (fr) {
        case 'liat':
            console.log('hi liat');
            break;
        case 'nimrod':
        case 'efrat':
            console.log('So cool...');
            break
        case 'oded':
            console.log('why oded?');
        default:
            console.log(`${fr} not familiar...`)

    }
}

