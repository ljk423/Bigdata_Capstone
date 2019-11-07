package com.example.weather_app.Boundary;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;

import androidx.appcompat.app.AppCompatActivity;

import com.example.babalzza.Control.IngredientController;
import com.example.babalzza.Entity.Ingredient;
import com.example.babalzza.R;
import com.example.weather_app.R;

public class IngredientAdditionForm extends AppCompatActivity {

    private ImageButton ib1_1, ib1_2, ib2_1, ib2_2;
    private EditText nText, qText, dText;
    private String name; private Integer quantity; private String duedate;
    private Ingredient.DbOpenHelper mDbOpenHelper;

    @Override
    // 식자재 버튼 create
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.fridge_add);

        ib1_1 = (ImageButton)findViewById(R.id.imageButton1_1);
        ib1_2 = (ImageButton)findViewById(R.id.imageButton1_2);
        ib2_1 = (ImageButton)findViewById(R.id.imageButton2_1);
        ib2_2 = (ImageButton)findViewById(R.id.imageButton2_2);

        mDbOpenHelper = new Ingredient.DbOpenHelper(this);
        mDbOpenHelper.open();
        mDbOpenHelper.create();

        ib1_1.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                add();
            }
        });
        ib1_2.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                add();
            }
        });
        ib2_1.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                add();
            }
        });
        ib2_2.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                add();
            }
        });
    }

    void add(/*final Context context /*, final NoteAdapter adapter*/){
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        LayoutInflater inflater_dg = getLayoutInflater();
        final View view = inflater_dg.inflate(R.layout.fridge_add_popup, null);
        builder.setView(view);
        builder.setPositiveButton("추가", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {

                nText = (EditText)view.findViewById(R.id.nameText);
                qText = (EditText)view.findViewById(R.id.quantityText);
                dText = (EditText)view.findViewById(R.id.duedateText);

                name = nText.getText().toString();
                quantity = Integer.parseInt(qText.getText().toString());
                duedate = dText.getText().toString();

                IngredientController.addIngredient(name, quantity, duedate);
            }
        });
        AlertDialog dialog = builder.create();
        dialog.setCanceledOnTouchOutside(false);
        dialog.show();
    }
}
