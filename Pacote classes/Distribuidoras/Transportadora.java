package Distribuidoras;

public class Transportadora {
  private String nome;
  private String veiculo;

    public Transportadora(String nomeTransportadora, String tipoVeiculo) {
        nome = nomeTransportadora;
        veiculo = tipoVeiculo;
    }

    public String getNomeTransportadora() {
        return nome;
    }
    
    public String getVeiculo() {
        return veiculo;
    }

    public void setVeiculo(String newVeiculo) {
        this.veiculo = newVeiculo;
    } 
}
