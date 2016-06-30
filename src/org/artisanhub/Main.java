package org.artisanhub;

public class Main {

    public static void main(String[] args) {
        String weekPath = "/home/rnavagamuwa/Documents/CSE/Semester7/DataMining/kaggle/weeklySeperatedData/week3.csv";
        ReadProduct readProduct =  new ReadProduct();
        System.out.println(readProduct.getProductCountPerWeek(weekPath,"1212"));
    }
}
