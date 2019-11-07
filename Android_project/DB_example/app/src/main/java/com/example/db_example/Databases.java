package com.example.db_example;

import android.provider.BaseColumns;

public class Databases {
    public static final class CreateDB implements BaseColumns{
        public static final String _KEY = "key";
        public static final String DATE = "date";
        public static final String PROVINCE = "province";
        public static final String IDX1 = "idx1";
        public static final String IDX2 = "idx2";
        public static final String IDX3 = "idx3";
        public static final String _TABLENAME0 = "index";
        public static final String _CREATE0 = "create table if not exists "+ _TABLENAME0 + "("
                + _KEY + " integer priamry key autoincrement, "
                + DATE + "integer not null, "
                + PROVINCE + "integer not null"
                + IDX1 + "integer not null"
                + IDX2 + "integer not null"
                + IDX3 + "integer not null";
    }
}
