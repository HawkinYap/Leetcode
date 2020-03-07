public class jz_offer02 {
    public String replaceSpace(StringBuffer str) {
        if (str == null)
            return null;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < str.length(); i++){
            if (String.valueOf(str.charAt(i)).equals(" ")){
                sb.append("%20");
            }else {
                sb.append(str.charAt(i));
            }
        }
        return String.valueOf(sb);
    }

    public static void main(String[] args) {
        StringBuffer str = new StringBuffer("We Rre Happy");
        jz_offer02 s = new jz_offer02();
        String result = s.replaceSpace(str);
        System.out.println(result);


    }
}