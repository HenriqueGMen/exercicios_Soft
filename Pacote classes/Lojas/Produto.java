package Lojas;

public class Produto {
    private String nome;
    private double preco;
    
    public Produto(String nomeProduto, double precoProduto) {
        nome = nomeProduto;
        preco = precoProduto;
    }

    public String getProduto() {
        return nome;
    }

    public void setProduto(String newProduto) {
        this.nome = newProduto;
    }
    
    public double getPreco() {
        return preco;
    }
    
    public void setPreco(double newPreco) {
        this.preco = newPreco;        
    }
}
