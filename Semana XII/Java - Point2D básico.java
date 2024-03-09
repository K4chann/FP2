public class Point2D {
    private double coordX;
    private double coordY;
    
    public Point2D(double value1, double value2) {
        this.coordX = value1;
        this.coordY = value2;
    }
    
    public double getX() {
        return coordX;
    }
    
    public double getY() {
        return coordY;
    }
    
    public void setX(double newValue) {
        coordX = newValue;
    }
    
    public void setY(double newValue) {
        coordY = newValue;
    }
}
