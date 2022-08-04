//Código escrito em Javascript
function nomeMaiusculo(name) {
 const nomeMaiusculo = name.toUpperCase();
 return nomeMaiusculo;
}

console.log(nomeMaiusculo("Carlos Henrique"));


function firstName(name) {
  const nomeCompleto = name.split(" ");
  const primeiroNome = nomeCompleto.shift();
  return primeiroNome
}

console.log(firstName("Carlos Henrique Gomes Mendonça"));


function quantidadeDeLetras(valor) {
  const tamanho = valor.length;
  return tamanho;
}

console.log(quantidadeDeLetras("Paralelepípedo"));
