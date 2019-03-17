const pipe = (fn1, fn2, fn3) => (str) => fn1(fn2(fn3(str)));

const consoleIt = x => console.log(x);

const toUpper = str => str.toUpperCase();
const toRevese = str => str.split("").reverse().join("");

function a() {
    return 'a'
}

const consoleUpperReversed = pipe(consoleIt, toRevese, toUpper);

consoleUpperReversed("adg jasdg jhasgd jgd asjdg asjdg asdjgas ");


