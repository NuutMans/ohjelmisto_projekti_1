console.log('Moro)');

// taulukko array
let items = [1, 2, 3, {name: 'monke'}, [0, 1, 2], 'merkkijono'];
console.log(items);


// alkioon viitataan indeksillä
console.log(items[3]);

// alkion arvoa voidaan muuttaa indeksin avulla
items[0] = 99;
console.log(items);

// on mahdollista lisätä alkioita väliin joita ei ole määritelty
items[9] = 'Olen uusi alkio';
console.log(items);

// välissä on nyt määrittelemätön alkio ei undefined
// ei tarvitse miettiä tätä vielä
console.log(items[6]);


let fruits = ['kiwi', 'banana', 'apple', 'mango'];
console.log(fruits);
console.log('Taulukon pituus:', fruits.length);

// document on html tiedosto
let elem = document.querySelector('#hearing');
console.log(elem);
console.dir(elem);
//elem.innerText = 'mod2 esimerkki taululta'

// Taulukon looppaus eri tavoin
// perinteinen for
// yleinen tapa, tarvitaan indeksi

console.log('-------------------------');
console.log('tämä on perinteinen for-looppi');

for (let i = 0; i < fruits.length; i++) {
    console.log(`hedelmä ${i + 1} on ${fruits[i]}`);
}

// helppo ja nopea tapa iteroida ilman indeksiä
console.log('-------for-of------------------');
console.log('Läpikäynti for / of rakenteella jolla saadaan arvot');

for (let fruit of fruits) {
    console.log(fruit);
}


// harvemmin käytetään taulukoiden kanssa
// JavaScript objektien kanssa tosi hyvä
console.log('--------for-in-----------------');
console.log('Läpikäynti for /  rakenteella jolla saadaan arvot ja index');
for (const index in fruits) {
    console.log(index, fruits[index]);
}


document.querySelector('body').style.transform = "rotate(270deg)";



/*
    sort() sorts the array alphabetically
    reverse() reverses the items in the array in reverse order

 */

fruits.sort()
console.log(fruits);
fruits.reverse()
console.log(fruits);

// ei toimi numeroiden kanssa kovinkaan hyvin

const ages = [23000, 40, 63, 25, 2000];
ages.sort();
console.log(ages);

// tämä toimii numeroiden kanssa
ages.sort((a, b) => a - b)
console.log(ages);
ages.sort((a, b) => b - a)
console.log(ages);

/*

    shift() deletes and returns the 1st item in the array
    pop() deletes and returns the last item in the array
    push(value) adds the value at the end of the array, multiple values separated by commas
    includes(value) checks whether the array contains the given value


 */


let fruityys = ['kiwi', 'banana', 'apple', 'mango'];
// shift () poistetaan taulukon ensimmäinen arvo ja otetaan muuttuja talteen
const fruity = fruityys.shift();
console.log('poistettiin', fruity)
console.log(fruityys);

// unshift lisää taulukon alkuun
fruityys.unshift('mandarin');
console.log(fruityys);

// sama kuin shift mutta vika
const vika = fruityys.pop();
console.log('Poistettiin', vika)
console.log(fruityys)

fruityys.push('satsuma', 'orange');
console.log(fruityys);

// includes tarkistaa onko arvo taulukossa ja palauttaa true / false
console.log(fruityys.includes('kiwi'));

// object literal, olio
// samankaltainen kuin sanakirja pythonissa


const duck = {
    name: 'Aku',
    age: 313
}

console.log(duck);
console.log(duck[name]);
console.log(duck['name']);

// muutetaan arvoja
duck['name'] = 'Aku Ankka';
console.log(duck);

// haetaan nimi ja muutetaan nimi
console.log(duck.name);
duck.name = 'Iines Ankka';
console.log(duck);

// uusi ominaisuus
duck.profession = 'Working like a duck';
// vaihdetaan arvo
duck.profession = 'Swimming like a duck';
console.log(duck);

// tulostetaan consoleen Moikka [ankan nimi]
let sayhello = `Moikka ${duck.name}`;
console.log(sayhello);


delete duck.profession;
console.log(duck)

const duck2 = {
    name: 'Roope Ankka',
    age: 80,
    getInfo: function () {
        return this.name + ' on ' + this.age + '- vuotias;'
    }
}

let info = duck2.getInfo();
console.log(info);

// JS funktiot!!!!!!!!!!!!!!

// ns. perinteinen funktion määrittely
function greet(name) {
    const greeting = `Moikka ${name}`
    console.log();
    return greeting
}

console.log(greet('VALEEEEEEEEEEEEEEEE'));

// arrow / nuolifunktio, edellistä yksinkertaisempi
// uudempi ja modernimpi tapa käyttää funktioita
// voidaan kirjoittaa yksirivisen, tällä ei palauteta
// käyttämällä return sanaa


const nuoliFunktio = () => {
    console.log('Ollaan nuolifunktiossa');
};
nuoliFunktio();

const quadraticSum = (a, b) => (a + a + b + b);
console.log(quadraticSum(3, 8));

// foreach voidaan iteroida taulukon jäsenet läpi

const numerot = [52, 73, 76, 78, 91, 26, 35];
numerot.forEach((num, index) => {
    console.log(`Indeksi on ${index}, arvo on ${num}`);
});