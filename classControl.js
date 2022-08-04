class ControleRemoto {
  constructor(marca){
      this.marca = marca
      this.volume = 0
  }

  aumentarVolume(){
      if(this.volume < 100) {
          this.volume += 1
      } else {
          console.error("Volume máximo")
      }
  }

  diminuirVolume(){
      if(this.volume > 0) {
          this.volume -= 1
      } else {
          console.error("Volume minimo")
      }
  }
  
  static pilhas = 2;   
}


const controle1 = new ControleRemoto('LG')
controle1.aumentarVolume();
console.log(controle1)
const controle2 = new ControleRemoto('Samsung')
controle2.aumentarVolume();
controle2.aumentarVolume();
console.log(controle2)
const controle3 = new ControleRemoto('Sony')
controle3.diminuirVolume()
console.log(controle3)
