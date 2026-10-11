// Latihan 2: loop dan fungsi

// tabel perkalian
function tabelPerkalian(angka) {
  for (let i = 1; i <= 10; i++) {
    console.log(angka + " x " + i + " = " + angka * i);
  }
}
tabelPerkalian(7);

// faktorial
function faktorial(n) {
  let hasil = 1;
  for (let i = 2; i <= n; i++) {
    hasil *= i;
  }
  return hasil;
}
console.log("5! =", faktorial(5));
console.log("0! =", faktorial(0));

// cek bilangan prima
function cekPrima(n) {
  if (n < 2) {
    return false;
  }
  for (let i = 2; i < n; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}
console.log("7 prima?", cekPrima(7));
console.log("12 prima?", cekPrima(12));

// FizzBuzz 1 sampai 100
for (let i = 1; i <= 100; i++) {
  if (i % 15 === 0) {
    console.log("FizzBuzz");
  } else if (i % 3 === 0) {
    console.log("Fizz");
  } else if (i % 5 === 0) {
    console.log("Buzz");
  } else {
    console.log(i);
  }
}
