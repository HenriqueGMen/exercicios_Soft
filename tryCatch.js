// Código escrito em javascript

function divisao(dividendo, divisor) {
  try {
    if (divisor === 0) throw new Error ("Impossivel dividir por 0")
    return dividendo / divisor
  } catch (error) {
    console.error(error)
  }
}

console.log(divisao(20, 5))
console.log(divisao(8, 0))
