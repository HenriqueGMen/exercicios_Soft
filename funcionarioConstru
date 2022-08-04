//Código escrito em Javascript

class ContaBancaria {
    constructor(nomeCompleto, saldo) {
      this.nomeCompleto = nomeCompleto;
    	this.saldo = saldo;
	}
	
	get nomeCliente() {
    	return `Olá, ${this.nomeCompleto}`
	}
	
	set nomeCliente(valor) {
        if(valor.length < 8) {
           throw new Error(‘Digite seu nome completo’)
    	}
        this.nomeCompleto = valor
	}
	
	get mudarSaldo() {
    	return `O seu saldo é de R$${this.saldo} reais`
	}
	
	set mudarSaldo(valor) {
    	if(valor < 0) {
        	this.saldo = 0
    	} else {
        	this.saldo = valor
    	}
	}
}
 
const cliente1 = new ContaBancaria();
cliente1.nomeCliente = "José Mendes";
cliente1.mudarSaldo = -15;
console.log(cliente1.nomeCliente);
console.log(cliente1.mudarSaldo);
 
const cliente2 = new ContaBancaria()
cliente2.nomeCliente = "Ana Patricia";
cliente2.mudarSaldo = 200;
console.log(cliente2.nomeCliente);
console.log(cliente2.mudarSaldo);
