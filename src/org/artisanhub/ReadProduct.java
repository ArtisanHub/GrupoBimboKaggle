
package org.artisanhub;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadProduct {

    public int getProductCountPerWeek(String filePath, String productId) {
        BufferedReader br = null;
        int count = 0;

        try {
            br = new BufferedReader(new FileReader(filePath));

            String ex;
            while((ex = br.readLine()) != null) {
                String[] currentRow = ex.split(",");
                if(currentRow[5].equals(productId)) {
                    ++count;
                }
            }
        } catch (IOException var15) {
            var15.printStackTrace();
        } finally {
            try {
                if(br != null) {
                    br.close();
                }
            } catch (IOException var14) {
                var14.printStackTrace();
            }

        }

        return count;
    }
}
