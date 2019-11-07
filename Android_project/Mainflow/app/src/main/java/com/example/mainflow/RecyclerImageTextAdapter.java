package com.example.mainflow;

import android.content.Context;
import android.text.Layout;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class RecyclerImageTextAdapter extends RecyclerView.Adapter<RecyclerImageTextAdapter.ViewHolder> {
    private ArrayList<RecyclerItem> mData = null;

    // 리스트 객체를 생성자에서 전달 받기
    RecyclerImageTextAdapter(ArrayList<RecyclerItem> list){
        mData = list;
    }

    @Override
    public RecyclerImageTextAdapter.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType){
        Context context = parent.getContext();
        LayoutInflater inflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View view = inflater.inflate(R.layout.recycler1_item, parent, false);
        RecyclerImageTextAdapter.ViewHolder vh = new RecyclerImageTextAdapter.ViewHolder(view);

        return vh;
    }

    @Override
    public void onBindViewHolder(RecyclerImageTextAdapter.ViewHolder holder, int position){

        RecyclerItem item = mData.get(position);

        holder.icon.setImageDrawable(item.getIcon());
        holder.title.setText(item.getTitleStr());
        holder.expl.setText(item.getExplainStr());
    }

    @Override
    public int getItemCount(){
        return mData.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder{
        ImageView icon;
        TextView title;
        TextView expl;

        ViewHolder(View itemVIew){
            super(itemVIew);

            icon = itemVIew.findViewById(R.id.icon);
            title = itemVIew.findViewById(R.id.title);
            expl = itemVIew.findViewById(R.id.explaination);
        }
    }

}
