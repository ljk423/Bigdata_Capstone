package com.example.weather_app.Control;

import com.example.babalzza.Entity.Ingredient;
import com.example.weather_app.Entity.Ingredient;

public class IngredientController {

    public static void addIngredient(String name, Integer quantity, String duedate) {
        Ingredient ingredient = new Ingredient("",0,"");

        ingredient.setName(name);
        ingredient.setQuantity(quantity);
        ingredient.setDueDate(duedate);

        ingredient.saveIngredient(ingredient);
    }

    public static void readIngredient(Ingredient ingredient) {
        Ingredient.showIngredient(ingredient);
    }

}
