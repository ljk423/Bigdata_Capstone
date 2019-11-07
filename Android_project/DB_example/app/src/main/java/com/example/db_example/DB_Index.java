package com.example.db_example;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import com.example.db_example.Databases;

public class DB_Index {
    private String date;
    private int province;
    private int idx1;
    private int idx2;
    private int idx3;
    // 질병 개수 나올때까지 돌리기
    private String names[] = {"flue", "cold", "headache"};
    // 이런 식으로 순서에 맞춰 질병 이름 출력 가능하도록
    private static final String DATABASE_NAME = "InnerDatabase(SQLite).db";
    private static final int DATABASE_VERSION = 1;
    public static SQLiteDatabase nDB:
    private static DatabaseHelper mDBHelper;

    private static class DatabaseHelper extends SQLiteOpenHelper{
        public DatabaseHelper(Context context, String name, SQLiteDatabase.CursorFactory factory, int version){
            super(context, name, factory, version);
        }

        @Override
        public void onCreate(SQLiteDatabase db){ db.execSQL(Databases.CreateDB._CREATE0);}

        @Override
        public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
            db.execSQL("DROP TABLE IF EXISTS" + Databases.CreateDB._TABLENAME0);
            onCreate(db);
        }
    }

    public static class DbOpenHelper {
        private Context mCtx;

        public DbOpenHelper()
    }
}
