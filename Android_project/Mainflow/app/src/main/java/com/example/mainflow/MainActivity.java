package com.example.mainflow;


import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.graphics.drawable.Drawable;
import android.os.Bundle;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    RecyclerView mRecyclerView = null;
    RecyclerImageTextAdapter mAdapter = null;
    ArrayList<RecyclerItem> mList = new ArrayList<RecyclerItem>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mRecyclerView = findViewById(R.id.recycler1);

        mAdapter = new RecyclerImageTextAdapter(mList);
        mRecyclerView.setAdapter(mAdapter);

        mRecyclerView.setLayoutManager(new LinearLayoutManager(this));

        // add item

        addItem(getDrawable(R.drawable.fever_fine), "독감", "양호");

        mAdapter.notifyDataSetChanged();
    }
    public void addItem(Drawable icon, String title, String expl) {
        RecyclerItem item = new RecyclerItem();

        item.setIcon(icon);
        item.setTitle(title);
        item.setExpl(expl);

        //list.add(item);
    }
}
