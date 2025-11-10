/* tämä on monen rivin kommentti
Tässä tiedostossa on ensimmäisiä JavaScript-esimerkkejä
 */

//Tämä on yhden rivin kommentti


'use strict'; // Muista käyttää aina tiedoston alussa

// Käytä const-avainsanaa muuttujan esittelyyn paitsi jos sen arvoa
// tarvitsee myöhemmin muuttaa, silloin käytä let-avainsanaa
// älä käytä var-avainsanaa, koska se on vanhentunut tapa

let teksti = 'Moi maailma!'

console.log(teksti)
teksti = 'Moi Joku!';

//alert('Kukkuu!');

document.querySelector('.output').textContent = teksti;

let name = 'Alex';
let age = 23
let greeting = `Moi ${name}, ${age}`; // backspacen vieressä oleva hipsu.
// Ei ole hyvä käytäntö koodata stringin sisään
console.log(greeting);

// syötteen lukeminen
//name = prompt('Anna nimesi');
//console.log('käyttäjän syöte', userInput);
//age = parseInt(prompt('Anna ikäsi:'));

if (10 < age && age < 100) {
    greeting = `Moi ${name}, ikäsi vuoden päästä ${age} v!`;
    document.querySelector('.output').textContent = greeting;

} else {
    console.log('Olet liian nuori tälle sivulle.');
}


// age = parseInt(age); // tämä on ihan ok, jos ei tarvitse alkuperäistä



// Math-luokka
// noppaesimerkki
const result = Math.ceil(Math.random()*6);
console.log('nopan heitto', result);

switch (result) {
    case 6:
        console.log('Voitit 100 e');
        break;
    case 5:
        console.log('Voitit 50 e');
        break;
    case 4:
        console.log('Voitit 20 e');
        break;
    default:
        console.log('Et voittanut mitään');
}


/*
while, käytä kun et tiedä täysin monta kertaa toteutetaan
toistetaan vaina kun ehto on tosi
eroaa do while sillä että ei välttämättä toteuteta kertaakaan
meillä on aina alkuehto joka tarkistetaan
 */

let count = 0;

while (count < 5) {
    console.log('Laskuri:', count);
    count++;
}

// do-while
// looppi halutaan suorittaa ainakin kerran ennen ehtoa
//let number = 0;

//do{
//    console.log('Tämä tulostuu ainakin kerran vaikka ehto ei täyttyisi')
//} while (number < 5)

let result2 = 3;

do {
    result2 = Math.floor(Math.random()*6)+1;
    console.log(result2)
} while (result2 < 6);


let numero = 6;

do {
    console.log('tämä tulostuu ainakin kerran vaikka ehto ei täyttyisi')
    numero++;
} while (numero < 6);

// tilanteisiin jossa haluat toistaa loopin x määrä kertoja
// esim kun käydään taulunkon indeksit läpi

for (let i = 0; i <= 10 ; i++) {
    console.log('luku on:', i);
}

for (let i = 10; i >= 1 ; i--) {
    console.log(i);
}