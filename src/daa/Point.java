package daa;

/** Immutable finite 2D point. Coincident points are allowed as separate entries. */
public record Point(double x, double y) {
    public Point {
        if (!Double.isFinite(x) || !Double.isFinite(y)) {
            throw new IllegalArgumentException("Point coordinates must be finite");
        }
    }
}
