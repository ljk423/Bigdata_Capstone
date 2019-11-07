package com.bigdataproject.wa_index_page;

public class Excelwork {
    private String date;
    private String flu;
    private String asthma;
    private String arthritis;
    private String regionCode;

    public String getDate(){
        return date;
    }
    public void setDate(String date){
        this.date = date;
    }
    public String getFlu(){
        return flu;
    }
    public void setFlu(String flu){
        this.flu = flu;
    }
    public String getAsthma(){
        return asthma;
    }
    public void setAsthma(String asthma){
        this.asthma = asthma;
    }
    public String getArthritis(){
        return arthritis;
    }
    public void setArthritis(String arthritis){
        this.arthritis = arthritis;
    }
    public String getRegionCode(){
        return regionCode;
    }
    public void setRegionCode(String regionCode){
        this.regionCode = regionCode;
    }

    @Override
    public String toString(){
        StringBuffer sb = new StringBuffer();

        sb.append("Date: "+date);
        sb.append(" ,FLU : "+flu);
        sb.append(" ,ASTHMA : "+asthma);
        sb.append(" ,ARTHRITIS : "+arthritis);
        sb.append(", REGIONCODE : "+regionCode);
        return sb.toString();
    }

}