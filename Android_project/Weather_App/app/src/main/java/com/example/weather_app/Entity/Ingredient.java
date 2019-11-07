package com.example.weather_app.Entity;

import android.content.ContentValues;
import android.content.Context;
import android.database.SQLException;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import com.example.babalzza.Databases;

public class Ingredient {
    private String name;
    private Integer quantity;
    private String duedate;

    private static final String DATABASE_NAME = "InnerDatabase(SQLite).db";
    private static final int DATABASE_VERSION = 1;
    public static SQLiteDatabase mDB;
    private static DatabaseHelper mDBHelper;

    private static class DatabaseHelper extends SQLiteOpenHelper{

        public DatabaseHelper(Context context, String name, SQLiteDatabase.CursorFactory factory, int version) {
            super(context, name, factory, version);
        }

        @Override
        public void onCreate(SQLiteDatabase db){
            db.execSQL(Databases.CreateDB._CREATE0);
        }

        @Override
        public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion){
            db.execSQL("DROP TABLE IF EXISTS "+Databases.CreateDB._TABLENAME0);
            onCreate(db);
        }
    }

    public static class DbOpenHelper {
        private Context mCtx;

        public DbOpenHelper(Context context){
            this.mCtx = context;
        }

        public DbOpenHelper open() throws SQLException {
            mDBHelper = new DatabaseHelper(mCtx, DATABASE_NAME, null, DATABASE_VERSION);
            mDB = mDBHelper.getWritableDatabase();
            return this;
        }
        public void create(){
            mDBHelper.onCreate(mDB);
        }
        public void close(){ mDB.close(); }
    }
    public Ingredient (String name, Integer quantity, String duedate) {
        super();
        this.name = name;
        this.quantity = quantity;
        this.duedate = duedate;
    }

    public static long saveIngredient(Ingredient ingredient) {
        String name = ingredient.getName();
        Integer quantity = ingredient.getQuantity();
        String duedate = ingredient.getDueDate();

        ContentValues values = new ContentValues();

        values.put(Databases.CreateDB.NAME, name);
        values.put(Databases.CreateDB.QUANTITY, quantity);
        values.put(Databases.CreateDB.DUEDATE, duedate);

        return mDB.insert(Databases.CreateDB._TABLENAME0, null, values);
    }

    public static void showIngredient(Ingredient ingredient) {
        // read에 대해 구현할 부분
        // 팝업?
    }

    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Integer getQuantity() {
        return quantity;
    }
    public void setQuantity(Integer quantity) {
        this.quantity = quantity;
    }
    public String getDueDate() {
        return duedate;
    }
    public void setDueDate(String duedate) {
        this.duedate = duedate;
    }
}
