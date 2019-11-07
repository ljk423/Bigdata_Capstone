package com.bigdataproject.wa_index_page;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;


public class ExcelReader {
    /*
        xls 파일을 분석하여 List<Excelwork> 객체로 반환
        @param filepath
        @return
     */
    @SuppressWarnings("resource")
    public List<Excelwork> xlsToWeatherIndexList(String filepath){
        List<Excelwork> list = new ArrayList<Excelwork>();

        FileInputStream fis = null;
        HSSFWorkbook workbook = null;

        try {
            fis = new FileInputStream((filepath));
            // HSSFWorkbook은 엑셀 파일 전체 내용을 담고 있는 객체
            workbook = new HSSFWorkbook(fis);

            // 탐색에 사용할 sheet, row, cell 객체 생성\

            HSSFSheet   curSheet;
            HSSFRow     curRow;
            HSSFCell    curCell;
            Excelwork   wk;

            //sheet 탐색 for 문
            for(int sheetIndex = 0; sheetIndex < workbook.getNumberOfSheets(); sheetIndex++){
                // 현재 sheet 반환
                curSheet = workbook.getSheetAt(sheetIndex);
                // row 탐색 for
                for(int rowIndex = 0; rowIndex < curSheet.getPhysicalNumberOfRows(); rowIndex++){
                    // row 0번째는 헤더 정보이므로 무시 (colnames)
                    if(rowIndex != 0){
                        //현재 row 반환
                        curRow = curSheet.getRow(rowIndex);
                        wk = new Excelwork();
                        String value;

                        //row의 첫번째 cell값이 비어있지 않은 경우만 cell 탐색
                        if(!"".equals(curRow.getCell(0).getStringCellValue())){
                            //cell 탐색 for
                            for(int cellIndex = 0; cellIndex < curRow.getPhysicalNumberOfCells(); cellIndex++){
                                curCell = curRow.getCell(cellIndex);

                                if(true){
                                    value ="";
                                    // cell 스타일이 다르더라도 일단 String으로 반환
                                    switch (curCell.getCellType()){
                                        case HSSFCell.CELL_TYPE_FORMULA:
                                            value = curCell.getCellFormula();
                                            break;
                                        case HSSFCell.CELL_TYPE_NUMERIC:
                                            value = curCell.getNumericCellValue()+"";
                                            break;
                                        case HSSFCell.CELL_TYPE_STRING:
                                            value = curCell.getStringCellValue();
                                            break;
                                        case HSSFCell.CELL_TYPE_BLANK:
                                            value = curCell.getBooleanCellValue()+"";
                                            break;
                                        case HSSFCell.CELL_TYPE_ERROR:
                                            value = curCell.getErrorCellValue()+"";
                                            break;
                                        default:
                                            value = new String();
                                            break;
                                    }
                                    //현재 column index에 따라서 wk에 입력
                                    switch (cellIndex){
                                        case 0: // date
                                            wk.setDate(value);
                                            break;
                                        case 1: // flu
                                            wk.setFlu(value);
                                            break;
                                        case 2: //asthma
                                            wk.setAsthma(value);
                                            break;
                                        case 3: //arthritis
                                            wk.setArthritis(value);
                                            break;
                                        case 4: //regionCode
                                            wk.setRegionCode(value);
                                            break;
                                        default:
                                            break;
                                    }
                                }
                            }
                            // cell 탐색 후 wk 추가
                            list.add(wk);
                        }
                    }
                }
            }

        } catch (FileNotFoundException e){
            e.printStackTrace();
        } catch (IOException e){
            e.printStackTrace();
        } finally {
            try {
                // 사용한 자원을 finally에서 해제
                if( workbook!=null) workbook.close();
                if( fis!=null) fis.close();
            } catch (IOException e){
                e.printStackTrace();
            }
            return list;
        }
    }
}
