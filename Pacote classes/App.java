import Transportadora.*;
import Lojas.*;

public class App {
  public static void main(String[] args) {
    Produto primeiroProduto = new Produto("Camisa", 119.99);
    primeiroProduto.setProduto("Calça");
    primeiroProduto.setPreco(200);    
    System.out.println(primeiroProduto.getProduto());
    System.out.println(primeiroProduto.getPreco());


    Filial filialLoja = new Filial("Recife");
    filialLoja.setLocalidade("Caruaru");
    System.out.println(filialLoja.getLocalidade());


    Transportadora tranporta = new Transportadora("ABC Transports", "Caminhão");
    tranporta.setVeiculo("Moto");
    System.out.println(tranporta.getVeiculo());  
  }
}
