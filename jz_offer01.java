public class jz_offer01{
    public boolean find(int[][] array, int target){
        int rows = array.length;
        int cols = array[0].length;
        if (array != null && rows > 0 && cols >0) {
            int row = 0;
            int col = cols - 1;
            while (row < rows && col >= 0) {
                if (array[row][col] == target) {
                    return true;
                }
                else if (array[row][col] > target) {
                    col--;
                }
                else {
                    row++;
                }
            }
            return false;
        }
        else {
            return false;
        }
    }
    public static void main(String[] args) {
       int array[][] = {{1, 2, 8, 9}, {2, 4, 9, 12},{4, 7, 10, 13},{6, 8, 11, 15}};
       int target = 7;
       jz_offer01 s = new jz_offer01();
       boolean result = s.find(array, target);
       System.out.print(result); 
    }
}