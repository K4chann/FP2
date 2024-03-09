public class Circle {
    private double radio;
    
    public Circle(double value) {
        this.radio = value;
    }
    
    public double getRadious() {
        return this.radio;
    }
    
    public void setRadious(double newValue) {
        // Se debería controlar el valor del radio, pero no es necesario en estos ejercicios
        // Una posible solución es almacenar el valor absoluto.
        // this.radio = (newValue >= 0) newValue : -newValue;
        radio = newValue;
    }
    
    public double area() {
        return Math.PI * Math.pow(this.radio, 2);
    }
}
