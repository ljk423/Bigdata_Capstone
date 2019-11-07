package com.bigdataproject.wa_index_page;

import java.util.List;

public class FakeMain {
    public static void main(String[] args){
        ExcelReader excelReader = new ExcelReader();
        String filepath = "C:\\excel\\weather_index.xls";
        System.out.println("*****xls*****");
        List<Excelwork> excelworks = excelReader.xlsToWeatherIndexList(filepath);
        printList(excelworks);
    }
    public static void printList(List<Excelwork> list) {
        Excelwork wk;

        for (int i = 0; i < list.size(); i++){
            wk = list.get(i);
            System.out.println(wk.toString());
        }
    }
}
