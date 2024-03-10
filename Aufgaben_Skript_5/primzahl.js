// JavaScript zur Bestimmung der Primzahlen und Messung der Rechenzeit
function isPrime(num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 === 0 || num % 3 === 0) return false;
    let i = 5;
    while (i * i <= num) {
        if (num % i === 0 || num % (i + 2) === 0) return false;
        i += 6;
    }
    return true;
}

function findPrimes(digits) {
    const startTime = performance.now();
    const number = BigInt('7' + '0'.repeat(digits - 2) + '1'); // Erzeugen der 13-stelligen Dezimalzahl
    const primes = [];
    let currentNumber = BigInt(2);
    while (currentNumber <= number) {
        if (isPrime(currentNumber)) primes.push(currentNumber);
        currentNumber += BigInt(1);
    }
    const endTime = performance.now();
    console.log('Primzahlen:', primes);
    console.log('Zeit zur Berechnung:', endTime - startTime, 'Millisekunden');
}

findPrimes(13); // Primzahlen für eine 13-stellige Dezimalzahl finden