// import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.regex.Pattern;

public class learn {  

    static String javaHome;

    static String join(String sep, String... elements) {
        StringBuilder sb = new StringBuilder();
        for (String e : elements) {
          if (e != null) {
            if (sb.length() > 0) {
              sb.append(sep);
            }
            sb.append(e);
          }

          System.out.println(sb.toString());
        }

        return sb.toString();
    }

    public static void main(String[] args)  
    {  
        System.out.println("Hello");

        // 如果变量在类中，如果不是静态类型的那么就必须要实例化该类，再通过实例化对象调用变量
        // ```java
        // learn l = new learn();
        // l.javaHome != null
        // ```
        if (javaHome != null) {
            System.out.println("java != null");
        } else {
            System.out.println("java == null");
        }
        
        System.out.println(join(File.separator, System.getProperty("java.home"), "bin", "java"));

        String entries = "/a/b/c/d/";
        System.out.println(File.pathSeparator);
        System.out.println(Pattern.quote(File.pathSeparator));

        String[] split = entries.split(File.pathSeparator);
        
        for (String entry : split) {
            System.out.println(entry);    
        }
        
    }
}

