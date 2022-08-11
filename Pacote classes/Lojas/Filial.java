package Lojas;

public class Filial {
    private String localidade;

    public Filial(String nomeLocalidade) {
        localidade = nomeLocalidade;
    }
    
    public String getLocalidade() {
        return localidade;
    }
    
    public void setLocalidade(String localidade) {
        this.localidade = localidade;
    }
}
