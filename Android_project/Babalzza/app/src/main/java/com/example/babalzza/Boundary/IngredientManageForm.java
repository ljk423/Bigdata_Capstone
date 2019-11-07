package com.example.weather_app;

import androidx.appcompat.app.AppCompatActivity;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.EditText;
import android.widget.Toast;

import com.example.babalzza.Control.IngredientController;
import com.example.babalzza.R;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

public class IngredientManageForm extends AppCompatActivity implements View.OnClickListener {

    private Animation fab_open, fab_close;
    private Boolean isFabOpen = false;
    private FloatingActionButton fab, fab1, fab2, fab3;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.fridge_main);

        fab_open = AnimationUtils.loadAnimation(getApplicationContext(), R.anim.open);
        fab_close = AnimationUtils.loadAnimation(getApplicationContext(), R.anim.close);

        fab = (FloatingActionButton) findViewById(R.id.floatingActionButton);
        fab1 = (FloatingActionButton) findViewById(R.id.createButton);
        fab2 = (FloatingActionButton) findViewById(R.id.modifyButton);
        fab3 = (FloatingActionButton) findViewById(R.id.deleteButton);

        fab.setOnClickListener(this);
        fab1.setOnClickListener(this);
        fab2.setOnClickListener(this);
        fab3.setOnClickListener(this);
    }

    public void onClick(View v) {
        int id = v.getId();
        switch (id) {
            case R.id.floatingActionButton:
                anim();
                break;

            case R.id.createButton:
                anim();
                Toast.makeText(this, "추가", Toast.LENGTH_SHORT).show();
                Intent addintent= new Intent(IngredientManageForm.this, IngredientAdditionForm.class);
                IngredientManageForm.this.startActivity(addintent);
                break;

            case R.id.modifyButton:
                anim();

                AlertDialog.Builder builder = new AlertDialog.Builder(this);
                LayoutInflater inflater_dg = getLayoutInflater();

                final View view = inflater_dg.inflate(R.layout.fridge_change_popup, null);
                builder.setView(view);
                builder.setPositiveButton("수정", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {

                        /*
                        nText = (EditText)view.findViewById(R.id.nameText);
                        qText = (EditText)view.findViewById(R.id.quantityText);
                        dText = (EditText)view.findViewById(R.id.duedateText);

                        name = nText.getText().toString();
                        quantity = Integer.parseInt(qText.getText().toString());
                        duedate = dText.getText().toString();

                        IngredientController.addIngredient(name, quantity, duedate);
                         */
                    }
                });
                AlertDialog dialog = builder.create();
                dialog.setCanceledOnTouchOutside(false);
                dialog.show();
                break;

            case R.id.deleteButton:
                anim();
                Toast.makeText(this, "삭제", Toast.LENGTH_SHORT).show();
                break;
        }
    }
    // 버튼 애니메이션 효과
    public void anim() {
        if (isFabOpen) {
            fab3.startAnimation(fab_close);
            fab2.startAnimation(fab_close);
            fab1.startAnimation(fab_close);
            fab1.setClickable(false);
            fab2.setClickable(false);
            fab3.setClickable(false);
            isFabOpen = false;
        } else {
            fab3.startAnimation(fab_open);
            fab2.startAnimation(fab_open);
            fab1.startAnimation(fab_open);
            fab1.setClickable(true);
            fab2.setClickable(true);
            fab3.setClickable(true);
            isFabOpen = true;
        }
    }
}
