package com.example.mainflow;

import android.graphics.drawable.Drawable;

public class RecyclerItem {
    private Drawable iconDrawble;
    private String titleStr;
    private String explainStr;

    public void setIcon(Drawable icon){
        iconDrawble = icon;
    }
    public void setTitle(String title){
        titleStr = title;
    }
    public void setExpl(String expl){
        explainStr = expl;
    }

    public Drawable getIcon(){
        return this.iconDrawble;
    }
    public String getTitleStr(){
        return this.titleStr;
    }
    public String getExplainStr(){
        return this.explainStr;
    }
}
