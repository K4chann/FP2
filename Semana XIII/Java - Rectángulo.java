import java.util.Arrays;

public class Rectángulo {
	private double base, altura;
    
    public Rectángulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }
    
    public double getBase() {
        return base;
    }
    
    public double getAltura() {
        return altura;
    }
    
    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        if (other.getClass() != other.getClass() || other == null) return false;
        Rectángulo obj = (Rectángulo) other;
        return this.getBase() == obj.getBase() && this.getAltura() == obj.getAltura();
    }
    
    @Override
    public String toString() {
        return "Rectángulo de base: " + this.base + " y altura: " + this.altura;
    }
}
